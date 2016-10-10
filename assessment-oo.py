"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main advantages of object orientation are abstraction,
   encapsulation, and polymorphism. The idea of abstraction is that by creating
   methods to the class that can be referenced and used later without actually
   knowing each line of codes written in each method. It saves programers a lot
   of time by just calling the method itself, without going through the codes
   under methods. Encapsulation means that each class will have defined different
   instances and their attributes which they are all come as a package under class.
   polymorphism is referring to the ability of interchanging the use of instances
   within data tree inside class and subclasses. subclasses instances can inherit the
   class attributes and methods and also creat local versions of that.


2. What is a class?
    A class is an user-defined type of things that enable

3. What is an instance attribute?
    An instance attribute is the variable that lives only in that instance.

4. What is a method?
    A method is a function that is defined under class definition.

5. What is an instance in object orientation?
    An instance in obeject orientation is an object of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   The difference between class attributes and instance attributes is that class
   attributes are shared throughout the entire class, whereas instance attributes
   only belongs to the corresponding instances which other instances cannot call on.

"""


# Parts 2 through 5:

# Create your classes and class methods

class Student(object):
    """A student class."""

    def __init__(self, f_name, l_name, address):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address

student1 = Student('Jasmine', 'Debugger', '0101 Computer Street')
student2 = Student('Jaqui', 'Console', '888 Binary Ave')


class Question(object):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

question1 = Question('What is the capital of Alberta?', 'Edmonton')
question2 = Question('Who is the author of Python?', 'Guido Van Rossum')

class Exam(object):
    def __init__(self, name):
        questions = []

midterm = Exam(questions)
final = Exam(questions)

    def add_question(self, question, correct_answer):
        print Question.question1,.add()


