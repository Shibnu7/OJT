class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

class Bus(Vehicle):
    def __init__(self, seating_capacity=50):
        super().__init__(seating_capacity)


bus = Bus()
print(f"Bus seating capacity: {bus.capacity}")
