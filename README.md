# Daily Expenses Tracker

A simple desktop application built with Python and Tkinter to help you log and manage your daily expenses.


## What It Does

* **Track Spending:** Easily add, view, edit, or delete any expense record (Item Name, Price, Date).
* **Local Storage:** All your data is saved locally on your computer in a file called `myexpenses.db`.
* **Balance Check:** Instantly calculates your total spending and remaining balance against a hardcoded budget (currently set at **1500**).
* **Simple Interface:** Uses the standard Python Tkinter library.

---

## How to Use the Application (End-User)

If you have the compiled application files, using the app is very simple.

### Required Files

The application needs **both** of these files to function:

1.  `ExpensesApp.exe` (The main program executable)
2.  `myexpenses.db` (The data file where all your expenses are saved)

### Instructions

1.  Place the two files (`.exe` and `.db`) in the same location (e.g., a dedicated folder on your Desktop).

> **⚠️ IMPORTANT NOTE ON DATA**
> The `myexpenses.db` file is your database. It is **required** to run the program and contains ALL your saved expense history. If you delete or move this file, the application will lose all your data.

---

| File/Directory | Role |
| :--- | :--- |
| `main.py` | Contains the Tkinter GUI setup and all application logic. |
| `mydb.py` | The custom class for handling all SQLite database connections and operations (CRUD). |
| `.gitignore` | Ensures that private user data (`*.db`) and generated build files (`dist/`, `build/`) are kept off the repository. |

