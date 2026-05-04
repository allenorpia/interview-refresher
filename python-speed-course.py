
""" 
    What is Python?
        Python is a high-level, interpreted programming language known for its readability and versatility.
        It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.


 """


""" 
    DATA TYPES IN PYTHON
        1. Numeric Types: int, float, complex   
        2. Sequence Types: list, tuple, range
        3. Text Type: str
        4. Set Types: set, frozenset
        5. Mapping Type: dict
        6. Boolean Type: bool

        # INTEGER 
        x = 10
        print(type(x))  # Output: <class 'int'>
        x = -26 

        FLOAT 
        y = 3.14
        print(type(y))  # Output: <class 'float'>

        STRING
        name = "Python"
        print(type(name))  # Output: <class 'str'>  

        BOOLEAN
        is_active = True
        print(type(is_active))  # Output: <class 'bool'>    

        
 """
x = 10
print(type(x))
x= -26
y = 3.14
print(type(y))

introduction = 'Hello World!'

""" 
    OUTPUT AND PRINTING
        In Python, you can use the print() function to display output to the console.

        Example:
        print('Hello World!')  # Output: Hello World!

        print(4.5, 'Hello', True)  # Output: 4.5 Hello True


 """


""" 
    VARIABLES IN PYTHON
        Variables are used to store data values. In Python, you don't need to declare the type of a variable explicitly.

        Example:
        x = 5               # Integer
        y = 3.14            # Float
        name = "Python"     # String
        is_active = True    # Boolean

        You can change the value of a variable at any time:
        x = 10              # Now x is 10
        name = "Java"      # Now name is "Java"

 """

""" 
    PYTHON NAMEING CONVENTIONS
        1. Use lowercase letters and underscores to separate words (snake_case).
        2. Variable names must start with a letter (a-z, A-Z) or an underscore (_), followed by letters, digits (0-9), or underscores.
        3. Avoid using Python reserved keywords as variable names (e.g., if, else, while, for, etc.).
        4. Use descriptive names that convey the purpose of the variable.   
        5. Be consistent with your naming conventions throughout your code.

    Example:    
        valid_variable_name = 10
        anotherVariable = 20  # Not recommended (camelCase)
        _private_variable = 30  

 """
valid_variable_name = 'var'

""" 
    INPUT IN PYTHON
        In Python, you can use the input() function to take input from the user.

        Example:
        name = input("Enter your name: ")
        print("Hello, " + name + "!")

        age = input("Enter your age: ")
        print("You are " + age + " years old.") 

        email = input('Enter your email: ')

 """

""" 
    ARITHMETIC OPERATORS IN PYTHON
        1. Addition (+): Adds two numbers.
        2. Subtraction (-): Subtracts the second number from the first.
        3. Multiplication (*): Multiplies two numbers.      
        4. Division (/): Divides the first number by the second (returns a float).
        5. Floor Division (//): Divides the first number by the second and returns the largest integer less than or equal to the result.
        6. Modulus (%): Returns the remainder of the division of the first number by the second.
        7. Exponentiation (**): Raises the first number to the power of the second.             
    Example:
        a = 10      
        b = 3
        print(a + b)  # Output: 13
        print(a - b)  # Output: 7       
        print(a * b)  # Output: 30
        print(a / b)  # Output: 3.3333333333333335
        print(a // b) # Output: 3
        print(a % b)  # Output: 1
        print(a ** b) # Output: 1000

    Whenever you use the division operator (/), the result is always a float, even if both operands are integers.   

    int() function can be used to convert a float to an integer by truncating the decimal part.
    Example:    
        x = 5.99
        y = int(x)
        print(y)  # Output: 5
    int() does not round the number; it simply removes the decimal portion.
    int() can also convert strings that represent whole numbers into integers.  

    float() function can be used to convert an integer or a string representing a number into a float.
    Example:    
        x = 5
        y = float(x)
        print(y)  # Output: 5.0 


 """


