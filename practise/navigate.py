#3 inputs : 5,5 | 0,1,N | MMRMMRMRRM

import sys

lower_boundary = (0,0)
move_by = 1
compass = ("W", "N", "E", "S")
spin = ("L", "R")
command = ("M",)


class Navigate(object):
    def __init__(self, x, y, direction, upper_x, upper_y):
        self.x = x
        self.y = y
        self.direction = direction
        self.upper_x = upper_x
        self.upper_y = upper_y
        
    def MoveForward(self):
        self.validate_boundaries()
        if self.direction == "N":
            self.y = self.y + move_by

        elif self.direction == "E":
            self.x = self.x + move_by

        elif self.direction == "S":
            self.y = self.y - move_by

        elif self.direction == "W":
            self.x = self.x - move_by

        if self.direction not in compass:
            print "Invalid input: A rover can move forward in the North(N), East(E), West(W) or South(S) direction only."
        else:
            return self.x, self.y, self.direction

    def Spin(self, turn):
        current_direction = self.direction
        if turn == "L":
            new_index = (compass.index(current_direction) - 1) % 4
        elif turn == "R": 
            new_index = (compass.index(current_direction) + 1) % 4

        self.direction = compass[new_index]
        if turn not in spin:
            print "Invalid direction: A rover can spin only in the left (L) or right (R) direction."
        else:
            return self.x, self.y, self.direction

        self.direction = compass[new_index]

    def validate_boundaries(self):
        if 0 <= self.x <= self.upper_x and 0 <= self.y <= self.upper_y: 
            pass
        else:
            print "Boundaries reached, cannot move forward."
            sys.exit(1)


# main program starts here
if __name__ == '__main__':
    try: 
        # take input from the user
        upper_boundary = raw_input("Enter the upper right co-ordinates : ").split(',')
        pos = raw_input("Enter the current position : ").split(',')
        instr = raw_input("Enter the series of Instructions to be followed : ")

        # converting raw_input to int
        upper_boundary = [int(x) for x in upper_boundary]
        pos = [int(x) if idx < 2 else x for idx,x in enumerate(pos) ]

        list_of_instr = (x for x in instr)
        # validate input position
        if len(pos) != 3  and isinstance(pos[0], int) and isinstance(pos[1], int) and pos[2] not in compass:
            print "Invalid input"
            sys.exit(1)

        # validate upper boundaries
        elif len(upper_boundary) != 2 and isinstance(upper_boundary[0], int) and isinstance(upper_boundary[1], int):
            print "Invalid Input"
            sys.exit(1)

        #iterate over series of instr to reach the desired location
        else:
            for instr in list_of_instr:
                #import pdb; pdb.set_trace()
                obj = Navigate(pos[0], pos[1], pos[2], upper_boundary[0], upper_boundary[1])
                # if L or R, then spin
                if instr in spin:
                    pos = obj.Spin(instr)
                # else if M, then move forward
                elif instr in command:
                    pos = obj.MoveForward()
            print pos

    except Exception, e:
        import traceback
        print "Error : %s" % (e)
        print traceback.format_exc()
        sys.exit(1)
