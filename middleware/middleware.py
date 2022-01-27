# This method ensures the first rover is landed within the plateau perimeter

def roverIsWithinPerimeter(rover_x, plateau_x, rover_y, plateau_y, pointer):
    rover_x = int(rover_x)
    rover_y = int(rover_y)
    plateau_x = int(plateau_x)
    plateau_y = int(plateau_y)
    points = "NSEW"

    if ((rover_x > plateau_x or rover_x < 0) or (rover_y > plateau_y or rover_y < 0)):
        raise Exception("The rover co-ordinates are outside the borders of the plateau")

    if pointer not in points:
        raise Exception("That is not a valid cardinal point")
    
    

# This method ensures that the second/subsequent rovers are landed within the plateau perimeter and not is/not landing on another rover

def roverIsWithinPerimeter_x(rover_x, plateau_x, rover_y, plateau_y, pointer, pre_rover = ()):
    rover_x = int(rover_x)
    rover_y = int(rover_y)
    plateau_x = int(plateau_x)
    plateau_y = int(plateau_y)
    points = "NSEW"

    if ((rover_x == pre_rover[0]) and (rover_y == pre_rover[1])):
        raise Exception("Cannot land rover here, an existing rover already occupies this position")

    if ((rover_x > plateau_x or rover_x < 0) or (rover_y > plateau_y or rover_y < 0)):
        raise Exception("The rover co-ordinates are outside the borders of the plateau")

    if pointer not in points:
        raise Exception("That is not a valid cardinal point")


# This method ensures valid movements are pre-determined before the first rover begins movement

def isValidMovement(x_pos, y_pos, upper_x, upper_y, pointer):
    if pointer == "N":
        if (y_pos == upper_y):
            raise Exception("Invalid movement, you're trying to go out of bounds")
    if pointer == "S":
        if (y_pos == 0):
            raise Exception("Invalid movement, you're trying to go out of bounds")
    if pointer == "W":
        if (x_pos == 0):
            raise Exception("Invalid movement, you're trying to go out of bounds")
    if pointer == "E":
        if (x_pos == upper_x):
            raise Exception("Invalid movement, you're trying to go out of bounds")




# This method ensures valid movements are pre-determined before the second/subsequent rovers begins movement 

def isValidMovement_x(x_pos, y_pos, upper_x, upper_y, pointer, pre_rover = ()):
    if pointer == "N":
        if ((y_pos == upper_y) or ((x_pos == pre_rover[0]) and (y_pos == pre_rover[1] - 1))):
            raise Exception("Invalid movement, you're either trying to go out of bounds or collide with a rover")
    if pointer == "S":
        if ((y_pos == 0) or ((x_pos == pre_rover[0]) and (y_pos == pre_rover[1] + 1))):
            raise Exception("Invalid movement, you're either trying to go out of bounds or collide with a rover")
    if pointer == "W":
        if ((x_pos == 0) or ((y_pos == pre_rover[1]) and (x_pos == pre_rover[0] + 1))):
            raise Exception("Invalid movement, you're either trying to go out of bounds or collide with a rover")
    if pointer == "E":
        if ((x_pos == upper_x) or ((y_pos == pre_rover[1]) and (x_pos == pre_rover[0] - 1))):
            raise Exception("Invalid movement, you're either trying to go out of bounds or collide with a rover")