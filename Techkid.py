from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/school")
def school():
    return redirect("http://techkids.vn ")

if __name__ == '__main__':
  app.run(debug=True)
