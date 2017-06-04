"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
The three main advantages are abstraction, encapsulation, and polymorphism.
Abstraction - hiding the details we don't need
Encapsulation - Keeping everything together
Polymorphism - Interchangeability of components

2. What is a class?
Classes are a data type and the foundation of object-oriented programming.
A class defines the general behavior that a whole category of objects can have, 
and that information that can be associated with those objects.

3. What is an instance attribute?
An indiviual property define for that particular instance such as a person's salary.

4. What is a method?
A method is a like a function defined for a class. It will always have at least
one parameter, self.

5. What is an instance in object orientation?
An indiviual occurrence of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is defined for all instances for the class.
An instance attribute is only for a particular instance.
Class attribute = All humans species = "homo sapien"
Instance attribute = But each human will have an indiviual name (self.name)
"""


# Parts 2 through 5:
# Create your classes and class methods
# class AbstractObject(object):
# """ Master class created to hold attributes for the 3 subclasses who are in
# no other way connected to each other. This class will never be called on its own"""



class Student(object):
    """ Holds student information"""

    def __init__(self, first_name, last_name, address):
         """Initialize student attributes."""

         self.first_name = first_name
         self.last_name = last_name
         self.address = address

class Question(object):
    """ Questions and correct answer"""

    def __init__(self, question, correct_answer):
        """Initialize questions attributes."""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = raw_input(self.question)
        return answer == self.correct_answer

class Exam(object):
    """ Type of exams and questions"""

    def __init__(self, name):
         """Initialize exam attributes."""

         self.name = name
         self.questions = []

    def add_question(self, *questions):

        self.questions = self.questions + list(questions)

    def administer(self):
        correct_answer = 0
        for question in self.questions:
            answer = question.ask_and_evaluate()
            if answer == True:
                correct_answer +=1
        return float(correct_answer)/len(self.questions) * 100


class StudentExam(object):
    """Give student an exam."""
    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        self.score = self.exam.administer()
        print self.score


class Quiz(Exam):
    """Take attributes from parent Exam but grades differently."""
    def administer(self):
        score = super(self, Quiz).administer() #calls method from Exam 
        if score > 50:
            return True
        else:
            return False


class StudentQuiz(StudentExam):
    """Give student a quiz."""
    def __init__(self, student, quiz):
        """Initialize StudentQuiz attributes."""
        self.student = student
        self.quiz = quiz
        self.passed = None

    def take_test(self):
        self.passed = self.quiz.administer()
        print self.score


def example():
    example_exam = Exam("Practice Test")
    question_1 = Question("What is the capital of Alberta?", "Edmonton")
    question_2 = Question("Who is the author of Python?","Guido Van Rossum")
    question_3 = Question("What is 2 + 2?", "4")
    example_exam.add_question(question_1, question_2, question_3)
    example_student = Student("Pip", "Pain", "0101 Computer Street")
    example_student_exam = StudentExam(example_student, example_exam)
    example_student_exam.take_test()