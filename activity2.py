# create class
class vehicle:

    # create init method
    def __init__(self, max_speed, mileage):

        # bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage

# object creation
modelx = vehicle(240, 18)

# access the variables inside init method
print("model max speed is", modelx.max_speed)
print("model mileage is", modelx.mileage)