# define the cheese_and_crackers function with two arguments: cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")


print("We can just give the function numbers directly:")
# call funtion with numbers
cheese_and_crackers(20, 30)


print("Or we can use variables from our script:")
# name two variables
amount_of_cheese = 10
amount_of_crackers = 50

# call function with variables defined above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# call function with maths
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# call funtion with variable and maths
print("And we can combine to two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 200)


# Evaluation function
def evaluation_eleves(final_score, mid_term_score, absence):
    print(f"The student has {absence} during the semester.")
    print(f"The student has a mid-term score of {mid_term_score} points.")
    print(f"Final score of the student for the semester is {final_score} points.")
    if final_score > 9:
        print("Congradualation, the student has passed the evaluation!")
    else:
        print("Sorry, the student has not passed the evaluation.")

print("Please input times of absence, as well as the mid-term score and the final score below.")
absence_input_users = int(input('> Times of absences: '))
mid_term_score_input_users = int(input('> Mid-term_score: '))
final_score_input_users = int(input('> Final score: '))

evaluation_eleves(final_score_input_users, mid_term_score_input_users, absence_input_users)

print("This is the end of the evaluation. \nThanks you.")
