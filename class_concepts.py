# Python Class Concepts
# A comprehensive demonstration of OOP concepts in Python

# =====================================================================
# 1. Using self
# =====================================================================
# In Python, 'self' is a convention (not a keyword) that refers to the instance
# of a class. It's always the first parameter in instance methods.
# Unlike languages like Java or C++, Python makes the instance reference explicit.
class Student:
    def __init__(self, name, marks):
        # 'self' refers to the current instance being created
        # This is similar to 'this' in other languages
        self.name = name    # Create and initialize instance variable 'name'
        self.marks = marks  # Create and initialize instance variable 'marks'
    
    def display(self):
        # 'self' is required to access instance variables
        # Without it, Python would look for local variables named 'name' and 'marks'
        return f"Student: {self.name}, Marks: {self.marks}"
    
    # Note: If you don't use self in a method, consider making it a @staticmethod

# =====================================================================
# 2. Using cls
# =====================================================================
# 'cls' is a convention for class methods, which operate on the class itself
# rather than on instances. Class methods can modify class state that applies
# to all instances of the class.
class Counter:
    # Class variable - shared by all instances
    # This is defined in the class namespace, not in any method
    count = 0
    
    def __init__(self):
        # Access class variable through the class name
        # Increment count when a new instance is created
        Counter.count += 1
    
    @classmethod  # This decorator marks the method as a class method
    def get_count(cls):
        # 'cls' refers to the class itself, not an instance
        # This allows the method to be called on the class (Counter.get_count())
        # or on any instance (counter1.get_count())
        return cls.count  # Using cls instead of Counter makes inheritance work properly

# =====================================================================
# 3. Public Variables and Methods
# =====================================================================
# In Python, all attributes and methods are public by default
# There's no enforced access control like in Java or C++
# Python follows the philosophy: "We're all consenting adults here"
class Car:
    def __init__(self, brand):
        # This is a public attribute - accessible from anywhere
        self.brand = brand
    
    # This is a public method - can be called from anywhere
    def start(self):
        return f"The {self.brand} car is starting..."
    
    # Python doesn't have true private/protected members
    # Instead, it uses naming conventions (see example 7)

# =====================================================================
# 4. Class Variables and Class Methods
# =====================================================================
# Class variables are shared among all instances of a class
# They belong to the class, not to any specific instance
class Bank:
    # Class variable - shared by all instances
    bank_name = "National Bank"
    
    @classmethod
    def change_bank_name(cls, name):
        # Class methods can modify class variables
        # This affects all instances of the class
        cls.bank_name = name
        # Using cls instead of the direct class name allows this method
        # to work properly in inheritance scenarios
    
    def get_bank_name(self):
        # Instance methods can access class variables
        # Note: It's better to access as Bank.bank_name or self.__class__.bank_name
        # to avoid confusion with instance variables
        return Bank.bank_name
        
    # Warning: If you set self.bank_name in an instance, it creates an instance
    # variable that shadows the class variable for that specific instance

# =====================================================================
# 5. Static Variables and Static Methods
# =====================================================================
# Static methods don't operate on the instance or the class
# They're just regular functions that are logically grouped in the class
class MathUtils:
    # Class/static variable
    PI = 3.14159
    
    @staticmethod  # This decorator marks the method as static
    def add(a, b):
        # Static methods don't receive 'self' or 'cls'
        # They can't access or modify instance or class state
        # They're just utility functions grouped in the class namespace
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    # Static methods are useful for utility functions that are
    # related to the class but don't need to access its state

# =====================================================================
# 6. Constructors and Destructors
# =====================================================================
# Constructors initialize objects, destructors clean up resources
# Python manages memory automatically, so destructors are less common
class Logger:
    def __init__(self):
        # __init__ is the constructor method
        # It's called when an object is created
        # It initializes the object's state
        print("Logger object created")
        self.log_file = open("log.txt", "a")  # Open a resource
    
    def log(self, message):
        self.log_file.write(message + "\n")
    
    def __del__(self):
        # __del__ is the destructor method
        # It's called when the object is about to be destroyed
        # It's used to release resources (close files, connections, etc.)
        # Warning: Don't rely on __del__ being called in a timely manner
        # Python's garbage collection is non-deterministic
        if hasattr(self, 'log_file'):
            self.log_file.close()  # Close the resource
        print("Logger object destroyed")
    
    # Better alternative to __del__ - explicit cleanup
    def destroy(self):
        # Explicit cleanup method is more reliable than __del__
        if hasattr(self, 'log_file'):
            self.log_file.close()
        print("Logger object destroyed")

