# 📝 Student Question Paper Management System (SQPMS)

A Python-based **quiz management system** built in two versions:  

1. **Basic Version (JSON Storage + OOP)**  
   - Uses Object-Oriented Programming concepts.  
   - Stores data in local JSON files (`questions.json`, `results.json`).  

2. **Advanced Version (PostgreSQL Database)**  
   - Uses `psycopg2` to connect Python with PostgreSQL.  
   - Stores data in relational tables (`questions`, `results`).  
   - More scalable and secure for real-world use.


---

## ✨ Features

### 👨‍🏫 Teacher Menu
- 🔑 Secure login with password.
- ➕ Add multiple-choice questions (MCQs).
- 👀 View all added questions with correct answers.
- 📊 View student results (saved from completed quizzes).

### 🎓 Student Menu
- 📝 Enter student details (Name, Roll No, Class, School).
- 🧾 Attempt quiz questions (all compulsory).
- 🧮 Automatic result calculation:
  - ✅ Score
  - 📌 Total
  - 📈 Percentage
- 💾 Results stored in either:
  - `results.json` (JSON version)  
  - `results` table (PostgreSQL version)

---

## 🛠️ Technologies Used
- **Python 3**
- **OOP Concepts**  
- **JSON** for storing questions and results
- **time.sleep()** for UI effects

### PostgreSQL Version
- **Python 3**  
- **psycopg2** library for PostgreSQL connection  
- **PostgreSQL Database**  
- **pgAdmin4** for database management  

---
## 📂 Project Structure
📦 your-repo
 ┣ 📜 main.py         # Python program (PostgreSQL version)
 ┣ 📜 schema.sql      # Database schema (PostgreSQL tables)
 ┣ 📜 old_main.py     # JSON version (optional)
 ┣ 📜 questions.json  # Questions storage (JSON version)
 ┣ 📜 results.json    # Results storage (JSON version)
 ┗ 📜 README.md       # Documentation

