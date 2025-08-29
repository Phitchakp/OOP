var ElectricalSystem = /** @class */ (function () {
    function ElectricalSystem() {
    }
    ElectricalSystem.prototype.setVoltage = function (vol) {
        console.log("Electrical voltage set to ".concat(vol, "V"));
    };
    ElectricalSystem.prototype.turnOn = function () {
        console.log("Electrical system turned ON");
    };
    ElectricalSystem.prototype.turnOff = function () {
        console.log("Electrical system turned OFF !!");
    };
    return ElectricalSystem;
}());
var PlumbingSystem = /** @class */ (function () {
    function PlumbingSystem() {
    }
    PlumbingSystem.prototype.setPressure = function (press) {
        console.log("Plumbing pressure set to ".concat(press, " PSI"));
    };
    PlumbingSystem.prototype.turnOn = function () {
        console.log("Plumbing system turned ON");
    };
    PlumbingSystem.prototype.turnOff = function () {
        console.log("Plumbing system turned OFF !!");
    };
    return PlumbingSystem;
}());
var GasSystem = /** @class */ (function () {
    function GasSystem() {
    }
    GasSystem.prototype.setFlowRate = function (rate) {
        console.log("Gas flow set to ".concat(rate, " m\u00B3/h"));
    };
    GasSystem.prototype.turnOn = function () {
        console.log("Gas system turned ON");
    };
    GasSystem.prototype.turnOff = function () {
        console.log("Gas system turned OFF !!");
    };
    return GasSystem;
}());
var Payment = /** @class */ (function () {
    function Payment() {
    }
    Payment.prototype.setPayment = function (name, pay) {
        console.log("".concat(name, " has already paid ").concat(pay, " Euro"));
    };
    return Payment;
}());
var House = /** @class */ (function () {
    function House(name, pay) {
        if (pay === void 0) { pay = 0; }
        this.payment = new Payment();
        this.plumbing = new PlumbingSystem();
        this.electrical = new ElectricalSystem();
        this.gas = new GasSystem();
        this.name = name;
        this.pay = pay;
    }
    House.prototype.turnOnSystems = function () {
        this.payment.setPayment(this.name, this.pay);
        this.electrical.setVoltage(120);
        this.electrical.turnOn();
        this.plumbing.setPressure(500);
        this.plumbing.turnOn();
        this.gas.setFlowRate(15);
        this.gas.turnOn();
        console.log("All systems are up and running 🚀");
    };
    House.prototype.shutdown = function () {
        this.electrical.turnOff();
        this.plumbing.turnOff();
        this.gas.turnOff();
        console.log("All systems have been shut down 📴");
        console.log("Dear ".concat(this.name, ", Please contact to our oprator"));
    };
    return House;
}());
// Client code
var alice = new House('Alice', 500);
alice.turnOnSystems();
// const bob = new House("Bob");
// bob.shutdown();