""" 
    STRING METHODS
        1. lower(): Converts all characters in the string to lowercase.
        2. upper(): Converts all characters in the string to uppercase.
        3. strip(): Removes leading and trailing whitespace from the string.
        4. replace(old, new): Replaces occurrences of a substring with a new substring.
        5. split(separator): Splits the string into a list of substrings based on the specified separator.
        6. join(iterable): Joins elements of an iterable (like a list) into a single string, separated by the string on which it is called.
        7. find(substring): Returns the lowest index of the substring if found in the string; otherwise, returns -1.
        8. format(): Formats specified values in a string.
 """


x = 10
print(type(x))
name = input('Enter your name: ')
age = input('Enter your age: ')

y = int(age) + x
print('Hello World!')
name.lower()
name.upper()

print(name * x)   

""" 
    CONDITIONAL OPERATORS IN PYTHON
        1. Equal to (==): Checks if two values are equal.
        2. Not equal to (!=): Checks if two values are not equal.
        3. Greater than (>): Checks if the left value is greater than the right value.
        4. Less than (<): Checks if the left value is less than the right value.
        5. Greater than or equal to (>=): Checks if the left value is greater than or equal to the right value.
        6. Less than or equal to (<=): Checks if the left value is less than or equal to the right value.   
    
        You can compare strings with greater than or less than operators based on lexicographical order (dictionary order). 
        Example:
            str1 = "apple"  
            str2 = "banana"
            print(str1 < str2)  # Output: True, because "apple" comes before "banana"

        CHAINED CONDITIONALS
            You can chain multiple comparisons in a single expression.
            Example:
                x = 10
                print(5 < x < 15)  # Output: True, because x is greater than 5 and less than 15 

 """

""" 
    LOGICAL OPERATORS IN PYTHON
        1. and: Returns True if both operands are true.
        2. or: Returns True if at least one operand is true.    
        3. not: Returns True if the operand is false; otherwise, returns False.


 """

""" 
    IF-ELSE STATEMENTS IN PYTHON
        if statement: Used to execute a block of code if a specified condition is true. 
        else statement: Used to execute a block of code if the condition in the if statement is false.
        elif statement: Used to check multiple conditions in sequence.
        Example:
            age = int(input("Enter your age: "))
            if age < 18:
                print("You are a minor.")
            elif age >= 18 and age < 65:
                print("You are an adult.")
            else:
                print("You are a senior citizen.")


 """

if age < 21: 
    print('You are not allowed to go inside the club.')
elif age >= 21:
    print('You are allowed to go inside the club.')
else:
    print('Invalid age input.')


""" 
    LISTS AND TUPLES IN PYTHON
        Lists:  
            - Mutable (can be changed after creation).
            - Defined using square brackets [].
            - Can contain elements of different data types.
            Example:
                my_list = [1, 2.5, "Hello", True]
                my_list.append(10)  # Adds 10 to the end of the list
                print(my_list)  # Output: [1, 2.5, "Hello", True, 10]
        Tuples:
            - Immutable (cannot be changed after creation).     
            - Defined using parentheses ().
            - Can contain elements of different data types.
            Example:
                my_tuple = (1, 2.5, "Hello", True)  
                print(my_tuple)  # Output: (1, 2.5, "Hello", True)

        Lists are more flexible due to their mutability, while tuples are often used for fixed collections of items.

        list vs tuple:
            1. Mutability: Lists are mutable, while tuples are immutable.
            2. Syntax: Lists use square brackets [], while tuples use parentheses ().
            3. Performance: Tuples can be more memory efficient and faster than lists for certain operations.
            4. Use Cases: Lists are used for collections of items that may change, while tuples are used for fixed collections of items.

        What operations are faster on lists compared to tuples?
            1. Item Assignment: Modifying elements in a list is faster since lists are mutable.
            2. Appending/Removing Elements: Adding or removing elements from a list is faster due to its dynamic nature.
            3. Sorting: Lists can be sorted in place, which is generally faster than creating a new sorted tuple.   
            4. Iteration: Iterating through a list can be slightly faster due to better memory locality.        
            5. Memory Management:

        What operations are faster on tuples compared to lists?
            1. Creation: Creating a tuple is generally faster than creating a list due to its immutability.
            2. Memory Usage: Tuples use less memory than lists, which can lead to better performance in memory-constrained environments.
            3. Hashing: Tuples can be used as keys in dictionaries and elements in sets, while lists cannot, making tuple lookups faster in these contexts.
            4. Iteration: In some cases, iterating through a tuple can be faster
                due to its fixed size and immutability. 
                Memory Efficiency:      

          
        The actual items of a list are stored in contiguous memory locations, allowing for efficient access and modification.

        Lists provide various built-in methods for manipulation, such as append(), remove(), pop(), sort(), and reverse().

 """

