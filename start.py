import os
import threading
import webbrowser
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def get_password_file_path():
    tools_folder = "/home/user/Tools/project/Password Search/password"
    return os.path.join(tools_folder, "password.txt")

def get_new_file_path():
    tools_folder = "/home/user/Tools/project/Password Search/password"
    return os.path.join(tools_folder, "new.txt")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_password", methods=["POST"])
def check_password():
    try:
        data = request.get_json()
        password = data.get("password")

        if password:
            password_file_path = get_password_file_path()

            if not os.path.exists(password_file_path):
                return jsonify({"message": "Password file not found.", "found": False})

            with open(password_file_path, "r") as file:
                passwords = file.read().splitlines()

            if password in passwords:
                return jsonify({"message": "Password found!", "found": True})
            else:
                new_file_path = get_new_file_path()

                with open(new_file_path, "a") as new_file:
                    new_file.write(password + "\n")

                return jsonify({"message": "Password not found, but added to new.txt.", "found": False})

        return jsonify({"message": "Please enter a password.", "found": False})

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}", "found": False})

def open_browser():
    webbrowser.open("http://127.0.0.1:5005/")

def start_app():
    threading.Timer(1, open_browser).start()
    app.run(debug=True, host="0.0.0.0", port=5005)

if __name__ == "__main__":
    start_app()
