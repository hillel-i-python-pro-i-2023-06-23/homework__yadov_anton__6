import requests
from flask import Flask
from app.config import FILES_INPUT_DIR
from app.user_generator import generate_users
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/get-content/')
def read_file():
    file = FILES_INPUT_DIR.joinpath('sample2.txt')
    with open(file) as f:
        content = f.read()
    return content
@app.route('/generate-users')
def show_users():
    users_formatted=[]
    for index, user in enumerate(generate_users(100)):
        string = (f'<li> Name: {user.name}: email: {user.email}</li>')
        users_formatted.append(string)
    _temp = "\n".join(users_formatted)
    return f"<ol>{_temp}</ol>"

@app.route('/space')
def response():
    url = 'http://api.open-notify.org/astros.json'
    respons = requests.get(url)
    data = respons.json()
    number=f"Total in cosmos:{data['number']}"
    return number


@app.route("/mean")
def read_csv_file():
    url = 'https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt'
    df = pd.read_csv(url)
    height = df['Height(Inches)'].mean()
    weight = df['Weight(Pounds)'].mean()
    mean = f'Mean height {height * 2.54} cm <br> Mean weight {weight * 0.453592} kg'
    return mean



if __name__ == '__main__':
    app.run()
