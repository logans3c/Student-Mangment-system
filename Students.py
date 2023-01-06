def grade_to_letter(grade):
    if int(grade) >= 90:
        return "A"
    elif int(grade) >= 80:
        return "B"
    elif int(grade) >= 70:
        return "C"
    elif int(grade) >= 60:
        return "D"
    else:
        return "F"
def grade_to_point(grade):
    if int(grade) >= 90 :
        return 4.0
    if int(grade) >=80 :
        return 3.0
    if int(grade) >= 70 :
        return 2.0
    if int(grade) >=60 :
        return 1.0
    if int(grade) <60 :
        return 0.0
    
GRADE_MAPPING ={
    100: "A+",
    90: "A",
    89: "B+",
    80: "B",
    79: "C+",
    70: "C",
    69: "D+",
    60: "D",
    59: "F",
    0: "F" ,
}
def display_letter_grade(student_data, course_code):
    """Displays the letter grade for a course.
    
    Args:
        student_data: A dictionary of student data.
        course_code: The code of the course.
    """
    # Check if the course is in the student's list of registered courses
    if "-Registered courses" in student_data and course_code in student_data["-Registered courses"]:
        # Get the index of the course in the list of registered courses
        course_index = student_data["-Registered courses"].split(" ").index(course_code)
        # Get the grade for the course
        grade = student_data["-Grades"].split(" ")[course_index]
        # Convert the grade to a letter grade
        letter_grade = grade_to_letter(grade)
        print(f"Your grade in {course_code} is {letter_grade}.")
    else:
        print("The course is not in your list of registered courses.")


    
POINT_MAPPING = {
    "A+": 4.0,
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0,
}

"""
output : {first:"ahmed",cours:"ph,qw,er"}
output : course 1 credit hours grade
         course 2 credit hours grade
"""
def read_student_data(student_id):
    student_data = {}
    with open("students.txt", "r") as f:
        lines = f.readlines()
        # Find the start and end indices of the student data block
        start_index = None
        end_index = None
        for i, line in enumerate(lines):
            if line.startswith("-ID:"):
                id = line.strip().split(":")[1]
                if id == student_id:
                    start_index = i-2
                    break
        if start_index is not None:
            for i in range(start_index+1, len(lines)):
                if lines[i].startswith("_"):
                    end_index = i
                    break
        if start_index is not None and end_index is not None:
            # Extract the student data block
            student_block = lines[start_index:end_index]
            # Parse the student data
            for line in student_block:
                key, value = line.strip().split(":")
                
                student_data[key] = value

        if start_index == None:
            return None, None


    return student_data ,start_index
#read_students_data("S1011")
   












def calc_gpa(student_data):
    """Calculates the student's GPA.
    
    Args:
        student_data: A dictionary of student data.
        
    Returns:
        The student's GPA.
    """
    total_points = 0
    total_credits = 0
    # Get the list of registered courses
    if "-Registered courses" in student_data:
        registered_courses = student_data["-Registered courses"].split(" ")
        
    else:
        registered_courses = []
    # Get the list of grades
    if "-Grades" in student_data:
        grades = student_data["-Grades"].split(" ")
    else:
        grades = []
    # Get the list of credit hours
    if "-Fullfilled credit hours" in student_data:
        credit_hours = student_data["-Fullfilled credit hours"].split(" ")
    else:
        credit_hours = []
    # Calculate the total points and credits for all courses
    #print(registered_courses)
    for i, course_code in enumerate(registered_courses):
        # Get the course data
        course_data = read_course_data(course_code)
        # Get the credit hours for the course
        if i < len(credit_hours):
            credit_hour = int(credit_hours[i])
        else:
            credit_hour = course_data["Credit hours"]
        # Get the grade for the course
        if i < len(grades):
            grade = int(grades[i])
        else:
            grade = 0
        # Convert the grade to a point value
        point_value = grade_to_point(grade)
        # Calculate the points and credits for the course
        course_points = point_value * credit_hour
        total_points += course_points
        total_credits += credit_hour

#         """print(f"""
#         cc {course_code}
#         credit hour: {credit_hour}
#         credit point: {point_value}
#         """)
# ""
    # Calculate the GPA
    if total_credits == 0:
        return 0
    gpa = total_points / total_credits
    
    return gpa



def display_student_record(student_data):
    record = ""
    """Displays the student's academic record.
    
    Args:
        student_data: A dictionary of student data.
    """
    # Get the list of registered courses
    if "-Registered courses" in student_data:
        registered_courses = student_data["-Registered courses"].split(" ")
    else:
        registered_courses = []
    # Get the list of grades
    if "-Grades" in student_data:
        grades = student_data["-Grades"]
    else:
        grades = []
    # Display the student's academic record
    print("Academic Record:")
    for i, course_code in enumerate(registered_courses):
        # Get the grade for the course
        if i < len(grades.split(" ")):
            grade = grades.split(" ")[i]
        else:
            grade = 0
        # Convert the grade to a letter grade
        letter_grade = grade_to_letter(grade)
        record+=f"{course_code}: {letter_grade} : {grade}\n"
    
    print(record)
    return record

#def register_course(student_data):
    #registered_courses = student_data["-Registered courses"]
    #print("Enter the course code of the course you want to register for:")
    #course = input()
    #if course in registered_courses:
        #print("You are already registered for this course.")
    #else:
        #registered_courses.append(course)
        #grades.append(0)
        #print("Course registration successful.")
