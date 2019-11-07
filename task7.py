
class Student:
    def __init__(self, full_name, age, major):
        self.full_name = full_name
        self.age = age
        self.major = major
        

    def result(self):
        result_ = f"name:{self.full_name}---age:{self.age}---major:{self.major}"
        print(result_)

Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope",32,"Physics")
Steve.result()
Johnny.result()
Penny.result()