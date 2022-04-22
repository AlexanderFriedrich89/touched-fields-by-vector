from collections import OrderedDict
from numpy import full as np_full

#define class Point to use for coordinates and vectors
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



#calculate vector between two points
def calculate_vector(start, end):
    vector = end - start
    return vector


#calculate all fields the vector goes through
#do calculation for all steps in x and y direction
def calc_touched_fields(vector, start_point, end_point):
    
    vector_x = float(vector.get_x())
    vector_y = float(vector.get_y())

    steps_x_direction = vector_x * 2
    steps_y_direction = vector_y * 2

    factor_x = abs(0.5 / vector_x)
    factor_y = abs(0.5 / vector_y)
    
    #use offset to avoid calculation directly on field border
    offset = 0.005
    
    touched_fields = []

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


#calculate length of vector. use value later for sorting
def calc_pythago(vector):
    x = vector.get_x()
    y = vector.get_y()
    res = int(x)**2 + int(y)**2
    #print(res)
    return res


#sort list of touched fields. convert to dictionary with length of vector as key value
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


#validate user input to avoid errors due to incorrect input and datatypes
def validate_input_int(input_value):
    try:
        val = input_value
        if len(val) == 2:
            val_x = int(val[0])
            val_y = int(val[1])
            return True
        else:
            print()
            print("ERROR: input incorrect!")
            print()
            return False
    except ValueError:
        print()
        print("ERROR: enter Integers only!")
        print()
    

#generate a grid to show calculated touched fields / vector
def generate_grid(vector, touched, start_point, end_point):
    rows, columns = (abs(vector.get_y()), abs(vector.get_x()))
    grid = np_full((rows + 1, columns + 1), 0)

    #if start not 0 , set offset-to-origin: x + x*(-1) and y + y+(-1)
    #calc all points with offset-to-origin

    #point xy + offset + xy translation
    #use only offset and translation to get line in positive quadrant
    
    #offset to move vector to origin
    #translate to move vector to positive quadrant because of array indexes
    #otherwise vector could not fit in grid
    offset_x = offset_y = 0

    if (start_point.get_x() != 0 or start_point.get_y() != 0):
        offset_x = start_point.get_x() * (-1)
        offset_y = start_point.get_y() * (-1)
    
    translate_x = translate_y = 0
    #if offset > 0 then translate - offset 
    if vector.get_x() < 0 and vector.get_y() < 0:
        translate_x = end_point.get_x() * (-1) - offset_x
        translate_y = end_point.get_y() * (-1) - offset_y
    else:
        if vector.get_x() < 0:
            translate_x = end_point.get_x() * (-1) - offset_x
        if vector.get_y() < 0:
            translate_y = end_point.get_y() * (-1) - offset_y

    #print("off x: " + str(offset_x))
    #print("off y: " + str(offset_y))
    #print("trans x: " + str(translate_x))
    #print("trans y: " + str(translate_y))

    #print("vec: " + str(vector.values()))
    #print("rows: " + str(rows))
    #print("columns: " + str(columns))
    
    #print(touched)

    grid_start = Point(start_point.get_x() + offset_x + translate_x, start_point.get_y() + offset_y + translate_y)
    print("GRID: start point at: " + str(grid_start.get_x()) + "|" + str(grid_start.get_y()))
    
    n=0
    for k in touched:
        x = touched[n].get_x() + offset_x + translate_x
        y = touched[n].get_y() + offset_y + translate_y
        #print("x/y: " + str(x) + " " + str(y))
        grid[y][x] = 1
        n += 1
 
    print(grid)
    print("\n")
    print("------")
    print()



#main loop for user input
#call needed steps for calculation according to choosen option
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
            generate_grid(vector, touched, start_point, end_point)
        elif user_input == "2":
            start_point = Point(0,0)
            end = input("end point x y: ").split()
            if validate_input_int(end):
                end_point = Point(int(end[0]),int(end[1]))
                vector = calculate_vector(start_point, end_point)
                touched = calc_touched_fields(vector, start_point, end_point)
                sort_touched_fields(touched, start_point, end_point)
                generate_grid(vector, touched, start_point, end_point)
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
                    generate_grid(vector, touched, start_point, end_point)
        elif user_input == "q":
            mainloop = False
        else:
            print("input NOT VALID!!!\n")

        print()



#start program execution
start()
