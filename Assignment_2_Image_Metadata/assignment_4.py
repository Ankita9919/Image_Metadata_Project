from pymongo import MongoClient
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path
from collections import Counter
from datetime import datetime
import re
import ast


client = MongoClient("mongodb://127.0.0.1:27017/")

db = client["image_metadata"]

BASE_FOLDER = Path("segregated_images")


def clean_text(value):

    if value is None:
        return "Unknown"

    value = str(value)

    value = value.replace("\x00", "")
    value = value.strip()

    if value == "":
        return "Unknown"

    return value


def get_metadata(image_path):

    metadata = {
        "filename": image_path.name,
        "file_path": str(image_path)
    }

    try:

        image = Image.open(image_path)

        exif_data = image.getexif()

        for tag_id, value in exif_data.items():

            tag = TAGS.get(
                tag_id,
                str(tag_id)
            )

            if isinstance(value, bytes):

                try:
                    value = value.decode(
                        errors="ignore"
                    )

                except:
                    value = str(value)

            metadata[tag] = clean_text(value)

    except Exception as e:

        print(
            "Could not read:",
            image_path.name,
            e
        )

    return metadata


def create_collection_name(make, model):

    make = clean_text(make)
    model = clean_text(model)

    name = f"{make}_{model}"

    name = re.sub(
        r'[^a-zA-Z0-9_-]',
        "_",
        name
    )

    name = re.sub(
        r'_+',
        "_",
        name
    )

    name = name.strip("_")

    if not name:
        name = "Unknown_Unknown"

    return name[:120]


def store_all_metadata():

    if not BASE_FOLDER.exists():

        print(
            "\nsegregated_images folder not found!"
        )

        return

    total = 0

    extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".heic",
        ".heif"
    ]

    print(
        "\nStoring image metadata...\n"
    )

    for image_path in BASE_FOLDER.rglob("*"):

        if image_path.suffix.lower() not in extensions:
            continue

        try:

            metadata = get_metadata(
                image_path
            )

            make = metadata.get(
                "Make",
                "Unknown"
            )

            model = metadata.get(
                "Model",
                "Unknown"
            )

            collection_name = create_collection_name(
                make,
                model
            )

            collection = db[
                collection_name
            ]

            existing = collection.find_one(
                {
                    "filename":
                    image_path.name
                }
            )

            if existing:

                print(
                    image_path.name,
                    "-> already stored"
                )

                continue

            metadata["inserted_at"] = (
                datetime.now()
                .astimezone()
                .isoformat()
            )

            collection.insert_one(
                metadata
            )

            print(
                image_path.name,
                "->",
                collection_name
            )

            total += 1

        except Exception as e:

            print(
                image_path.name,
                "-> SKIPPED:",
                e
            )

    print("\n--------------------------------")
    print(
        "New images stored:",
        total
    )
    print("--------------------------------")


def get_brand_from_collection(collection_name):

    if collection_name.startswith(
        "Unknown_"
    ):
        return None

    # Extract brand from known collection patterns

    known_brands = [
        "samsung",
        "Xiaomi",
        "vivo",
        "OPPO",
        "OnePlus",
        "Nothing",
        "motorola",
        "iQOO",
        "INFINIX",
        "Apple"
    ]

    for brand in known_brands:

        if collection_name.startswith(
            brand + "_"
        ):

            return brand

    return None


def maximum_brand():

    brand_count = Counter()

    collections = db.list_collection_names()

    for collection_name in collections:

        brand = get_brand_from_collection(
            collection_name
        )

        if brand is None:
            continue

        count = db[
            collection_name
        ].count_documents({})

        brand_count[brand] += count

    if not brand_count:

        print(
            "\nNo brand information found."
        )

        return

    maximum = max(
        brand_count.values()
    )

    print(
        "\n================================"
    )

    print(
        "BRAND WITH MAXIMUM PHOTOS"
    )

    print(
        "================================"
    )

    for brand, count in brand_count.items():

        if count == maximum:

            print(
                "Brand:",
                brand,
                "| Photos:",
                count
            )


def manual_metadata():

    print(
        "\n================================"
    )

    print(
        "MANUAL METADATA ENTRY"
    )

    print(
        "================================"
    )

    print(
        "\nEnter metadata as a Python dictionary."
    )

    print(
        "\nExample:"
    )

    print(
        "{'filename': 'test.jpg', "
        "'Make': 'Samsung', "
        "'Model': 'Galaxy S24 Ultra'}"
    )

    user_input = input(
        "\nEnter dictionary: "
    )

    try:

        metadata = ast.literal_eval(
            user_input
        )

        if not isinstance(
            metadata,
            dict
        ):

            print(
                "\nEnter dictionary only."
            )

            return

        make = metadata.get(
            "Make",
            "Unknown"
        )

        model = metadata.get(
            "Model",
            "Unknown"
        )

        collection_name = create_collection_name(
            make,
            model
        )

        metadata["inserted_at"] = (
            datetime.now()
            .astimezone()
            .isoformat()
        )

        db[
            collection_name
        ].insert_one(
            metadata
        )

        print(
            "\nMetadata inserted successfully!"
        )

        print(
            "Collection:",
            collection_name
        )

    except Exception as e:

        print(
            "\nInvalid dictionary!"
        )

        print(e)


def display_collections():

    print(
        "\n================================"
    )

    print(
        "MONGODB COLLECTIONS"
    )

    print(
        "================================"
    )

    collections = db.list_collection_names()

    for collection in collections:

        count = db[
            collection
        ].count_documents({})

        print(
            collection,
            "->",
            count,
            "documents"
        )


def menu():

    while True:

        print(
            "\n========================================"
        )

        print(
            "        IMAGE METADATA SYSTEM"
        )

        print(
            "========================================"
        )

        print(
            "1. Display brand with maximum photos"
        )

        print(
            "2. Enter metadata manually"
        )

        print(
            "3. Display MongoDB collections"
        )

        print(
            "4. Exit"
        )

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            maximum_brand()

        elif choice == "2":

            manual_metadata()

        elif choice == "3":

            display_collections()

        elif choice == "4":

            print(
                "\nProgram ended."
            )

            break

        else:

            print(
                "\nInvalid choice!"
            )


print(
    "\nMongoDB connected successfully!"
)

store_all_metadata()

menu()