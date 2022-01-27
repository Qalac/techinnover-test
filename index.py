from Rover.rover import Rover
from Plateau.plateau import Plateau
from middleware.middleware import *

plateau_dim = input("Enter the upper-right co-ordinates of the rectangular plateau in order X Y: \n").upper().replace(" ","")

#  -----------    Setting the dimensions of the plateau    ----------------

plateau = Plateau(plateau_dim[0], plateau_dim[1])


rover_dim = input("Enter the rover's landing co-ordinates in this format(X Y [orientation]): \n").upper().replace(" ","")

# ------------- checks if the rover will be landed within the perimeter of the plateau   ------------------

roverIsWithinPerimeter(rover_dim[0], plateau_dim[0], rover_dim[1], plateau_dim[1], rover_dim[2])


inst_string = input("Enter instructions to be carried out by the rover: \n").upper().replace(" ","")



# ------------------------ setting up the first rover with its landing co-ordinates ------------------------

rover = Rover(rover_dim[0], rover_dim[1], rover_dim[2])

# ------------------- intepreting instruction string to move rover --------------------------

for index in inst_string:
    if index == "L":
        rover.setLeft()
    elif index == "R":
        rover.setRight()
    elif index == "M":
        isValidMovement(rover.x_pos, rover.y_pos, plateau.x, plateau.y, rover.dir)
        rover.moveForward()

print(rover.position)




# ------------------  collecting data for the second/subsequent rover ----------------------



rover_dim_x = input("Enter the second rover's landing co-ordinates in this format(X Y [orientation]): \n").upper().replace(" ","")

# ------------- checks if the rover will be landed within the perimeter of the plateau and also not on another rover  ------------------

roverIsWithinPerimeter_x(rover_dim_x[0], plateau_dim[0], rover_dim_x[1], plateau_dim[1], rover_dim_x[2], pre_rover=rover.position)


inst_string_x = input("Enter instructions to be carried out by the rover: \n").upper().replace(" ","")


# ------------------------ setting up the second/subsequent rover with its landing co-ordinates ------------------------

rover_x = Rover(rover_dim_x[0], rover_dim_x[1], rover_dim_x[2])

# ------------------- intereting instruction string to move rover --------------------------

for index in inst_string_x:
    if index == "L":
        rover_x.setLeft()
    elif index == "R":
        rover_x.setRight()
    elif index == "M":
        isValidMovement_x(rover_x.x_pos, rover_x.y_pos, plateau.x, plateau.y, rover_x.dir, pre_rover=rover.position)
        rover_x.moveForward()

print(rover_x.position)


