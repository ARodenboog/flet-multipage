import flet as ft


def NavBar(page):
    NavBar = ft.AppBar(
        title=ft.Text("Flet Router Example"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go("/")),
            ft.IconButton(
                ft.icons.SETTINGS_ROUNDED, on_click=lambda _: page.go("/settings")
            ),
        ],
    )

    return NavBar
