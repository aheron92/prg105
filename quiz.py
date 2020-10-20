"""
Creates 10 instances of questions,
lets 2 people answer 5 questions each and
determines winner.
"""


import question


def main():
    q1 = question.Question("Which nut is used to make dynamite? ", "A. Almonds", "B. Pine nuts", "C. Peanuts",
                           "D. Walnuts", "C")
    q2 = question.Question("What was the first cold breakfast cereal invented in 1863? ", "A. Corn flakes",
                           "B. Granola", "C. Bran flakes", "D. Cheerios", "B")
    q3 = question.Question("Who invented Coca-Cola? ", "A. Asa Griggs Candler", "B. Charles Elmer Hires",
                           "C. John Matthews", "D. John Pemberton", "D")
    q4 = question.Question("How many calories per gram are stored in protein? ", "A. 2", "B. 3", "C. 4", "D. 5", "C")
    q5 = question.Question("What is the only U.S. state to grow coffee beans? ", "A. Florida", "B. California",
                           "C. Hawaii", "D. Louisiana", "C")
    q6 = question.Question('What does the word "onion" mean in Latin? ', "A. White sphere", "B. Small oyster",
                           "C. Large pearl", "D. White oyster", "C")
    q7 = question.Question("What is the only edible food that never expires? ", "A. White rice", "B. Honey", "C. Rye",
                           "D. Barley", "B")
    q8 = question.Question("What condiment was sold in the 1830’s as medicine? ", "A. Soy Sauce", "B. Ranch dressing",
                           "C. Ketchup", "D. Maple syrup", "C")
    q9 = question.Question("What is a tall chef’s hat called? ", "A. Trilby", "B. Toque", "C. Skull cap",
                           "D. Bucket hat", "B")
    q10 = question.Question("How many flowers do honeybees need to visit in order to make one pound of honey? ",
                            "A. 900,000", "B. 1 million", "C. 1.5 million", "D. 2 million", "D")

    set_1 = [q1, q2, q3, q4, q5]
    set_2 = [q6, q7, q8, q9, q10]

    player1 = 0
    player2 = 0

    print("Welcome to the Food Trivia Game!  Each player will be given 5 questions to answer.  Player 1 goes first!")

    for query in set_1:
        print('\n')
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter of the correct answer: ")
        if guess.upper() == query.get_answer():
            print("Right you are!")
            player1 += 1
            print("Player 1 earned: " + str(player1) + " points.")
        else:
            print("Sorry, that is incorrect.")

    for query in set_2:
        print('\n')
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess2 = input("Please enter the letter of the correct answer: ")
        if guess2.upper() == query.get_answer():
            print("Right you are!")
            player2 += 1
            print("Player 2 earned: " + str(player2) + " points.")
        else:
            print("Sorry, that is incorrect.")


main()
