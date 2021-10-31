from webapp.send_received_cmd_form import send_received_cmd
from flask import current_app as app
from flask import render_template
import yaml

with open("devices.yaml") as f:
    devices = yaml.safe_load(f)


# Делаем переход на главную страницу
@app.route('/')
def index():
    return render_template('index.html')


# Делаем переход на страницу авторизации
@app.route('/logIn')
def showLogin():
    title = 'Login'
    return render_template('login.html', page_title=title)


# Делаем переход на страницу мониторинга
@app.route('/monitoring')
def showMonitoring():
    title = 'Monitoring'
    return app.redirect('/dash_app', page_title=title)


# Страница роутера R1
@app.route('/r1', methods=["POST", "GET"])
def r1():
    title = 'R1 model: Cisco 7201'
    device = devices[0]
    command_form = send_received_cmd(device)
    return render_template('r1.html', page_title=title, form=command_form)


# Страница роутера R2
@app.route('/r2', methods=["POST", "GET"])
def r2():
    title = 'R2 model: Cisco 2901'
    device = devices[1]
    command_form = send_received_cmd(device)
    return render_template('r2.html', page_title=title, form=command_form)


# Страница роутера R3
@app.route('/r3', methods=["POST", "GET"])
def r3():
    title = 'R3 model: Cisco 881'
    device = devices[2]
    command_form = send_received_cmd(device)
    return render_template('r3.html', page_title=title, form=command_form)


if __name__ == "__main__":
    app.run(debug=True)
