import random

# quiz_file = open('io files/quiz_file.txt', 'w')

# for i in range(100):
#     random_num = random.randint(50,100)
#     quiz_file.write(str(random_num) + "\n")
# quiz_file.close()

# # way number 2 (better way) without worrying about closing file

# with open('io files/quiz_file.txt', 'w') as quiz_file:
#     for i in range(100):
#         random_num = random.randint(50,100)
#         quiz_file.write(str(random_num) + "\n")


# #7
# with open("io files/LibraryVisits.csv", "r") as daily_visits:
#     total_visitors = 0
#     total_days = 0
#     for row in daily_visits:
#         row_items = row.split(",")
#         total_visitors += int(row_items[1])
#         total_days += 1
#     print(f' Average number of visitors at the library is: {total_visitors/total_days}')


#1

# with open('QuizInts.txt', 'w') as f:
#     for i in range(100):
#         random_num = random.randint(50,200)
#         f.write(str(random_num) + '\n')

#2

# with open('thisFile.txt', 'r') as f:
#     with open('thatFile.txt', 'w') as d:
#         for i, line in enumerate(f):
#             if i % 2 == 0:
#                 d.write(line)

#3

# with open('MyName.txt', 'w') as f:
#     f.write('Fatah Ibrahim')

# with open('MyName.txt', 'r') as q:
#     for line in q:
#         for y in line:
#             print(y)

#5 
# with open('LunchData.txt', 'r') as f:
#     total_served = 0
#     for row in f:
#         f_ppl = row.split()
#         total_served += int(f_ppl[1])
#     print(total_served)
    

#6 
with open('aMorePerfectUnion.txt', 'r') as f:
    amount_of_letters = {}
    file_context = f.read()
    lower = file_context.lower()
    for letter in lower:
        if letter in amount_of_letters:
            amount_of_letters[letter] += 1
        else:
            amount_of_letters[letter] = 1

print(amount_of_letters)


#11

# with open('SongPlays.txt', 'r') as f:
#     next(f)
#     amount_plays = {}
#     for line in f:
#         parts = line.strip().split()
#         if len(parts) >= 2:
#             name = parts[0]
#             play_count = int(parts[1])
#             amount_plays[name] = play_count
#     print(amount_plays)

#12


        
