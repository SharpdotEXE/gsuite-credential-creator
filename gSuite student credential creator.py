

#take input
school = input("enter school name: ")
name = input("enter student name: ")
student_ID = input("enter student ID: ")
student_grade = input("enter student grade: ")
school_initials = school[0].title() + 'PS'

#create domain based on name of school
if school != 'lane':
    domain = f'@{school}.k12.ok.us'
else:
    domain = "@lanepublicschools.org"

#graduating year reference
grade_to_year = {1: 34, 2: 33, 3: 32, 4: 31, 5: 30, 6: 29, 7: 28, 8: 27, 9: 26, 10: 25, 11: 24, 12: 23}

#manipulating variables
name = name.title()
first_name = name.split()[0]
last_name = name.split()[1]
student_ID = student_ID[-4:]
graduating_year = grade_to_year[int(student_grade)]
graduating_year = str(graduating_year)


#define format that will be used for username
if school != 'indianola':
    username = first_name + '.' + last_name + graduating_year + domain
else:
    username = first_name[0] + last_name + graduating_year + domain

#create password
password = school_initials + student_ID + '!'

#display results
print(f'you entered: {school}, {name}, {student_ID}, {student_grade}')
print(f'username: {username}')
print(f'password: {password}')