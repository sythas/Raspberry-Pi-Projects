from ping import Ping

# this class combines all of the cars ping sensors into a single component.
# will return a dict with front, right, left, and back measurements and a shift
# amount that gives you the delta of the right measurement between this and the
# lookup
class Location:
    def __init__(self, sample):
        self.sample = sample

        self.front = Ping(33, 35)
        self.right = Ping(29, 31)
        #self.back = Ping(38, 40)
        #self.left = Ping(16, 18)
	self.previous = { 'right': -1 }

    def getLocation(self):
        right = self.right.measure(self.sample)
        shift = right - self.previous['right'] if self.previous['right'] > -1 else 0

        self.previous = {
            'front': self.front.measure(self.sample),
            'right': right,
            'shift': shift
        }

        return self.previous

    def getFront(self):
        return self.front.measure(1)

    def getRight(self):
        return self.right.measure(1)
