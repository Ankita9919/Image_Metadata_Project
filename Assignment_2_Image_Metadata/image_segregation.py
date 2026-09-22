import os
import re
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from pymongo import MongoClient

SOURCE_FOLDER = "dataset"
OUTPUT_FOLDER = "segregated_images"

client = MongoClient("mongodb://localhost:27017/")
db = client["image_metadata"]
collection = db["images"]

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def clean_name(name):
    name = str(name)
    name = name.replace("\x00", "")
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = name.strip()

    if not name:
        return "Unknown"

    return name


for filename in os.listdir(SOURCE_FOLDER):

    if not filename.lower().endswith(
        (".jpg", ".jpeg", ".png", ".heic", ".heif")
    ):
        continue

    file_path = os.path.join(SOURCE_FOLDER, filename)

    try:
        image = Image.open(file_path)

        exif = image.getexif()
        metadata = {}

        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value

        brand = metadata.get("Make")
        model = metadata.get("Model")

        if not brand or not model:
            print(f"{filename} -> Metadata not found")
            continue

        brand = clean_name(brand)
        model = clean_name(model)

        brand_folder = os.path.join(
            OUTPUT_FOLDER,
            brand
        )

        model_folder = os.path.join(
            brand_folder,
            model
        )

        os.makedirs(model_folder, exist_ok=True)

        destination = os.path.join(
            model_folder,
            filename
        )

        shutil.copy2(
            file_path,
            destination
        )

        collection.update_one(
            {"file_name": filename},
            {
                "$set": {
                    "file_name": filename,
                    "brand": brand,
                    "model": model,
                    "source_path": file_path,
                    "destination_path": destination
                }
            },
            upsert=True
        )

        print(
            f"{filename} -> {brand} -> {model}"
        )

    except Exception as e:
        print(f"{filename} -> Error: {e}")


print("\nCompleted.")
