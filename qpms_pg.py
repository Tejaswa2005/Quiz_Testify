from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

# Now you can get them
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
TEACHER_PASSWORD = os.getenv('TEACHER_PASSWORD')

import psycopg2  #this connects python with postgresql
import time

#connector of postgresql
def get_connection():
    return psycopg2.connect(
        host='localhost',
        port='5432',
        database='qpmsDB',
        user='postgres',
        password=DB_PASSWORD
    )
# TEACHER
def teacher_menu():
    
    teacher = input('Enter your name with your title (Mr./Ms.) : ')
    password = TEACHER_PASSWORD
    print('Confirming your password...')
    time.sleep(1) 
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
      time.sleep(1)
      
      if choice == '1':
          text = input("Enter question: ")
          options = []
          i = 1
          while i <= 4:
            options.append(input(f"Option {i}: ")) # append adds the option and f"Options is an formatted string which inserts options directly in a string.
            i += 1
          correct = int(input("Correct option (1-4): "))
          
          #connection to psql to save questions 
          conn = get_connection() #calls your connection between python and psql
          cur = conn.cursor()  #cusror object read/write data in the database
          cur.execute(       #actually runs your sql command
                'INSERT INTO questions (text, option1, option2, option3, option4, correct) VALUES (%s, %s,%s,%s,%s, %s)',
                 #%s are the used in library of psycopg2 and also cuts the strings and special characters and also safe from malicious attacks.
                 (text, options[0], options[1], options[2], options[3], correct)
            )
          conn.commit()  #save your changes to database (permanently)
          cur.close()  #closes cursor as it consumes memory otherwise
          conn.close()  #closes connection
          time.sleep(1)
          print("# Question added successfully #")
          
      elif choice == '2':
          conn = get_connection()
          cur = conn.cursor()
          cur.execute("SELECT id, text, option1, option2, option3, option4, correct FROM questions")
          questions = cur.fetchall() #this will fetch all the questions o/w only 1 ques will be fetched also fetchall works as tuple not dictionary
          cur.close()
          conn.close()
          if not questions:
              print('NO questions are added yet.\n Please first add the questions!\n')
          else:
              for q in questions:
               print('Question:', q[1])
               print('1', q[2])
               print('2', q[3])
               print('3', q[4])
               print('4', q[5])
               options = [q[2], q[3], q[4], q[5]]  # Convert options into a list from tuple 
               correct_index = q[6] - 1
               print('Answer:', options[correct_index])
      elif choice == '3':
            # View student results
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT name, roll_no, class, school, score, percentage FROM results")
            results = cur.fetchall()
            cur.close()
            conn.close()

            if not results:
                print("No student results found.")
            else:
                print("\n----Student Results----")
                for res in results:  #res lets you loop through each student record.
                    name, roll_no, student_class, school, score, percentage = res
                    print(f"Name: {name}, Roll No: {roll_no}, Class: {student_class}, School: {school}, Score: {score}, Percentage: {percentage}%")
                print("-----------------------\n")
   
                
      elif choice == '4':
          print('Logging Out ...')
          time.sleep(1)
          print('Hope to see you again' , teacher , '!')
          break 
      else :
          print('Invalid choice ! Try Again. ')
          
# STUDENT
def student_menu():
    print('----Student Details----')
    Student = input('Enter Your Name= ').strip()   #.split() throws a list separated by commas
    Roll_No = input('Your Roll-no.= ')
    Class = input('Your class= ')
    School = input('School Name= ')
    print('Submitting your details...')
    time.sleep(1)
    print('Redirecting you to next page')
    print('Loading...')
    print('___________________')
    print('----Exam Page----')
    time.sleep(1)
    print('___________________')
    # Load questions from Postgresql
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, text, option1, option2, option3, option4, correct FROM questions")
    questions = cur.fetchall()
    cur.close()
    conn.close()
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
            for i, q in enumerate(questions, start=1):
             print('Question', i, ':', q[1])
             print('1', q[2])
             print('2', q[3])
             print('3', q[4])
             print('4', q[5])
                
             while True:
                    answer = input('Enter your answer (1-4): ')
                    if answer in ['1','2','3','4']:
                        answer = int(answer)
                        break
                    else:
                        print('Invalid answer! Enter (1, 2, 3, or 4) options only.\n')
                
             if answer == q[6]:    
                 score += 1

            percentage = (score / total) * 100
            print('Submitting your test...')
            time.sleep(2)
            print('Calculating your result: ')
            time.sleep(1)
            print('You Score:' ,score, '/' , total)
            print('Total Score:' ,total)
            print('Percentage:', round(percentage, 2), '%') # it will accept percentage upto 2 decimal places. 
            
            # Save result to psql
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """ INSERT INTO results (name, roll_no, class, school, score, percentage)
                    VALUES (%s, %s, %s, %s, %s, %s) """,
                (Student, Roll_No, Class, School, score, round(percentage, 2))
            )
            conn.commit()
            cur.close()
            conn.close()

            print('Your result has been saved!\n')
            
        elif choice == '2':
           print('Logging out...')
           break
        else:
            print('Invalid choice! Try again...')
            
          
# MAIN PROGRAM     
def main():
    print('!!--------------------Welcome-------------------!!')
    print('-----Student Question Paper Management System-----')

    while True:
        print('1. Teacher')
        print('2. Student')
        print('3. Quit')
        role = input("Select a number: ")   # keep as string for comparison

        if role == '1':
            teacher_menu()
        elif role == '2':
            student_menu()
        elif role == '3':
            print('Thanks for visiting us\nHave a nice day')
            print('------------------------')
            break
        else:
            print("Invalid Number, try again.")
            
            
# RUN PROGRAM           
if __name__ == "__main__":      # we use this to run our main () directly from this code not to import or call from somewhere else .
    main()                      