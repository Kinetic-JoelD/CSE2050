
#Keeping our code DRY, Don't Repeat Yourself. By noticing the repeat patterns 
# in the professor and student class we factored it out to
# It also makes it easier to adjust for programming errors

class Person:
    def __init__(self, name, netID):
        self.name = name
        self.netID = netID


# Create a class student that has: 

# Instance variables name, netid, credits (total), courses {course:grade} dictionary,
# add_course [semester, course] 


"""
Sotres information about people at uconn
class professor

Instance Variables
============
* name
* netID
* title
* office
* courseload
=============
*add_course() - Instance Methods

"""

class Professor(Person):
    def __init__(self, param_name, param_netID, param_title, param_office, param_courseload):
        Person.__init__(self, param_name, param_netID)
        self.title = param_title
        self.office = param_office
        self.courseload = param_courseload
    def add_course(self, semester, course):
        """adds crouse to the courseload for the given semester """
        if semester in self.courseload:
            self.courseload[semester].add(course)
        else:
            self.courseload[semester] = {course}

    

class Student(Person):
    def __init__(self, name, netID, totCred, courses):
        Person.__init__(self, name, netID)
        self.totCred = totCred
        self.courses = courses

    def add_course(self,semester, course, grade):
        if semester in self.courses:
            self.courses[semester].update({course:grade})
        else:
            self.courses[semester] = {course:grade}