# =====================================================================
# 7. Access Modifiers: Public, Private, and Protected
# =====================================================================
# Python doesn't have true access modifiers, but uses naming conventions
# and name mangling to simulate them
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public - accessible from anywhere
        self._salary = salary     # Protected - convention only (still accessible)
        self.__ssn = ssn          # Private - name mangling (harder to access)
        # Name mangling: __ssn becomes _Employee__ssn internally
    
    def get_salary(self):
        # Accessor method for protected attribute
        return self._salary
    
    def has_ssn(self):
        # Accessor method for private attribute
        # We don't return the actual SSN for privacy
        return bool(self.__ssn)
    
    def _protected_method(self):
        # Protected method - convention only
        # Indicates that this method is intended for internal use
        return "This method is intended for internal use"
    
    def __private_method(self):
        # Private method - name mangling applies
        # Becomes _Employee__private_method internally
        return "This method is private"

# =====================================================================
# 8. The super() Function
# =====================================================================
# super() is used to call methods from a parent class
# It's especially useful in inheritance hierarchies
class Person:
    def __init__(self, name):
        # Base class constructor
        self.name = name
    
    def introduce(self):
        return f"Hi, I'm {self.name}"

class Teacher(Person):
    def __init__(self, name, subject):
        # Call the parent class constructor
        # This avoids having to repeat the code in Person.__init__
        super().__init__(name)  # Equivalent to Person.__init__(self, name)
        
        # Add Teacher-specific initialization
        self.subject = subject
    
    def get_info(self):
        # We can also use super() to call other parent methods
        introduction = super().introduce()
        return f"{introduction} and I teach {self.subject}"
    
    # Benefits of super():
    # 1. Avoids hardcoding the parent class name
    # 2. Works correctly with multiple inheritance
    # 3. Prevents calling the parent method multiple times in diamond inheritance

# =====================================================================
# 9. Abstract Classes and Methods
# =====================================================================
# Abstract classes can't be instantiated and force subclasses to implement
# certain methods. They're used to define interfaces.
from abc import ABC, abstractmethod

class Shape(ABC):  # ABC = Abstract Base Class
    @abstractmethod  # This decorator marks the method as abstract
    def area(self):
        # Abstract methods have no implementation
        # Subclasses MUST implement this method
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        # Abstract classes can have concrete methods too
        return f"This shape has an area of {self.area()}"
    
    # You cannot instantiate an abstract class:
    # shape = Shape()  # This would raise TypeError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Must implement all abstract methods
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    # If we forgot to implement any abstract method, Python would
    # raise TypeError when we try to instantiate Rectangle

# =====================================================================
# 10. Instance Methods
# =====================================================================
# Instance methods operate on specific instances of a class
# They can access and modify instance state
class Dog:
    # Class variable
    species = "Canis familiaris"
    
    def __init__(self, name, breed):
        # Instance variables - unique to each instance
        self.name = name
        self.breed = breed
        self.tricks = []  # Each dog has its own list of tricks
    
    # Instance method - operates on the specific dog instance
    def bark(self):
        return f"{self.name} ({self.breed}) says: Woof!"
    
    # Instance method that modifies instance state
    def learn_trick(self, trick):
        self.tricks.append(trick)
        return f"{self.name} has learned to {trick}!"
    
    # Instance method that accesses both instance and class variables
    def describe(self):
        return f"{self.name} is a {self.breed}, which is a {self.species}"

# =====================================================================
# 11. Class Methods
# =====================================================================
# Class methods operate on the class itself
# They're often used for alternative constructors
class Book:
    # Class variable
    total_books = 0
    
    def __init__(self, title, author=None):
        self.title = title
        self.author = author
        # Call class method to update the count
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        # Class method modifies class state
        cls.total_books += 1
    
    @classmethod
    def get_total_books(cls):
        # Class method accesses class state
        return cls.total_books
    
    # Class methods are often used as factory methods (alternative constructors)
    @classmethod
    def create_anonymous_book(cls, title):
        # This is a factory method that creates a book with no author
        return cls(title, None)
    
    @classmethod
    def from_string(cls, book_str):
        # Parse a string like "Title|Author" and create a Book
        title, author = book_str.split("|")
        return cls(title, author)

# =====================================================================
# 12. Static Methods
# =====================================================================
# Static methods don't operate on instance or class state
# They're utility functions that are logically related to the class
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Static method - doesn't use self or cls
        # It's just a utility function that belongs to the class namespace
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9
    
    @staticmethod
    def is_freezing(celsius):
        # Static methods can call other static methods
        return celsius <= 0
    
    # When to use static methods:
    # 1. When the function doesn't need access to instance or class state
    # 2. When the function is logically related to the class
    # 3. To organize utility functions that are related to the class purpose

# =====================================================================
# 13. Composition
# =====================================================================
# Composition is a design pattern where a class contains instances of other classes
# It represents a "has-a" relationship (Car has-an Engine)
class Engine:
    def __init__(self, capacity, fuel_type="gasoline"):
        self.capacity = capacity
        self.fuel_type = fuel_type
        self.running = False
    
    def start(self):
        self.running = True
        return f"Engine with {self.capacity}L capacity started"
    
    def stop(self):
        self.running = False
        return "Engine stopped"

