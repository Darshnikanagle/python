# conditional statement (if/elif/else)

# # 1.if statement(simple condition check)
# age=18
# if age>=18:
#     print("you are eligible to vote.")


# if-else statement(two options:true/flase)

# tem=60
# if tem>25:
#     print("it is a hot")
# else:
#     print("it is a cool day")

# # 1.check odd and even no
# num=int(inpt("enter a number:"))
# ifnum%2==0 print


# age=18
# if age>=18:
#     print("you are eligible to vote.")
# else:
#     print("you are not eligible to vote")

# # checking pass or fail

# marks=int(input("enter your marks:"))
# if marks>40:
#     print("you passd the exam")
# else:
#     print("you failed the exam!")
 
# #  check add or even number

# num=int(input("Enter a numbr:"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")




# if-elif-else statement(multiple condition)
# grading system
marks=int(input("enter your marks:"))

if marks>90:
    print("grade:A")
elif marks>75:
    PRINT("GRADE:B")
elif marks>50:
    PRINT("GRADE:C")
else:
    PRINT("GRADE:F(FAIL)")


# checking temp

# temp=int(input("enter the temp:"))
# if temp>30:
#     print('it is hot outside:')
# elif temp>20:
#     print("it is weather is warm:")
# elif temp>10:
#     print("it bit cold:")
# else:
#     print("it is very cold outside:")
   

# number checking (positive, negative,zera)

# num= int(input("enter a number:"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")


# Problem 4: Time of Day Greeting
# Write a Python program that takes the hour of the day (in 24-hour format) as input and prints a greeting:

# If the time is between 5 AM and 11 AM, print "Good morning".
# If the time is between 12 PM and 5 PM, print "Good afternoon".
# If the time is between 6 PM and 10 PM, print "Good evening".
# If the time is between 11 PM and 4 AM, print "Good night".
   
# hour= int(input("enter the hour(0-23):"))
# if 5<=hour<=11:
#     print("good morning")
# elif 12<=hour<=17:
#     print("good afternoon")
# elif 18<=hour<=23:
#     print("good evening")
# else:
#     print("good night")




# nested if else statement

# cheacking number(positive,negative,zero,even,odd)

# num=int(input("enter the number:"))
# if num>0:
#     print("posiive")
#     if num%2==0:
#         print("even")
#     else:
#         prit("odd")
# else:
#     if num==0:
#         print("zero")
#     else:
#         print("negative")


# checking the result(pass, fail,distinction)

marks=int(input("enter your marks:"))
if marks>=40:
    print("you are passed the exam")
    if marks>=75:
        print("you got distinction")
    else:
        print("you paased ,but no distinction")
else:
    print("you failed the exam")


# Problem 1: Age and Gender
# Write a Python program that asks for the user's age and gender, then prints the following:

# If the user is a male and under 18 years old, print: "You are a young boy."
# If the user is a male and 18 years old or older, print: "You are an adult man."
# If the user is a female and under 18 years old, print: "You are a young girl."
# If the user is a female and 18 years old or older, print: "You are an adult woman."


# age=int(input("enter your age:"))
# Gender=input("your gender(male/female):").lower()

# if gender== male:
#     if age<18:
#         print("You are a young boy.")
     
#     else:
#         print("You are an adult man.")

# elif gender==female:
#     if age<18:
#         print("You are a young girl.")
#     else:
#         print("You are an adult woman.")

# else:
#      print("Invalid gender input. Please enter 'male' or 'female'.")



# Problem 4: Check Voting Eligibility
# Write a Python program that asks for the user's age and whether they are a citizen of the country, then check:

# If the user is 18 years old or older and a citizen, print: "You are eligible to vote."
# If the user is 18 years old or older but not a citizen, print: "You are not eligible to vote due to citizenship status."
# If the user is under 18, print: "You are not eligible to vote due to age."



# Problem:
# You are tasked with writing a program that takes a student's score as input and prints out the corresponding grade. The grading system is as follows:

# If the score is 90 or above, print "A"
# If the score is between 80 and 89 (inclusive), print "B"
# If the score is between 70 and 79 (inclusive), print "C"
# If the score is between 60 and 69 (inclusive), print "D"
# If the score is below 60, print FAIL

# grading sysytem

# student_name=(input("enter your name:"))
# percentage=int(input("enter your marks:"))


# if percentage<90:
#     print("A")
# elif percentage<80:
#     print("B")
# elif percentage<70:
#     print("C")
# elif percentage60:
#     print("D")
# else:
#     print(fail("F"))

