from pywebio.input import *
from pywebio.output import *
from flask import Flask 
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
#create a flask app
app = Flask(__name__)

def exam():
    name = input("Enter your name to start the exam", type="text")
    
    # Initialize the variable c to count correct answers
    c = 0

    # Question 1
    q1 = radio("If A can complete a job in 8 days and B can complete the same job in 12 days, how long will they take together to finish the job?", ["4 days", "5 days", "6 days", "7 days"])
    if q1 == "6 days":
        c += 1

    # Question 2
    q2 = radio("If 4 workers can complete a project in 20 days, how many days will 6 workers take to complete the same project?", ["10 days", "12 days", "15 days", "18 days"])
    if q2 == "12 days":
        c += 1

    # Question 3
    q3 = radio("If A can complete a job in 10 days and B can complete the same job in 15 days, how much of the job would be completed by A in one day?", ["1/10", "1/12", "1/15", "1/20"])
    if q3 == "1/10":
        c += 1

    # Question 4
    q4 = radio("If C can complete a job in 18 days and D can complete the same job in 24 days, how many days will they take to finish the job working together?", ["8 days", "9 days", "10 days", "12 days"])
    if q4 == "10 days":
        c += 1

    # Question 5
    q5 = radio("If a machine can produce 200 units of a product in 5 hours, how many units can it produce in 8 hours?", ["320 units", "400 units", "480 units", "520 units"])
    if q5 == "520 units":
        c += 1

    # Question 6
    q6 = radio("If P can complete a job in 15 days and Q can complete the same job in 20 days, how many days will it take for P and Q together to complete the job?", ["6 days", "8 days", "10 days", "12 days"])
    if q6 == "6 days":
        c += 1

    # Question 7
    q7 = radio("If X can complete a job in 9 days and Y can complete the same job in 12 days, how many days will it take for X and Y together to complete twice the job?", ["6 days", "8 days", "10 days", "12 days"])
    if q7 == "8 days":
        c += 1

    # Question 8
    q8 = radio("If M can complete a job in 25 days and N can complete the same job in 30 days, how many days will it take for N to complete the job alone if M leaves after working for 10 days?", ["12 days", "15 days", "18 days", "20 days"])
    if q8 == "15 days":
        c += 1

    # Question 9
    q9 = radio("If A and B together can complete a job in 7 days, and B alone can complete the job in 14 days, how long would it take for A to complete the job alone?", ["10 days", "14 days", "21 days", "28 days"])
    if q9 == "4 days":
        c += 1

    # Question 10
    q10 = radio("If a team of 8 people can build a wall in 6 days, how long would it take for a team of 12 people to build the same wall?", ["3 days", "4 days", "5 days", "6 days"])
    if q10 == "18 days":
        c += 1

    # Question 11
    q11 = radio("If the average of five consecutive even integers is 24, what is the largest of these integers?", ["44", "46", "48", "50"])
    if q11 == "48":
        c += 1

    # Question 12
    q12 = radio("A train travels 300 miles in 3 hours. What is its average speed in miles per hour?", ["50 mph", "75 mph", "100 mph", "150 mph"])
    if q12 == "100 mph":
        c += 1

    # Question 13
    q13 = radio("If the price of a product is increased by 20%, by what percentage should it be reduced to bring it back to its original price?", ["16%", "18%", "20%", "25%"])
    if q13 == "16%":
        c += 1

    # Question 14
    q14 = radio("The sum of three consecutive odd integers is 69. What is the middle integer?", ["21", "23", "25", "27"])
    if q14 == "25":
        c += 1

    # Question 15
    q15 = radio("A bag contains 5 red balls and 4 green balls. If two balls are drawn randomly, what is the probability that both are red?", ["1/18", "1/15", "1/10", "1/9"])
    if q15 == "1/9":
        c += 1

    # Question 16
    q16 = radio("If 3x - 5 = 16, what is the value of 4x?", ["9", "11", "13", "15"])
    if q16 == "15":
        c += 1

    # Question 17
    q17 = radio("The area of a rectangle is 45 square meters. If the length is 9 meters, what is the width of the rectangle?", ["3 meters", "4 meters", "5 meters", "6 meters"])
    if q17 == "5 meters":
        c += 1

    # Question 18
    q18 = radio("If a shirt costs $20 and is discounted by 25%, what is the final price of the shirt?", ["$12.50", "$15.00", "$17.50", "$18.75"])
    if q18 == "$15.00":
        c += 1

    # Question 19
    q19 = radio("If a car travels 120 miles in 2 hours, what is its average speed in miles per minute?", ["1", "1.5", "2", "2.5"])
    if q19 == "2.5":
        c += 1

    # Question 20
    q20 = radio("If the product of two consecutive integers is 72, what are the integers?", ["8 and 9", "9 and 10", "10 and 11", "11 and 12"])
    if q20 == "9 and 10":
        c += 1

    # Checks pass or fail
    if c > 18:
        put_text(name + ", your score is " + str(c))
        style(put_text("Result: Passed"), "color:green")
    else:
        put_text(name + ", your score is " + str(c))
        style(put_text("Result: Failed"), "color:red")
    put_text("Thank You for participating....")
app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])
app.run(host="localhost",port=5000)