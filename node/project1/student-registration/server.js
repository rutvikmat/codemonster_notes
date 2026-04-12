const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const db = require("./db");

const app = express();
const PORT = 3000;

app.use(cors());
app.use(bodyParser.json());
app.use(express.static("public"));

/* POST API - Add Student */
app.post("/add-student", (req, res) => {
  const { name, email, course } = req.body;

  if (!name || !email || !course) {
    return res.status(400).json({ message: "All fields are required" });
  }

  const sql = "INSERT INTO students (name, email, course) VALUES (?, ?, ?)";
  
  db.query(sql, [name, email, course], (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).json({ message: "Database error" });
    } else {
      res.json({ message: "Student added successfully" });
    }
  });
});

/* GET API - Fetch Students */
app.get("/students", (req, res) => {
  const sql = "SELECT * FROM students";

  db.query(sql, (err, results) => {
    if (err) {
      console.error(err);
      res.status(500).json({ message: "Database error" });
    } else {
      res.json(results);
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});