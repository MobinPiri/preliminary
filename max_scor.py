count1 = int(input("Please enter the number of students : "))
Dict, List = {}, []
for i in range(1, count1 + 1):
    print("-------------------------------------------\n")
    name = input(f"please enter the name of student-{i}:  ")
    student_number = int(input(f"please enter the student number of student-{i}:  "))
    average = float(input(f"please enter the avrage of student-{i}:  "))
    List.append(average)
    Dict[i] = {"name": name,
               "student_number": student_number,
               "average": average}
Max = max(List)
for key, value in Dict.items():
    if value['average'] == Max:
        print("name : ", value["name"], "    student_number :", value["student_number"], " average : ", value["average"])