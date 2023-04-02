import flet as ft

from views.router import Router
from components.app_bar import NavBar


def main(page: ft.Page):
    page.theme_mode = "dark"
    page.appbar = NavBar(page)
    router = Router(page)
    page.on_route_change = router.route_change
    page.add(router.body)
    # Go to index page
    page.go("/")


ft.app(target=main, assets_dir="assets", port=8000, view=ft.WEB_BROWSER)
