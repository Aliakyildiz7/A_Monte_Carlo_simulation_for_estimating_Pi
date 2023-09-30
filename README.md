# A_Monte_Carlo_simulation_for_estimating_Pi

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
