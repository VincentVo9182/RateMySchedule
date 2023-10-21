class Student:
    def __init__(self, first_name, last_name, eid, major, classification, minor, schedule_image=None):
        self.first_name = first_name
        self.last_name = last_name
        self.eid = eid
        self.major = major
        self.classification = classification
        self.minor = minor
        self.schedule_image = schedule_image

    def __str__(self):
        return f"{self.first_name} {self.last_name} (EID: {self.eid}) - {self.major}, {self.classification}, Minor: {self.minor}"