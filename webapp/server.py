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

@app.route('/r1')
def r1():
    title = 'R1 model: Cisco 7201'
    return render_template('r1.html', page_title=title)

@app.route('/r2')
def r2():
    title = 'R2 model: Cisco 2901'
    return render_template('r2.html', page_title=title)

@app.route('/r3')
def r3():
    title = 'R3 model: Cisco 881'
    return render_template('r3.html', page_title=title)

if __name__=="__main__":
    app.run(debug=True)
