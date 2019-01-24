from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'Maths':80,'C':70,'java':60}
   print dict
   return render_template('result.html', result = dict, list1=list1)

@app.route('/result')
def result1():
   dict = {'Maths':80,'C':70,'java':60}
   print dict
   return render_template('result.html', result = dict, list1=list1)


if __name__ == '__main__':
   app.run(debug = True)
