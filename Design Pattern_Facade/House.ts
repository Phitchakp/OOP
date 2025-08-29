class ElectricalSystem {
    setVoltage(vol: number): void {
        console.log(`Electrical voltage set to ${vol}V`);
    }
    turnOn(): void {
        console.log("Electrical system turned ON");
    }
    turnOff(): void {
        console.log("Electrical system turned OFF !!");
    }
}


class PlumbingSystem {
    setPressure(press: number): void {
        console.log(`Plumbing pressure set to ${press} PSI`);
    }
    turnOn(): void {
        console.log("Plumbing system turned ON");
    }
    turnOff(): void {
        console.log("Plumbing system turned OFF !!");
    }
}


class GasSystem {
    setFlowRate(rate: number): void {
        console.log(`Gas flow set to ${rate} m³/h`);
    }
    turnOn(): void {
        console.log("Gas system turned ON");
    }
    turnOff(): void {
        console.log("Gas system turned OFF !!");
    }
}


class Payment{
    setPayment(name: string ,pay: number): void {
        console.log(`${name} has already paid ${pay} Euro`);
    }
}



class House {
    private name : string;
    private pay : number;
    private payment = new Payment();
    private plumbing = new PlumbingSystem();
    private electrical = new ElectricalSystem();
    private gas = new GasSystem();

    constructor(name:string, pay:number =0) {
        this.name = name;
        this.pay = pay;
    }

    public turnOnSystems(): void {
        this.payment.setPayment(this.name, this.pay)
        this.electrical.setVoltage(120);
        this.electrical.turnOn();
        this.plumbing.setPressure(500);
        this.plumbing.turnOn();
        this.gas.setFlowRate(15);
        this.gas.turnOn();

        console.log("All systems are up and running 🚀");
    }

    public shutdown(): void {
        this.electrical.turnOff();
        this.plumbing.turnOff();
        this.gas.turnOff();
        console.log("All systems have been shut down 📴");
        console.log(`Dear ${this.name}, Please contact to our oprator`)
    }
}

// Client code
const alice = new House('Alice', 500);
alice.turnOnSystems();

const bob = new House("Bob");
bob.shutdown();


