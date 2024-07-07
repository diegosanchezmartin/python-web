import reflex as rx
import datetime
from python_web.styles.styles import Size as Size
from python_web.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    current_year = datetime.datetime.now().year
    return rx.vstack(
        rx.image(
            src="logoDSM.png",
            width=Size.ICON.value,
            height="auto",
            margin_top=""
        ),
        rx.link(
            "© 2022-" + format(current_year) + " <\\\\diegosanchezmartin> by Diego Sánchez Martín.",
            href="https://www.google.es",
            is_external=True,
            font_size = Size.MEDIUM.value,
        ),
        rx.text(
            "From El Bierzo to the World, with ♥.",
            font_size = Size.MEDIUM.value,
            margin_top = Size.ZERO.value,
        ),
        align="center",
        margin_bottom = Size.MEDIUM.value,
        padding_bottom = Size.SMALL.value,
        color = TextColor.FOOTER.value,
    )