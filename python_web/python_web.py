import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.hstack(
        rx.text(
            "diegosanchezmartin",
            height="40px"
        ),
        position ="sticky",
        bg="blue",
        padding="16px"
    )

app = rx.App()
app.add_page(index)