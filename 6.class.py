##Write a Python program to create a person class.
#Include attributes like name, country and date of birth.
##Implement a method to determine the person's age.
from datetime import date
class person :
    #constructor
    def __init__(self ,name , country , DateOfBirth ):
        self.name=name
        self.country=country
        self.DateOfBirth=DateOfBirth
    def CalculateAge (Self):
        today=date.today()
        age=today.year - self.DateOfBirth
        if today <date(today.year, self.DateOfBirth.month, self.DateOfBirth.day):
            age -=1
        return age



person1=person("aya" ,"f",date(1962, 7, 12))
print (person1)
