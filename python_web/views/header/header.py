import reflex as rx
from python_web.components.link_icon import link_icon
from python_web.components.info_text import info_text
from python_web.styles.styles import Size as Size
from python_web.styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="DSM", size="7"),
            rx.vstack(
                rx.heading(
                    "Diego Sánchez Martín", 
                    size = "5",
                    margin_bottom = Size.ZERO.value,
                    color = TextColor.HEADER.value,
                ),
                rx.text(
                    "@diegosanchezmartin",
                    margin_top = Size.ZERO.value,
                    margin_bottom = "5px !important",
                    color = TextColor.BODY.value,
                ),
                rx.hstack(
                    link_icon("https://www.x.com/diegosnchzmrtn"),
                    link_icon("https://www.instagram.com/diegosnchezmartin"),
                    link_icon("https://www.facebook.com/diegosnchezmartin/"),
                    link_icon("https://www.tiktok.com/@diegosnchezmartin?_t=8nlNPDxoOtk&_r=1"),
                    link_icon("https://open.spotify.com/user/1162596043?si=475d0776b71a4f81"),
                ),
                spacing="0",
                justify="center"
            ),
            align_items="center",
            spacing="4",
        ),
        rx.flex(
            info_text("2+", "años de experencia"),
            rx.spacer(),
            info_text("10K+", "componentes automatizados"),
            rx.spacer(),
            info_text("100+", "aplicaciones creadas"),
            width="100%"
        ),
        rx.text(
            f"""
            Soy ingeniero de software con una maestría en inteligencia artificial.
            Actualmente trabajo como QA Engineer en multiples aplicaciones: 
            Aplicaciones de escritorio, desarrollo web, firmware y plataformas móviles.
            Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
            """,
            color = TextColor.BODY.value,
        ),
        align_items="start",
        spacing="5",
    )
