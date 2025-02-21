class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"Calling {number} from {self.model}..... ")

    def get_info(self):
        return f"{self.brand} {self.model} - ${self.price}"
    
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, health_monitoring):
        super().__init__(brand, model, price)  
        self.health_monitoring = health_monitoring  

    def track_heart_rate(self):
        print(f"{self.model} is tracking heart rate ")

    def get_info(self):  # Overriding parent method (Polymorphism)
        return f"{self.brand} {self.model} - ${self.price} (Health: {self.health_monitoring})"

# Creating objects
phone = Smartphone("Apple", "iPhone 15", 999)
watch = Smartwatch("Samsung", "Galaxy Watch 6", 299, "Enabled")

# Using methods
print(phone.get_info())  
phone.call("123-456-7890")

print(watch.get_info())  
watch.track_heart_rate()


#Assignment 2

class Vehicle:
    def move(self):
        pass  

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()