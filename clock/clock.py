class Clock:
    def __init__(self, hour, min):
        self.min = (hour * 60 + min) % 60
        self.hour = ((hour * 60 + min) // 60) % 24 

    def __repr__(self):
        return "%02d:%02d" %(self.hour, self.min)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def add(self, min):
        self.hour = ((self.hour * 60 + min + self.min) // 60) % 24
        self.min = (self.min + min) % 60
        return "%02d:%02d" %(self.hour, self.min)


