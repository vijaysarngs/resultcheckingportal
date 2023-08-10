import tkinter as tk
from tkinter import messagebox
import mysql.connector
global function_selection_window

def student_login():
    login_window.destroy()  # Close the login window

    data_entry_window = tk.Tk()
    data_entry_window.title("Data Entry")
    data_entry_window.geometry("300x300")
    data_entry_window.configure(bg="lightgray")

    def check_data():
        # Retrieve user-entered data
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        age = age_entry.get()
        semester = semester_entry.get()
        year = year_entry.get()
        department = department_entry.get()

        # Check if the data is valid
        if validate_student_data(first_name, last_name, age, semester, year, department):
            data_entry_window.destroy()  # Close the data entry window
            function_selection_window = tk.Tk()
            function_selection_window.title("Function Selection")
            function_selection_window.geometry("300x200")
            function_selection_window.configure(bg="lightgray")

            # Styling the function selection window
            label = tk.Label(function_selection_window, text="Select an Operation", font=("Arial", 16), bg="lightgray")
            label.pack(pady=20)

            check_marks_button = tk.Button(function_selection_window, text="Check Marks", command=check_marks,
                                           font=("Arial", 12), bg="purple", fg="white")
            check_marks_button.pack(pady=10, padx=50, ipadx=10)

            re_evaluation_button = tk.Button(function_selection_window, text="Re-evaluation", command=re_evaluation,
                                             font=("Arial", 12), bg="orange", fg="white")
            re_evaluation_button.pack(pady=10, padx=50, ipadx=10)

            calculate_cgpa_button = tk.Button(function_selection_window, text="Calculate CGPA", command=calculate_cgpa,
                                              font=("Arial", 12), bg="green", fg="white")
            calculate_cgpa_button.pack(pady=10, padx=50, ipadx=10)

            function_selection_window.mainloop()
        else:
            messagebox.showwarning("Data Check", "The entered data is not valid. Please re-enter the data.")

    # Styling the data entry window
    label = tk.Label(data_entry_window, text="Enter Your Details", font=("Arial", 16), bg="lightgray")
    label.pack(pady=20)

    # First Name
    first_name_label = tk.Label(data_entry_window, text="First Name:", font=("Arial", 12), bg="lightgray")
    first_name_label.pack()
    first_name_entry = tk.Entry(data_entry_window, font=("Arial", 12))
    first_name_entry.pack()

    # Last Name
    last_name_label = tk.Label(data_entry_window, text="Last Name:", font=("Arial", 12), bg="lightgray")
    last_name_label.pack()
    last_name_entry = tk.Entry(data_entry_window, font=("Arial", 12))
    last_name_entry.pack()

    # Age
    age_label = tk.Label(data_entry_window, text="Age:", font=("Arial", 12), bg="lightgray")
    age_label.pack()
    age_entry = tk.Entry(data_entry_window, font=("Arial", 12))
    age_entry.pack()

    # Semester
    semester_label = tk.Label(data_entry_window, text="Current Semester:", font=("Arial", 12), bg="lightgray")
    semester_label.pack()
    semester_entry = tk.Entry(data_entry_window, font=("Arial", 12))
    semester_entry.pack()

    # Year of College
    year_label = tk.Label(data_entry_window, text="Year of College:", font=("Arial", 12), bg="lightgray")
    year_label.pack()
    year_entry = tk.Entry(data_entry_window, font=("Arial", 12))
    year_entry.pack()

    # Department
    department_label = tk.Label(data_entry_window, text="Department:", font=("Arial", 12), bg="lightgray")
    department_label.pack()
    department_entry = tk.Entry(data_entry_window, font=("Arial", 12))
    department_entry.pack()

    submit_button = tk.Button(data_entry_window, text="Submit", command=check_data, font=("Arial", 12), bg="green",
                              fg="white")
    submit_button.pack(pady=20)

    data_entry_window.mainloop()


def validate_student_data(first_name, last_name, age, semester, year, department):
    # Add your validation logic here
    # Return True if the data is valid, False otherwise
    return True


def check_marks():
    # function_selection_window.destroy()  # Close the function selection window

    marks_entry_window = tk.Tk()
    marks_entry_window.title("Check Marks")
    marks_entry_window.geometry("300x300")
    marks_entry_window.configure(bg="lightgray")

    def validate_marks_data():
        # Retrieve user-entered data
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        course_code = course_code_entry.get()
        course_name = course_name_entry.get()
        faculty_name = faculty_name_entry.get()

        # Check if the data exists in the student marks table of the database
        if check_database(first_name, last_name, course_code, course_name, faculty_name):
            mark = fetch_mark(first_name, last_name, course_code, course_name, faculty_name)
            messagebox.showinfo("Check Marks", f"The mark for {course_name} is {mark}")
        else:
            messagebox.showwarning("Data Check", "The entered data does not match. Please re-enter the data.")

    # Styling the marks entry window
    label = tk.Label(marks_entry_window, text="Enter Marks Details", font=("Arial", 16), bg="lightgray")
    label.pack(pady=20)

    # First Name
    first_name_label = tk.Label(marks_entry_window, text="First Name:", font=("Arial", 12), bg="lightgray")
    first_name_label.pack()
    first_name_entry = tk.Entry(marks_entry_window, font=("Arial", 12))
    first_name_entry.pack()

    # Last Name
    last_name_label = tk.Label(marks_entry_window, text="Last Name:", font=("Arial", 12), bg="lightgray")
    last_name_label.pack()
    last_name_entry = tk.Entry(marks_entry_window, font=("Arial", 12))
    last_name_entry.pack()

    # Course Code
    course_code_label = tk.Label(marks_entry_window, text="Course Code:", font=("Arial", 12), bg="lightgray")
    course_code_label.pack()
    course_code_entry = tk.Entry(marks_entry_window, font=("Arial", 12))
    course_code_entry.pack()

    # Course Name
    course_name_label = tk.Label(marks_entry_window, text="Course Name:", font=("Arial", 12), bg="lightgray")
    course_name_label.pack()
    course_name_entry = tk.Entry(marks_entry_window, font=("Arial", 12))
    course_name_entry.pack()

    # Faculty Name
    faculty_name_label = tk.Label(marks_entry_window, text="Faculty Name:", font=("Arial", 12), bg="lightgray")
    faculty_name_label.pack()
    faculty_name_entry = tk.Entry(marks_entry_window, font=("Arial", 12))
    faculty_name_entry.pack()

    submit_button = tk.Button(marks_entry_window, text="Submit", command=validate_marks_data, font=("Arial", 12),
                              bg="green", fg="white")
    submit_button.pack(pady=20)

    marks_entry_window.mainloop()


