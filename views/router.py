import flet as ft

# views
from views.index import build_index
from views.settings import build_settings


class Router:
    def __init__(self, page: ft.Page):
        self.routes = {
            "/": build_index(page),
            "/settings": build_settings(page)
        }
        self.body = ft.Container(content=self.routes["/"])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
