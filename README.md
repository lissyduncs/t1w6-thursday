# t1w6-thursday

## control flow
order in which lines of code ar execited in a program
print("hello, welcome to programming with Python")

a=10
b=5
result = a + b

print(f"the result of adding {a} nd {b} is {result}")

print("thank you")

# sequential control flow
Execution of code statements based on some input

if tomorrow is Saturday
    set alarm for 7

if tomorrow is Friday, 
    set alarm for 6

 # Boolean data type
 Data type that has two values: True or False. Boolean values are used to control of the program

 # Comparison operator/relational operators
 Decide the relationship between the operands. Result of the comparison is a boolean value (True?False)

 if tomorrow ==Saturady

 # if, elif, else, 
 simplest form of AI
 if checks the condition
 #today = "Tuesday":

#if today == "Monday":
  ##  print("set alarm for 5am")
#elif today == "Tuesday":
    #print("set alarm for 6am")
#elif today == "Saturday":
 #   print("set alarm for 7am")
 #else (print "set alarm for 8am")

 # pass
 does nothing, just passes... for now

 # Boolean Operators

 AND, OR NOT. Operands need to be Boolean as well
 or= if either is true=true

# terminory operator
condenses series of code to one line
 message = "its hot outside" id temperature > 30 else "its not hot outside"
 print(message)

# match case
day_number= 3

match day_number: 
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"
    case 3:
        day_name = "Wednesday"
    case 4:
        day_name = "Thursday"
    
print(day_name)