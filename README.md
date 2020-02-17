# CircuitPython stuffs
some small circuitpython programs that I made for school.

"small"

README is a text file describing all the stuff I have made so far. it taught me how to use nano (a text editor).


## RGB

### description
a library for using RGBLEDs. it lets you set them to any of the 6 primary/secondary colors, white, and off.

### lessons learned
the pin must be set to high to trun that specific color off. hooray for logic.


## button_count_LCD

### description 
counts up or down when a button is pressed depending on wether a switch has been flipped and prints the value to an LCD. 

### lessons learned
i don't remember any lessons i learned with this one but there was probably something.


## capacitive_touch_servo

### description
moves a servo one way when you touch one wire and the other way when you touch the other.

### lessons learned
how to use capacitive touch.


## color_scale_distance_thing

### description
fades the onboard neopixel through the color scale depending on the input from the distance sensor.

### lessons learned
linear equations are very usefull, even if the thing you are using them for has nothing to do with linear equations.


## fading_led

### description
single color LED that fades in and out as time progresses.

### lessons learned
neopixels are a thing that exists.


## photointerrupter_LCD_thing

### description
counts the number of times a photointerrupter has been interrupted and displays the number to an LCD every 4 seconds.

### lessons learned
i learned how wire a photointerrupter. it makes less sense than you might think. even though i learned how to do this last year.


## rAiNbOwS

### description
created to be used by the RGB library and makes two RGBLEDs do rainbow things. i made it much more complicated than the assignment required, but it was fun and shiny, so here we are.

### lessons learned
i have no idea


## FancyLED

### description
another library, this time for 3 seperate single color LEDs.

### lessons learned
didn't learn much of anything here either.


## complicated_wiring

### description
the thing I used to test FancyLED. i burned out 3 LEDs and most of my sanity making this.

### lessons learned
do not try this at home kids. if you do, color code your wires.



wherever you see '#pylint: disable-msg=import-error' it means that the library before it works only with circuitpython and not regular python. '#pylint: disable-msg=import-error' makes the compiler stop sending error messages about things that arne a real problem.
