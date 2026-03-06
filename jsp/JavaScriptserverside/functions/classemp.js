class Employee {
  // The constructor maps your variables to the new object
  constructor(empId, firstName, lastName, desg, salary, leaveType, emailId, mobileNo) {
    this.empId = empId;
    this.firstName = firstName;
    this.lastName = lastName;
    this.desg = desg;       // Short for Designation
    this.salary = salary;
    this.leaveType = leaveType;
    this.emailId = emailId;
    this.mobileNo = mobileNo;
  }
}

// Creating the first employee object
const empObj1 = new Employee( 
  101, 
  "Amit", 
  "Sharma", 
  "Software Engineer", 
  75000, 
  "Sick Leave", 
  "amit.s@company.com", 
  "9876543210"
);

// Creating the second employee object
const empObj2 = new Employee(
  102, 
  "Sita", 
  "Verma", 
  "Project Manager", 
  95000, 
  "Annual Leave", 
  "sita.v@company.com", 
  "9123456789"
);

console.log(empObj1);
console.log(empObj2);