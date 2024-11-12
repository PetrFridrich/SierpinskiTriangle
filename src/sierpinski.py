import turtle
import math

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class Sierpinski:

    def __init__(self, max_depth=6, altitude=500):

        # Set the maximum depth for recursion and the triangle's altitude (height)
        self.max_depth = max_depth
        self.altitude = altitude

        # Calculate the top point of the triangle
        self.top = Point(x=0, y=self.altitude / 2)

        # Calculate the side length of the base of the equilateral triangle
        side_length = (2 * self.altitude) / math.sqrt(3)

        # Calculate the left and right bottom points of the triangle
        self.left = Point(x=self.top.x - side_length / 2, y=self.top.y - self.altitude)
        self.right = Point(x=self.top.x + side_length / 2, y=self.top.y - self.altitude)


    def sierpinski_recursion(self, top, left, right, depth):

        # Draw the triangle at the current level
        self.draw_single_triangle(top, left, right)

        # If depth is greater than 1, continue recursion for smaller triangles
        if depth > 1:
            # Calculate midpoints of each side to form smaller triangles
            top_left_mid = Point(left.x + (top.x - left.x) / 2, left.y + (top.y - left.y) / 2)
            top_right_mid = Point(right.x + (top.x - right.x) / 2, right.y + (top.y - right.y) / 2)
            left_right_mid = Point(left.x + (right.x - left.x) / 2, left.y + (right.y - left.y) / 2)

            # Recursively draw the smaller triangles for the next level
            # Left sub-triangle
            self.sierpinski_recursion(top_left_mid, left, left_right_mid, depth - 1)
            # Top sub-triangle
            self.sierpinski_recursion(top, top_left_mid, top_right_mid, depth - 1)
            # Right sub-triangle
            self.sierpinski_recursion(top_right_mid, left_right_mid, right, depth - 1)


    def draw_single_triangle(self, top, left, right):

        # Move the turtle to the starting point (left vertex)
        self.t.penup()
        self.t.goto(left.x, left.y)
        self.t.pendown()
        
        # Draw lines connecting left -> right -> top -> left to complete the triangle
        self.t.goto(right.x, right.y)
        self.t.goto(top.x, top.y)
        self.t.goto(left.x, left.y)


    def draw_triangles(self):

        # Initialize the turtle
        self.t = turtle.Turtle()
        self.t.speed(3)  # Set drawing speed (1: slowest, 10: fastest)

        # Begin the recursive drawing process
        self.sierpinski_recursion(self.top, self.left, self.right, self.max_depth)

        # Hide the turtle and display the window after completion
        self.t.hideturtle()
        turtle.done()


