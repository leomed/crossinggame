from turtle import Turtle
STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 200
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.player_start()

    def player_start(self):
        """The creation of the turtle"""
        self.shape("turtle")
        self.color("yellow")
        self.penup()
        # go to start  is a method
        self.go_to_start()
        self.setheading(90)

    def move_forward(self):
        """It allows the turtle to move"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """This function redirects the turtle to the bottom
         of the screen in the y_line
         """
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """If player reaches the end It's
        because he passed the level
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

