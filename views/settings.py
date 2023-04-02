import flet as ft


def build_settings(page: ft.Page):
    # Local event handlers
    def toggle_dark_mode(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        page.update()

    def exit_app(e):
        page.window_destroy()

    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Text("My Settings", size=30),
                    ft.IconButton(icon=ft.icons.SETTINGS_ROUNDED, icon_size=30),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.TextButton(
                        "Light/Dark Mode",
                        icon=ft.icons.WB_SUNNY_OUTLINED,
                        on_click=toggle_dark_mode,
                    )
                ],
            ),
        ]
    )

    return content
