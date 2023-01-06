import time
import csv
import os
from fpdf import FPDF
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():

    # retrieve data from students, faculty members and put each one in a seperated dictionary
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
        "types": [],
        "courses taught": []
    }

    Students_file = open("students.txt", "r")
    Faculty_file = open("faculty.txt", "r")

    sdata_list = Students_file.read().split("\n")
    fdata_list = Faculty_file.read().split("\n")
    # read students data
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

    # read faculty data
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
        elif attribute[0] == "-Type":
            faculty_data["types"].append(attribute[1])
        else:
            continue

    Faculty_file.close()
    Students_file.close()

    welcome_admin()
    menu(students_data, faculty_data)


def welcome_admin():
    # a function that welcomes the admin
    print("*"*50)
    print("*"*50)
    print("|", end="")
    print("Welcome Admin".center(48, "_"), end="")
    print("|")
    print("*"*50)
    print("*"*50)


def read_courses():
    # read the course data and return a dict of it
    courses_data = {
        "code": [],
        "name": [],
        "description": [],
        "credit hours": [],
        "preq": []
    }
    Courses_file = open("courses.txt", "r")
    cdata_list = Courses_file.read().split("\n")
    for i in range(len(cdata_list)):
        attribute = cdata_list[i].split(":")
        if attribute[0] == "-Code":
            courses_data["code"].append(attribute[1])
        elif attribute[0] == "-Name":
            courses_data["name"].append(attribute[1])
        elif attribute[0] == "-Description":
            courses_data["description"].append(attribute[1])
        elif attribute[0] == "-Credit hours":
            courses_data["credit hours"].append(attribute[1])
        elif attribute[0] == "-Prerequisites":
            courses_data["preq"].append(attribute[1])
        else:
            continue
    Courses_file.close()
    return courses_data


def menu(students_data, faculty_data):
    # Letting the admin choose an operation
    print("1]Search\n2]Remove\n3]Update\n4]Display info\n5]Add\n6]exit\n7]Create a printable student report")
    answer = input("Enter choice[1,2,3,4,5,6,7]: ").strip()
    # input validation
    while answer not in ["1", "2", "3", "4", "5", "6", "7"]:
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
    elif answer == "6":
        good_bye_admin(students_data)
    else:
        create_report()


# A function to write the data on the file again that recieves two parameters, the dict that contains the data and the file name
def create_report():

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

    Students_file = open("students 2.txt", "r")

    sdata_list = Students_file.read().split("\n")

    # read students data
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

    # read faculty data

    Students_file.close()
    id = input('Enter student id:').strip()
    while id not in students_data["ids"]:
        id = input('Enter a valid student id:').strip()
    index = students_data["ids"].index(id)
    first_name = students_data["first names"][index]
    last_name = students_data["last names"][index]
    email = students_data["emails"][index]
    mobile = students_data["mobiles"][index]
    gpa = students_data["c_gpas"][index]
    level = students_data["levels"][index]
    registered_courses = students_data["registered courses"][index].split()
    hours = students_data["credit hours"][index]
    completed_courses = students_data["completed courses"][index].split()
    grades = students_data["grades"][index].split()

    # The GUI part

    pdf = FPDF()
    pdf.add_page()
    pdf.image('EUI.jpg', 150, -1, 55)
    if id == "S1011":
        pdf.image('S1011.JPG', x=130, y=75, w=60, h=45)
    elif id == "S1012":
        pdf.image('S1012.JPG', x=130, y=75, w=60, h=45)
    elif id == "S1013":
        pdf.image('S1013.JPG', x=130, y=75, w=60, h=45)
    elif id == "S1014":
        pdf.image('S1014.JPG', x=130, y=75, w=60, h=45)
    else:
        pdf.image('EXTRA.JPG', x=130, y=75, w=60, h=45)

    pdf.set_font('Times', 'U', 20)
    pdf.cell(175, 35, first_name + "'s Report", align='C')

    pdf.ln(15)
    pdf.set_font('Times', 'B', 12)
    pdf.ln(20)
    pdf.cell(40, 10, 'First Name:')
    pdf.ln(3)
    pdf.set_font('Times', 'I', 12)
    pdf.cell(45, 13, first_name)

    pdf.set_font('Times', 'B', 12)
    pdf.ln(10)
    pdf.cell(55, 10, 'Last Name:')
    pdf.ln(3)
    pdf.set_font('Times', 'I', 12)
    pdf.cell(60, 13, last_name)

    pdf.set_font('Times', 'B', 12)
    pdf.ln(10)
    pdf.cell(55, 10, 'Level:')
    pdf.ln(3)
    pdf.set_font('Times', 'I', 12)
    pdf.cell(60, 13, level)

    pdf.set_font('Times', 'B', 12)
    pdf.ln(10)
    pdf.cell(55, 10, 'Email:')
    pdf.ln(3)
    pdf.set_font('Times', 'I', 12)
    pdf.cell(60, 13, email)

    pdf.set_font('Times', 'B', 12)
    pdf.ln(10)
    pdf.cell(55, 10, 'Phone Number:')
    pdf.ln(3)
    pdf.set_font('Times', 'I', 12)
    pdf.cell(60, 13, mobile)

    pdf.set_font('Times', 'B', 12)
    pdf.ln(10)
    pdf.cell(55, 10, 'For '+first_name + "'s Courses and Grades:")
    for y in range(len(grades)):
        pdf.set_font('Times', 'U', 12)
        pdf.ln(10)
        pdf.cell(55, 10, registered_courses[y] + ':')
        pdf.ln(3)
        pdf.set_font('Times', 'I', 12)
        pdf.cell(60, 13, grades[y])

    pdf.set_font('Times', 'B', 12)
    pdf.ln(10)
    if completed_courses[0] != 'None':
        pdf.cell(55, 10, 'For '+first_name + "'s Completed Courses:")

        for C in completed_courses:
            pdf.set_font('Times', 'I', 12)
            pdf.ln(10)
            pdf.cell(55, 10, C)

    else:
        pdf.set_font('Times', 'B', 12)
        pdf.ln(10)
        pdf.cell(55, 10, first_name + ' Did not complete any course yet!')

    pdf.output(first_name + ' Report.pdf', 'F')


