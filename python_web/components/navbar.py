import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size
from python_web.styles.colors import Color as Color
from python_web.styles.colors import TextColor as TextColor

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.chakra.span(
                "</diegosanchezmartin>",
                color = TextColor.HEADER.value,
                font_size = Size.LARGE.value,
            ),
        ),
        position ="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0",
        style=styles.navbar_title_style,
    )