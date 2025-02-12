class Pupil:
    def __init__(self, first_name, last_name, year, GPA):
        self.first_name=first_name
        self.last_name=last_name
        self.year=year
        self.GPA=GPA

    def get_info(self):
        return f"Name:{self.first_name}, Last_name{self.last_name}, Year:{self.year}, GPA:{self.GPA}"
    
pupila=Pupil("Asliddin","Usmonov","2008","100")

print(pupila.get_info)

class PupilManager:
    def __init__(self):
        self.pupils=[]

    def add_pupil(self, pupil):
        self.pupils.append(pupil)
    
    def get_pupils(self):
        for pupil in self.pupils:
            print(pupil.get_info())
    
    def get_max_gpa(self):
        gpa=0
        for pupil in self.pupils:
            if pupil.gpa > gpa:
                gpa=pupil.gpa

        return gpa    

pupila=Pupil("Asliddin", "Usmonov", 2008, 100)
pupilb=Pupil("Qodirov", "Dilmurod", 2008, 99)

manager=PupilManager()

manager.add_pupil(pupila)

