from flask import Flask, render_template
app = Flask(__name__)

# Dùng template
@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
   height = height*0.01
   BMI = (weight/(height*height))
   return render_template("BMI.html", BMI=BMI)

# K dùng template
@app.route("/bmi2/<int:weight>/<int:height>")
def bmi2(weight,height):
   height = height*0.01
   bmi2 = (weight/(height*height))
   print ("My BMI: ",bmi2)
   if bmi2<16:
      p= "Severly underweight"
   elif 16<=bmi2<18.5:
      p = "Underweight"
   elif 18.5<=bmi2<25:
      p = "Normal"
   elif 25<=bmi2<30:
      p = "Overwieght"
   else: p = "Obese"  
   return "Your BMI: " + str(bmi2) +" "+ p    

if __name__ == '__main__':
  app.run(debug=True)
 