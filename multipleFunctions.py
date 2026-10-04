class multiFunc:
   def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
       
   def OddEven():
       addEvenNumber = int(input("Enter a number:"))
       if addEvenNumber%2 ==0:
           print(addEvenNumber,"is Even number")
       else:
           print(addEvenNumber,"is add number")

   def elegibilityMarriage():
    gender = input("Your Gender:")
    marriageAge = int(input("Your Age:"))
    
    if gender =="Male" and marriageAge >=21 :
       print ("ELIGIBLE")
    elif gender =="Female" and marriageAge >=18 :
       print ("ELIGIBLE")
    else:
       print ("Not ELIGIBLE")  

   def calculateMark():
    Subject1= 98
    Subject2= 87
    Subject3= 95
    Subject4= 95
    Subject5= 93 
    Total = Subject1+Subject2+Subject3+Subject4+Subject5
    Percentage = Total/5
    print("Subject1=",Subject1)
    print("Subject2=",Subject2)
    print("Subject3=",Subject3)
    print("Subject4=",Subject4)
    print("Subject5=",Subject5)
    print("Total:",Total)
    print("Percentage:",Percentage)    
    
    