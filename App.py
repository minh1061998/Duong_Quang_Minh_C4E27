from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello C4E27"

@app.route("/say-hi/<name>/")
def sayhi(name):
    return "Hi " + name   

@app.route("/sum/<int:a>/<int:b>")  
def sum(a,b):
    return str(a+b)

@app.route("/poem")
def poem():
    poems = [
        {
        "title":"Thơ",
        "content":"Hôm nay trăng lên cao quá",
        "author":"Huế",
        "gender":"female",
        },
        {
        "title":"Thơ 2",
        "content":"Trách bản thân hạ phàm không đúng chỗ",
        "author":"Quân",
        "gender":"male",
        }
    ]
    return render_template("poem.html",poems=poems)


if __name__ == '__main__':
  app.run(debug=True)

