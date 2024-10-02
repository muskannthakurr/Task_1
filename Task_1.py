print("Simple Calculator")
num1 = int(input("Enter first number :"))
operator = input("Enter the desired operator(-,+,*,/) :")
num2 = int(input("Enter secound number :"))

if operator == "-":
  print("Substraction of num1 and num2 :",num1 - num2)
elif operator == "+":
  print("Addition of num1 and num2 :",num1 + num2)
elif operator == "*":
  print("Multiplication of num1 and num2 :",num1 * num2)
elif operator == "/":
  print("Division of num1 and num2 :",num1 / num2)
else:
  print("Enter the right operator")