class uppercase:
    def __init__(self):
        self.str1=""
    def enter(self):
        self.str1=input("Enter a string ")
    def upper(self):
        print("The string in uppercase letters is ",self.str1.upper())   
s1=uppercase()
s1.enter()
s1.upper() 