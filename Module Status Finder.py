Credits = {0,20,40,60,80,100,120}
Progress_count = 0
Trailer_count = 0
Excluded_count = 0
Retriever_count = 0
Option = {'y', 'q'}
Values = []
User = {'s', 't'}

from graphics import *
def histogram():
    win = GraphWin("Histogram", 550, 620)#Open the window object called "win" with title and size 
    win.setBackground("honeydew")#Set the background colour of the window

    my_heading = Text(Point(270,30), "Histogram Results")#Set the heading of the histogram
    my_heading.draw(win)
    my_heading.setFace("arial")
    my_heading.setSize(22)
    my_heading.setStyle("bold")
    my_heading.setTextColor("darkolivegreen")

    aLine = Line(Point(50,525), Point(505,525))#Draw the x-axis of the histogram
    aLine.draw(win)

    space = 90#Width of one rectangle
    bar_space = 20#The space between two rectangles

    height1 = (Progress_count*100)/6.7
    aRectangle = Rectangle(Point(70,525), Point(70+space,525-height1))#Draw the first rectangle of histogram
    aRectangle.setFill("palegreen")
    aRectangle.draw(win)

    aText = Text(Point(115,540),"Progress")#Show the name of the above rectangle
    aText.setFace("arial")
    aText.setSize(14)
    aText.setStyle("bold")
    aText.setTextColor("slategrey") 
    aText.draw(win)
    aText1 = Text(Point(115,515-height1),Progress_count)#Show the number of count of the above rectangle
    aText1.setFace("arial")
    aText1.setSize(16)
    aText1.setStyle("bold")
    aText1.setTextColor("slategrey")
    aText1.draw(win)

    height2 = (Trailer_count*100)/6.7
    bRectangle = Rectangle(Point(160+bar_space,525), Point(180+space,525-height2))#Draw the second rectangle of histogram
    bRectangle.setFill("darkseagreen")
    bRectangle.draw(win)

    bText = Text(Point(225,540),"Trailer")#Show the name of the above rectangle
    bText.setFace("arial")
    bText.setSize(14)
    bText.setStyle("bold")
    bText.setTextColor("slategrey")
    bText.draw(win)
    bText1 = Text(Point(225,515-height2),Trailer_count)#Show the number of count of the above rectangle
    bText1.setFace("arial")
    bText1.setSize(16)
    bText1.setStyle("bold")
    bText1.setTextColor("slategrey")
    bText1.draw(win)

    height3 = (Retriever_count*100)/6.7
    cRectangle = Rectangle(Point(270+bar_space,525), Point(290+space,525-height3))#Draw the third rectangle of histogram 
    cRectangle.setFill("darkolivegreen3")
    cRectangle.draw(win)

    cText = Text(Point(336,540),"Retriever")#Show the name of the above rectangle
    cText.setFace("arial")
    cText.setSize(14)
    cText.setStyle("bold")
    cText.setTextColor("slategrey")
    cText.draw(win)
    cText1 = Text(Point(336,515-height3),Retriever_count)#Show the number of count of the above rectangle
    cText1.setFace("arial")
    cText1.setSize(16)
    cText1.setStyle("bold")
    cText1.setTextColor("slategrey")
    cText1.draw(win)

    height4 = (Excluded_count*100)/6.7
    dRectangle = Rectangle(Point(380+bar_space,525), Point(400+space,525-height4))#Draw the fourth rectangle of histogram
    dRectangle.setFill("mistyrose2")
    dRectangle.draw(win)

    dText = Text(Point(445,540),"Excluded")#Show the name of the above rectangle
    dText.setFace("arial")
    dText.setSize(14)
    dText.setStyle("bold")
    dText.setTextColor("slategrey")
    dText.draw(win)
    dText1 = Text(Point(445,515-height4),Excluded_count)#Show the number of count of the above rectangle
    dText1.setFace("arial")
    dText1.setSize(16)
    dText1.setStyle("bold")
    dText1.setTextColor("slategrey")
    dText1.draw(win)

    total_count = Progress_count + Trailer_count + Retriever_count + Excluded_count
    eText = Text(Point(82,580),total_count)#Show the number of total count
    eText.setFace("arial")
    eText.setSize(20)
    eText.setStyle("bold")
    eText.setTextColor("slategrey")
    eText.draw(win)
    fText = Text(Point(220,580),"outcomes in total.")
    fText.setFace("arial")
    fText.setSize(20)
    fText.setStyle("bold")
    fText.setTextColor("slategrey")
    fText.draw(win)

while True:
    decision1 = input("\nAre you a student or a staff?\nPlease enter 's' for student or 't' for staff: ")#Select the user type
    if decision1 not in User:
        print("Please select the correct User")
        continue
    else:
        break
while True:    
    try:
        Pass = int(input("\nEnter your credits at pass: "))#Input the pass credits
        if Pass not in Credits:
            print("Out of range")
            continue
        else:
            while True:
                Defer = int(input("Enter your credits at defer: "))#Input the defer credits
                if Defer not in Credits:
                    print("Out of range")
                    continue
                else:
                    break
            while True:
                Fail = int(input("Enter your credits at fail: "))#Input the fail credits
                if Fail not in Credits:
                    print("Out of range")
                    continue
                else:
                    break
            if Pass + Defer + Fail != 120:#Check total count
                print("Total incorrect")
                continue
            else:
                if Pass == 120:
                    print("Progress")
                    outcome = "Progress"
                    Progress_count += 1#Calculate progress count
                elif Pass == 100:
                    print("Progress(module trailer)")
                    outcome = "Progress(module trailer)"
                    Trailer_count += 1#Calculate trailer count
                elif Fail >= 80:
                    print("Exclude")
                    outcome = "Exclude"
                    Excluded_count += 1#Calculate excluded count
                else:
                    print("Do not progress-module retriever")
                    outcome = "Do not progress-module retriever"
                    Retriever_count += 1#Calculate retriever count
            Values.append([outcome, Pass, Defer, Fail])#append outputs to the list

            f = open("Values.txt", "w")#Make the text file
            for d in Values:
                f.write(f"{d[0]} - {d[1]},{d[2]},{d[3]}\n")
        if decision1 == 's':
            break
        else:
            while True:
                decision2 = input("\nWould you like to enter more sets of Credits?\nEnter 'y' for yes or 'q' to quit and view results: ")#Select continue the program or exit the program 
                if decision2 not in Option:
                    print("Please select the correct option")
                    continue
                else:
                    break
            if decision2 == 'y':
                continue
            else:
                histogram()

                print("\n----------Part2_List----------")
                for i in Values:#Make the list
                    print(f"{i[0]} - {i[1]},{i[2]},{i[3]}")

                print("\n----------Part3_Text File----------")
                f = open("Values.txt", "r")#Make the text file
                document = f.read()
                print(document)
                f.close()
                break
    except ValueError:
        print("Integer required")







    
    
    
        


        





                                
    
        
        
            
            
                
                   
                    
                        
                
                    
                    
                        
                        
                                
                                
                                    
                                
                                    

    
   
       
            

        


              
    
