import re
from getFinal import getFinal

class Homework:
    def __init__(self, txtfile):
        with open("student_py/"+txtfile, "r") as f:
            self.answer = f.read()
        self.tokens = self.answer.split()
        self.total_marks = 58
        self.txtfile = txtfile

    def check_all(self):
        results = []
        results.append(self.check_abstract_notation())
        results.append(self.check_abstract_notation_use())
        results.append(self.check_parameters_and_mangling())
        results.append(self.check_getters())
        results.append(self.check_setters())
        results.append(self.check_str())
        results.append(self.check_eq())
        results.append(self.check_drive())
        results.append(self.check_instance())
        results.append(self.check_append())
        results.append(self.check_for())
        results.append(self.check_print())

        error_dict = {1: "check abstract class notation",
                      2: "check abstract class notation use",
                      3: "check parameters and mangling",
                      4: "check getters",
                      5: "check setters",
                      6: "check __str__ overloaded method",
                      7: "check __eq__ overloaded method",
                      8: "check drive() abstract method with decorator",
                      9: "check correct instantiation of Car and Trailer objects",
                      10: "check appending objects to list",
                      11: "check for loop",
                      12: "check print() and object.drive()"}

        removed = 0
        while False in results:
            removed += 1
            print("Test {} needs to be manually checked.".format(
                results.index(False)+removed))
            print("\t-", error_dict[results.index(False)+removed])
            results.pop(results.index(False))

        print("Total: {}/{}".format(sum(results), self.total_marks))

    def check_abstract_notation(self):
        imports = len(re.findall(r"from abc import ABC", self.answer)) + len(re.findall(r"abstractmethod", self.answer))
        if imports >= 2:
            return 2
        return False
    
    def check_abstract_notation_use(self):
        uses = len(re.findall(r"class [Aa]utomobile\(ABC\):", self.answer))
        uses += len(re.findall(r"class [Cc]ar\(Automobile\):", self.answer))
        uses += len(re.findall(r"class [Tt]railer\(Automobile\):", self.answer))
        if uses >= 3:
            return 5
        print("class declarations: {}".format(uses))
        print()
        return False

    def check_parameters_and_mangling(self):
        parameters = 1 if len(re.findall(r"def __init__\s*\(self,.*\):", self.answer)) > 0 else 0
        parameters += 1 if len(re.findall(r"def __init__\s*\(.*make.*\):", self.answer)) > 0 else 0
        parameters += 1 if len(re.findall(r"def __init__\s*\(.*model.*\):", self.answer)) > 0 else 0
        parameters += 1 if len(re.findall(r"def __init__\s*\(.*year.*\):", self.answer)) > 0 else 0
        parameters += 1 if len(re.findall(r"def __init__\s*\(.*mileage.*\):", self.answer)) > 0 else 0
        parameters += 1 if len(re.findall(r"def __init__\s*\(.*value.*\):", self.answer)) > 0 else 0
        parameters += 1 if len(re.findall(r"def __init__\s*\(.*vin.*\):", self.answer)) > 0 else 0
        parameters += 1 if len(re.findall(r"def __init__\s*\(.*mpg.*\):", self.answer)) > 0 else 0
        mangling = len(re.findall(r"self.__([A-Za-z][A-Za-z0-9]*)\s*=.*\1.*", self.answer))
        supers = len(re.findall(r"super\(\).__init__\([\w ,=]*\)", self.answer))
        if parameters >= 8 and mangling >= 12 and supers >= 2:
            return 11
        print("Parameters: {}".format(parameters))
        print("Mangles: {}".format(mangling))
        print("Supers: {}".format(supers))
        print()
        return False

    def check_getters(self):
        gets = len(re.findall(r"def get\w*\(self\)", self.answer))
        if gets >= 13:
            return 9
        print("Gets: {}".format(gets))
        print()
        return False
    
    def check_setters(self):
        sets = len(re.findall(r"def set\w*\(self,", self.answer))
        if sets >= 2:
            return 4
        print("Sets: {}".format(sets))
        print()
        return False

    def check_str(self):
        strs = len(re.findall(r"def __str__\(self\):", self.answer))
        supers = len(re.findall(r"super\(\).__str__\(\)", self.answer))
        if strs >= 3 and supers >= 2:
            return 6
        print("__str__'s: {}".format(strs))
        print("__str__ super's: {}".format(supers))
        print()
        return False

    
    def check_eq(self):
        eqs = len(re.findall(r"def __eq__\(self,", self.answer))
        supers = len(re.findall(r"super\(\).__eq__", self.answer))
        if eqs >= 3 and supers >= 2:
            return 6
        print("__eq__'s: {}".format(eqs))
        print("__eq__ supers: {}".format(supers))
        print()
        return False

    def check_drive(self):
        abstracts = len(re.findall(r"@abstractmethod", self.answer))
        drives = len(re.findall(r"def drive\(self\):", self.answer))
        if abstracts >= 1 and drives >= 3:
            return 6
        print("@abstractmethod's: {}".format(abstracts))
        print("drive's: {}".format(drives))
        print()
        return False
    
    def check_instance(self):
        cars = len(re.findall(r"\w+\s*=\s*[Cc]ar\([\w .,\"\']*\)", self.answer))
        trailers = len(re.findall(r"\w+\s*=\s*[Tt]railer\([\w ,.\"\']*\)", self.answer))

        if cars >= 1 and trailers >= 1:
            return 3
        print("Cars: {}".format(cars))
        print("Trailers: {}".format(trailers))
        print()
        return False
    
    def check_append(self):
        appends = len(re.findall(r"\w*.append\([\w ,\'\"\(\)]*\)", self.answer))

        if appends >= 2:
            return 2
        return False
    
    def check_for(self):
        fors = len(re.findall(r"for \w* in \w*:", self.answer))

        if fors >= 1:
            return 2
        return False
    
    def check_print(self):
        prints = len(re.findall(r"print\s*\(\w*\)", self.answer))
        drives = len(re.findall(r"[a-zA-Z]\w*.drive\(\)", self.answer))

        if prints >= 1:
            return 2
        return False
    


if __name__ == "__main__":
    file = getFinal()
    hw1 = Homework(file)
    hw1.check_all()
