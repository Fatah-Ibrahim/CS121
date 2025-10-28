amounts_of_standards_met = int(input("How many standards have you meet?: "))
amounts_of_zeros = int(input("How many zeros did you get?: "))

if amounts_of_standards_met >= 57:
    print("Your grade is A+")
elif amounts_of_standards_met <= 56 and amounts_of_zeros == 0:
   print("Your grade is A")
elif amounts_of_standards_met <= 52 and amounts_of_zeros == 0:
    print("Your grade is A-")
elif amounts_of_standards_met <= 50 and amounts_of_zeros == 0:
   print("Your grade is B+")
elif amounts_of_standards_met <= 47 and amounts_of_zeros == 0:
   print("Your grade is B")
elif amounts_of_standards_met <= 45 and amounts_of_zeros == 0:
    print("Your grade is B-")
elif amounts_of_standards_met <= 43 and amounts_of_zeros == 0:
    print("Your grade is C+")
elif amounts_of_standards_met <= 40:
   print("Your grade is C")
elif amounts_of_standards_met <= 35:
    print("Your grade is D")
elif amounts_of_standards_met <= 43 and amounts_of_zeros <= 3:
    print("Your grade is F")
