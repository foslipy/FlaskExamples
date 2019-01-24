from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/value/<name>')
def value(name):
   return 'Welcome without HTTP Method %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('value',name = user))
   else:
      user = request.args.get('name') 
'''args is dictionary object containing a list of pairs of form parameter and its corresponding value'''
      return redirect(url_for('value',name = user))

if __name__ == '__main__':
   app.run(debug = True)