my_list = [1,2,3,4,5]
print(len(my_list))  # Output: 5
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
my_list.pop()
print(my_list)  # Output: [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
my_list[0] = 'hello'
print(my_list)  # Output: ['hello', 2, 3, 4, 5] 

my_tuple = (1,2,3)
print(len(my_tuple))
my_tuple[0] = 7    # Output: 1
print(my_tuple)  # Output: (1, 2, 3)


""" 
    FOR LOOPS IN PYTHON
        A for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.

        Example:
            # Iterating over a list
            my_list = [1, 2, 3, 4, 5]
            for item in my_list:
                print(item)

            # Iterating over a string
            my_string = "Hello"
            for char in my_string:
                print(char)

            # Using range() to generate a sequence of numbers
            for i in range(5):
                print(i)  # Output: 0, 1, 2, 3, 4

        start: The starting value of the sequence (inclusive). Default is 0.
        stop: The ending value of the sequence (exclusive). 
        step: The difference between each number in the sequence. Default is 1.
        Example:
                for i in range(1, 10, 2):
                    print(i)  # Output: 1, 3, 5, 7, 9   

        The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
        Example:        
            my_list = ['a', 'b', 'c']
            for index, value in enumerate(my_list):
                print(index, value) 

        

 """

for i in range(5):
    print(i)

for i in range(0, 10, 1):
    print(i % 2 == 0)

for index, value in enumerate(my_list):
    print(index, value)

for item in my_list:
    print(item)


""" 
    WHILE LOOPS IN PYTHON
        A while loop is used to repeatedly execute a block of code as long as a specified condition is true.

        Example:
            count = 0
            while count < 5:
                print(count)
                count += 1  # Increment count by 1

        The loop will continue until the condition (count < 5) becomes false.

        Be cautious with while loops to avoid infinite loops, which occur when the condition never becomes false.   

 """


count = 0
while count < 10:
    print(count)
    count += 1


""" 
    SLICE OPERATIONS IN PYTHON
        Slicing is a way to extract a portion of a sequence (like a list, tuple, or string) by specifying a start index, an end index, and an optional step.
        The syntax for slicing is: sequence[start:end:step] 
        1. start: The index where the slice starts (inclusive). Default is 0.
        2. end: The index where the slice ends (exclusive). Default is the length of the sequence.
        3. step: The difference between each index in the slice. Default is 1.

        Example:
            my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            slice1 = my_list[2:7]        # Output: [2, 3, 4, 5, 6]
            slice2 = my_list[:5]         # Output: [0, 1, 2, 3, 4]
            slice3 = my_list[5:]         # Output: [5, 6, 7, 8, 9]
            slice4 = my_list[::2]        # Output: [0, 2, 4, 6, 8]
            slice5 = my_list[1:8:3]      # Output: [1, 4, 7]    
            slice6 = my_list[-5:-1]      # Output: [5, 6, 7, 8]
            slice7 = my_list[::-1]       # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverses the list)   



 """