class CarWithEngine:
    def __init__(self, brand, engine_capacity, fuel_type="gasoline"):
        self.brand = brand
        # Composition: Car has-an Engine
        # The Engine is created inside the Car and doesn't exist independently
        # If the Car is destroyed, the Engine is also destroyed
        self.engine = Engine(engine_capacity, fuel_type)
        self.speed = 0
    
    def start_engine(self):
        return f"{self.brand} car: {self.engine.start()}"
    
    def stop_engine(self):
        return f"{self.brand} car: {self.engine.stop()}"
    
    def accelerate(self, amount):
        if self.engine.running:
            self.speed += amount
            return f"{self.brand} accelerating to {self.speed} km/h"
        else:
            return "Cannot accelerate. Engine is not running."
    
    def get_engine_capacity(self):
        return self.engine.capacity
    
    # Benefits of composition:
    # 1. More flexible than inheritance
    # 2. Can change the composed object at runtime
    # 3. Avoids the fragile base class problem

# =====================================================================
# 14. Aggregation
# =====================================================================
# Aggregation is a special form of composition where the contained objects
# can exist independently of the container
# It's a "has-a" relationship, but with independent lifetimes
class EmployeeForDept:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def describe(self):
        return f"{self.name} - {self.role}"

class Department:
    def __init__(self, name, employees):
        self.name = name
        # Aggregation: Department has references to Employee objects
        # The employees exist independently and can belong to multiple departments
        # If the Department is destroyed, the employees continue to exist
        self.employees = employees
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    
    def list_employees(self):
        return self.employees
    
    # Key difference from composition:
    # In aggregation, the contained objects (employees) can exist independently
    # and can be shared among multiple containers (departments)

# =====================================================================
# 15. Method Resolution Order (MRO) and Diamond Inheritance
# =====================================================================
# MRO determines the order in which Python searches for methods in inheritance
# Diamond inheritance occurs when a class inherits from two classes that share a common ancestor
class A:
    def show(self):
        return "Method from A"
    
    def everyone_has_this(self):
        return "Method from A"

class B(A):
    def show(self):
        return "Method from B"
    
    def everyone_has_this(self):
        return "Method from B"

class C(A):
    def show(self):
        return "Method from C"
    
    def everyone_has_this(self):
        return "Method from C"

class D(B, C):  # Multiple inheritance - Python supports this directly
    def show(self):
        # We can call specific parent implementations if needed
        # return B.show(self)  # Call B's implementation
        # return C.show(self)  # Call C's implementation
        # return super().show()  # Call the next method in the MRO (B's implementation)
        
        # Or override completely
        return "Method from D"
    
    # We don't override everyone_has_this, so Python will use the MRO
    # to determine which parent's version to call
    
    # Python's MRO uses the C3 linearization algorithm
    # For class D(B, C), the MRO is [D, B, C, A, object]
    # This means Python looks for methods in D first, then B, then C, then A

