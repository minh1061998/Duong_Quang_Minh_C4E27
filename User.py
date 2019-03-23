from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    Users = {
        "minh":  {
            "name": "Dương Quang Minh",
            "age": "21",
            "gender": "male"
        },
        "duc":  {
            "name": "Phạm Minh Đức",
            "age": "21",
            "gender": "male"
        },
        "ngoc": {
            "name": "Nghiêm Huyền Ngọc",
            "age": "21",
            "gender": "female"
        }  
    }
    if username in Users:
        username = Users[username]
        return render_template("user.html",username = username)
    else:
        return "User name not found"    
   


if __name__ == '__main__':
  app.run(debug=True)
 