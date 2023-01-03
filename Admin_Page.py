import time


def main():
    # retrieve data
    # first_names,last_names,ids,mobiles,emails,c_gpas,levels,reg_courses,hours,grades
    students_data = {
        "first names": [],
        "last names": [],
        "ids": [],
        "mobiles": [],
        "emails": [],
        "c_gpas": [],
        "levels": [],
        "registered courses": [],
        "completed courses": [],
        "credit hours": [],
        "grades": []
    }
    faculty_data = {
        "first names": [],
        "last names": [],
        "ids": [],
        "courses taught": []
    }
    Students_file = open("students.txt", "r")
    Faculty_file = open("faculty.txt", "r")
    sdata_list = Students_file.read().split("\n")
    fdata_list = Faculty_file.read().split("\n")
    for i in range(len(sdata_list)):
        attribute = sdata_list[i].split(":")
        if attribute[0] == "-First name":
            students_data["first names"].append(attribute[1])
        elif attribute[0] == "-Last name":
            students_data["last names"].append(attribute[1])
        elif attribute[0] == "-ID":
            students_data["ids"].append(attribute[1])
        elif attribute[0] == "-Mobile":
            students_data["mobiles"].append(attribute[1])
        elif attribute[0] == "-Email":
            students_data["emails"].append(attribute[1])
        elif attribute[0] == "-C-GPA":
            students_data["c_gpas"].append(attribute[1])
        elif attribute[0] == "-Academic level":
            students_data["levels"].append(attribute[1])
        elif attribute[0] == "-Registered courses":
            students_data["registered courses"].append(attribute[1])
        elif attribute[0] == "-Fullfilled credit hours":
            students_data["credit hours"].append(attribute[1])
        elif attribute[0] == "-Grades":
            students_data["grades"].append(attribute[1])
        elif attribute[0] == "-Completed courses":
            students_data["completed courses"].append(attribute[1])
        else:
            continue
    for i in range(len(fdata_list)):
        attribute = fdata_list[i].split(":")
        if attribute[0] == "-First name":
            faculty_data["first names"].append(attribute[1])
        elif attribute[0] == "-Last name":
            faculty_data["last names"].append(attribute[1])
        elif attribute[0] == "-ID":
            faculty_data["ids"].append(attribute[1])
        elif attribute[0] == "-Courses taught":
            faculty_data["courses taught"].append(attribute[1])
        else:
            continue
    Faculty_file.close()
    Students_file.close()
    welcome_admin()
    menu(students_data, faculty_data)


def welcome_admin():
    print("*"*50)
    print("*"*50)
    print("|", end="")
    print("Welcome Admin".center(48, "_"), end="")
    print("|")
    print("*"*50)
    print("*"*50)


def menu(students_data, faculty_data):
    print("1]Search\n2]Remove\n3]Update\n4]Display info\n5]Add\n6]exit")
    answer = input("Enter choice[1,2,3,4,5,6]: ").strip()
    while answer not in ["1", "2", "3", "4", "5", "6"]:
        answer = input("Enter a valid choice please[1,2,3,4,5,6]: ").strip()
    if answer == "1":
        search(students_data, faculty_data)
    elif answer == "2":
        remove(students_data, faculty_data)
    elif answer == "3":
        update(students_data, faculty_data)
    elif answer == "4":
        display_info(students_data, faculty_data)
    elif answer == "5":
        add(students_data, faculty_data)
    else:
        good_bye_admin()