def write_data(data, filename):
    # open the file and write the data in the same file format
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
                elif key == "types":
                    word = "Type"
                Faculty_file.write("-"+word+":"+data[key][i]+"\n")
            Faculty_file.write("_"*50 + "\n")
        Faculty_file.close()
    elif filename == "courses.txt":
        Courses_file = open("courses.txt", "w")
        for i in range(len(data["code"])):
            for key in data:
                if key == "code":
                    word = "Code"
                elif key == "name":
                    word = "Name"
                elif key == "description":
                    word = "Description"
                elif key == "credit hours":
                    word = "Credit hours"
                elif key == "preq":
                    word = "Prerequisites"
                Courses_file.write("-"+word+":"+data[key][i]+"\n")
            Courses_file.write("_"*50 + "\n")
        Courses_file.close()

    return


def write_csv(students_data):
    myfile = open("studs.csv", "w")
    myfile.write("First,Last,ID")
    all_courses = read_courses()
    codes = all_courses["code"]
    for code in codes:
        myfile.write(","+code)
    myfile.write("\n")
    ids = students_data["ids"]
    studs = []
    for i in range(len(ids)):
        mylist = []
        mylist.append(students_data["first names"][i])
        mylist.append(students_data["last names"][i])
        mylist.append(students_data["ids"][i])
        for course in codes:
            if course in students_data["registered courses"][i].split():
                index = (students_data["registered courses"]
                         [i].split()).index(course)
                grades = students_data["grades"][i].split()
                mylist.append(grades[index])
            else:
                mylist.append("None")

        studs.append(mylist)
    w = csv.writer(myfile)
    w.writerows(studs)
    myfile.close()


def remove(students_data, faculty_data):
    # remove a student or faculty member using id

    def remove_student(students_data):
        id = input("Enter student id you want to delete: ").strip()
        # check if id entered is valid for student
        while id[0] != "S" or len(id) != 5:
            id = input("Enter a valid student id please: ").strip()
        print("Loading....")
        time.sleep(1)
        # check if id is in students ids
        if id in students_data["ids"]:

            id_index = students_data["ids"].index(id)
            print("Are you sure you want to remove", students_data["first names"][id_index],
                  students_data["last names"][id_index], "from the system (y/n): ", end="")
            ans = input().lower().strip()
            # input validation
            while ans not in ["y", "n"]:
                ans = input(
                    "Please enter a valid choice (y/n): ").lower().strip()
            if ans == "n":
                return
            for key in students_data:
                students_data[key].remove(students_data[key][id_index])
            # call function write data to update the file
            write_data(students_data, "students.txt")
            print("Student deleted succesfully....")
            time.sleep(0.5)

        else:
            print("No matching id found")
        return

    def remove_faculty(faculty_data):
        id = input("Enter faculty member id you want to delete: ").strip()
        # checking if id is valid for a faculty member
        while id[0] != "F" or len(id) != 5:
            id = input("Enter a valid faculty member id please: ").strip()
        print("Loading....")
        time.sleep(1)
        # check if id is in faculty members ids
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
            # update the file
            write_data(faculty_data, "faculty.txt")
            print("Faculty member deleted succesfully....")
            time.sleep(0.5)

        else:
            print("no matching id found")
    # asking admin if he want to remove student or faculty member
    choice = input(
        "1]Remove a student\n2]Remove a faculty member\nYour choice[1,2]: ").strip()

    # input validation
    while choice not in ["1", "2"]:
        choice = input("Please enter a valid choice[1,2]: ").strip()
    if choice == "1":
        remove_student(students_data)
    else:
        remove_faculty(faculty_data)

    return question(students_data, faculty_data)


