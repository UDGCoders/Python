charRange=['a','b','c','d','e','f']
numbRange=[1,2,3,4,5,6]

colorCode=input("Enter Color Code: ")
if len(colorCode)<3 or len(colorCode) > 6:
    print("color code is atleast 3 chars")
else:
    if '#' in colorCode:
        print("Valid Starting") 
    else:
        print("not a valid starting point")