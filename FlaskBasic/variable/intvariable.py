from flask import Flask
app = Flask(__name__)

@app.route('/hi/<int:no>')
def hello_name(no):
   return 'Roll Number is  %d!' % no

if __name__ == '__main__':
   app.run(debug = True)
