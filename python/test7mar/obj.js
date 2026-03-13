function createEmp(name, id, department, salary) {
    const employee = {
        name: name,
        id: id,
        department: department,
        salary: salary
    };

    return employee;
}

let emp1 = createEmp("Rutvik", 101, "IT", 50000);
console.log(emp1);