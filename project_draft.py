print("*"*70)
print("\n\n\n            WELCOME TO THE STUDENT PAGE")
print("\n- WHAT ARE YOU WANT TO DO")
print("\n1) REGISTER OR DROP COURSES")
print("\n2) CHECK YOUR DEGREE IN LETTERS")
print("\n3) CHECK YOUR GPA")

print("\n\n\n\n\n\n","*"*50)

# Read the courses from the courses.txt file
def reg_or_drop():
    with open('courses.txt', 'r') as f:
        courses = [line.strip().split() for line in f]

# Print the available courses
    print('Available courses:')
    for i, (name, credits) in enumerate(courses):
        print(f'{i + 1}. {name} ({credits} credits)')

# Initialize the list of registered courses
    registered_courses = []

# Main loop
    while True:
    # Prompt the user to choose an action
        action = input('Enter R to register for a course, D to drop a course, or Q to quit: ')

        if action == 'R':
        # Register for a course
            print('Enter the number of the course you want to register for:')
            for i, (name, credits) in enumerate(courses):
                print(f'{i + 1}. {name} ({credits} credits)')

        # Get the number of the course the user wants to register for
            course_number = int(input())

        # Add the course to the list of registered courses
            registered_courses.append(courses[course_number - 1])
            print(f'Successfully registered for {courses[course_number - 1][0]}')
        elif action == 'D':
        # Drop a course
            if not registered_courses:
                print('You are not registered for any courses.')
            else:
                print('Enter the number of the course you want to drop:')
                for i, (name, credits) in enumerate(registered_courses):
                    print(f'{i + 1}. {name} ({credits} credits)')

            # Get the number of the course the user wants to drop
                course_number = int(input())

            # Remove the course from the list of registered courses
                del registered_courses[course_number - 1]
                print(f'Successfully dropped {courses[course_number - 1][0]}')
        elif action == 'Q':
        # Quit the program
            break
        else:
            print('Invalid action. Try again.')

#def course_info():

def calculate_cgpa(grades, credits):
    # grades is a list of tuples, where each tuple contains the letter grade and credit hours for a course
    # credits is a list of integers, where each integer is the credit hours for a course
    
    # create a dictionary that maps letter grades to grade points
    grade_points = {
        'A+': 4.0,
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'F': 0.0
    }
    
    # initialize variables to track the total number of credits and the total number of grade points
    total_credits = 0
    total_grade_points = 0
    
    # loop through each course
    for grade, credit in zip(grades, credits):
        # add the credit hours for the course to the total number of credits
        total_credits += credit
        # add the grade points for the course to the total number of grade points
        total_grade_points += grade_points[grade] * credit
    
    # divide the total number of grade points by the total number of credits to calculate the C-GPA
    cgpa = total_grade_points / total_credits
    
    return cgpa


#To use this function, you can pass in two lists: one for the letter grades and one for the credit hours. For example:
student_grade_in_letters=0
credit_hours_for_each_course=0
grades = student_grade_in_letters
credits = credit_hours_for_each_course

#cgpa = calculate_cgpa(grades, credits)
#print(cgpa)


def choice():
    global u_choice
    u_choice = str(input("\nPLEASE CHOSE THE NUMBER OF THE SERVICE YOU WANT : "))
   
choice()
while u_choice not in ["1","2","3"] :
    print("PLEASE ENTER VALID NUM")
    choice()
if u_choice=="1" :
    reg_or_drop()
elif u_choice=="2":
    letter_Grade()
elif u_choice=="3":
    calculate_cgpa()       