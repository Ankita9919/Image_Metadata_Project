import os
import shutil

SOURCE_FOLDER = "dataset"
OUTPUT_FOLDER = "location_segregated"
LOCATION = "Adamas_University"
SUB_LOCATION = "AU-6_SOET"

destination = os.path.join(
    OUTPUT_FOLDER,
    LOCATION,
    SUB_LOCATION
)

os.makedirs(destination, exist_ok=True)

count = 0

for filename in os.listdir(SOURCE_FOLDER):

    if not filename.lower().endswith(
        (".jpg", ".jpeg", ".png", ".heic", ".heif")
    ):
        continue

    source = os.path.join(SOURCE_FOLDER, filename)
    target = os.path.join(destination, filename)

    shutil.copy2(source, target)
    count += 1

    print(filename, "->", LOCATION, "->", SUB_LOCATION)

print("\nTotal images segregated:", count)
print("Output folder:", destination)
