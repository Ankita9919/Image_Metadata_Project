# Assignment 1 - MongoDB CRUD Operations

## Objective

Perform database and collection operations using MongoDB and MongoDB Shell.

## Database

Database Name: `sample`

Collection Name: `sample`

## Operations Performed

1. Created/selected the `sample` database.
2. Inserted 5 student documents into the `sample` collection.
3. Updated the department of all students to `CSE`.
4. Updated the age of all 5 students.
5. Updated department based on age:
   - Even age → `BCA`
   - Odd age → `CSE`
6. Added dummy Aadhaar numbers to all documents.
7. Displayed serial number, document serial number, and insertion timestamp in IST.
8. Created the `BTech_D Sample` collection.
9. Dropped the `BTech_D Sample` collection.

## Final Data

| Serial No. | Document Serial No. | Name | Age | Department |
|---|---|---|---:|---|
| 1 | DOC001 | Student1 | 21 | CSE |
| 2 | DOC002 | Student2 | 24 | BCA |
| 3 | DOC003 | Student3 | 23 | CSE |
| 4 | DOC004 | Student4 | 20 | BCA |
| 5 | DOC005 | Student5 | 25 | CSE |

## Timestamp

The insertion timestamp was obtained from the MongoDB ObjectId and converted to Indian Standard Time using `Asia/Kolkata`.

## Technologies Used

- MongoDB
- MongoDB Shell (mongosh)
- JavaScript

## Files

- `mongo_commands.js` - Contains all MongoDB commands used for this assignment.
- `README.md` - Documentation of the assignment.

## Note

Dummy Aadhaar values were used for demonstration purposes.
No real Aadhaar information is included in this repository.