import reflex as rx
from python_web.components.navbar import navbar
from python_web.views.header import header
class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header()
    )

app = rx.App()
app.add_page(index)