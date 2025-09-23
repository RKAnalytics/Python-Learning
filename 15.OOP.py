# OOP Concepts in Python ---> it is a BluePrint for creating Objects means it allows us to create our own data types
class Factory: # so Factory is a custom data type that can store information about a factory e.g model, location, capacity and production
    model = 2019 # these are attributes--> these are variables that belong to the class
    location = "USA" # and these are also know as class attributes
    capacity = 1000

    def produce(self): # this is a method---> these are functions that belong to the class
        print("Producing goods in the factory...")

    print("This will initialize only once. not every time we create an object.") # this is called initialization


# now in order to access the attributes and methods we will use dot notation

# here is one thing and that the object is temporary being made and it will gonna destroy after one line 

print(Factory().model) # accessing attribute 
print(Factory().location) # accessing attribute
print(Factory().capacity) # accessing attribute
Factory().produce() # accessing method


# now we are making the object of the class

obj = Factory() # here obj is the object of the class Factory it is basically accessing the class attributes and methods so from now on we dont
# have to write Factory() every time we can just use obj.model, obj.location, obj.capacity, obj.produce()



###########################################################################################################


## CONSTRUCTOR--> a constructor is a special method that is automatically called when an object of a class is created.
# It is used to initialize the attributes of the class. The constructor method is defined using the __init__() method and it calls 
# after the object is created.

class Student:
    def __init__(self, name, age):
        self.name = name #when the object is created the values are passed to the constructor and then the constructor initializes the attributes of the class
        self.age = age

    def display(self): # here the self captures the object's location
        print("Name:", self.name)
        print("Age:", self.age) 

obj = Student("Rafay", 19)
obj.display()


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)

    @classmethod # its like a shortcut template to create an object
    def create_teacher(cls): # now pointing the class location
        print("Creating a new teacher...")
        return cls("Rafay", "BIO") # this line basically means --> return Teacher("Rafay", "BIO")-->"Rafay" aur "BIO" constructor
                                   #(__init__) ke through object ke attributes self.name aur self.subject mein store ho jaate hain.

    
t1 = Teacher.create_teacher()
print(t1.display())

obj2 = Teacher("Mr. Smith", "Mathematics")
obj2.display()

########################################################################################################



class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)


    @classmethod
    def from_default(cls, data):
        print("Creating a new teacher with default values...")
        return cls(data["Name"], data["Subject"])


data = {"Name" : "Rafay", "Subject" : "BIO"}
t1 = Teacher.from_default(data)
print(t1.display())



####################################################################################################

## Now there are four pillars of OOP:

# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism


## Inheritance allows a class to inherit attributes and methods from another class.
class Student:

    name = "John Doe"
    age = 20

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class G_Student(Student):
    pass

obj = G_Student()

print(obj.display())


# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} speaks")

class Human(Animal): # so the constructor of the Human class will call the constructor of the Animal class
    def __init__(self,name ,age):
        super().__init__(name) # super() function is used to call the constructor of the parent class 
        # and it tells that the name has already been initialized in parent cclass
        self.age = age 
    
    def show(self):
        print(f"{self.name} is {self.age} years old")

animal1 = Animal("Generic Animal")
animal1.speak()

human1 = Human("John", 30)
human1.show()


# Multiple Inheritance

class Human:
    def __init__(self, name):
        self.name = name

class Aliens:
    def __init__(self, age):
        self.age = age

class Friends(Human, Aliens):
    def __init__(self, name, age):
        Human.__init__(self, name)
        Aliens.__init__(self, age)

    def display(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}")


obj2 = Friends("Rafay", 30)

obj2.display()

# multilevel inheritance

class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips
    
class LahoreFactory(Factory):
    def __init__(self, material, zips, colour):
        super().__init__(material, zips)
        self.colour = colour

class KarachiFactory(LahoreFactory):
    def __init__(self, material, zips, colour, pockets):
        super().__init__(material, zips, colour)
        self.pockets = pockets
    
    def display(self):
        print(f"Material: {self.material}, Zips: {self.zips}, Colour: {self.colour}, Pockets: {self.pockets}")

obj = KarachiFactory("Cotton", 5, "Blue", 2)
obj.display()


###############################################################################################################


## Polymorphism

# method overriding

class Animal:
    def show(self):
        print("Hello")

class Human(Animal):
    def show(self): # here this method is overriding the parent class method
        print("Hello, I am a human")

obj = Human()
obj.show()

# Duck typing

class Animal:
    def show(self):
        print("Hello")

class Human(Animal):
    def show(self): # here this method is overriding the parent class method
        print("Hello, I am a human")

obj = Animal()
obj2 = Human()
obj.show()
obj2.show()


######################################################################################################

#  ENCAPSULATION--> it is the process of wrapping data and methods into a single unit it means hiding the internal details of how things work
# and only showing t=when its needed so how we gonna do that so there are access modifiers there are 3 type of access modifiers
# 1. Public
# 2. Protected
# 3. Private

# Private members are not accessible from outside the class. They are denoted by a double underscore prefix.
# they cannot be accessed directly from outside the class and cant be changed 

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self): # so by doing this we can access  the private members from inside the class now we can access it to outside the class
        print("Name:", self.__name)
        print("Age:", self.__age)

obj = Student("Rafay", 19)
print(obj.display())

##########################################################################################################


# Abstraction --> Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object. In Python, we can achieve abstraction using abstract classes and interfaces.
# in simple words if you want to setup some rules for your classes and objects, you can use abstraction to define
# those rules without exposing the underlying implementation.

# there are set of rules that needs to be followed by the child class
# a method is defined in the parent class and is meant to be overridden in the child class.
# it means that you defined the method in the parent class and you havent implemented it and for the implementation
# you have to provide the implementation in the child class.


from abc import ABC, abstractmethod

class abstrat(ABC): # inheriting the ABC class
    @abstractmethod
    def area(self):
        pass

class Square(abstrat):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(abstrat):
    def __init__(self, radius):
        self.radius = radius

    def area(self): # due to self it can access the instance variable and can have the access the attributes because it is pointing to the instance and 
        # can capture the location of the object in memory where all the attributes are stored
        return 3.14 * self.radius * self.radius
    
class Combine(Square, Circle):
    def __init__(self, side, radius):
        Square.__init__(self, side) # initializing the Square class
        Circle.__init__(self, radius) # initializing the Circle class because both classes have different __init__ methods

    def display(self):
        print(f"""The radius of Circle is {self.radius} and the side of the square is {self.side} and
               the area of a square is {Square.area(self)} and the area of a circle is {Circle.area(self)}""")

obj = Combine(5, 5)
print(obj.display())

from abc import abc , abstractmethod 

class abstract ()