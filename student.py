class Student:
    def __init__(self, first_name, last_name, eid, major, classification, minor, schedule_image=None):
        self.first_name = first_name
        self.last_name = last_name
        self.eid = eid
        self.major = major
        self.classification = classification
        self.minor = minor
        self.schedule_image = schedule_image

        # Getter methods
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_eid(self):
        return self.eid

    def get_major(self):
        return self.major

    def get_classification(self):
        return self.classification

    def get_minor(self):
        return self.minor

    def get_schedule_image(self):
        return self.schedule_image

    # Setter methods
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_eid(self, eid):
        self.eid = eid

    def set_major(self, major):
        self.major = major

    def set_classification(self, classification):
        self.classification = classification

    def set_minor(self, minor):
        self.minor = minor
        
    def set_schedule_image(self, schedule_image):
        self.schedule_image = schedule_image


    def __str__(self):
        return f"{self.first_name} {self.last_name} (EID: {self.eid}) - {self.major}, {self.classification}, Minor: {self.minor}"