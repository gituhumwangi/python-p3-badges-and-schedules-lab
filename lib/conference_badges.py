def badge_maker(name):
    badge_name = f"Hello, my name is {name}."
    return badge_name


def batch_badge_creator(names):
    altered_names = list()
    for n in names:
        altered_names.append(f"Hello, my name is {n}.")
    return altered_names
    

def assign_rooms(names):
    room_assigned = list()
    index = 1
    for n in names:
        room_assigned.append(f"Hello, {n}! You'll be assigned to room {index}!")
        index += 1
    return room_assigned

def printer(names):
    badge_list = batch_badge_creator(names)
    assign_rooms_list = assign_rooms(names)
    for n in badge_list:
        print(n)
    for i in assign_rooms_list:
        print(i)
    return badge_list, assign_rooms_list
print(printer(["Dennis","Gituhu"]))