def check_prerequisites(student_data, course_code):
    """Checks if the student has completed the prerequisites for the specified course.
    
    Args:
        student_data: A dictionary of student data.
        course_code: The code of the course to check prerequisites for.
        
    Returns:
        True if the student has completed the prerequisites, False otherwise.
    """
    course_data = read_course_data(course_code)
    if "prerequisites" not in course_data:  # No prerequisites defined for this course
        return True
    if not course_data["prerequisites"]:  # No prerequisites defined for this course
        return True
    for prerequisite in course_data["prerequisites"]:
        if prerequisite not in student_data["completed_courses"]:  # Student has not completed a prerequisite
            return False
    return True


def read_course_data(course_code):
    """Reads course data from courses.txt.
    
    Args:
        course_code: The code of the course to read data for.
        
    Returns:
        A dictionary of course data.
    """
    with open("courses.txt") as f:
        lines = f.readlines()
    course_data = {}
    for line in lines:
        if ":" not in line:  # Skip lines that do not contain a colon
            continue
        key, value = line.strip().split(":")
        if key == "Code" and value == course_code:
            course_data["code"] = value
        elif key == "Name":
            course_data["name"] = value
        elif key == "Description":
            course_data["description"] = value
        elif key == "Credit hours":
            course_data["credit_hours"] = int(value)
        elif key == "Prerequisites":
            course_data["prerequisites"] = value.split()
    return course_data



"""
def register_course(student_data, course_code):
    Registers the student for a course.
    
    Args:
        student_data: A dictionary of student data.
        course_code: The code of the course to register for.
        
    Returns:
        True if the student was successfully registered for the course, False otherwise.
    
    if not check_prerequisites(student_data, course_code):
        print("You have not completed the prerequisites for this course.")
        return False
    if "registered_courses" not in student_data:  # Initialize the registered courses list if it does not exist
        student_data["registered_courses"] = []
    if course_code in student_data["registered_courses"]:
        print("You are already registered for this course.")
        return False
    student_data["registered_courses"].append(course_code)
    if "grades" not in student_data:  # Initialize the grades list if it does not exist
        student_data["grades"] = []
    student_data["grades"].append(0)  # Add a grade of 0 for the course
    print(f"You have been registered for {course_code}.")
    return True

"""

def register_course(student_id, course_code):
    student_data, startIndex = read_student_data(student_id)
    courses  =read_courses()
    

    if student_data  != None:

        if course_code not in courses["code"]:
            print("Invalid course code")
            return

        if course_code in student_data["-Registered courses"]:
            print("You are already registered for this course.")
            return
        
        if not check_prerequisites(student_data, course_code):
            print("You have not completed the prerequisites for this course.")
            return
        
        student_data["-Registered courses"] = student_data["-Registered courses"] +" "+ course_code
        student_data["-Grades"] += " 0"  # Add a grade of 0 for the course
        
        # Write updated student data to the file
        lines = []
        with open("students.txt", "r") as f:
            lines = f.readlines()

        with open("students.txt","w") as f:
            lines[startIndex + 10] ="-Grades:"+ student_data["-Grades"] + "\n" 
            lines[startIndex+7] = "-Registered courses:"+ student_data["-Registered courses"] + "\n"
            f.write("".join(lines))
    else:
        print("No student with this id was found")

def read_courses():
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

def drop_course(student_id, course_code):
    """Drops a course from the student's academic record.
    
    Args:
        student_data: A dictionary of student data.
        course_code: The code of the course to be dropped.
    """
    student_data, startIndex = read_student_data(student_id)
    courses  =read_courses()
    
    
    if student_data  != None:

        print(student_data["-Registered courses"].split(" "))
        if not(course_code in student_data["-Registered courses"].split(" ")):
            print("You are not registered for this course.")
            return
        
        for i in range(len(student_data["-Registered courses"].split(" "))):
            if student_data["-Registered courses"].split(" ")[i] == course_code:
                break

        student_data["-Registered courses"] = student_data["-Registered courses"].replace(course_code+" ","")

        grades = student_data["-Grades"].split(" ")
        grades.pop(i)
        student_data["-Grades"] = " ".join(grades)

        # Write updated student data to the file
        lines = []
        with open("students.txt", "r") as f:
            lines = f.readlines()

        with open("students.txt","w") as f:
            lines[startIndex + 10] ="-Grades:"+ student_data["-Grades"] + "\n" 
            lines[startIndex+7] = "-Registered courses:"+ student_data["-Registered courses"] + "\n"
            f.write("".join(lines))
    else:
        print("No student with this id was found")

#data = read_student_data()

#register_course(data)


def run_function(student_data,student_id):
    """Prompts the user to choose a function to run and runs it.
    
    Args:
        student_data: A dictionary of student data, as returned by read_student_data.
    """
    while True:
        print("Enter the number of the function you want to run:")
        print("1. Register for a course")
        print("2. Drop a course")
        print("3. Display letter grade for a course")
        print("4. Display academic record")
        print("5. Calculate GPA")
        print("6. Quit")
        choice = input()
        if choice == "1":
            print("Enter the course code for the course you want to register for:")
            course_code = input()
            register_course(student_id, course_code)
        elif choice == "2":
            print("Enter the course code for the course you want to drop:")
            course_code = input()
            drop_course(student_id, course_code)
        elif choice == "3":
            print("Enter the course code for the course you want to check the letter grade for:")
            course_code = input()
            display_letter_grade(student_data, course_code)
        elif choice == "4":
            display_student_record(student_data)
            
        elif choice == "5":
            print("Your GPA is: {:.2f}".format(calc_gpa(student_data)))
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    student_id = input("Enter student ID: ")
    student_data = read_student_data(student_id)[0]
    if student_data is None:
        print("Invalid student ID")
        return

    run_function(student_data,student_id)

    #run_function(student_data)


main()




