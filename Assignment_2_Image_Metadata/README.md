# Image Metadata Project

A Python and MongoDB based image metadata management project developed as part of the UDB Lab coursework.

The project focuses on extracting image metadata, organizing images based on device information and location, segregating specific university locations, and storing image metadata in MongoDB collections.

---

## Project Overview

This project is divided into four major assignments:

1. Image segregation based on phone Make and Model
2. Location-based image segregation
3. Adamas University and AU-6 SOET image segregation
4. MongoDB-based image metadata storage and management

The project uses Python for image processing and MongoDB for metadata storage.

---

## Technologies Used

* Python
* MongoDB
* PyMongo
* Pillow
* Python `pathlib`
* Python `datetime`
* Regular Expressions
* MongoDB Collections
* Git & GitHub

---

# Assignment 1 — Image Segregation by Make and Model

### Objective

To organize images according to the device manufacturer and device model obtained from image metadata.

### Working

The Python script:

1. Reads images from the dataset.
2. Extracts metadata from the images.
3. Reads the `Make` field.
4. Reads the `Model` field.
5. Creates a folder for the device brand.
6. Creates a model subfolder.
7. Copies the image into the corresponding model folder.

### Example Structure

```text
segregated_images/
│
├── samsung/
│   ├── Galaxy_A15_5G/
│   ├── Galaxy_A36_5G/
│   └── Galaxy_S26/
│
├── Xiaomi/
│   ├── 23049PCD8I/
│   ├── Redmi_12_5G/
│   └── POCO_F7/
│
├── vivo/
│   ├── V23e_5G/
│   └── V50/
│
└── OPPO/
    ├── CPH2603/
    └── OPPO_A78_5G/
```

### Python File

```text
image_segregation.py
```

---

# Assignment 2 — Location-Based Image Segregation

### Objective

To identify and segregate images according to their location metadata.

The location information was extracted from image metadata and used to organize the images into appropriate folders.

### Output Structure

```text
location_segregated/
│
└── Adamas_University/
    │
    └── AU-6_SOET/
```

### Python File

```text
location_segregation.py
```

---

# Assignment 3 — Adamas University → AU-6 SOET Segregation

### Objective

To further filter the location-segregated images and identify images specifically associated with:

```text
Adamas University
        ↓
AU-6 SOET
```

The final location-specific dataset contains the images identified as belonging to AU-6 SOET.

### Output Structure

```text
location_segregated/
└── Adamas_University/
    └── AU-6_SOET/
```

This step provides a more specific subset of the location-based image dataset.

---

# Assignment 4 — MongoDB Image Metadata Management

### Objective

To establish a Python-MongoDB connection and store image metadata into appropriate MongoDB collections based on the image Make and Model.

### MongoDB Database

```text
Database: image_metadata
```

### Collection Naming

Collections are generated using:

```text
Make_Model
```

For example:

```text
samsung_Galaxy_A15_5G
Xiaomi_23049PCD8I
vivo_V23e_5G
OPPO_OPPO_A78_5G
Apple_iPhone_13
```

### Metadata Storage

The program extracts metadata such as:

* Filename
* File path
* Make
* Model
* Date/time metadata
* EXIF metadata
* Other available image metadata
* Insert timestamp

Each image's metadata is stored as a MongoDB document.

---

## Assignment 4 Menu System

The Python program provides a menu-based interface.

```text
========================================
        IMAGE METADATA SYSTEM
========================================

1. Display brand with maximum photos
2. Enter metadata manually
3. Display MongoDB collections
4. Exit
```

### Option 1 — Maximum Photo Brand

The program counts the number of stored photos for each recognized brand and displays the brand with the maximum number of photos.

Example output:

```text
================================
BRAND WITH MAXIMUM PHOTOS
================================

Brand: Xiaomi | Photos: 8
```

### Option 2 — Manual Metadata Entry

The user can enter metadata as a Python dictionary.

Example:

```python
{
    'filename': 'manual_test.jpg',
    'Make': 'Samsung',
    'Model': 'Galaxy S24 Ultra',
    'DateTimeOriginal': '2026:09:22 18:30:00',
    'Description': 'Manual metadata test'
}
```

The program automatically determines the appropriate MongoDB collection from the `Make` and `Model`.

Example:

```text
Samsung_Galaxy_S24_Ultra
```

### Option 3 — Display Collections

The program displays the MongoDB collections and the number of documents stored in each collection.

Example:

```text
samsung_Galaxy_A15_5G -> 1 documents
Xiaomi_23124RN87I -> 2 documents
Apple_iPhone_13 -> 1 documents
```

### Option 4 — Exit

Safely terminates the program.

---

# MongoDB Workflow

```text
Images
   │
   ▼
Extract EXIF Metadata
   │
   ▼
Read Make + Model
   │
   ▼
Create Collection Name
   │
   ▼
MongoDB
   │
   ├── samsung_Galaxy_A15_5G
   ├── Xiaomi_23049PCD8I
   ├── vivo_V23e_5G
   ├── OPPO_OPPO_A78_5G
   └── ...
```

---

# Project Structure

```text
Image_Metadata_Project/
│
├── Assignment_2_Image_Metadata/
│   │
│   ├── image_segregation.py
│   ├── location_segregation.py
│   ├── assignment_4.py
│   ├── .gitignore
│   │
│   ├── dataset/
│   ├── Image_Dataset/
│   ├── segregated_images/
│   ├── location_segregated/
│   └── preview_sheets/
│
└── README.md
```

> Note: Image datasets and personal photographs are not included in the public GitHub repository.

---

# Installation

Create and activate a Python virtual environment:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install pillow pymongo
```

---

# MongoDB Setup

Make sure MongoDB Server is running.

Check MongoDB Shell:

```powershell
mongosh --version
```

The Python program connects to MongoDB using:

```text
mongodb://127.0.0.1:27017/
```

---

# Running the Project

### Assignment 1

```powershell
python image_segregation.py
```

### Assignment 2 / 3

```powershell
python location_segregation.py
```

### Assignment 4

```powershell
python assignment_4.py
```

---

# GitHub Repository

The project source code is maintained in this repository:

**Image Metadata Project**

https://github.com/Ankita9919/Image_Metadata_Project

---

# Privacy Note

The project processes image metadata and personal photographs locally.

For privacy and repository-size reasons, the actual image dataset and personal photographs are not included in the public GitHub repository.

Only the required Python source code and project documentation are maintained in GitHub.

---

# Learning Outcomes

Through this project, the following concepts were practiced:

* Python file and folder handling
* Image EXIF metadata extraction
* Image classification using metadata
* Location-based image filtering
* Python-MongoDB connectivity
* MongoDB database and collection management
* Document insertion and querying
* Dictionary-based user input
* Menu-driven Python applications
* Git and GitHub version control
* Data organization and privacy-aware dataset handling

---

## Author

**Ankita Mandal**

B.Tech CSE
Adamas University


