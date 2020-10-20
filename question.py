"""
Lesson Objective(s):
-Create Classes
-Create multiple instances (objects) of a class

Lesson:
In this programming exercise, you will create a simple trivia game for two players. The program will work like this:

Starting with player 1, each player gets a turn at answering 5 trivia questions. (There should be a total of
10 questions.) When a question is displayed, 4 possible answers are also displayed. Only one of the answers is correct,
and if the player selects the correct answer, he or she earns a point.
After answers have been selected for all the questions, the program displays the number of points earned by each player
and declares the player with the highest number of points the winner.
To create this program, write a Question class to hold the data for the trivia question. The question class should have
attributes for the following data:

A trivia question
Possible answer 1
Possible answer 2
Possible answer 3
Possible answer 4
The number of the correct answer (1, 2, 3, or 4)
The Question class should also have an appropriate __init__ method, accessors, and mutators.

The program should have a list or a dictionary containing 10 Question Objects, one for each trivia question.
Make up your own trivia question on the subject or subjects of your choice for the objects.
"""


class Question:
    def __init__(self, question, a1, a2, a3, a4, answer):
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__answer = answer

    def set_question(self, question):
        self.__question = question

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self, a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self, a4):
        self.__a4 = a4

    def set_answer(self, answer):
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_answer(self):
        return self.__answer
