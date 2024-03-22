import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_verbal_question():
    # Generate a variety of verbal problems
    problem_type = random.choice(['Basic English', 'Advanced English'])
    
    if problem_type == 'Basic English':
        question = "What is the opposite of 'up'?"
        options = ['A) Down', 'B) Left', 'C) Right', 'D) Above']
        correct_option = 'A'
    else:  # Advanced English
        question = "What is the meaning of the word 'ubiquitous'?"
        options = ['A) Present everywhere', 'B) Unique', 'C) Rare', 'D) Limited to a region']
        correct_option = 'A'
    
    return question, options, correct_option

def generate_arithmetic_question():
    # Generate a variety of arithmetic problems
    problem_type = random.choice(['Train', 'Advanced Arithmetic', 'Partnership', 'Profit and Loss', 'Banking Maths'])
    
    if problem_type == 'Train':
        speed = random.randint(40, 80)
        time = random.randint(5, 15)
        length = (speed * 5) * time // 18
        question = f"A train running at the speed of {speed} km/hr crosses a pole in {time} seconds. What is the length of the train?"
        options = [f'A) {length}', f'B) {length + 10}', f'C) {length - 10}', f'D) {length + 20}']
        correct_option = 'A'
    elif problem_type == 'Advanced Arithmetic':
        num1 = random.randint(50, 100)
        num2 = random.randint(10, 50)
        question = f"What is the result of {num1} divided by {num2} plus {num2} multiplied by {num1}?"
        options = [f'A) {num1 // num2 + num2 * num1}', f'B) {num1 // num2 - num2 * num1}', f'C) {num1 * num2 + num2 // num1}', f'D) {num1 // num2 + num1 * num2}']
        correct_option = 'A'
    elif problem_type == 'Partnership':
        investment_A = random.randint(1000, 5000)
        investment_B = random.randint(1000, 5000)
        ratio_A = random.randint(1, 5)
        ratio_B = random.randint(1, 5)
        time = random.randint(1, 5)
        profit = random.randint(500, 2000)
        question = f"A and B invest in a business in the ratio {ratio_A} : {ratio_B}. If they share a profit of Rs. {profit} after {time} years, how much does each get?"
        total_investment = investment_A + investment_B
        share_A = (investment_A / total_investment) * profit
        share_B = (investment_B / total_investment) * profit
        options = [f'A) {round(share_A)}', f'B) {round(share_B)}', f'C) {round(share_A) - 100}', f'D) {round(share_B) + 100}']
        correct_option = 'A'
    elif problem_type == 'Profit and Loss':
        cost_price = random.randint(1000, 5000)
        profit_percentage = random.randint(10, 50)
        selling_price = int(cost_price * (1 + profit_percentage / 100))
        question = f"A shopkeeper sells an item at Rs. {selling_price} with a profit of {profit_percentage}%. What is the cost price of the item?"
        options = [f'A) {cost_price}', f'B) {cost_price - 200}', f'C) {cost_price + 300}', f'D) {cost_price * 2}']
        correct_option = 'A'
    else:  # Banking Maths
        principal = random.randint(10000, 50000)
        rate = random.randint(5, 15)
        time = random.randint(1, 5)
        compound_interest = int(principal * ((1 + rate / 100) ** time))
        question = f"What is the compound interest on a principal amount of Rs. {principal} at {rate}% per annum compounded annually for {time} years?"
        options = [f'A) {compound_interest}', f'B) {compound_interest + 5000}', f'C) {compound_interest - 3000}', f'D) {compound_interest * 2}']
        correct_option = 'A'
    
    return question, options, correct_option

def generate_logical_question():
    # Generate a variety of logical problems
    problem_type = random.choice(['Sequence Prediction', 'Blood Relation', 'Directions', 'Seating Arrangement', 'Coding-Decoding'])
    
    if problem_type == 'Sequence Prediction':
        sequence = [random.randint(1, 10) for _ in range(4)]
        next_number = sequence[-1] + (sequence[1] - sequence[0])
        question = f"What number comes next in the sequence: {sequence[0]}, {sequence[1]}, {sequence[2]}, ___?"
        options = [f'A) {next_number}', f'B) {next_number + 1}', f'C) {next_number - 1}', f'D) {next_number * 2}']
        correct_option = 'A'
    elif problem_type == 'Blood Relation':
        question = "John's father's sister is Mike's mother. How is Mike related to John?"
        options = ['A) Aunt', 'B) Uncle', 'C) Sister', 'D) Brother']
        correct_option = 'A'
    elif problem_type == 'Directions':
        question = "If you are facing north and you turn 90 degrees clockwise, which direction are you facing now?"
        options = ['A) East', 'B) West', 'C) South', 'D) North-East']
        correct_option = 'A'
    elif problem_type == 'Seating Arrangement':
        question = "If A sits next to B, and B sits next to C, who sits in the middle?"
        options = ['A) A', 'B) B', 'C) C', 'D) D']
        correct_option = 'B'
    else:  # Coding-Decoding
        question = "If 'BENCH' is coded as 'FJSLR', what is the code for 'APPLE'?"
        options = ['A) FPXMP', 'B) FUURP', 'C) FPYOM', 'D) FFUEM']
        correct_option = 'B'
    
    return question, options, correct_option

def generate_fake_question():
    # Choose a random question type
    category = random.choice(['Verbal', 'Arithmetic', 'Logical'])
    if category == 'Verbal':
        return generate_verbal_question()
    elif category == 'Arithmetic':
        return generate_arithmetic_question()
    else:
        return generate_logical_question()

if __name__ == "__main__":
    num_questions = 200000

    question_data = []
    questions_added = set()

    while len(questions_added) < num_questions:
        question = generate_fake_question()
        if question[0] not in questions_added:  # Ensure unique questions
            question_data.append({'Question': question[0], 'Option1': question[1][0], 'Option2': question[1][1], 'Option3': question[1][2], 'Option4': question[1][3], 'CorrectOption': question[2]})
            questions_added.add(question[0])

    df = pd.DataFrame(question_data)
    df.to_csv("aptitude_questions.csv", index=False)

    print("CSV file generated successfully!")
