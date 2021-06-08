from abc import ABC, abstractmethod

class Automobile(ABC):
    def __init__(self, make, model, year, mileage, value, vin, mpg):
        self.__make = make
        self.__model = model
        self.__year = year
        self.mileage = mileage
        self.value = value
        self.__vin = vin
        self.__mpg = mpg
        
    def __str__(self):
        return("This is a " + str(self.__year) + " " + str(self.__make) + " " + str(self.__model) + " " + "which uses" + " " + str(self.__mpg) +\
              ". Its ID is " + str(self.__vin) + ", and it has a mileage of " + str(self.mileage) + ", valuing it at " + str(self.value))
    
    #Compares two Automobiles's vehicle identification number.
    def __eq__(self, other):
        return (self.__vin == other.getVin())
    
    #Derived class's implementation prints out an appropriate message
    @abstractmethod
    def drive(self):
        pass
        
    #Getters
    #Most getters that the derived classes will use are here for sake of redundancy
    def getMake():
        return self.__make
    
    def getModel():
        return self.__model
    
    def getYear():
        return self.__year
    
    def getMileage():
        return self.mileage
    
    def getValue():
        return self.value
    
    def getVIN():
        return self.__vin
    
    def getMPG():
        return self.__mpg

class Car(Automobile):
    def __init__(self, make, model, year, mileage, value, vin, mpg, seatcount):
        super().__init__(make, model, year, mileage, value, vin, mpg)
        self.__seatcount = seatcount
        
    #Both overriding classes are using the inherited variant, because the inherited variant already basically has everything this class would have for these methods anyway.
    def __str__(self):
        return super().__str__()
    
    def __eq__(self):
        return super().__eq__()
    
    def drive(self):
        print("The car has been driven for 1 mile")
        
    #Getter and Setters
    def getSeats(self):
        return self.__seatcount
    
    def setMileage(self, mileage):
        self.mileage = mileage
        
    def setValue(self, value):
        self.value = value

class Trailer(Automobile):
    def __init__(self, make, model, year, mileage, value, vin, mpg, height, width, length):
        super().__init__(make, model, year, mileage, value, vin, mpg)
        self.__height = height
        self.__width = width
        self.__length = length
    
    #Both overriding classes are using the inherited variant, because the inherited variant already basically has everything this class would have for these methods anyway.
    def __str__(self):
        return super().__str__()
    
    def __eq__(self):
        return super().__eq__()
    
    #"Drives" the trailer.
    def drive(self):
        print("The trailer has been driven for 3 miles.")
    
    #Volume = height * length * width, returns the trailer's volume
    def getTrailerVolume(self):
        return self.getHeight() * self.getLength() * self.getWidth()
    
    def getHeight(self):
        return self.__height
    
    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width
    
    def setMileage(self, mileage):
        self.mileage = mileage
        
    def setValue(self, value):
        self.value = value
        
        
if __name__ == "__main__":
    autolist = []
    car1 = Car("Toyota", "Camry", 2002, 15000, 30000, 1, 30, 4)
    car2 = Car("Honda", "Prius", 2001, 17500, 45000, 2, 50, 5)
    car3 = Car("Ford", "Mustang", 2005, 25000, 37500, 3, 40, 8)
    trailer = Trailer("Tanker", "Example", 2007, 20000, 60000, 4, 75, 12, 30, 15)
    autolist.append(car1)
    autolist.append(car2)
    autolist.append(car3)
    autolist.append(trailer)
    
    for v in autolist:
        print(v)
        v.drive()