"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction: 
   You keep "unneccessary" details hidden. No need to know how exactly that
   is being done as long as it is being done correctly.

   Encapsulation: 
   Helps keep your code organized and easily accessible for maintance and
   corrections. 

   Polymorphism: 
   Helps predictability. Subclasses of a class should always have
   the same parameters. 

2. What is a class?
    Class is a tool that lets you structure your software in particular ways. 
    It helps keep organization and maintain consistency.

3. What is an instance attribute?
    Similar to a key in a dictionary. 
    An attribute is a method particular to that one instance, and not common
    to all objects in the class. 

4. What is a method?
    A method is a function defined inside a class or subclass.

5. What is an instance in object orientation?
    An instance is the occurrence of a class. Equivalent to an object.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute is something common to everything in that class.
   A instance attribute is pertinent only for that instance of the class and
   not for everything else. 



"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Store student data. 
    Names, last names and addresses. 
    
    """

    def __init__(self, first_name, last_name, address):

        self.first_name = first_name
        self.last_name = last_name
        self. address = address


class Question(object):
    """Stores questions and their correct answers. 
    """

    def __init__(self, question, correct_answer):
        # should enter question and answer as strings.

        self.add_question = question
        self.correct_answer = correct_answer

    def ask_question(self):

        user_answer = raw_input(self.add_question)

        if user_answer == self.correct_answer: 
            return True

        else: 
            return False


class Exam(object):
    """Stores questions to later generate exams. """

    def __init__(self, name):

        self.questions = []
        # list for questions to be used for exams? 

    def add_question(self, question):
        """Adds questions to specific exams."""

        self.questions.append(question)

    def administer(self):

        right_answers = 0
        wrong_answers = 0

        for question in self.questions: 
            
            if question.ask_question() == True: 
                right_answers += 1

            else: 
                wrong_answers += 1

        score = float(right_answers) / (right_answers + wrong_answers)

        return score

class StudentExam(object):
    """Stores students, exams and student's score for said exam."""

    def __init__(self, student, exam):

        self.student = student
        self.exam = exam


    def take_test(self):
        """Administers exam and assigns score to StudentExam"""

        self.score = self.exam.administer()
        
        print "Your score is {}.".format(self.score)


class Quiz(Exam):
    """Adjusts the score to be 1 for Pass or 0 for Fail."""
    
    def administer(self):
        score = super(Quiz, self).administer()

        if float(score) > 0.5:
            return "Your score is 1. You passed!"

        else: 
            return "Your score is 0. You failed."




def example():

    exam = Quiz('Midterm')

    question_1 = Question('What is the method for adding an element to a set? ',
        '.add()')
    exam.add_question(question_1)
    question_2 = Question('What does pwd stand for? ', 'print working directory')
    exam.add_question(question_2)
    question_3 = Question('What are the three class advantages? ',
                            'abstraction, encapsulation and polymorphism')
    exam.add_question(question_3)

    student = Student('Kenner', 'Miner', '1155 4th St.')
    
    student_exam = StudentExam(student, exam)
    
    student_exam.take_test()








