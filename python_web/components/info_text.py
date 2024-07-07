import reflex as rx
from python_web.styles.styles import Size as Size
from python_web.styles.colors import Color as Color
from python_web.styles.colors import TextColor as TextColor

def info_text(title:str, body: str) -> rx.Component:
    return rx.box(
        rx.chakra.span(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f" {body}",
        font_size = Size.INTERMEDIATE.value,
        color = TextColor.BODY.value,
    )