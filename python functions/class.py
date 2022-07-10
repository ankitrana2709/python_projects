class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
flight = Flight(3)
peoples = ["Ankit","Byomkesh","Chatterjee","Dakshin"]
for people in peoples:
    success = flight.add_passenger(people)
    if success:
        print(f"Added {people} to flight successfully.")
    else:
        print(f"No available seats for {people}.")

