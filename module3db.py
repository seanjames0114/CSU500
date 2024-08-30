restriced_names = ["sean", "jeff", "brian"]

current_name = "sean"

door_open = False
def checkName(c_n):
    if(c_n in restriced_names):
        door_open = False
        return door_open
    else:
        door_open = True
        return door_open

print("Current Name is : ", current_name)
print(checkName(current_name))

current_name = "kyle"

print("Current Name is : ", current_name)
print(checkName(current_name))