def write_data(data, filename):
    if filename == "students.txt":
        Students_file = open("students.txt", "w")

        for i in range(len(data["ids"])):
            for key in data:
                if key == "first names":
                    word = "First name"
                elif key == "last names":
                    word = "Last name"
                elif key == "ids":
                    word = "ID"
                elif key == "mobiles":
                    word = "Mobile"
                elif key == "emails":
                    word = "Email"
                elif key == "c_gpas":
                    word = "C-GPA"
                elif key == "levels":
                    word = "Academic level"
                elif key == "registered courses":
                    word = "Registered courses"
                elif key == "credit hours":
                    word = "Fullfilled credit hours"
                elif key == "grades":
                    word = "Grades"
                elif key == "completed courses":
                    word = "Completed courses"
                Students_file.write(
                    "-"+word+":"+data[key][i]+"\n")
            Students_file.write("_"*50 + "\n")
        Students_file.close()
    elif filename == "faculty.txt":
        Faculty_file = open("faculty.txt", "w")
        for i in range(len(data["ids"])):
            for key in data:
                if key == "first names":
                    word = "First name"
                elif key == "last names":
                    word = "Last name"
                elif key == "ids":
                    word = "ID"
                elif key == "courses taught":
                    word = "Courses taught"
                Faculty_file.write("-"+word+":"+data[key][i]+"\n")
            Faculty_file.write("_"*50 + "\n")
        Faculty_file.close()
    return


def remove(students_data, faculty_data):
    def remove_student(students_data):
        id = input("Enter student id you want to delete: ").strip()
        while id[0] != "S" or len(id) != 5:
            id = input("Enter a valid student id please: ").strip()
        print("Loading....")
        time.sleep(1)
        if id in students_data["ids"]:

            id_index = students_data["ids"].index(id)
            print("Are you sure you want to remove", students_data["first names"][id_index],
                  students_data["last names"][id_index], "from the system (y/n): ", end="")
            ans = input().lower().strip()
            while ans not in ["y", "n"]:
                ans = input(
                    "Please enter a valid choice (y/n): ").lower().strip()
            if ans == "n":
                return
            for key in students_data:
                students_data[key].remove(students_data[key][id_index])

            write_data(students_data, "students.txt")
            print("Student deleted succesfully....")
            time.sleep(0.5)

        else:
            print("No matching id found")
        return

    def remove_faculty(faculty_data):
        id = input("Enter faculty member id you want to delete: ").strip()
        while id[0] != "F" or len(id) != 5:
            id = input("Enter a valid faculty member id please: ").strip()
        print("Loading....")
        time.sleep(1)
        if id in faculty_data["ids"]:
            id_index = faculty_data["ids"].index(id)
            print("Are you sure you want to remove", faculty_data["first names"][id_index],
                  faculty_data["last names"][id_index], "from the system (y/n): ", end="")
            ans = input().lower().strip()
            while ans not in ["y", "n"]:
                ans = input(
                    "Please enter a valid choice (y/n): ").lower().strip()
            if ans == "n":
                return
            for key in faculty_data:
                faculty_data[key].remove(faculty_data[key][id_index])
            write_data(faculty_data, "faculty.txt")
            print("Faculty member deleted succesfully....")
            time.sleep(0.5)

        else:
            print("no matching id found")

    choice = input(
        "1]Remove a student\n2]Remove a faculty member\nYour choice[1,2]: ").strip()
    while choice not in ["1", "2"]:
        choice = input("Please enter a valid choice[1,2]: ").strip()
    if choice == "1":
        remove_student(students_data)
    else:
        remove_faculty(faculty_data)
    return question(students_data, faculty_data)


