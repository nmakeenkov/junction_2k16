class QuadcopterController:
    def set_y_velocity(self, power):
        assert power >= -100 and power <= 100

    def set_x_velocity(self, power):
        assert power >= -100 and power <= 100

    def land(self):
        pass

    def take_off(self):
        pass


class Quadcopter:
    def get_controller(self):
        pass

    def get_id(self):
        pass

    def get_x(self):
        pass

    def get_y(self):
        pass

    def get_charge_level(self):
        pass

class Human:
    def get_id(self):
        pass

    def get_x(self):
        pass

    def get_y(self):
        pass


class Wall:
    # (x, y)
    def get_point1(self):
        pass

    def get_point2(self):
        pass


class ChargingStation:
    def get_x(self):
        pass

    def get_y(self):
        pass


class Room:
    def get_walls(self):
        pass

    def get_charging_stations(self):
        pass

    def get_people(self):
        pass

    def get_quadcopters(self):
        pass
