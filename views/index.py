import flet as ft


def build_index(page: ft.Page):
    content = ft.Column(
        [
            ft.Row(
                [ft.Text("Welcome to my Flet Router Tutorial", size=50)],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ]
    )
    return content
