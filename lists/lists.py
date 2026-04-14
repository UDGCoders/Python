if __name__ == '__main__':
    records=[]
    for _ in range(int(input("Enter the range: "))):
        name = input("Enter Your Name; ")
        score = float(input())
        records.append([name,score])
        
    for items in records:
        print(items)