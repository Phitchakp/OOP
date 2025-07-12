class Student {
    constructor(a1, a2, a3, a4) {
        this.name = a1;
        this.age = a2;
        this.grade = a3;
        this.address = a4;
    }
    toString() {
        return `Name: ${this.name}, Age: ${this.age}, Grade: ${this.grade}, Address: ${this.address}`;
    }
}
class StudentManagementSystem {
    constructor() {
        this.students = [];
    }
    addStudent(Student) {
        this.students.push(Student);
    }
    printStudents() {
        this.students.forEach((student) => {
            console.log(student.toString());
        });
    }
}
// Main
const sms = new StudentManagementSystem();
const alice = new Student("Alice", 20, "A", "UK");
const bob = new Student("Bob", 22, "B", "Italy");
sms.addStudent(alice);
sms.addStudent(bob);
sms.printStudents();
