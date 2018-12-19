class car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self):
        old_speed = self.speed
        new_speed = old_speed + 10
        self.speed = new_speed

    def decelerate(self):
        self.speed -= 10

    def speedchange(self, how_much):
        old_speed = self.speed
        new_speed = old_speed + how_much
        Non_negative_number = how_much (????)
        if how_much > 0:
            print("Car speeds up by how_much mph")
            self.speed = self.speed + how_much
        if new_speed > 0:
            print("Car reduces speed by how_much mph")
            self.speed = self.speed + how_much
        if new_speed < 0:
            print("Car slows to a stop")
            self.speed = 0
        else:
            print("Car maintains speed")

    def currentspeed (self, how_fast):
        old_speed = self.speed
        new_speed = how_fast
        self.speed = how_fast
        if old_speed > 0 and how_fast < 0:
            print("Car slows to a stop")
            self.speed = 0

        if old_speed > 0 and how_fast = 0:
            print("Car slows to a stop")
            self.speed = 0

        if old_speed = 0:
            print("Car remains stopped")
            self.speed = 0

        if how_fast > old_speed:
            print("Car speeds up to how_fast mph")
            self.speed = self.speed + how_much

        if how_fast < old_speed:
            print("Car reduces speed to how_fast mph")
            self.speed = 0

        else:
            print("Car maintains speed")


class conductor:
    def __init__(self, api_key=None):

        @property
        def api_key(self):...

        def get_track_circuits(self):...

        def get_lines(self):...

        def get_stations(self, line_code):...

        def get_station_parking_information(self, station_code): ...

        def get_station_lat_lon(self): ...

        def get_train_positions(self): ...

class TrackCircuit:...

class DevilsObject:...

Speed_change
If how_much = positive number, print “Car speeds up by how_much”
If how_much = negative number but new_speed minus how_much is greater than 0, print “Car reduces speed by how_much”
If how_much = negative number but new_speed minus how_much is less than 0, print “Car slows to a stop”
Current_speed
If how_fast = greater new_speed, print “Car speeds up to how_fast”
If how_fast = less than new_speed but greater than 0, print “Car reduces speed to how_fast”
If how_fast = less than new_speed but less than 0, print “Car slows to a stop”


