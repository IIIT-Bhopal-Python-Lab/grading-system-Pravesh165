while(True): # this while loop is for infinite iterations
    marks = input("Enter your Marks: ") # marks variable is been given input
    
    if(marks=="EXIT"): # when I input EXIT then program should exit
        print("Exit the program")
        break
    
    try: # if I give any input then try should execute but if some error occurs then except should run
        marks = int(marks)

        if(marks>=0 and marks<40): print("F") # if marks is greater than or equal to 0 and less than 40 then it should print F
        elif(marks>=40 and marks<=59): print("D") # if marks is greater than or equal to 40 and less than or equal to 59 then it should print D
        elif(marks>=60 and marks<=74): print("C") # if marks is greater than or equal to 60 and less than or equal to 74 then it should print C
        elif(marks>=75 and marks<=89): print("B") # if marks is greater than or equal to 75 and less than or equal to 89 then it should print B
        elif(marks>=90 and marks<=100): print("A") # if marks is greater than or equal to 90 and less than or equal to 100 then it should print A
        else: print("Invalid Input") # when input is numeric but not in the range bw 0 and 100
        
    except ValueError: # when input is other than digits
        print("Error....Enter number bw 0 and 100")
