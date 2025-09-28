# take number input from user and tell whether number is even and odd using if/else

number = int(input("Enter the first number: "))

if number % 2 == 0:
    print("Number is even: ", number)
else:
    print("Number is odd: ", number)
    
# take marks input from user and tell whether pass/fail (A/B/C/Fail)

marks = int(input("Enter the marks: "))

if marks > 90:
    print("Grade A :",marks)
elif marks > 75:
    print("Grade B: ", marks)
elif marks > 45:
    print("Grade C: ", marks)
else:
    print("Fail: ", marks)

