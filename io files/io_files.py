import random

quiz_file = open('io files/quiz_file.txt', 'w')

for i in range(100):
    random_num = random.randint(50,100)
    quiz_file.write(str(random_num) + "\n")
quiz_file.close()

# way number 2 (better way) without worrying about closing file

with open('io files/quiz_file.txt', 'w') as quiz_file:
    for i in range(100):
        random_num = random.randint(50,100)
        quiz_file.write(str(random_num) + "\n")


#7
with open("io files/LibraryVisits.csv", "r") as daily_visits:
    total_visitors = 0
    total_days = 0
    for row in daily_visits:
        row_items = row.split(",")
        total_visitors += int(row_items[1])
        total_days += 1
    print(f' Average number of visitors at the library is: {total_visitors/total_days}')