def display_info(students_data, faculty_data, index="all"):
    # display info has three parameters :if first parameter is 0 then function displays faculty members info , if second parameter is 0 then the function displays students info
    # And by default third paramter equals "all" to display all the members info but if an argument is entered in it, then it is the index of the member to display his info
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

                print("-Fullfilled credit hours:" +
                      students_data["credit hours"][i])
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
            print("-Fullfilled credit hours:" +
                  students_data["credit hours"][index])
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
                print("-Type:"+faculty_data["types"][i])
                print("-Courses taught:"+faculty_data["courses taught"][i])
                print("_"*50)
        else:
            print(f"-Name :"+faculty_data["first names"]
                  [index], faculty_data["last names"][index])
            print(f"-ID:"+faculty_data["ids"][index])
            print("-Type:"+faculty_data["types"][index])
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


def good_bye_admin(students_data):
    # terminating the program
    print("*"*50)
    print("*"*50)
    print("|", end="")
    print("Good Bye Admin".center(48, "_"), end="")
    print("|")
    print("*"*50)
    print("*"*50)
    time.sleep(1)
    write_csv(students_data)
    exit(0)


def question(students_data, faculty_data):
    # asking user if he wants to do another operation or not
    answer = input(
        "Do you want to perform another operation?(y/n): ").strip().lower()
    while answer not in ["y", "n"]:
        answer = input("Enter a valid choice please(y/n): ").strip().lower()
    if answer == "y":
        return menu(students_data, faculty_data)
    else:
        return good_bye_admin(students_data)


def search(students_data, faculty_data):
    # search function contains two nested functions in it , a function for students and a function for faculty members
    def search_student(students_data):
        print("1]Search by name\n2]Search by id\n")
        answer = input("Enter choice[1,2]: ").strip()
        # input validation
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


