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


def remove(students_data, faculty_data):
    def remove_student(students_data):
        id = input("Enter student id you want to delete: ").strip()
        while id[0] != "S" or len(id) != 5:
            id = input("Enter a valid student id please: ").strip()
        print("Loading....")
        time.sleep(1)
        if id in students_data["ids"]:
            id_index = students_data["ids"].index(id)
            for key in students_data:
                students_data[key].remove(students_data[key][id_index])
            print(students_data)
            Students_file = open("students.txt", "w")

            for i in range(len(students_data["ids"])):
                for key in students_data:
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
                    Students_file.write(
                        "-"+word+":"+students_data[key][i]+"\n")
                Students_file.write("_"*50 + "\n")
            Students_file.close()

        else:
            print("No matching id found")
        return

    def remove_faculty(faculty_data):

        pass

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
                print("-Fullfilled credit hours:" +
                      students_data["credit hours"][i])
                print("-Grades:"+students_data["grades"][i])
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
            print(f"-Fullfilled credit hours:" +
                  students_data["credit hours"][index])
            print(f"-Grades:"+students_data["grades"][index])
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
    exit(0)


def question(students_data, faculty_data):
    answer = input(
        "Do you want to perform another operation?(y/n): ").strip().lower()
    while answer not in ["y", "n"]:
        answer = input("Enter a valid choice please(y/n): ")
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
                    display_info(students_data, i)
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

# function in which admin can be able to add a student, Faculty member , course and an instructor 
def add() :
    while True :
        print("1]Add Student\n2]Add Faculty member\n3]Add course\n4]Add instructor\n")
        answer = input("Enter choice[1,2,3,4]: ").strip()
        while answer not in ["1", "2", "3", "4"]:
           answer = input("Enter a valid choice please[1,2,3,4]: ").strip()
        if answer == "1":
           add_student()
        elif answer == "2":
           add_faculty()
        elif answer == "3":
           add_course()
        elif answer == "4":
           add_instractor()
        answer = input("Do you want to perform another operation?(y/n): ").strip().lower()
        while answer not in ["y", "n"]:
           answer = input("Enter a valid choice please(y/n): ")
        if answer == "n":
            good_bye_admin()
            break 

# newstudent_id() is a function that gets an id for the new student
def newstudent_id() :
    accountfile = open("accounts.txt","r")
    data = accountfile.read()
    accountfile.close()
    for item in range(1,10000) :
        new_id = "S" + str(item).rjust(4,"0")
        if data.find(new_id) == -1 :
            return new_id

#
def email_checker(semail) :
    while semail.find("@") == -1 :
        print("Your Email is invalid\nYour Email should contains '@'")
        semail = input("Enter A valid Email :")
    return   semail
        

# mobile_checker() checks if a mobi,e ks valid or not 
def mobile_checker(smobile) :
    while  (len(smobile) < 11) or ( len(smobile) > 11 ) :
        print ("your mobile number is invalid\nA valid mobile phone number is 11 digits long")
        smobile = input("Enter a vaild mobile ")
    while True  :
        if smobile.startswith("011") or smobile.startswith("012") or smobile.startswith("015") or smobile.startswith("010") :
            return smobile
        else :
            print ("your mobile number should starts either with: 010, 011, 012, or 015 ")
            smobile = input("Enter a vaild mobile ")
    return smobile

    
# add_student() is a function that add a new student data
def add_student() :
        file_addstudent = open ( "students.txt","a")
        first_name = input (" Enter your first name : ")
        last_name = input (" Enter your last name : ")
        student_email = input (" Enter your Email : ")
        semail = email_checker(student_email)
        student_mobile = input (" Enter your mobile : ")
        smobile = mobile_checker(student_mobile)
        student_id = newstudent_id()
        file_addstudent.write("-"*50)
        file_addstudent.write("\n-First name:"+first_name+"\n-Last name:"+last_name+"\n-ID:"+student_id+"\n-Mobile:"+smobile+"\n-Email"+semail)
        file_addstudent.write("\n-C-GPA:0\n-Academic level:Freshman\n-Registered courses:PH129 / PH130 / CR504\n-Fullfilled credit hours:130\n-Grades:PH129->70 / PH130->80 / CR504->90\n")
        file_addstudent.close()


# newfaculty_id() is a function that gets a new id for the faculty member
def newfaculty_id() :
    account_file = open("accounts.txt","r")
    data = account_file.read()
    account_file.close()
    for item in range(1,10000) :
        newf_id = "F" + str(item).rjust(4,"0")
        if data.find(newf_id) == -1 :
            return newf_id

# add_faculty() is a function that add a new faculty member to our data
def add_faculty() :
        file_addfaculty = open ( "faculty.txt","a")
        first_name = input (" Enter your first name : ")
        last_name = input (" Enter your last name : ")
        num_courses = int(input("Enter the number of courses taught : "))
        facultycourses = ""
        for item in range (num_courses) :
            courses_taught = input(" Enter the course name :")
            facultycourses += courses_taught +"/"
        faculty_id = newfaculty_id()
        file_addfaculty.write("-"*50)
        file_addfaculty.write("\n-First name:"+first_name+"\n-Last name:"+last_name+"\n-ID:"+faculty_id+"\n-Courses taught :"+facultycourses+"\n")
        file_addfaculty.close()

main()
