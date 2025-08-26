class PlumbingSystem {
    setPressure(v: number): void {
        console.log(`Plumbing pressure set to ${v} PSI`);
    }
    turnOn(): void {
        console.log("Plumbing system turned ON");
    }
    turnOff(): void {
        console.log("Plumbing system turned OFF");
    }
}

class ElectricalSystem {
    setVoltage(v: number): void {
        console.log(`Electrical voltage set to ${v}V`);
    }
    turnOn(): void {
        console.log("Electrical system turned ON");
    }
    turnOff(): void {
        console.log("Electrical system turned OFF");
    }
}

class House {
    private plumbing = new PlumbingSystem();
    private electrical = new ElectricalSystem();

    public turnOnSystems(): void {
        this.electrical.setVoltage(120);
        this.electrical.turnOn();
        this.plumbing.setPressure(500);
        this.plumbing.turnOn();
        console.log("All systems are up and running 🚀");
    }

    public shutdown(): void {
        this.electrical.turnOff();
        this.plumbing.turnOff();
        console.log("All systems have been shut down 📴");
    }
}

// Client code
const client = new House();
client.turnOnSystems();
client.shutdown();

