class Student{
    private name: String;
    private age: Number;
    private grade: String
    address: String;

    constructor (a1:string, a2:number, a3:string, a4:string) {
        this.name = a1;
        this.age = a2;
        this.grade = a3;
        this.address = a4;
    }

    toString() {
        return `Name: ${this.name}, Age: ${this.age}, Grade: ${this.grade}, Address: ${this.address}` ;
    }
}

class StudentManagementSystem {
    students: Student[];
    constructor() {
        this.students = [];
    }

    addStudent(Student: Student) {
        this.students.push(Student);
    }

    printStudents() {
        this.students.forEach((student) => {
            console.log( student.toString());
        });
    }
}

// Main
const sms = new StudentManagementSystem() ;
const alice = new Student( "Alice", 20, "A", "UK");
const bob = new Student("Bob", 22, "B", "Italy");
sms.addStudent(alice);
sms.addStudent(bob);
sms.printStudents();

