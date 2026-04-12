const mysql = require("mysql2");

const db = mysql.createConnection({
  host: "localhost",
  user: "root", // change this
  password: "root@123", // change this
  database: "student_db"
});

db.connect((err) => {
  if (err) {
    console.error("Database connection failed:", err);
  } else {
    console.log("Connected to MySQL");
  }
});

module.exports = db;