""" 
    SETS
        A set is an unordered collection of unique elements in Python. Sets are mutable, meaning you can add or remove elements after creation.

        Creating a Set:
            You can create a set using curly braces {} or the
            set() constructor.
            Example:        
                my_set = {1, 2, 3}
                another_set = set([4, 5, 6])    
        Basic Set Operations:
            1. Adding Elements: Use the add() method to add an element to a set.
                my_set.add(4)  # my_set is now {1, 2, 3, 4}
            2. Removing Elements: Use the remove() or discard() method to remove an element from a set.
                my_set.remove(2)  # my_set is now {1, 3, 4}
            3. Membership Testing: Use the in keyword to check if an element is in a set.
                print(3 in my_set)  # Output: True  
            4. Set Operations: You can perform various set operations like union, intersection, difference, and symmetric difference.
            set1 = {1, 2, 3}        
            set2 = {3, 4, 5}
            union_set = set1.union(set2)              # Output: {1, 2, 3, 4, 5}
            intersection_set = set1.intersection(set2) # Output: {3}    
            difference_set = set1.difference(set2)     # Output: {1, 2}
            symmetric_difference_set = set1.symmetric_difference(set2) # Output: {1, 2, 4, 5}



 """

my_set = {1,2,3,4,5}
my_set.add(7)
print(my_set)  # Output: {1, 2, 3, 4, 5, 7}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 7}
print(4 in my_set)  # Output: True

""" 
    DICTIONARIES IN PYTHON
        A dictionary is an unordered collection of key-value pairs in Python. Dictionaries are mutable, meaning you can add, remove, or modify key-value pairs after creation.
        Creating a Dictionary:
            You can create a dictionary using curly braces {} or the dict() constructor.
            Example:
                my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
                another_dict = dict(name='Bob', age=30, city='Los Angeles') 
        Basic Dictionary Operations:
            1. Accessing Values: You can access the value associated with a key using square brackets [] or the get() method.
                print(my_dict['name'])        # Output: Alice
                print(my_dict.get('age'))     # Output: 25      
            2. Adding/Modifying Key-Value Pairs: You can add a new key-value pair or modify an existing one by assigning a value to a key.
                my_dict['age'] = 26           # Modifies the age to 26  
                my_dict['country'] = 'USA'    # Adds a new key-value pair
            3. Removing Key-Value Pairs: You can remove a key-value pair using the del statement or the pop() method.
                del my_dict['city']           # Removes the key 'city'  
                age = my_dict.pop('age')      # Removes 'age' and returns its value
            4. Iterating Through a Dictionary: You can iterate through the keys, values, or key-value pairs of a dictionary using a for loop.
                for key in my_dict:
                    print(key, my_dict[key])
                for key, value in my_dict.items():          
                    print(key, value)   




 """

my_dict = {
    'name' : 'John',
    'age' : 30,
    'city' : 'San Francisco',
    'email' : 'JohnDoe@gmail.com'}

del my_dict['email']
print(my_dict)  # Output: {'name': 'John', 'age': 30
age = my_dict.pop('age')
print(my_dict)  # Output: {'name': 'John', 'city': 'San Francisco'}

for key in my_dict:
    print(key, my_dict[key])

for key,value in my_dict.items():
    print(key, value)

""" 
    SETS VS DICTIONARIES
        1. Structure:   Sets are collections of unique elements, while dictionaries are collections of key-value pairs.     
        2. Syntax: Sets are defined using curly braces {} or the set() constructor, while dictionaries are defined using curly braces {} with key-value pairs or the dict() constructor.
        3. Mutability: Both sets and dictionaries are mutable, meaning you can add, remove, or modify elements after creation.
        4. Use Cases: Sets are used when you need to store unique items and perform set operations, while dictionaries are used when you need to associate values with unique keys for efficient data retrieval.    


 """

""" 
    COMPREHENSIONS IN PYTHON
        Comprehensions provide a concise way to create lists, sets, or dictionaries in Python.

        List Comprehension:
            Syntax: [expression for item in iterable if condition]
            Example:
                squares = [x**2 for x in range(10) if x % 2 == 0]  # Output: [0, 4, 16, 36, 64]

        Set Comprehension:
            Syntax: {expression for item in iterable if condition}
            Example:
                unique_squares = {x**2 for x in range(10) if x % 2 == 0}  # Output: {0, 4, 16, 36, 64}

        Dictionary Comprehension:
            Syntax: {key_expression: value_expression for item in iterable if condition}
            Example:
                square_dict = {x: x**2 for x in range(10) if x % 2 == 0}  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}   


 """