def check_database(first_name, last_name, course_code, course_name, faculty_name):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kutta@123",
            database="vijay"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute the SELECT query to check if the data exists in the student marks table
        query = "SELECT * FROM studentmarks WHERE first_name = %s AND last_name = %s AND course_code = %s AND course_name = %s AND faculty_name = %s"
        values = (first_name, last_name, course_code, course_name, faculty_name)
        cursor.execute(query, values)

        # Check if any rows are returned from the query
        result = cursor.fetchone()
        if result:
            return True

        # Close the cursor and connection
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)

    return False


def fetch_mark(first_name, last_name, course_code, course_name, faculty_name):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kutta@123",
            database="vijay"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute the SELECT query to fetch the mark
        query = "SELECT marks FROM studentmarks WHERE first_name = %s AND last_name = %s AND course_code = %s AND course_name = %s AND faculty_name = %s"
        values = (first_name, last_name, course_code, course_name, faculty_name)
        cursor.execute(query, values)

        # Fetch the mark
        mark = cursor.fetchone()[0]

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return mark
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)

    return None


def re_evaluation():
    messagebox.showinfo("Re-evaluation", "Re-evaluation function selected.")


def calculate_cgpa():
    cgpa_window = tk.Tk()
    cgpa_window.title("Calculate CGPA")
    cgpa_window.geometry("300x200")
    cgpa_window.configure(bg="lightgray")

    # Function to calculate CGPA
    def calculate():
        semester = semester_entry.get()
        course_codes = course_codes_entry.get().split(',')

        # Retrieve the marks from the studentmarks table
        marks = get_student_marks(semester, course_codes)

        if marks:
            total_marks = sum(marks)
            cgpa = (total_marks / 4)/10
            messagebox.showinfo("CGPA Calculation", f"Your CGPA for semester {semester} is: {cgpa:.2f}")
        else:
            messagebox.showwarning("Data Check", "No marks found for the entered data.")

    # Styling the CGPA calculation window
    label = tk.Label(cgpa_window, text="Calculate CGPA", font=("Arial", 16), bg="lightgray")
    label.pack(pady=20)

    # Semester
    semester_label = tk.Label(cgpa_window, text="Enter Semester:", font=("Arial", 12), bg="lightgray")
    semester_label.pack()
    semester_entry = tk.Entry(cgpa_window, font=("Arial", 12))
    semester_entry.pack()

    # Course Codes
    course_codes_label = tk.Label(cgpa_window, text="Enter Course Codes (comma-separated):", font=("Arial", 12),
                                  bg="lightgray")
    course_codes_label.pack()
    course_codes_entry = tk.Entry(cgpa_window, font=("Arial", 12))
    course_codes_entry.pack()

    submit_button = tk.Button(cgpa_window, text="Calculate", command=calculate, font=("Arial", 12), bg="green",
                              fg="white")
    submit_button.pack(pady=20)

    cgpa_window.mainloop()


def get_student_marks(semester, course_codes):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kutta@123",
            database="vijay"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Prepare the IN clause for course codes
        placeholders = ', '.join(['%s'] * len(course_codes))

        # Execute the SELECT query to retrieve the marks
        query = f"SELECT marks FROM studentmarks WHERE semester = %s AND course_code IN ({placeholders})"
        values = [semester] + course_codes
        cursor.execute(query, values)

        # Fetch all the rows and extract the marks
        marks = [row[0] for row in cursor.fetchall()]

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return marks

    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)

    return None

def teacher_login():
    messagebox.showinfo("you have selected the tecahers portal")
# Create the login window
login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("300x200")
login_window.configure(bg="lightgray")

# Styling the login window
label = tk.Label(login_window, text="Select Login Type", font=("Arial", 16), bg="lightgray")
label.pack(pady=20)

teacher_button = tk.Button(login_window, text="Teacher Login", command=teacher_login, font=("Arial", 12), bg="orange",
                           fg="white")
teacher_button.pack(pady=10, padx=50, ipadx=10)

student_button = tk.Button(login_window, text="Student Login", command=student_login, font=("Arial", 12), bg="blue",
                           fg="white")
student_button.pack(pady=10, padx=50, ipadx=10)

login_window.mainloop()