def update(students_data, faculty_data):
    def update_student(students_data):
        id = input("Enter student id you want to edit: ").strip()
        while id[0] != "S" or len(id) != 5:
            id = input("Enter a vaild student id please: ").strip()
        if id in students_data["ids"]:
            id_index = students_data["ids"].index(id)
            print("Student info".center(50, "#"))
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
                students_data["mobiles"][id_index] = mobile
            elif choice == "5":
                email = input("Enter updated email: ").strip()
                while "@" not in email or email.split("@")[1] != "students.eui.edu.eg":
                    email = input("Enter a valid email: ").strip()
                students_data["emails"][id_index] = email
            elif choice == "6":
                try:
                    print("\nBe careful gpa is calculated by the system. Any change in gpa value does not change the grades".center(
                        100), "*")
                    print()
                    gpa = float(input("Enter updated GPA: ").strip())
                    while gpa > 4 or gpa < 0:
                        gpa = float(
                            input("Enter a vaild updated GPA: ").strip())
                    gpa = str(gpa)
                    students_data["c_gpas"][id_index] = gpa
                    return

                except:
                    print("...Invalid gpa value...")
                    return
            elif choice == "7":
                all_courses = read_courses()
                courses = input(
                    "Enter all updated registered courses: ").strip()
                if len(courses.split()) != len(students_data["grades"][id_index].split()):
                    print("\nFailed...Enter full number of courses please\n")
                    return
                courses_list = courses.split()
                for item in courses_list:
                    if item not in all_courses["code"]:
                        print("\nFailed...Enter a vaild course code please\n")
                        return

                students_data["registered courses"][id_index] = courses
            elif choice == "8":
                hours = input("Enter updated fullfilled credit hours:").strip()
                for char in hours:
                    if char not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                        print("Failed... Credit hours entered value is not correct")
                        return
                students_data["credit hours"][id_index] = hours
                hours = int(hours)
                if hours < 25:
                    students_data["levels"][id_index] = "Freshman"
                elif hours > 24 and hours < 55:
                    students_data["levels"][id_index] = "Sophomore"
                elif hours > 54 and hours < 85:
                    students_data["levels"][id_index] = "Junior"
                else:
                    students_data["levels"][id_index] = "Senior"
            elif choice == "9":
                course = input(
                    "Enter name of the course you want to update the grade of:").strip()
                course_list = students_data["registered courses"][id_index].split(
                )
                grades_list = students_data["grades"][id_index].split()
                while course not in course_list:
                    course = input(
                        "Enter a correct name of the course you want to update the grade of:").strip()
                grade_index = course_list.index(course)
                grade = input(
                    "Enter updated grade of the course (in numbers without percentage): ").strip()
                grades_list[grade_index] = grade
                students_data["grades"][id_index] = " ".join(grades_list)
            write_data(students_data, "students.txt")

        else:
            print("No matching ids found")
        return

    def update_faculty(faculty_data):
        id = input("Enter faculty member id you want to update: ").strip()
        while id[0] != "F" or len(id) != 5:
            id = input("Enter a vaild faculty member id please: ").strip()
        if id in faculty_data["ids"]:
            id_index = faculty_data["ids"].index(id)
            print("Faculty member info".center(50, "#"))
            display_info(0, faculty_data, id_index)
            print("#"*50)
            print(
                "1]Update first name\t2]Update second name\n3]Update id\t\t4]Update courses taught\n5]Assign staff member to instructor\n")
            ans = input("Your choice (1,2,3,4,5): ").strip()
            while ans not in ["1", "2", "3", "4", "5"]:
                ans = input("Enter a valid choice (1,2,3,4,5): ").strip()
            if ans == "1":
                name = input("Enter updated first name: ").strip().capitalize()
                faculty_data["first names"][id_index] = name
            elif ans == "2":
                name = input("Enter updated last name: ").strip().capitalize()
                faculty_data["last names"][id_index] = name
            elif ans == "3":
                id = input("Enter updated id: ").strip()
                while id[0] != "F" or len(id) != 5:
                    id = input("Enter a vaild updated id: ").strip()
                faculty_data["ids"][id_index] = id
            elif ans == "4":
                courses_data = read_courses()
                courses_taught = faculty_data["courses taught"][id_index].split(
                )
                print("Choose the course you want to update\n")
                for i in range(len(courses_taught)):
                    print(i+1, "]", courses_taught[i], sep="")
                choice = input("\nYour choice: ").strip()
                while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    choice = input("\nEnter valid choice: ").strip()
                if int(choice) > len(courses_data):
                    print("Failed... your choice is out of range\n")
                    return
                course = input("Enter updated course code: ").strip()
                if course not in courses_data["code"]:
                    print("\nFailed...course code is not available in the university\n")
                    return
                index = int(choice) - 1
                courses_taught[index] = course
                faculty_data["courses taught"][id_index] = " ".join(
                    courses_taught)
            elif ans == "5":
                all_courses = read_courses()
                if faculty_data["types"][id_index] == "instructor":
                    print("Failed...Faculty member is already an instructor\n")
                    return
                courses = input(
                    "Enter course(s) code(s) the instructor will teach: ").strip()
                course_list = courses.split()
                for i in range(len(course_list)):
                    if course_list[i] not in all_courses["code"]:
                        print(
                            "Failed...One of the courses doesn't belong to university\n")
                        return
                faculty_data["types"][id_index] = "instructor"
                faculty_data["courses taught"][id_index] = " ".join(
                    course_list)

            write_data(faculty_data, "faculty.txt")

        else:
            print("No matching ids found")

    choice = input(
        "1]Update a student\n2]Update a faculty member\nYour choice: [1,2]: ").strip()
    while choice not in ["1", "2"]:
        choice = input("Enter a valid choice please [1,2]: ").strip()
    if choice == "1":
        update_student(students_data)
    else:
        update_faculty(faculty_data)
    return question(students_data, faculty_data)


