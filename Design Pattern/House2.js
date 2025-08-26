var PlumbingSystem = /** @class */ (function () {
    function PlumbingSystem() {
    }
    PlumbingSystem.prototype.setPressure = function (v) {
        console.log("Plumbing pressure set to ".concat(v, " PSI"));
    };
    PlumbingSystem.prototype.turnOn = function () {
        console.log("Plumbing system turned ON");
    };
    PlumbingSystem.prototype.turnOff = function () {
        console.log("Plumbing system turned OFF");
    };
    return PlumbingSystem;
}());
var ElectricalSystem = /** @class */ (function () {
    function ElectricalSystem() {
    }
    ElectricalSystem.prototype.setVoltage = function (v) {
        console.log("Electrical voltage set to ".concat(v, "V"));
    };
    ElectricalSystem.prototype.turnOn = function () {
        console.log("Electrical system turned ON");
    };
    ElectricalSystem.prototype.turnOff = function () {
        console.log("Electrical system turned OFF");
    };
    return ElectricalSystem;
}());
var House = /** @class */ (function () {
    function House() {
        this.plumbing = new PlumbingSystem();
        this.electrical = new ElectricalSystem();
    }
    House.prototype.turnOnSystems = function () {
        this.electrical.setVoltage(120);
        this.electrical.turnOn();
        this.plumbing.setPressure(500);
        this.plumbing.turnOn();
        console.log("All systems are up and running 🚀");
    };
    House.prototype.shutdown = function () {
        this.electrical.turnOff();
        this.plumbing.turnOff();
        console.log("All systems have been shut down 📴");
    };
    return House;
}());
// Client code
var client = new House();
client.turnOnSystems();
client.shutdown();
