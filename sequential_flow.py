
#today = "Tuesday":

#if today == "Monday":
  ##  print("set alarm for 5am")
#elif today == "Tuesday":
    #print("set alarm for 6am")
#elif today == "Saturday":
 #   print("set alarm for 7am")
 #else (print "set alarm for 8am")

 #message = "its hot outside" id temperature > 30 else "its not hot outside"
 #print(message)

 #day_number = 5

# prompt the user to enrer score
score = int(input("Enter the score (0-100):"))

#determines grade based on score
if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"the grade for score {score} is {grade}")

