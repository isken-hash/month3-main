import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world")
    greeting_history = []
    history_text = ft.Text("История приветствий:")

    name_input = ft.TextField(label="Введите имя")

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)

        if name:
            greeting_text.value = f"Hello {name}"
            name_input.value = ""

            timestamp = datetime.now().strftime("%H:%M:%S")
            greeting_history.append(f"{timestamp} {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            print("User ничего не ввел")
            greeting_text.value = 'Пожалуйста, введите имя!'

        page.update()

  
    def on_remove_last_click(_):
        if greeting_history:
            greeting_history.pop()
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            history_text.value = "История приветствий:\n(пусто)"
        page.update()

    
    page.add(
        name_input,
        ft.ElevatedButton("send", on_click=on_button_click),
        ft.ElevatedButton("Удалить последнее", on_click=on_remove_last_click),
        greeting_text,
        history_text
    )

ft.app(target=main)
