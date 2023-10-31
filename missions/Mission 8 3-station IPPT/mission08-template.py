#
# CS1010S --- Programming Methodology
#
# Mission 8
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)
    data = rows[1:-2]
    age_title = rows[-2]
    rep_title = rows[-1]
    return create_table(data, age_title, rep_title)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

print("## Q1 ##")
# Sit-up score of a 24-year-old who did 10 sit-ups.
print(access_cell(situp_table, 24, 10))    # 0

# Push-up score of a 18-year-old who did 30 push-ups.
# print(access_cell(pushup_table, 18, 30))   # 16

# Run score of a 30-year old-who ran 12 minutes (720 seconds)
# print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
# print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def pushup_score(pushup_table, age, pushup):
    "Your Solution Here"

def situp_score(situp_table, age, situp):
    "Your Solution Here"

def run_score(run_table, age, run):
    "Your Solution Here"

# print("## Q2 ##")
# print(pushup_score(pushup_table, 18, 61))   # 25
# print(pushup_score(pushup_table, 18, 70))   # 25
# print(situp_score(situp_table, 24, 0))      # 0

# print(run_score(run_table, 30, 720))        # 36
# print(run_score(run_table, 30, 725))        # 35
# print(run_score(run_table, 30, 735))        # 35
# print(run_score(run_table, 30, 500))        # 50
# print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    "Your Solution Here"

# print("## Q3 ##")
# print(ippt_award(50))     # F
# print(ippt_award(51))     # P
# print(ippt_award(61))     # P$
# print(ippt_award(75))     # S
# print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    "Your solution here"

# print("## Q4 ##")
# print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
# print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
# print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
# print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
# print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########

def parse_results(csvfilename):
    "Your solution here"

# print("## Q5 ##")
ippt_takers_data = parse_results("ippt_takers_data.csv")
# print(ippt_takers_data[0])
# print(ippt_takers_data[1])
# print(ippt_takers_data[2])
# print(ippt_takers_data[3])

# Expected Output:
# ('Name', 'Age', 'Push-Ups', 'Sit-Ups', '2.4-Km-Run', 'Total-Score', 'Award')
# ('Sean Hendricks', 38, 25, 74, 1212, 42, 'F')
# ('Phillip Brown DDS', 59, 15, 15, 852, 61, 'P$')
# ('Ryan Gray MD', 24, 45, 78, 1074, 46, 'F')


##########
# Task 6 #
##########

def num_awards(ippt_takers_data, age):
    "Your solution here"

# print("## Q6 ##")
# print(num_awards(ippt_takers_data, 25))
# print(num_awards(ippt_takers_data, 28))

# Expected Output:
# {'F': 56, 'P': 20, 'G': 18, 'P$': 14, 'S': 10}
# {'F': 54, 'S': 13, 'G': 16, 'P': 8, 'P$': 12}


##########
# Task 7 #
##########

def top_k_scores(ippt_takers_data, k, age):
    "Your solution here"

# print("## Q7 ##")
# print(top_k_scores(ippt_takers_data, 5, 25))
# print(top_k_scores(ippt_takers_data, 1, 28))
# print(top_k_scores(ippt_takers_data, 2, 28))

# Expected Output:
# [('Joseph Burns', 100), ('Mike Williams', 98), ('Rachel Serrano', 98), ('Margaret Jennings', 97), ('Alexandra Day', 95), ('Stephen Boyer', 95)]
# [('Eric Villegas', 100), ('Melissa Evans', 100)]
# [('Eric Villegas', 100), ('Melissa Evans', 100)]