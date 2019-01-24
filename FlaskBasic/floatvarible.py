from flask import Flask
app = Flask(__name__)

@app.route('/hi/<float:name>')
def hello_name(name):
   return 'Hello %f!' % name

if __name__ == '__main__':
   app.run(debug = True)
