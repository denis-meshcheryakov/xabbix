"""
Функция принимает со страницы роутера команду и флаг command_type.
Передает на обработку функции send_command_to_router.py
Выводит результат обработки на страницу роутера.
"""

from flask import flash

from webapp.forms import GetCommand
from webapp.send_command_to_router import send_command


def send_received_cmd(device):
    command_form = GetCommand()
    if command_form.validate_on_submit():
        command_type = command_form.command_type.data
        get_command = command_form.command.data
        if command_type is True:
            get_command = get_command.split("*")
        output = send_command(device=device, command=get_command,
                              command_type=command_type)
        output = output.split('\n')
        for i in output:
            flash(i)
    return command_form
