from lib import car_dir

class Stearing:
    def __init__(self):
        car_dir.setup()
        car_dir.home()

    def turn(angle):
        if angle > 50 || angle < -50:
            return

        cur_dir.turn(450 + angle)