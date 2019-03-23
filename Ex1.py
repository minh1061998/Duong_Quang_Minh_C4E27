from flask import Flask, render_template
app = Flask(__name__)

@app.route("/about-me")
def aboutme():
    aboutme = {
        "Name": "Dương Quang Minh",
        "Work": "Sinh viên",
        "School": "MTA",
        "Hobbies": "Ăn, Ngủ"
    }
    return render_template("aboutme.html", aboutme = aboutme)



if __name__ == '__main__':
  app.run(debug=True)
