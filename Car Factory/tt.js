// =======================================================
// Main simulation class to run the Car Factory
// =======================================================
public class CarFactorySimulator {

    public static void main(String[] args) {
        System.out.println("🚗 Car Factory Simulator - Running the Java Version 🚗\n");

        // Set up the chain of responsibility for validation rules.
        ValidationHandler sportsCarSafetyRule = new SportsCarSafetyRuleHandler();
        ValidationHandler mandatoryAudioRule = new MandatoryAudioRuleHandler();
        sportsCarSafetyRule.setNext(mandatoryAudioRule);

        // Set up the Observer pattern. The factory is the subject.
        CarFactorySubject carFactorySubject = new CarFactorySubject();
        carFactorySubject.addObserver(new QualityControlObserver());
        carFactorySubject.addObserver(new ShippingObserver());
        carFactorySubject.addObserver(new MarketingObserver());

        // --- SIMULATION 1: Building a valid Sports Car ---
        System.out.println("--- SIMULATION 1: Attempting to build a valid Sports Car ---");
        System.out.println("   (Expecting success with Safety and Premium Audio packages)");
        try {
            // Define the order
            String carType = "Sports Car";
            String[] selectedPackages = {"Sports Package", "Premium Audio", "Safety Upgrades"};

            // 1. Chain of Responsibility: Validate the order
            System.out.println("\n[System] Validating order for " + carType + "...");
            ValidationResult validationResult = sportsCarSafetyRule.handle(carType, selectedPackages);

            if (!validationResult.isSuccess()) {
                System.out.println("🛑 Order Rejected: " + validationResult.getMessage());
                return;
            }

            // 2. Factory Method: Create the base car
            System.out.println("\n[System] Order validated successfully. Proceeding with production.");
            Car myCar = CarFactory.buildCar(carType);

            // 3. Decorator: Apply customization packages
            System.out.println("[System] Applying selected packages...");
            for (String pkg : selectedPackages) {
                myCar = CarDecoratorFactory.applyPackage(myCar, pkg);
                System.out.println("    - " + pkg + " applied.");
            }

            // Final output of the built car
            System.out.println("\n🎉 Car Production Complete!");
            System.out.println("   - Type: " + myCar.getDescription());
            System.out.println("   - Features: " + String.join(", ", myCar.getFeatures()));

            // 4. Observer: Notify departments
            System.out.println("\n[System] Notifying observers of new car production...");
            carFactorySubject.notifyObservers("carProduced", myCar);
            
        } catch (Exception e) {
            System.err.println("🛑 An error occurred: " + e.getMessage());
        }

        System.out.println("\n" + "=".repeat(60) + "\n");

        // --- SIMULATION 2: Building an invalid Sports Car (missing Safety) ---
        System.out.println("--- SIMULATION 2: Attempting to build an invalid Sports Car ---");
        System.out.println("   (Expecting rejection due to missing Safety Upgrades)");
        try {
            // Define the invalid order
            String carType = "Sports Car";
            String[] selectedPackages = {"Sports Package", "Premium Audio"};

            // 1. Chain of Responsibility: Validate the order
            System.out.println("\n[System] Validating order for " + carType + "...");
            ValidationResult validationResult = sportsCarSafetyRule.handle(carType, selectedPackages);

            if (!validationResult.isSuccess()) {
                System.out.println("🛑 Order Rejected: " + validationResult.getMessage());
                // The simulation stops here as expected
            } else {
                System.out.println("\n[System] Order validated successfully. Proceeding with production.");
                Car myCar = CarFactory.buildCar(carType);
                System.out.println("[System] Applying selected packages...");
                for (String pkg : selectedPackages) {
                    myCar = CarDecoratorFactory.applyPackage(myCar, pkg);
                    System.out.println("    - " + pkg + " applied.");
                }
                System.out.println("\n🎉 Car Production Complete!");
                carFactorySubject.notifyObservers("carProduced", myCar);
            }
        } catch (Exception e) {
            System.err.println("🛑 An error occurred: " + e.getMessage());
        }
    }
}

// =======================================================
// Interface and Classes for the Factory Method and Decorator Patterns
// =======================================================

/**
 * The base interface for a Car. This is the Component
 * in the Decorator pattern.
 */
interface Car {
    String getDescription();
    String[] getFeatures();
    String getType();
}

