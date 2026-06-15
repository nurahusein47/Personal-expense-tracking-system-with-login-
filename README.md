
Personal Expense Tracker System (with Login System)

A simple command-line personal expense tracker built in Python with a login system, allowing users to securely add, view, and analyze their daily expenses.

Introduction

In this project, I developed a Personal Expense Tracker System using Python. The system allows users to log in first and then manage their daily expenses. After successful login, the user can add, view, and analyze their spending in a simple and organized way.

Objectives

The main objective of this project is to help users track their daily expenses in an easy way while also applying basic programming concepts such as loops, conditions, and lists. I also wanted to combine a simple login system with data management.

Features

· Login system with username and password
· Limited login attempts (3 tries)
· Add new expenses with amount and category
· View all saved expenses
· Calculate total spending
· Show category-wise summary
· Find the highest expense
· Simple menu-driven system

Tech Stack

· Python 3.x
· Command-line interface

Installation

1. Make sure Python 3 is installed on your system.
2. Save the main code file as expense_tracker.py.
3. Run the script:
  
   python expense_tracker.py
   
Usage

1. Launch the program.
2. Enter your username and password (default: admin / 1234).
3. After successful login, use the menu to:
   · Add expenses (name + amount)
   · View all recorded expenses
   · See total spending
   · Exit the program

Sample Output

== PERSONAL EXPENSE TRACKER SYSTEM ==
Enter Username: admin
Enter Password: 1234
Login Successful!

--- MENU ---
1. Add Expense
2. View Expenses
3. Show Total Expense
4. Exit
Enter your choice: 1
Enter expense name: Food
Enter amount: 100
Expense added successfully!

Enter your choice: 2
1. Food - 100.00

Enter your choice: 3
Total Expenses: 100.00 $

Enter your choice: 4
Food : 100

Highest Expense: Food - 100
Concepts Used

· Variables
· Lists and dictionaries
· Conditional statements (if/else)
· Loops (while, for)
· Input handling
· Basic logic building

Algorithm

1. Start the program
2. Ask the user to log in
3. Check username and password
4. Allow 3 login attempts
5. If login is correct, open the main menu
6. If login fails, stop the program
7. Show menu options
8. Perform selected operation
9. Repeat until user exits

What I Learned

From this project, I learned how to build a complete Python program that includes login security and data management. I improved my understanding of lists, dictionaries, loops, and conditions. I also learned how to organize a program into different features and make it interactive for users.

Future Improvements

In the future, I would like to improve this project by:

· Adding a database so that data is saved permanently
· Supporting multiple users
· Adding charts for better visualization
· Converting this project into a graphical user interface (GUI) application
· Adding date tracking and export options like PDF or Excel

Conclusion

In conclusion, this project helped me understand how to combine different programming concepts into one working system. I learned how to build a login system and manage data effectively. This project increased my confidence in programming and helped me think in a more structured way when solving problems.

Acknowledgments

· Inspired by daily personal finance management needs.
· Thanks to basic Python tutorials and practice projects that helped shape this system.


 the Author

Nura Husein
Student / Beginner Python Developer

This project was developed as part of a learning exercise to strengthen programming fundamentals. Passionate about building small, useful tools and gradually moving into real-world applications.

· GitHub: nurahusein47(https://github.com/nurahusein)
· Goal: Continue improving and building more interactive systems with databases and GUIs.
Licence
This project is for educational purposes only.

Version

v1.0 – Basic login + expense tracking with category summary and highest expense feature (command-line based)
