if __name__ == '__main__':
    students = []
    # Sample Input: 5 students
    # Harry 37.21, Berry 37.21, Tina 37.2, Akriti 41, Harsh 39
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # 1. Find second lowest grade
    unique_grades = sorted(list(set(s[1] for s in students)))
    second_lowest = unique_grades[1]
    
    # 2. Extract names with that grade
    low_names = [s[0] for s in students if s[1] == second_lowest]
    
    # 3. Sort alphabetically and print
    for name in sorted(low_names):
        print(name)
