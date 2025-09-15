import json 
class Registration_Page:
    def __init__(self):
        self.name=''
        self.rollno=''
        self.yourclass=''
        self.school=''
    def display(self):
        print('----Student Details----')
        self.name=input('Your Name= ')
        self.rollno=input('Your Roll-no.= ')
        self.yourclass=input('Your class= ')
        self.school=input('School Name= ')
        
        # check if details are empty
        while (self.name == '' or self.rollno == '' or self.yourclass == '' or self.school == ''):
            print('Error! Please Enter your details')
            self.name = input('Your Name= ')
            self.rollno = input('Your Roll-no.= ')
            self.yourclass = input('Your class= ')
            self.school = input('School Name= ')
            # error1 is that i used while loop for run the test condition as i used everywhere but in oops we have to define each n every thing..
        print('Submitting_Details...') #error 2 indentation that this print and return are not under while loop
            
        return Question_Page(self.name,self.rollno,self.yourclass,self.school)
        
class Question_Page:
    def __init__(self,name,rollno,yourclass,school):
        self.name= name
        self.rollno= rollno
        self.yourclass= yourclass
        self.school= school
        
    def display(self):
        print('----Exam Page----')
        print('___________________')
        print('Note: All Questions are compulsory')
        print('Also! You can choose option only once and can not go back')
        print('Choose option between 1-4')
        
        score=0           #error 3 i used sum here but its a variable in python
        print('Q1. What is the capital of India ?')
        print('1.Chandigarh\n 2.Lakshadweep\n 3.Delhi\n 4.Lucknow\n')
        answer = int(input('Enter your option no.(digit)= \n'))
        if answer<=0 or answer>4:
         print('Error!Please choose next option correctly between 1-4') 
        if answer==3:
           score=score+1
         
        print('Q2. Who discovered 0 ?')
        print('1.Ramanujan\n 2.Aryabhatta\n 3.Kalpana chawla\n 4.Swami Dayanand\n')
        answer = int(input('Enter your option no.(digit)= \n'))
        if answer<=0 or answer>4:
         print('Error!Please choose next option correctly between 1-4') 
        if answer==2:
           score=score+1
             
        print('Q3. Who is the first person landed on moon ?')
        print('1.Rakesh Kumar\n 2.Swami Vivekanand\n 3.Kalpana chawla\n 4.Neil Armstrong\n')
        answer = int(input('Enter your option no.(digit)= \n'))
        if answer<=0 or answer>4:
         print('Error!Please choose next option correctly between 1-4') 
        if answer==4:
           score=score+1
           
        print('Q4. What is 7*7+7/7-7 ?')
        print('1.43\n 2.1\n 3.56\n 4.7\n')
        answer = int(input('Enter your option no.(digit)= \n'))
        if answer<=0 or answer>4:
         print('Error!You did not choose between 1-4') 
        if answer==1:
            score=score+1
            percentage = score/4*100
             
        print('----Calculating Your Result----')
        print('You have scored= ', score)
        print('Your Percentage= ', percentage)
        if percentage<=25.0:
            print('Fail')
        elif  percentage>25 and percentage<=50:
            print('Keep Better')
        elif percentage>50 and percentage<=75:
            print('Average')
        else:
            print('Outstanding Performance')
            
        
        # ✅ Save data to JSON file
        student_data = {
            "name": self.name,
            "rollno": self.rollno,
            "class": self.yourclass,
            "school": self.school,
            "score": score,
            "percentage": percentage       #it saves students data as a dictionary in curly braces as use here 
        }

        try:
            with open("results.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []           #Try to open results.json and load old data.If file doesn’t exist (first run), start with an empty list.

        data.append(student_data)  #Adds the current student’s result to the list.

        with open("results.json", "w") as f: 
             json.dump(data, f, indent=4)   #Save all results back into the file in neat format.

        print("YOUR ANSWERS ARE RECORDED")
         
if __name__=='__main__':        #We use it to control what runs when a file is executed directly vs. when it is imported. This ensures your exam starts only when you run your file directly.
    details_page = Registration_Page()    #Creates an object of your first page (Registration_Page).At this point, only the object exists, nothing is printed.
    exam_page = details_page.display()    #Calls the display() method of Registration_Page.
    exam_page.display()                   #Calls the display() method of the Question_Page object.
         
         # We use it by "JSON" to use it import JSON and then student_data as we want to save it and using try as shown using comments