def display_info(students_data, faculty_data, index="all"):
    def s_info(students_data):
        if index == "all":
            print("Loading....")
            time.sleep(1)
            for i in range(len(students_data["ids"])):
                print("-Name :"+students_data["first names"]
                      [i]+" "+students_data["last names"][i])
                print("-ID:"+students_data["ids"][i])
                print("-Mobile:"+students_data["mobiles"][i])
                print("-Email:"+students_data["emails"][i])
                print("-C-GPA:"+students_data["c_gpas"][i])
                print("-Academic level:"+students_data["levels"][i])
                print("-Registered courses:" +
                      students_data["registered courses"][i])
                print("-Completed courses:" +
                      students_data["completed courses"][i])
                # calculate total credit hours to display
                hours = students_data["credit hours"][i].split()
                total = 0
                for j in range(len(hours)):
                    total += int(hours[j])
                total = str(total)
                print("-Fullfilled credit hours:"+total)
                grades = students_data["grades"][i].split()
                course = students_data["registered courses"][i].split()
                print("-Grades:", end="")
                for i in range(len(grades)):
                    print(f"{course[i]}->{grades[i]}", end=" ")
                print()

                print("_"*50)
        else:
            print(f"-Name :"+students_data["first names"]
                  [index], students_data["last names"][index])
            print(f"-ID:"+students_data["ids"][index])
            print(f"-Mobile:"+students_data["mobiles"][index])
            print(f"-Email:"+students_data["emails"][index])
            print(f"-C_GPA:"+students_data["c_gpas"][index])
            print(f"-Academic level:"+students_data["levels"][index])
            print(f"-Registered courses:" +
                  students_data["registered courses"][index])
            print("-Completed courses:" +
                  students_data["completed courses"][index])
            hours = students_data["credit hours"][index].split()
            total = 0
            for i in range(len(hours)):
                total += int(hours[i])
            total = str(total)
            print(f"-Fullfilled credit hours:" +
                  total)
            grades = students_data["grades"][index].split()
            course = students_data["registered courses"][index].split()
            print("-Grades:", end="")
            for i in range(len(grades)):
                print(f"{course[i]}->{grades[i]}", end=" ")
            print()
            print("_"*50)
            return
        return

    def f_info(faculty_data):
        if index == "all":
            print("Loading....")
            time.sleep(1)
            for i in range(len(faculty_data["ids"])):
                print("-Name :"+faculty_data["first names"]
                      [i]+" "+faculty_data["last names"][i])
                print("-ID:"+faculty_data["ids"][i])
                print("-Courses taught:"+faculty_data["courses taught"][i])
                print("_"*50)
        else:
            print(f"-Name :"+faculty_data["first names"]
                  [index], faculty_data["last names"][index])
            print(f"-ID:"+faculty_data["ids"][index])
            print(f"-Courses taught:"+faculty_data["courses taught"][index])
            print("_"*50)
            return
        return
    if students_data == 0:
        f_info(faculty_data)
    elif faculty_data == 0:
        s_info(students_data)
    else:
        choice = input(
            "1]Display Students data\n2]Display faculty members data\n\nYour choice[1,2]: ").strip()
        while choice not in ["1", "2"]:
            choice = input("Please enter a vaild choice[1,2]: ")
        if choice == "1":
            s_info(students_data)
        else:
            f_info(faculty_data)
        return question(students_data, faculty_data)


def good_bye_admin():
    print("*"*50)
    print("*"*50)
    print("|", end="")
    print("Good Bye Admin".center(48, "_"), end="")
    print("|")
    print("*"*50)
    print("*"*50)
    time.sleep(1)
    exit(0)


def question(students_data, faculty_data):
    answer = input(
        "Do you want to perform another operation?(y/n): ").strip().lower()
    while answer not in ["y", "n"]:
        answer = input("Enter a valid choice please(y/n): ").strip().lower()
    if answer == "y":
        return menu(students_data, faculty_data)
    else:
        return good_bye_admin()


