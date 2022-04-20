from collections import OrderedDict

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def values(self):
        return str(self.x) + "|" + str(self.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)




def calculate_vector(start, end):
    vector = end - start
    return vector



def calc_touched_fields(vector, start_point, end_point):
    
    vector_x = float(vector.get_x())
    vector_y = float(vector.get_y())

    steps_x_direction = vector_x * 2
    steps_y_direction = vector_y * 2

    factor_x = abs(0.5 / vector_x)
    factor_y = abs(0.5 / vector_y)
    
    offset = 0.005
    
    touched_fields = []
    #in loops add + start x und y

    #print("x loop")
    i=0
    for i in range(abs(int(steps_x_direction))):
        x_value = vector_x * (factor_x * (i+1) - offset) + int(start_point.get_x())
        y_value = vector_y * (factor_x * (i+1) - offset) + int(start_point.get_y())
        new_point = Point(int(round(x_value)), int(round(y_value)))
        #print(new_point.values())
        if new_point.values() in touched_fields:
            continue
        else:
            touched_fields.append(new_point)
    
    print()
    
    #print("y loop")
    i=0
    for i in range(abs(int(steps_y_direction))):
        x_value = vector_x * (factor_y * (i+1) - offset) + int(start_point.get_x())
        y_value = vector_y * (factor_y * (i+1) - offset) + int(start_point.get_y())
        new_point = Point(int(round(x_value)), int(round(y_value)))
        #print(new_point.values())
        if new_point.values() in touched_fields:
            continue
        else:
            touched_fields.append(new_point)

    return touched_fields



def calc_pythago(vector):
    x = vector.get_x()
    y = vector.get_y()
    res = int(x)**2 + int(y)**2
    #print(res)
    return res



def sort_touched_fields(touched_fields, start_point, end_point):
    
    print()
    print("start point: " + start_point.values())
    print("end point: " + end_point.values())
    print("vector: " + calculate_vector(start_point, end_point).values())
    print()
    #touched_fields.sort()
    print("touched fields: ")
    print("x|y")

    vector_dict = {}

    i=0
    for n in touched_fields:
        vector = calculate_vector(start_point, touched_fields[i])
        length_of_vector = calc_pythago(vector)
        vector_dict[length_of_vector] =  touched_fields[i].values()
        i += 1
        
    #print(vector_dict)
    #print()
    
    sorted_vector_dict = OrderedDict(sorted(vector_dict.items()))
    #print(sorted_vector_dict)
    #print()

    i=0
    for key in sorted_vector_dict.keys():
        print(sorted_vector_dict[key])
        i += 1
    
    print("\n")



def validate_input_int(input_value):
    try:
        val = input_value
        val_x = int(val[0])
        val_y = int(val[1])
        return True
    except ValueError:
        print()
        print("ERROR: enter Integers only!")
        print()
    


def start():
    mainloop = True

    while mainloop:
        print("")
        print(">> calculate touched fields by vector <<\n")
        print("choose option:\n")
        print("1 - example")
        print("2 - set end point")
        print("3 - set start and end point")
        print("q - quit")

        user_input = input("-> ")

        if user_input == "1":
            start_point = Point(0,0)
            end_point = Point(3,-5)
            vector = calculate_vector(start_point, end_point)
            touched = calc_touched_fields(vector, start_point, end_point)
            sort_touched_fields(touched, start_point, end_point)
        elif user_input == "2":
            start_point = Point(0,0)
            end = input("end point x y: ").split()
            if validate_input_int(end):
                end_point = Point(int(end[0]),int(end[1]))
                vector = calculate_vector(start_point, end_point)
                touched = calc_touched_fields(vector, start_point, end_point)
                sort_touched_fields(touched, start_point, end_point)
        elif user_input == "3":
            start = input("start point x y: ").split()
            if validate_input_int(start):
                start_point = Point(int(start[0]),int(start[1]))
                end = input("end point x y: ").split()
                if validate_input_int(end):
                    end_point = Point(int(end[0]),int(end[1]))
                    vector = calculate_vector(start_point, end_point)
                    touched = calc_touched_fields(vector, start_point, end_point)
                    sort_touched_fields(touched, start_point, end_point)
        elif user_input == "q":
            mainloop = False
        else:
            print("input NOT VALID!!!\n")

        print()
        #vector = calculate_vector(start_point, end_point)

        #calc_touched_fields(vector)



start()
