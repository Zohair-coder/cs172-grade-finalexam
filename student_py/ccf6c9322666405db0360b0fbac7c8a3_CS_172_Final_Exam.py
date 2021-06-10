# Author: Joseph Rajasekaran
# Date: 7 June 2021
# Purpose: CS-172 Final Exam Question 19

#PART A - abstract base class

from abc import ABC, abstractmethod

class Automobile(ABC):
    #constructor
    def __init__(self, make, model, year, mileage, value, vin, mpg):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__value = value
        self.__vin = vin
        self.__mpg = mpg
        
    #getters
    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model
    
    def getYear(self):
        return self.__year
    
    def getMileage(self):
        return self.__mileage
    
    def getValue(self):
        return self.__value
    
    def getVin(self):
        return self.__vin
    
    def getMpg(self):
        return self.__mpg
    
    #setters
    def setMileage(self, mileage):
        self.__mileage = mileage
        
    def setValue(self, value):
        self.__value = value
    
    #abstract method
    @abstractmethod
    def drive(self):
        pass
    
    #overloaded operators
    def __str__(self):
        string =  'Make: ' + str(self.__make) + '.\n'
        string += 'Model: ' + str(self.__model) + '.\n'
        string += 'Year: ' + str(self.__year) + '.\n'
        string += 'Mileage: ' + str(self.__mileage) + ' miles.\n'
        string += 'Value: $' + str(self.__value) + '.\n'
        string += 'Vin Number: ' + str(self.__vin) + '.\n'
        string += 'Mpg: ' + str(self.__mpg) + ' mpg.\n'
        return string
    
    def __eq__(self, other):
        if (self.__vin) == (other.getVin()):
            return True
        else:
            return False

# PART B - Derived class 1 - Car

class Car(Automobile):
    #constructor
    def __init__(self, make, model, year, mileage, value, vin, mpg, seats):
        super().__init__(make, model, year, mileage, value, vin, mpg)
        self.__seats = seats
        
    #getters - only the new attribute needs a getter, the rest can use the methods from parent class
    def getSeats(self):
        return self.__seats
    
    #setters - only the new attribute needs a setter, same reason as the getters
    def setSeats(self, seats): # seats can be taken out of a car to make more trunk space
        self.__seats = seats
        
    #implement the abstract method
    def drive(self):
        return "The Car is driving with the windows down.\n"
    
    #overload operators - __eq__ operator does not need to be repeated since vin doesn't change
    def __str__(self):
        string = super().__str__()
        string += 'Number of seats: ' + str(self.__seats) + '.\n'
        return string

# PART C - Derived class 2 - Trailer

class Trailer(Automobile):
    #constructor
    def __init__(self, make, model, year, mileage, value, vin, mpg, maxLoad, width, height, length, numAxels):
        super().__init__(make, model, year, mileage, value, vin, mpg)
        self.__maxLoad = maxLoad
        self.__width = width
        self.__height = height
        self.__length = length
        self.__numAxels = numAxels
        
    #getters - none of the getters from the parent class need to be rewritten
    def getMaxLoad(self):
        return self.__maxLoad
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def getLength(self):
        return self.__length
    
    def getNumAxels(self):
        return self.__numAxels
    
    def getTrailerVolume(self):
        volume = self.__width * self.__height * self.__length
        return volume
    
    #setters - parent class setters do not need to be repeated
    def setMaxLoad(self, maxLoad):
        self.__maxLoad = maxLoad
    
    def setWidth(self, width):
        self.__width = width
        
    def setHeight(self, height):
        self.__height = height
        
    def setLength(self, length):
        self.__length = length
        
    def setNumAxels(self, numAxels):
        self.__numAxels = numAxels
        
    #implement abstract methods
    def drive(self):
        return "The Trailer is carrying cargo and driving.\n"
    
    #overloaded opperators - __eq__ does not need to be overriden since vin doesn't change
    def __str__(self):
        string = super().__str__()
        string += 'Trailer Max Load: ' + str(self.__maxLoad) + ' lbs.\n'
        string += 'Trailer Volume: ' + str(self.getTrailerVolume()) + ' cubic feet.\n'
        string += 'Number of Axels: ' + str(self.__numAxels) + '.\n'
        return string

# PART D - main script

if __name__ == "__main__":
    #introduction
    print("***Car Dealership Inventory***\n")
    
    #create car objects using car class
    car1 = Car("Honda", "Accord", 2015, 40000, 20000, 7849, 30, 5)
    car2 = Car("Audi", "RS5", 2018, 20000, 70000, 9938, 19, 2)
    car3 = Car("Ram", "4x4", 2020, 10000, 50000, 8367, 25,6)
    
    #creat trailer
    trailer1 = Trailer("Ford", "Raptor", 2021, 500, 80000, 2543, 21, 1000, 10, 3, 7, 2)
    
    #create automobile list
    autoList = (car1, car2, car3, trailer1)
    
    #print loop
    for item in autoList:
        print(item)
        statement = item.drive()
        print(statement)
        
    #exit message
    print("That's all we have for today!")
    
    