x = [x for x in range(5)]
print(x)    # Output: [0, 1, 2, 3, 4]


""" 
    FUNCTIONS IN PYTHON
        A function is a reusable block of code that performs a specific task. Functions help in organizing code, improving readability, and reducing redundancy.

        Defining a Function:
            You can define a function using the def keyword followed by the function name and parentheses ().
            Example:
                def greet(name):
                    print("Hello, " + name + "!")

        Calling a Function:
            You can call a function by using its name followed by parentheses () and passing any required arguments.
            Example:
                greet("Alice")  # Output: Hello, Alice!

        Function Parameters and Arguments:
            - Parameters are the variables listed in the function definition.
            - Arguments are the values passed to the function when it is called.
            Example:
                def add(a, b):
                    return a + b
                result = add(5, 3)  # result is 8

        Return Statement:
            The return statement is used to exit a function and return a value to the caller.
            Example:
                def square(x):
                    return x ** 2
                result = square(4)  # result is 16

 """

def greet(name):
    print('Hello, ' + name + '!')

def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5  

def func(a,b):
    return a + b, a - b

r1, r2 = func(5,10)
print(r1, r2)       # Output: 15 -5


""" 
    UNPACK OPERATORS IN PYTHON
        The unpacking operator (*) is used to unpack elements from an iterable (like a list or tuple) into individual elements. 
        Example:
            my_list = [1, 2, 3]
            print(*my_list)  # Output: 1 2 3    



 """

new_list = [1,2,3]
print(*new_list)    # Output: 1 2 3


""" 
    ARGS AND KWARGS IN PYTHON
        *args allows a function to accept a variable number of positional arguments.    
        **kwargs allows a function to accept a variable number of keyword arguments.
        Example:        
            def my_function(*args, **kwargs):
                for arg in args:
                    print(arg)
                for key, value in kwargs.items():
                    print(f"{key}: {value}")

            my_function(1, 2, 3, name="Alice", age=25)  
            # Output:
            # 1     
            # 2
            # 3
            # name: Alice
            # age: 25       

            

 """

pairs = [(1,2), (3,4), (5,6)]   
def new_func(x,y):
    print(x, y)

for pair in pairs:
    new_func(*pair)


""" 
    SCOPE AND GLOBAL
        Scope refers to the visibility and lifetime of variables in different parts of a program. In Python, there are four types of scopes:
        1. Local Scope: Variables defined within a function are in the local scope and can only be accessed within that function.
        2. Enclosing Scope: Variables in the local scope of enclosing functions (nested functions) can be accessed by inner functions.
        3. Global Scope: Variables defined at the top level of a module or script are in the global scope and can be accessed from anywhere within that module.
        4. Built-in Scope: Python has a built-in scope that contains names of built-in functions and exceptions.

        The global keyword is used to declare that a variable inside a function refers to a global variable.
        Example:
            x = 10  # Global variable

            def my_function():
                global x
                x = 20  # Modifies the global variable
                print(x)

            my_function()  # Output: 20
            print(x)       # Output: 20


 """

""" 
    EXCEPTIONS AND ERROR HANDLING
        Exceptions are errors that occur during the execution of a program. Python provides a way to handle exceptions using try-except blocks.

        Example:
            try:
                # Code that may raise an exception
                result = 10 / 0
            except ZeroDivisionError:
                # Code to handle the exception
                print("Error: Division by zero is not allowed.")
            finally:
                # Code that will always execute
                print("Execution completed.")

        You can also catch multiple exceptions and use the else block to execute code if no exceptions occur.
        Example:
            try:
                num = int(input("Enter a number: "))
                result = 10 / num
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
            else:
                print("Result:", result)
            finally:
                print("Execution completed.")

 """

try:
    x = 7 / 0
except Exception as e:
    print("An error occuredL", e)
finally:
    print("Execution completed.")