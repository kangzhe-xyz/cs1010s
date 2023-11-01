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
    rep_title = ()
    for i in rows[0][1:]:
        rep_title += (int(i),)
    data = ()
    age_title = ()
    for i in rows[1:]:
        age_title += (int(i[0]),)
        data_to_add = ()
        for j in i[1:]:
            data_to_add += (int(j),)
        data += (data_to_add,)
        
    return create_table(data, age_title, rep_title)


pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

print("## Q1 ##")
# Sit-up score of a 24-year-old who did 10 sit-ups.
print(access_cell(situp_table, 24, 10))    # 0

# Push-up score of a 18-year-old who did 30 push-ups.
print(access_cell(pushup_table, 18, 30))   # 16

# Run score of a 30-year old-who ran 12 minutes (720 seconds)
print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def event_score(the_table, age, event): # simple HOF for Situp and Pushup
    if event < 1:
        event = 1
    elif event > 60:
        event = 60
    
    return access_cell(the_table, age, event)

def pushup_score(pushup_table, age, pushup):
    return event_score(pushup_table, age, pushup)

def situp_score(situp_table, age, situp):
    return event_score(situp_table, age, situp)

def run_score(run_table, age, run):
    if run % 10 != 0:
        run += (10 - run % 10)
        
    if run >= 1110:
        run = 1110
    elif run < 510:
        run = 510
    return access_cell(run_table, age, run)

print("## Q2 ##")
print(pushup_score(pushup_table, 18, 61))   # 25
print(pushup_score(pushup_table, 18, 70))   # 25
print(situp_score(situp_table, 24, 0))      # 0

print(run_score(run_table, 30, 720))        # 36
print(run_score(run_table, 30, 725))        # 35
print(run_score(run_table, 30, 735))        # 35
print(run_score(run_table, 30, 500))        # 50
print(run_score(run_table, 30, 1111))       # 0

##########
# Task 3 #
##########

def ippt_award(score):
    if score < 51:
        return "F"
    elif 51 <= score < 61:
        return "P"
    elif 61 <= score < 75:
        return "P$"
    elif 75 <= score < 85:
        return "S"
    else:
        return "G"

print("## Q3 ##")
print(ippt_award(50))     # F
print(ippt_award(51))     # P
print(ippt_award(61))     # P$
print(ippt_award(75))     # S
print(ippt_award(85))     # G

##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    score = 0
    score += pushup_score(get_pushup_table(ippt_table), age, pushup)
    score += situp_score(get_situp_table(ippt_table), age, situp)
    score += run_score(get_run_table(ippt_table), age, run)
    letter_grade = ippt_award(score)
    return (score, letter_grade)

print("## Q4 ##")
print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########

def parse_results(csvfilename):
    rows = read_csv(csvfilename)
    final = ()
    final += (('Name', 'Age', 'Push-Ups', 'Sit-Ups', '2.4-Km-Run', 'Total-Score', 'Award'),)
    for i in rows[1:]:
        name = i[0]
        age = int(i[1])
        pushup, situp, twopointfour = int(i[2]), int(i[3]), int(i[4])
        the_results = ippt_results(ippt_table, age, pushup, situp, twopointfour)
        the_row = (name, age, pushup, situp, twopointfour, the_results[0], the_results[1])
        final += (the_row,)
    return final

# print("## Q5 ##")
ippt_takers_data = parse_results("ippt_takers_data.csv")
print(ippt_takers_data[0])
print(ippt_takers_data[1])
print(ippt_takers_data[2])
print(ippt_takers_data[3])

# Expected Output:
# ('Name', 'Age', 'Push-Ups', 'Sit-Ups', '2.4-Km-Run', 'Total-Score', 'Award')
# ('Sean Hendricks', 38, 25, 74, 1212, 42, 'F')
# ('Phillip Brown DDS', 59, 15, 15, 852, 61, 'P$')
# ('Ryan Gray MD', 24, 45, 78, 1074, 46, 'F')


##########
# Task 6 #
##########

def num_awards(ippt_takers_data, age):
    awards_dictionary = {"F": 0, "P": 0, "P$": 0, "S": 0, "G": 0}
    for i in ippt_takers_data[1:]:
        if i[1] == age:
            awards_dictionary[i[-1]] += 1
    return awards_dictionary

print("## Q6 ##")
print(num_awards(ippt_takers_data, 25))
print(num_awards(ippt_takers_data, 28))

# Expected Output:
# {'F': 56, 'P': 20, 'G': 18, 'P$': 14, 'S': 10}
# {'F': 54, 'S': 13, 'G': 16, 'P': 8, 'P$': 12}


##########
# Task 7 #
##########

def top_k_scores(ippt_takers_data, k, age):
    listed_data = list(ippt_takers_data[1:])
    listed_data.sort(key = lambda x: str(x[0])) # sort by name first
    listed_data.sort(key = lambda x: int(x[-2]), reverse = True) # sort by score
    result = []
    for j in range(100,0,-1): # sets a threshold
        people_to_add = ()
        for i in listed_data: # run through
            if i[1] == age and i[-2] == j: # check age and score
                people_to_add += ((i[0], i[-2]),) # if match, add
        result += tuple(people_to_add) # add to result
        if len(result) >= k or j == 0: # terminating condition. if less than k, continue. if more than, return. if no more score, return.
            return result
        else: continue
    
        
print("## Q7 ##")
print(top_k_scores(ippt_takers_data, 5, 25))
print(top_k_scores(ippt_takers_data, 1, 28))
print(top_k_scores(ippt_takers_data, 2, 28))

# Expected Output:
# [('Joseph Burns', 100), ('Mike Williams', 98), ('Rachel Serrano', 98), ('Margaret Jennings', 97), ('Alexandra Day', 95), ('Stephen Boyer', 95)]
# [('Eric Villegas', 100), ('Melissa Evans', 100)]
# [('Eric Villegas', 100), ('Melissa Evans', 100)]