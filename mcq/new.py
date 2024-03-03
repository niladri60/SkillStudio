import requests
from pywebio.input import *
from pywebio.output import *

def fetch_questions():
    # Specify the number of questions and the category
    num_questions = 20
    category = 9  # General Knowledge

    # Make a request to the Open Trivia Database API
    response = requests.get(f'https://opentdb.com/api.php?amount={num_questions}&category={category}&type=multiple')
    
    # Parse the JSON response
    data = response.json()

    # Extract and return the list of questions
    return data['results']

def exam():
    name = input("Enter your name to start the exam", type="text")

    # Fetch questions from the API
    questions = fetch_questions()

    # Initialize the variable c to count correct answers
    c = 0

    for i, question in enumerate(questions, 1):
        # Extract question and options from the API response
        q_text = question['question']
        q_options = question['incorrect_answers']
        correct_answer = question['correct_answer']

        # Add the correct answer to the options list
        q_options.append(correct_answer)

        # Shuffle the options to avoid bias
        random.shuffle(q_options)

        # Present the question to the user
        user_answer = radio(f"Question {i}: {q_text}", q_options)

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            c += 1

    # Checks pass or fail
    if c > 10:
        put_text(name + ", your score is " + str(c))
        style(put_text("Result: Passed"), "color:green")
    else:
        put_text(name + ", your score is " + str(c))
        style(put_text("Result: Failed"), "color:red")

    put_text("Thank You for participating....")

# Run the exam function
exam()
