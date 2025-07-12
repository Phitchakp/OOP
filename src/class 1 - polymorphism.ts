abstract class Animal {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  makeSound(): void {}
}

class Dog extends Animal {
  private breed: string;
  private isHungry: boolean;

  constructor(givenName: string, givenBreed: string) {
    super(givenName);
    this.breed = givenBreed;
    this.isHungry = true;
  }

  feed(): void {
    if (this.isHungry) {
      console.log("eating...");
    } else {
      console.log("The dog is not eating");
    }
    if (this.breed === "Pitbul") {
      this.isHungry = true;
    } else {
      this.isHungry = false;
    }
    console.log(
      `The dog eat and is ${this.isHungry ? "hungry" : "not hungry"}`
    );
  }

  checkIsHungry(): boolean {
    return this.isHungry;
  }

  makeSound(): void {
    console.log(`Woof! ${this.name} is barking`);
  }
}

const bob: Dog = new Dog("Bob", "Pitbul");
bob.feed();
bob.feed();
console.log("is bob hungry", bob.checkIsHungry());

const john: Dog = new Dog("John", "Golden Retrieve");
john.feed();
john.feed();
console.log("is john hungry", john.checkIsHungry());

class Cat extends Animal {
  constructor(name: string) {
    super(name);
  }
  makeSound(): void {
    console.log(`Meow! ${this.name} is meowing`);
  }
}

const titi: Cat = new Cat("Titi");

const myListOfAnimals: Animal[] = [bob, titi];

myListOfAnimals.forEach((animal) => animal.makeSound());
