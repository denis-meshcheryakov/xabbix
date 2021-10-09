from flask import Flask, render_template, request, json

app = Flask(__name__)

#Делаем переход на главную страницу
@app.route('/')
def index():
    return render_template('index.html')

#Делаем переход на страницу авторизации
@app.route('/logIn')
def showLogin():
    return render_template('login.html')

#Делаем переход на страницу мониторинга
@app.route('/monitoring')
def showMonitoring():
    return render_template('monitoring.html')

if __name__=="__main__":
    app.run()
