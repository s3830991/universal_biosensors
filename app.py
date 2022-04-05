from flask import Flask
import MongodbConnect

app = Flask(__name__)


# input csv file's data into MongoDB
@app.route('/inputile')
def hello_world():  # put application's code here
    MongodbConnect.input_csv()


if __name__ == '__main__':
    app.run()
