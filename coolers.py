"""
    Nysa Clark
    Module 01 Programming Assignment
    Part B

    This program ...
"""

# class to keep track of the company's refillable water cooler

# attributes ("variables"):
# cooler location (ex: "break room", "warehouse")
# remaining water (in gallons)
# a constructor w/ a arguments/params for each attribute
# methods:
# a method to call when employee fills their bottle ...
# reduces the remaining water by half a gallon

# a method that replace supply, which resets the remaining water to 20 gallons

# a method to change the location of the cooler


class Cooler:
    def __init__(self, location, remaining_water):
        self.location = location
        self.remaining_water = remaining_water

    def fill_bottle(self):
        if self.remaining_water >= 0.5:
            self.remaining_water -= 0.5
        else:
            print("No more water.")

    def refill(self):
        self.remaining_water = 20

    def relocate(self, new_location):
        self.location = new_location


# create at least 2 water cooler instances
# & then simulate some usage of each by calling all of the methods
# can run automatically or ask the user for input & then display results

cooler1 = Cooler("break room", 1.5)

print(f"Cooler 1 is in the {cooler1.location}.")
print(f"Cooler 1 has {cooler1.remaining_water} gallons remaining.")
cooler1.fill_bottle()
cooler1.fill_bottle()
print(f"Cooler 1 has {cooler1.remaining_water} gallons remaining.")


cooler2 = Cooler("warehouse", 15)
cooler2.refill()
print(f"Cooler 2 has {cooler2.remaining_water} gallons remaining.")

cooler2.relocate("conference room")
print(f"Cooler 2 has been relocated to the {cooler2.location}.")
