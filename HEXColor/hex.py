charRange=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']


colorCode=input("Enter Color Code: ").lower().strip()
colorscodes=[]
if colorCode.startswith("#"):
    cleanCode=colorCode[1:]
    # print(colorCode)
    if all(char in charRange for char in cleanCode) and len(cleanCode) in (3,6):
        print('all values exists')
        print("Valid Starting") 
        colorscodes.append(colorCode)
    else:
        print("not matched ")
else:
    print("not a valid starting point")

print(colorscodes)