def search(students_data, faculty_data):
    def search_student(students_data):
        print("1]Search by name\n2]Search by id\n")
        answer = input("Enter choice[1,2]: ").strip()
        while answer not in ["1", "2"]:
            answer = input("Enter a valid choice please[1,2]: ").strip()

        if answer == "1":
            name = input("Enter name(first or last): ").capitalize().strip()
            print("Loading....")
            time.sleep(1)
            found = 0
            findings = []
            for i in range(len(students_data["first names"])):

                if students_data["first names"][i] == name and i not in findings:
                    found = 1
                    display_info(students_data, 0, i)
                    findings.append(i)
                if students_data["last names"][i] == name and i not in findings:
                    found = 1
                    display_info(students_data, 0, i)
                    findings.append(i)
            if found == 0:
                print("No matching names found")
            return

        else:
            answer = input("Enter ID: ").strip()
            print("Loading....")
            time.sleep(1)
            while answer[0] != "S" or len(answer) != 5:
                answer = input("Enter a correct student id please :").strip()
            if answer in students_data["ids"]:
                index = students_data["ids"].index(answer)
                display_info(students_data, 0, index)
            else:
                print("No matching ids found")
            return

    def search_faculty(faculty_data):
        print("1]Search by name\n2]Search by id\n")
        answer = input("Enter choice[1,2]: ").strip()
        while answer not in ["1", "2"]:
            answer = input("Enter a valid choice please[1,2]: ").strip()
        if answer == "1":
            name = input("Enter name(first or last): ").capitalize().strip()
            print("Loading....")
            time.sleep(1)
            found = 0
            findings = []
            for i in range(len(faculty_data["first names"])):

                if faculty_data["first names"][i] == name and i not in findings:
                    found = 1
                    display_info(0, faculty_data, i)
                    findings.append(i)
                if faculty_data["last names"][i] == name and i not in findings:
                    found = 1
                    display_info(0, faculty_data, i)
                    findings.append(i)
            if found == 0:
                print("No matching names found")
            return
        else:
            answer = input("Enter ID: ").strip()
            print("Loading....")
            time.sleep(1)
            while answer[0] != "F" or len(answer) != 5:
                answer = input(
                    "Enter a correct faculty member id please :").strip()
            if answer in faculty_data["ids"]:
                index = faculty_data["ids"].index(answer)
                display_info(0, faculty_data, index)
            else:
                print("No matching ids found")
            return

    print("1]Search for a student\n2]Search for a faculty member")
    answer = input("Enter choice: ")
    while answer not in ["1", "2"]:
        answer = input("Enter a valid choice please[1,2]: ")
    if answer == "1":
        search_student(students_data)
    else:
        search_faculty(faculty_data)
    return question(students_data, faculty_data)


main()


def update(students_data, faculty_data):
    def update_student(students_data):
        id = input("Enter student id you want to edit: ").strip()
        while id[0] != "S" or len(id) != 5:
            id = input("Enter a vaild student id please: ").strip()
        if id in students_data["ids"]:
            id_index = students_data["ids"].index(id)
            print("Student info".center("#", 50))
            display_info(students_data, 0, id_index)
            print("#"*50)
            choice = input("1]Update first name\t2]Update last name\t3]Update ID\t4]Update mobile\n5]Update email\t6]Update C-GPA\t7]Update registered courses\n8]Update credit hours\t9]Update grades\n\nYour choice (from 1 to 9): ").strip()
            while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                choice = input(
                    "Enter a valid choice please (from 1 to 9): ").strip()
            if choice == "1":
                name = input(
                    "Enter his updated first name: ").capitalize().strip()
                students_data["first names"][id_index] = name
            elif choice == "2":
                name = input(
                    "Enter his updated last name: ").capitalize().strip()
                students_data["last names"][id_index] = name
            elif choice == "3":
                id = input("Enter updated id: ").strip()
                while id[0] != "S" or len(id) != 5 or (id in students_data["ids"]):
                    if id in students_data:
                        id = input(
                            "...Id already exists...\nEnter a valid new id: ").strip()
                    else:
                        id = input("Enter a valid new id: ").strip()
                students_data["ids"][id_index] = id
            elif choice == "4":
                mobile = input("Enter updated mobile number: ").strip()
                while len(mobile) != 11 or (mobile[0:3] not in ["012", "011", "010", "015"]):
                    mobile = input(
                        "Enter a valid updated mobile number: ").strip()
                students_data["mobiles"] = mobile
            elif choice == "5":
                email = input("Enter updated email: ").strip()
                while "@" not in email or email.split("@")[1] != "students.eui.edu.eg":
                    email = input("Enter a valid email: ").strip()
                students_data["emails"] = email
            elif choice == "6":
                try:
                    gpa = float(input("Enter updated GPA: ").strip())
                    while gpa > 4 or gpa < 0:
                        gpa = float(input("Enter updated GPA: ").strip())
                    students_data["c_gpas"][id_index] = gpa

                except:
                    print("...Invalid gpa value...")
                    return
            elif choice == "7":
                pass

            else:
                print("No matching ids found")
        return

    def update_faculty(faculty_data):
        pass

    choice = input(
        "1]Update a student\n2]Update a faculty member\nYour choice: [1,2]: ").strip()
    while choice not in ["1", "2"]:
        choice = input("Enter a valid choice please [1,2]: ").strip()
    if choice == "1":
        update_student(students_data)
    else:
        update_faculty(faculty_data)
    return question(students_data, faculty_data)
