# global variable
def myfun():
    print(name)
name="python"
myfun()
def myfun1():
        global name1
        print("1st",name1)
        name="python language"
        print("2nd",name1)
name1="python"
myfun1()
print("3rd",name1)
        
