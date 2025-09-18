import json 
import time 
# TEACHER
def teacher_menu(questions):
    
    teacher = input('Enter your name with your title (Mr./Ms.) : ')
    password = '2022'   # or anything you want to do 
    entered = input('Enter Teacher_Menu Password: ')

    if entered != password:
        print('Access Denied! Wrong password.\n')
        return   # direct you to the main menu
    
    while True:
      print('--------Welcome--------')
      print('-----Teacher-Menu-----')
      print('Select what you want to do:-')
      
      print('1. Add Questions')
      print('2. View Questions')
      print('3. View Student Results')
      print('4. LogOut')
      choice = input('Enter your choice no.: ')
      
      if choice == '1':
          text = input("Enter question: ")
          options = []
          i = 1
          while i <= 4:
            options.append(input(f"Option {i}: ")) # append adds the option and f"Options is an formatted string which inserts options directly in a string.
            i += 1
          correct = int(input("Correct option (1-4): "))
          questions.append({"text": text, "options": options, "correct": correct}) # it is use as a dict. to store multiple data 
          print("# Question added successfully #")
          
           # Save questions to JSON
          with open("questions.json", "w") as file:   #dump the questions in json to save it ..
                json.dump(questions, file, indent=4)
          
      elif choice == '2':
          if not questions:
              print('NO questions are added yet.\n Please first add the questions!\n')
          else:
              for question in questions:
                  print('Question:', question['text'])   # print the question by calling the text in 1 choice 
                  print('1', question["options"][0])    # we use comma here to add space between no. and options 
                  print('2', question["options"][1])    # [] as it calling from text so it auto fills 
                  print('3', question["options"][2])    # calling option according to their index 
                  print('4', question["options"][3])
                  
                  correct_index = question['correct'] - 1   # call correct answer acc. to it's index no. 
                  print('Answer:', question['options'][correct_index])   
                  
      elif choice == '3':
            # View student results
            try:
                with open("results.json", "r") as file:
                    results = json.load(file)
                    if not results:
                        print("No student results found.")
                    else:
                        print("\n----Student Results----")
                        for res in results:
                            print(f"Name: {res['Name']}, Roll No: {res['Roll_No']}, Class: {res['Class']}, School: {res['School']}, Score: {res['Score']}, Total: {res['Total']}, Percentage: {res['Percentage']}%")
                        print("-----------------------\n")
            except FileNotFoundError:
                print("No student results found.")
                
      elif choice == '4':
          print('Logging Out ...')
          print('Hope to see you again' , teacher , '!')
          break 
      else :
          print('Invalid choice ! Try Again. ')
          
# STUDENT
def student_menu(questions):
    print('----Student Details----')
    Student = input('Enter Your Name= ')   #.split() throws a list separated by commas 
    Roll_No = input('Your Roll-no.= ')
    Class = input('Your class= ')
    School = input('School Name= ')
    print('Submitting your details...')
    print('Redirecting you to next page')
    print('Loading...')
    print('___________________')
    print('----Exam Page----')
    print('___________________')
    if not questions:
        print('NO questions available.\n Please contact your administrator.\n')  
        return 
    while True:
        print('Select what you want to do :')
        print('1. Start your quiz')
        print('2. Logout')
        choice = input('Enter your choice no.: ')
        
        if choice == '1':
            score = 0
            total = len(questions)     # as we don't know how many ques. are there 
            print('Note: All Questions are compulsory')
            for i in range(total):
                print('Question', i+1, ':', questions[i]['text']) #the for loops runs acc to calling function and their index in order.
                print('1', questions[i]['options'][0])
                print('2', questions[i]['options'][1])
                print('3', questions[i]['options'][2])
                print('4', questions[i]['options'][3])
                
                while True:
                    answer = input('Enter your answer (1-4): ')
                    if answer in ['1','2','3','4']:
                        answer = int(answer)
                        break
                    else:
                        print('Invalid answer! Enter (1, 2, 3, or 4) options only.\n')
                
                if answer == questions[i]['correct']:    
                    score += 1
            
                        
            percentage = (score / total) * 100
            print('Submitting your test...')
            time.sleep(2)
            print('Calculating your result: ')
            time.sleep(1)
            print('You Score:' ,score, '/' , total)
            print('Total Score:' ,total)
            print('Percentage:', round(percentage, 2), '%') # it will accept percentage upto 2 decimal places. 
            
              # Save student result to JSON 
            try:
                with open("results.json", "r") as file:
                    results = json.load(file)
            except FileNotFoundError:
                results = []

            results.append({
                "Name": Student,
                "Roll_No": Roll_No,
                "Class": Class,
                "School": School,
                "Score": score,
                "Total": total,
                "Percentage": round(percentage, 2)
            })

            with open("results.json", "w") as file:
                json.dump(results, file, indent=4)

            print('Your result has been saved!\n')
            
        elif choice == '2':
           print('Logging out...')
           break
        else:
            print('Invalid choice! Try again...')
            
            
# for  loading questions     
def load_questions():
    try:
        with open("questions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
    
          
# MAIN PROGRAM     
def main():
    print('!!--------------------Welcome-------------------!!')
    print('-----Student Question Paper Management System-----')

    questions = load_questions()   # shared list of questions  ###chatgpt as my previous ques. are not saved when i restart my program

    while True:
        print('1. Teacher')
        print('2. Student')
        print('3. Quit')
        role = input("Select a number: ")   # keep as string for comparison

        if role == '1':
            teacher_menu(questions)
        elif role == '2':
            student_menu(questions)
        elif role == '3':
            print('Thanks for visiting us\nHave a nice day')
            print('------------------------')
            break
        else:
            print("Invalid Number, try again.")
            
            
# RUN PROGRAM           
if __name__ == "__main__":      # we use this to run our main () directly from this code not to import or call from somewhere else .
    main()
          