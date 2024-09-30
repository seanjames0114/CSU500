# Dictionary containing course numbers and room numbers
course_rooms = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

# Dictionary containing course numbers and instructors
course_instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

# Dictionary containing course numbers and meeting times
course_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# Create a function that takes in a dict and the course number to search
# Return the dict if it is found 
def get_value(dictionary, search):
    return dictionary.get(search, "Course not found")

# Take in the course number from the user 
c_n = input('Enter the Course Number : ')

# Call the function to return the value found by the key
time = get_value(course_times, c_n)
instructor = get_value(course_instructors, c_n)
room = get_value(course_rooms, c_n) 

# If the course is found and not "Course not found" then print the values found. Otherwise print the value (it will be Course not found)
if time != "Course not found":
    print(f"Room: {room}, Instructor: {instructor}, Meeting Time: {time}")
else:
    print(time)