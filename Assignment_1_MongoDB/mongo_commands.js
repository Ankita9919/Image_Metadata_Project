use sample

db.sample.insertMany([
    {
        serial_no: 1,
        document_serial_no: "DOC001",
        name: "Student1",
        age: 20
    },
    {
        serial_no: 2,
        document_serial_no: "DOC002",
        name: "Student2",
        age: 21
    },
    {
        serial_no: 3,
        document_serial_no: "DOC003",
        name: "Student3",
        age: 22
    },
    {
        serial_no: 4,
        document_serial_no: "DOC004",
        name: "Student4",
        age: 19
    },
    {
        serial_no: 5,
        document_serial_no: "DOC005",
        name: "Student5",
        age: 23
    }
])

db.sample.updateMany(
    {},
    { $set: { department: "CSE" } }
)

db.sample.updateOne(
    { serial_no: 1 },
    { $set: { age: 21 } }
)

db.sample.updateOne(
    { serial_no: 2 },
    { $set: { age: 24 } }
)

db.sample.updateOne(
    { serial_no: 3 },
    { $set: { age: 23 } }
)

db.sample.updateOne(
    { serial_no: 4 },
    { $set: { age: 20 } }
)

db.sample.updateOne(
    { serial_no: 5 },
    { $set: { age: 25 } }
)

db.sample.updateMany(
    { age: { $mod: [2, 0] } },
    { $set: { department: "BCA" } }
)

db.sample.updateMany(
    { age: { $mod: [2, 1] } },
    { $set: { department: "CSE" } }
)

db.sample.updateOne(
    { serial_no: 1 },
    { $set: { aadhar: "XXXX-XXXX-1001" } }
)

db.sample.updateOne(
    { serial_no: 2 },
    { $set: { aadhar: "XXXX-XXXX-1002" } }
)

db.sample.updateOne(
    { serial_no: 3 },
    { $set: { aadhar: "XXXX-XXXX-1003" } }
)

db.sample.updateOne(
    { serial_no: 4 },
    { $set: { aadhar: "XXXX-XXXX-1004" } }
)

db.sample.updateOne(
    { serial_no: 5 },
    { $set: { aadhar: "XXXX-XXXX-1005" } }
)

db.sample.find(
    {},
    {
        _id: 0,
        serial_no: 1,
        document_serial_no: 1,
        name: 1,
        age: 1,
        department: 1,
        aadhar: 1
    }
)

db.sample.aggregate([
    {
        $project: {
            _id: 0,
            serial_no: 1,
            document_serial_no: 1,
            timestamp_IST: {
                $dateToString: {
                    date: { $toDate: "$_id" },
                    format: "%Y-%m-%d %H:%M:%S",
                    timezone: "Asia/Kolkata"
                }
            }
        }
    }
])

db.createCollection("BTech_D Sample")

show collections

db["BTech_D Sample"].drop()

show collections