def add(students_data, faculty_data):
    def add_student(students_data):
        print("#"*50)
        print("-"*50)
        print("Fill out this form")
        print("-"*50)
        print("#"*50)
        first_name = input("Enter first name: ").capitalize().strip()
        last_name = input("Enter last name: ").capitalize().strip()
        students_data["first names"].append(first_name)
        students_data["last names"].append(last_name)
        email = input("Enter email: ").strip()
        while "@" not in email or email.split("@")[1] != "students.eui.edu.eg":
            email = input("Enter a valid email: ").strip()
        students_data["emails"].append(email)
        mobile = input("Enter mobile number: ").strip()
        while len(mobile) != 11 or (mobile[0:3] not in ["012", "011", "010", "015"]):
            mobile = input(
                "Enter a valid updated mobile number: ").strip()
        students_data["mobiles"].append(mobile)
        id_nums = [0]
        for i in range(len(students_data["ids"])):
            num = students_data["ids"][i][2:]
            id_nums.append(int(num))
        id_num = max(id_nums)+1
        id = "S1"+(str(id_num)).zfill(3)
        students_data["ids"].append(id)
        students_data["registered courses"].append("PR138 PH139 CA120")
        students_data["levels"].append("Freshman")
        students_data["c_gpas"].append("0")
        students_data["credit hours"].append("0")
        students_data["grades"].append("0 0 0")
        students_data["completed courses"].append("None")
        write_data(students_data, "students.txt")
        print("#"*50)
        print("-"*50)
        print("Student added successfully")
        print("-"*50)
        print("#"*50)
        return

    def add_faculty(faculty_data):
        print("#"*50)
        print("-"*50)
        print("Fill out this form")
        print("-"*50)
        print("#"*50)
        fname = input("Enter first name: ").strip().capitalize()

        lname = input("Enter last name: ").strip().capitalize()

        print("1]Instructor or 2]staff member")
        ans = input("Your choice (1,2): ").strip()
        while ans not in ["1", "2"]:
            ans = input("Enter a valid choice (1,2): ").strip()
        if ans == "1":
            all_courses = read_courses()
            crs = input(
                "Enter course(s) code(s) the instructor will teach: ").strip().split()
            for item in crs:
                if item not in all_courses["code"]:
                    print("Failed...One of the courses does not belong to university")
                    return
            faculty_data["first names"].append(fname)
            faculty_data["last names"].append(lname)
            faculty_data["types"].append("instructor")
            faculty_data["courses taught"].append(" ".join(crs))
        else:
            faculty_data["first names"].append(fname)
            faculty_data["last names"].append(lname)
            faculty_data["types"].append("staff")
            faculty_data["courses taught"].append("None")
        id_nums = [0]
        for i in range(len(faculty_data["ids"])):
            num = faculty_data["ids"][i][2:]
            id_nums.append(int(num))
        id_num = max(id_nums)+1
        id = "F1"+(str(id_num)).zfill(3)
        faculty_data["ids"].append(id)
        write_data(faculty_data, "faculty.txt")
        print("#"*50)
        print("-"*50)
        print("Faculty member added successfully")
        print("-"*50)
        print("#"*50)
        return

    def add_course():
        print("#"*50)
        print("-"*50)
        print("Fill out this form")
        print("-"*50)
        print("#"*50)
        cdata = read_courses()
        c_name = input("Enter course name: ").strip().capitalize()
        c_desc = input("Enter course description: ").strip().capitalize()
        c_hours = input("Enter course credit hours: ").strip()
        for char in c_hours:
            if char not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                print("Failed...Invalid credit hours entered")
                return
        c_subj = input("Enter course subject: ").strip()
        c_level = input("Enter course level (1,2,3,4): ").strip()
        while c_level not in ["1", "2", "3", "4"]:
            c_level = input("Enter a valid course level (1,2,3,4): ").strip()
        c_preq = []
        id_nums = [0]
        for i in range(len(cdata["code"])):
            if cdata["code"][i][2] == c_level:
                num = cdata["code"][i][2:]
                id_nums.append(int(num))
        id_num = max(id_nums)+1

        if len(c_subj.split()) == 1:
            c_code = c_subj[0].upper() + c_subj[1].upper() + c_level
            c_code += (str(id_num))[1:].zfill(2)
        else:
            name = c_subj.split()
            c_code = name[0][0].upper() + name[1][0].upper() + c_level
            c_code += (str(id_num))[1:].zfill(2)
        for course in cdata["code"]:
            if (course[:2] == c_code[:2]) and course[2] < c_level:
                c_preq.append(course)
        cdata["code"].append(c_code)
        cdata["name"].append(c_name)
        cdata["description"].append(c_desc)
        cdata["credit hours"].append(c_hours)
        if len(c_preq) == 0:
            cdata["preq"].append("None")
        else:
            cdata["preq"].append(" ".join(c_preq))

        write_data(cdata, "courses.txt")
        print("#"*50)
        print("-"*50)
        print("Course added successfuly")
        print("-"*50)
        print("#"*50)
        return

    print("\n1]Add a student\n2]Add a faculty member\n3]Add a course\n")
    choice = input("Your choice (1,2,3): ").strip()
    while choice not in ["1", "2", "3"]:
        choice = input("Enter a valid choice (1,2,3): ").strip()
    if choice == "1":
        add_student(students_data)
    elif choice == "2":
        add_faculty(faculty_data)
    else:
        add_course()

    return question(students_data, faculty_data)
