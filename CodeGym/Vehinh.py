import turtle


shapeinput=input("circle ,triangle,or square , what is you favorite shape ? \n Enter your shape : ")
    
if (shapeinput == "circle") or (shapeinput == "triangle")  or (shapeinput=="square") :
    colorinput=input("what color you will it be ? yellow , red or blue ? \n Enter your color : ")
    if (colorinput =="yellow") or (colorinput == "red") or (colorinput=="blue"):
        
        pen=turtle.Screen()
        pen.bgcolor("black")
        pen.title("You shape")

        displayShape=turtle.Turtle()
        displayShape.shape(shapeinput)
        displayShape.color(colorinput)

        turtle.done()
    else:
        print("Sorry . I don't have this color ")
else :
    print("Sorry , I don't have this shape ")
