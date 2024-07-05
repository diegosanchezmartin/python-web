import reflex as rx
from python_web.styles.styles import Size as Size

def info_text(title:str, body: str) -> rx.Component:
    return rx.box(
        rx.span(
            title,
            font_weight="bold",
            color="blue"
        ),
        body,
        font_size = Size.MEDIUM.value,
    )