/**
 * Concrete Component for a Sedan.
 */
class Sedan implements Car {
    private final String type = "Sedan";

    @Override
    public String getDescription() {
        return "A comfortable " + type + ".";
    }

    @Override
    public String[] getFeatures() {
        return new String[]{"Base features of a " + type};
    }

    @Override
    public String getType() {
        return this.type;
    }
}

/**
 * Concrete Component for an SUV.
 */
class SUV implements Car {
    private final String type = "SUV";

    @Override
    public String getDescription() {
        return "A versatile " + type + ".";
    }

    @Override
    public String[] getFeatures() {
        return new String[]{"Base features of an " + type};
    }

    @Override
    public String getType() {
        return this.type;
    }
}

/**
 * Concrete Component for a Sports Car.
 */
class SportsCar implements Car {
    private final String type = "Sports Car";

    @Override
    public String getDescription() {
        return "A high-performance " + type + ".";
    }

    @Override
    public String[] getFeatures() {
        return new String[]{"Base features of a " + type};
    }

    @Override
    public String getType() {
        return this.type;
    }
}

/**
 * The Factory for creating different types of cars.
 * This class uses the Factory Method pattern.
 */
class CarFactory {
    public static Car buildCar(String carType) {
        System.out.println("[Factory] Initiating production for a new " + carType + "...");
        switch (carType.toLowerCase()) {
            case "sedan":
                return new Sedan();
            case "suv":
                return new SUV();
            case "sports car":
                return new SportsCar();
            default:
                throw new IllegalArgumentException("Unknown car type: " + carType);
        }
    }
}

/**
 * The base Decorator class. It must implement the same
 * interface as the component it wraps.
 */
abstract class CarDecorator implements Car {
    protected Car decoratedCar;

    public CarDecorator(Car decoratedCar) {
        this.decoratedCar = decoratedCar;
    }

    @Override
    public String getDescription() {
        return decoratedCar.getDescription();
    }

    @Override
    public String[] getFeatures() {
        return decoratedCar.getFeatures();
    }
    
    @Override
    public String getType() {
        return decoratedCar.getType();
    }
}

/**
 * Concrete Decorator for a Sports Package.
 */
class SportsPackageDecorator extends CarDecorator {
    public SportsPackageDecorator(Car decoratedCar) {
        super(decoratedCar);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " with a Sports Package.";
    }

    @Override
    public String[] getFeatures() {
        String[] originalFeatures = super.getFeatures();
        String[] newFeatures = new String[originalFeatures.length + 2];
        System.arraycopy(originalFeatures, 0, newFeatures, 0, originalFeatures.length);
        newFeatures[originalFeatures.length] = "Sport-tuned suspension";
        newFeatures[originalFeatures.length + 1] = "Upgraded alloy wheels";
        return newFeatures;
    }
}

/**
 * Concrete Decorator for a Premium Audio Package.
 */
class PremiumAudioDecorator extends CarDecorator {
    public PremiumAudioDecorator(Car decoratedCar) {
        super(decoratedCar);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " with Premium Audio.";
    }

    @Override
    public String[] getFeatures() {
        String[] originalFeatures = super.getFeatures();
        String[] newFeatures = new String[originalFeatures.length + 2];
        System.arraycopy(originalFeatures, 0, newFeatures, 0, originalFeatures.length);
        newFeatures[originalFeatures.length] = "High-fidelity sound system";
        newFeatures[originalFeatures.length + 1] = "Enhanced speakers";
        return newFeatures;
    }
}

/**
 * Concrete Decorator for Safety Upgrades.
 */
class SafetyUpgradesDecorator extends CarDecorator {
    public SafetyUpgradesDecorator(Car decoratedCar) {
        super(decoratedCar);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " with Safety Upgrades.";
    }

    @Override
    public String[] getFeatures() {
        String[] originalFeatures = super.getFeatures();
        String[] newFeatures = new String[originalFeatures.length + 2];
        System.arraycopy(originalFeatures, 0, newFeatures, 0, originalFeatures.length);
        newFeatures[originalFeatures.length] = "Advanced driver assistance systems";
        newFeatures[originalFeatures.length + 1] = "Enhanced airbag deployment";
        return newFeatures;
    }
}

/**
 * A simple factory for applying decorators.
 */
