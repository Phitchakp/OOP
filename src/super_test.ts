class A {

    constructor(name, age){
        this.name = name;
        this.age = age;
    }
}
/*
class B extends A {
    speed: number;


    constructor(name, age, speed){
        super(name, age);
        this.speed = speed;
    }
}
*/

const v1 = new A("Andy", 1);

console.log(v1.name);
console.log(v1.age);
