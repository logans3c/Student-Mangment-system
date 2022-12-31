def admin_page() :
    print("hello admin ")

def student_page() :
    print("hello student")
    

def faculty_page() :
    print("hello faculty")

            

def login_page() :
    accountfile = open("accounts.txt","r")
    lines = accountfile.readlines()
    count = 0
    while count < 3 :
        login_id = input("Enter your ID : ")
        login_pass = input("Enter your password : ")
        for i in range (len(lines)) :
            eachline = lines[i]
            line_details = eachline.rstrip("\n").split("\t")
            if (line_details[0]==login_id) and (line_details[1]==login_pass) :
                count = 4
                if line_details[0].startswith("A") :
                    admin_page()
                elif line_details[0].startswith("S"):
                    student_page()
                elif line_details[0].startswith("F") :
                    faculty_page()
                break
        else:
            count +=1
            print("your ID or password is invalid")
    else :
        if (count!=4) :
            print("try again")
    accountfile.close()




login_page()