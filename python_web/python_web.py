import reflex as rx
from python_web.components.navbar import navbar
from python_web.views.header.header import header
from python_web.views.links.links import links
from python_web.components.footer import footer
import python_web.styles.styles as styles
from python_web.styles.styles import Size as Size


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_top = Size.BIG.value,
                margin_bottom=Size.ZERO.value,
                padding=Size.BIG.value
            ),
            margin_bottom=Size.ZERO.value,
        ),
        footer()
    )

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=[
        "/fonts/ArgentCF-Regular.css",
        "/fonts/Montserrat.css",
        "/fonts/Montserrat-Bold.css",
    ],
)
app.add_page(
    index,
    title="DiegoSanchezMartin",
    description="Soy ingeniero de software con una maestría en inteligencia artificial. Actualmente trabajo como QA Engineer en multiples aplicaciones: Aplicaciones de escritorio, desarrollo web, firmware y plataformas móviles. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!"
)