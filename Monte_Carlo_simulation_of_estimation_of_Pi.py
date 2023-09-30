import random
import matplotlib.pyplot as plt
import math
import turtle
import tkinter as tk

"""
This code estimates the pi number, by generating random coordinates in a square
and checking if that square is also in inner tangent cirle of  the square.
Let r be the radius of the circle; Then:
    -Area of the square = 4 * r^2
    -Area of the circle = pi * r^2
Then the ratio must be pi / 4. If we multiply the hit rate with 4, in theory it should give us pi.

It also comes with the animation argument, which when set True, displays the dot on turtle screen and 
displays the estimated pi in a tkinter screen. However doing that greatly increases runtime.
"""


def random_coordinates_in_square():
    "Generates random coordinates in a 1 by 1 square"
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    return x, y


def is_in_circle(x, y):
    "Checks if the numbers are in the unit circle"
    if x ** 2 + y ** 2 <= 1:
        return True
    return False

def find_ratio_and_animate(n):

    """Finds the estimated pi with using random_coordinates_in_sqaure() and is_in_circle() methods for n trials.
    Saves the generated values in matrices for plotting.
    Also shows the generated points on a turtle screen as dots(green if it is in circle and red if it is not)
    Displays the number of trials and estimated pi value in tkinter screen.
    Use "animation=True" in main() for calling this function.
    You can run the program with small n values compared to find_ratio() with this.
    """


    #Setting up the turtle screen and pointer
    r = set_turtle_screen()
    pointer = turtle.Turtle()
    pointer.speed(0)
    pointer.penup()


    #Setting up the tkinter screen
    root = tk.Tk()
    trial_label = tk.Label(root, text="Number of Trials")
    trial_label.grid(row=0, column=0)
    Pi_label =tk.Label(root, text="Estimated Pi")
    Pi_label.grid(row=1, column=0)

    trial_entry = tk.Entry(root)
    trial_entry.grid(row=0, column=1)
    Pi_entry = tk.Entry(root)
    Pi_entry.grid(row=1, column=1)


    Pi_estimation = []  # The matrice to save estimated Pi values in ratio()
    Pi_real = []  # The matrice to save real Pi values from the math library
    X = []  # The matrice to save number of trials

    hit = 0 #Will only increase if in circle
    total = 0 #Will increase either way

    for _ in range(n):
        #print(_)
        x, y = random_coordinates_in_square()
        pointer.setpos(r * x, r * y)

        if is_in_circle(x, y):
            pointer.dot(10, "green")
            hit += 1
        else:
            pointer.dot(10, "red")

        total += 1
        Pi_estimation.append(4 * (hit / total))
        Pi_real.append(math.pi)
        X.append(_)


        Pi_entry.delete(0, tk.END)
        Pi_entry.insert(0, f"{Pi_estimation[-1]: .4f}")

        trial_entry.delete(0, tk.END)
        trial_entry.insert(0, str(_ + 1))

        root.update()

    return Pi_estimation, Pi_real, X


def find_ratio(n):

    """
    Does what find_ratio does without animation.
    Use "animation=false" in main() for calling this function.
    You can run the program with much bigger n values with this.
    """

    Pi_estimation = []  # The matrice to save estimated Pi values in ratio()
    Pi_real = []  # The matrice to save real Pi values from the math library
    X = []  # The matrice to save # of trials

    hit = 0 #Will only increase if in circle
    total = 0 #Will increase either way

    for _ in range(n):
        #print(_)
        x, y = random_coordinates_in_square()

        if is_in_circle(x, y):

            hit += 1

        total += 1
        Pi_estimation.append(4 * (hit / total))
        Pi_real.append(math.pi)
        X.append(_)

    return Pi_estimation, Pi_real, X


def plot_pi(Pi_estimation, Pi_real, X, n):

    """
    Plots the estimated pi vs number of trials in matplotlib library
    """

    plt.plot(X, Pi_estimation, label="Estimated_Pi")
    plt.plot(X, Pi_real, label="Real_Pi")
    plt.xlabel("Number of Trials")

    plt.title(f"Monte Carlo Simulation of Pi after {n:.2e} trials")

    plt.legend()

def set_turtle_screen():

    """
    Draws the circle and enclosing square in turtle
    """
    r = 250 #Radius of the circle, also determines screen dimensions.
    blank = 15 #Distance between square and edges of turtle window
    width = 2*r
    height = 2*r
    turtle.setup(width=width + 2 * blank, height=height + 2 * blank)

    drawer = turtle.Turtle()
    drawer.speed(0)

    drawer.penup()
    drawer.setpos(0, -r)
    drawer.pendown()

    drawer.circle(r)

    drawer.penup()
    drawer.setpos(-r, -r)
    drawer.pendown()
    drawer.hideturtle()

    for x in range(4):
        drawer.forward(2 * r)
        drawer.left(90)

    return r





def main(n, animation=True):

    """
    Main function to organize functions and their returns.
    """

    if animation == True:
        Pi_Estimation, Pi_Real, X = find_ratio_and_animate(n)
    else:
        Pi_Estimation, Pi_Real, X = find_ratio(n)


    plot_pi(Pi_Estimation, Pi_Real, X, n)
    print(f"Estimated Pi after {n: .2e} trials is {Pi_Estimation[-1]: .4f}")
    #plt.savefig(f"Pi_Estimation_after_{n: .2e}_trials.png")
    plt.show()


    if animation == True:
        turtle.done()

    return None


if __name__ == "__main__":
    main(n=int(1e3), animation=True)


