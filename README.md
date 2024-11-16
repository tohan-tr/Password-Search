Password Search is a web application that checks whether a given password exists in a database of 20 million leaked passwords and saves any missing passwords to a new file. Built with Flask, this tool provides a user-friendly interface using HTML, CSS, and JS for quick and easy usage.
Features

    Password Lookup: The entered password is searched in the password/password.txt file, and the user is notified if the password is found.
    Add New Password: If the password is not found in password.txt, it is automatically added to password/new.txt in the password folder.
    View Total Number of Passwords: By clicking on the information icon, the total number of stored passwords can be viewed.
    Copying Disabled: To increase security, right-clicking and copying actions are disabled.

Project Structure

    start.py: Python file that runs the Flask-based web application.
    password/password.txt: Main file where the stored passwords are kept.
    templates/index.html: HTML file for the user interface.

Installation

    Clone the repository:

git clone https://github.com/tohan-tr/Password-Search/tree/main

    Install required dependencies:

pip install -r requirements.txt

    Start the application:

python start.py

    Open the application by navigating to http://127.0.0.1:5005 in your browser.

Usage

    Password Lookup: Enter the password in the search bar and press "Enter" to begin the search.
    Results: If the password is found in password.txt, a "Password found!" message is displayed. If not, a "Password not found" message will appear.
    GitHub Profile: Click on the GitHub button at the top-right corner to access the project’s GitHub page.
