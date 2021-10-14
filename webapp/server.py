from flask import Flask, render_template, request, json

app = Flask(__name__)

#Делаем переход на главную страницу
@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html')

#Делаем переход на страницу авторизации
@app.route('/logIn')
def showLogin():
    title = 'Login'
    return render_template('login.html', page_title=title)

#Делаем переход на страницу мониторинга
@app.route('/monitoring')
def showMonitoring():
    title = 'Monitoring'
    return render_template('monitoring.html', page_title=title)

if __name__=="__main__":
    app.run(debug=True)
