import reflex as rx
import datetime
from python_web.styles.styles import Size as Size

def footer() -> rx.Component:
    current_year = datetime.datetime.now().year
    return rx.vstack(
        rx.image(
            src="faviconDSM.png"
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
            margin_top="0px !important",
        ),
        margin_bottom = Size.BIG.value,
    )