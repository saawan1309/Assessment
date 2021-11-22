class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

while True:
    a = int(input("Enter First Digit :"))
    b = int(input("Enter Second Digit :"))
    c = input("Select Operation (+,-,*,/) :")
    cal = calculator(a,b)
    if c == "+":
        print("Your Sum Of two number is :", cal.add())
    elif c == "-":
        print("Your Substraction Of two number is :", cal.sub())
    elif c == "*":
        print("Your Multiplication Of two number is :", cal.mult())
    elif c == "/":
        print("your Division Of two number is :", cal.div())

    d=input("you Want to Continue (Y/N): ").lower()
    if d=="n":
        break
    elif d=="y":
        continue
    else:
        print("Invalid input")
        break



