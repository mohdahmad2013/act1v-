class emp:
    def __init__(self):
        print("Employee class")
    def __del__(self):
        print("Destructor")
    def objclass():
        print("Object function created")
        obj=emp()
        print("Object function ended")
        return obj
print("Calling a function")
obj=emp.objclass()
print("Program ends")