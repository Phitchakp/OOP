interface IAnimal {
  name: string;
  eat(): void;
}

interface IDog {
  breed: string;
  numberOfLegs: number;

  bark(): void;
}

interface ILandAnimal {
  move(): void;
}

abstract class Animal implements IAnimal {
  name: string;
  eat(): void {
    console.log("Eating...");
  }
}

class Dog extends Animal implements ILandAnimal, IDog {
  breed: string;
  name: string;
  numberOfLegs: number;

  constructor(name: string, breed: string) {
    super();
    this.name = name;
    this.breed = breed;
  }

  bark(): void {
    console.log("Barking");
  }

  move(): void {
    console.log("Moving");
  }
}

const bob = new Dog("Bob", "PitBul");

const animalAsInterface: IAnimal[] = [bob];
const animalAsClass: Animal[] = [bob];

console.log("is Animal", bob instanceof Animal);
console.log("is Dog", bob instanceof Dog);