class CarDecoratorFactory {
    public static Car applyPackage(Car car, String packageName) {
        switch (packageName) {
            case "Sports Package":
                return new SportsPackageDecorator(car);
            case "Premium Audio":
                return new PremiumAudioDecorator(car);
            case "Safety Upgrades":
                return new SafetyUpgradesDecorator(car);
            default:
                throw new IllegalArgumentException("Unknown package: " + packageName);
        }
    }
}

// =======================================================
// Interface and Classes for the Chain of Responsibility Pattern
// =======================================================

/**
 * Class to hold the result of a validation check.
 */
class ValidationResult {
    private final boolean success;
    private final String message;

    public ValidationResult(boolean success, String message) {
        this.success = success;
        this.message = message;
    }

    public boolean isSuccess() {
        return success;
    }

    public String getMessage() {
        return message;
    }
}

/**
 * Abstract Handler for the Chain of Responsibility.
 */
abstract class ValidationHandler {
    protected ValidationHandler next;

    public ValidationHandler setNext(ValidationHandler next) {
        this.next = next;
        return next;
    }

    public ValidationResult handle(String carType, String[] selectedPackages) {
        if (this.next != null) {
            return this.next.handle(carType, selectedPackages);
        }
        return new ValidationResult(true, "All checks passed.");
    }
}

/**
 * A concrete Handler that checks if a Sports Car has Safety Upgrades.
 */
class SportsCarSafetyRuleHandler extends ValidationHandler {
    @Override
    public ValidationResult handle(String carType, String[] selectedPackages) {
        if (carType.equals("Sports Car")) {
            boolean hasSafetyPackage = false;
            for (String pkg : selectedPackages) {
                if (pkg.equals("Safety Upgrades")) {
                    hasSafetyPackage = true;
                    break;
                }
            }
            if (!hasSafetyPackage) {
                return new ValidationResult(false, "Rule Violation: Sports Cars must have Safety Upgrades for production.");
            }
            System.out.println("[Validation] ✔️ Passed rule for Sports Car safety.");
        }
        return super.handle(carType, selectedPackages);
    }
}

/**
 * A concrete Handler that checks if every car has Premium Audio.
 */
class MandatoryAudioRuleHandler extends ValidationHandler {
    @Override
    public ValidationResult handle(String carType, String[] selectedPackages) {
        boolean hasAudioPackage = false;
        for (String pkg : selectedPackages) {
            if (pkg.equals("Premium Audio")) {
                hasAudioPackage = true;
                break;
            }
        }
        if (!hasAudioPackage) {
            return new ValidationResult(false, "Rule Violation: All cars must have the Premium Audio package.");
        }
        System.out.println("[Validation] ✔️ Passed rule for mandatory audio.");
        return super.handle(carType, selectedPackages);
    }
}


// =======================================================
// Interface and Classes for the Observer Pattern
// =======================================================

import java.util.ArrayList;
import java.util.List;

/**
 * The Subject in the Observer pattern.
 */
class CarFactorySubject {
    private List<Observer> observers = new ArrayList<>();

    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    public void notifyObservers(String event, Car car) {
        for (Observer observer : observers) {
            observer.update(event, car);
        }
    }
}

/**
 * The Observer interface.
 */
interface Observer {
    void update(String event, Car car);
}

/**
 * A concrete Observer: Quality Control Department.
 */
class QualityControlObserver implements Observer {
    @Override
    public void update(String event, Car car) {
        if (event.equals("carProduced")) {
            System.out.println("[Quality Control] 🔍 New " + car.getType() + " produced. Performing final inspection...");
        }
    }
}

/**
 * A concrete Observer: Shipping Department.
 */
class ShippingObserver implements Observer {
    @Override
    public void update(String event, Car car) {
        if (event.equals("carProduced")) {
            System.out.println("[Shipping] 📦 " + car.getType() + " ready for shipment to the dealership.");
        }
    }
}

/**
 * A concrete Observer: Marketing Department.
 */
class MarketingObserver implements Observer {
    @Override
    public void update(String event, Car car) {
        if (event.equals("carProduced")) {
            System.out.println("[Marketing] 📢 Promoting the new " + car.getType() + " with the following features: " + String.join(", ", car.getFeatures()) + ".");
        }
    }
}