# =====================================================================
# 16. Function Decorators
# =====================================================================
# Decorators modify or enhance functions without changing their code
# They're a powerful way to add functionality like logging, timing, etc.
def log_function_call(func):
    # This is a decorator function that takes a function as input
    def wrapper(*args, **kwargs):
        # The wrapper function adds behavior before and after the original function
        print(f"Function {func.__name__} is being called with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)  # Call the original function
        print(f"Function {func.__name__} returned: {result}")
        return result
    
    # Return the enhanced function
    return wrapper

# Apply the decorator to a function
@log_function_call  # This is equivalent to: say_hello = log_function_call(say_hello)
def say_hello(name):
    return f"Hello, {name}!"

# Another example: timing decorator
def timing_decorator(func):
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to run")
        return result
    
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Function completed"

# =====================================================================
# 17. Class Decorators
# =====================================================================
# Class decorators modify or enhance classes
# They're applied to the class definition
def add_greeting(cls):
    # This decorator adds a method to the class
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting  # This is equivalent to: PersonWithGreeting = add_greeting(PersonWithGreeting)
class PersonWithGreeting:
    def __init__(self, name):
        self.name = name

# More practical example: singleton decorator
def singleton(cls):
    # This decorator ensures only one instance of the class exists
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        print(f"Connecting to database at {host}")
    
    def query(self, sql):
        return f"Executing {sql} on {self.host}"

# =====================================================================
# 18. Property Decorators: @property, @setter, and @deleter
# =====================================================================
# Properties allow controlled access to attributes
# They let you use methods as if they were attributes
class Product:
    def __init__(self):
        self._price = 0  # Protected attribute
    
    @property
    def price(self):
        # Getter method - called when you access product.price
        return self._price
    
    @price.setter
    def price(self, value):
        # Setter method - called when you assign product.price = value
        if value < 0:
            print("Price cannot be negative")
            return
        self._price = value
    
    @price.deleter
    def price(self):
        # Deleter method - called when you do: del product.price
        print("Deleting price")
        del self._price
    
    # Benefits of properties:
    # 1. Encapsulation - hide implementation details
    # 2. Validation - ensure attributes have valid values
    # 3. Computed attributes - calculate values on-the-fly
    # 4. Backward compatibility - change implementation without changing interface

# More complex example with computed property
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        # Computed property - calculated on-the-fly
        import math
        return math.pi * self._radius ** 2
    
    @property
    def diameter(self):
        return 2 * self._radius
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2  # This calls the radius setter

# =====================================================================
# 19. callable() and __call__()
# =====================================================================
# The __call__ method makes objects callable like functions
# This is useful for creating function-like objects with state
class Multiplier:
    def __init__(self, factor):
        # The object has state
        self.factor = factor
    
    def __call__(self, value):
        # This makes the object callable like a function
        # multiplier = Multiplier(2)
        # result = multiplier(5)  # This calls __call__(5)
        return value * self.factor

# More practical example: Counter with memory
class Counter:
    def __init__(self):
        self.count = 0
        self.values = []
    
    def __call__(self, value=None):
        if value is not None:
            self.values.append(value)
        self.count += 1
        return self.count
    
    def get_values(self):
        return self.values
    
    def reset(self):
        self.count = 0
        self.values = []

# =====================================================================
# 20. Creating a Custom Exception
# =====================================================================
# Custom exceptions make error handling more specific and meaningful
# They help distinguish between different error conditions
class InvalidAgeError(Exception):
    # Custom exception that inherits from the base Exception class
    def __init__(self, age, message="Age must be 18 or older"):
        self.age = age
        self.message = message
        # Call the base class constructor
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message} (got {self.age})"

def check_age(age):
    if age < 18:
        # Raise our custom exception
        raise InvalidAgeError(age)
    # If we get here, the age is valid
    return True

# More complex example: custom exception hierarchy
class DatabaseError(Exception):
    """Base class for database exceptions"""
    pass

class ConnectionError(DatabaseError):
    """Raised when a connection fails"""
    pass

class QueryError(DatabaseError):
    """Raised when a query fails"""
    def __init__(self, query, message):
        self.query = query
        self.message = message
        super().__init__(f"Query failed: {message}, Query: {query}")

# =====================================================================
# 21. Make a Custom Class Iterable
# =====================================================================
# Iterables can be used in for loops and other iteration contexts
# This is done by implementing __iter__ and __next__ methods
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        # __iter__ must return an iterator object
        # Here, we return self, making this class both an iterable and an iterator
        # An iterable must have __iter__ that returns an iterator
        # An iterator must have __next__ that returns the next value or raises StopIteration
        return self
    
    def __next__(self):
        # __next__ returns the next value or raises StopIteration when done
        if self.start >= 0:
            current = self.start
            self.start -= 1
            return current
        else:
            # Signal the end of iteration
            raise StopIteration

# More complex example: custom range with step
class CustomRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        # Create a separate iterator class
        return CustomRangeIterator(self.start, self.stop, self.step)

class CustomRangeIterator:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        # An iterator must also be iterable
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current < self.stop) or \
           (self.step < 0 and self.current > self.stop):
            value = self.current
            self.current += self.step
            return value
        else:
            raise StopIteration

# =====================================================================
# Main function to test all the classes
# =====================================================================
def main():
    print("\n1. Using self")
    student = Student("Alice", 95)
    print(student.display())
    
    print("\n2. Using cls")
    counter1 = Counter()
    counter2 = Counter()
    counter3 = Counter()
    print(f"Total counters created: {Counter.get_count()}")
    
    print("\n3. Public Variables and Methods")
    car = Car("Toyota")
    print(f"Car brand: {car.brand}")
    print(car.start())
    
    print("\n4. Class Variables and Class Methods")
    bank1 = Bank()
    bank2 = Bank()
    print(f"Initial bank name: {Bank.bank_name}")
    Bank.change_bank_name("New National Bank")
    print(f"Updated bank name: {bank1.get_bank_name()}")
    print(f"Same for all instances: {bank2.get_bank_name()}")
    
    print("\n5. Static Variables and Static Methods")
    print(f"2 + 3 = {MathUtils.add(2, 3)}")
    print(f"PI value: {MathUtils.PI}")
    
    print("\n6. Constructors and Destructors")
    print("Creating logger...")
    logger = Logger()
    logger.destroy()  # Explicit cleanup
    
    print("\n7. Access Modifiers")