from flask import Flask
app = Flask(__name__)

@app.route('/hi/<float:number>')
def hello_name(number):
   return 'Balance Amount %f!' % number

if __name__ == '__main__':
   app.run(debug = True)
