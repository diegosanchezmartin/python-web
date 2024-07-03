import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="DSM", size="6"),
        rx.text("@diegosanchezmartin"),
        rx.text("Buenas! 👋🏽 Me llamo Diego Sánchez Martín"),
        rx.text("""Soy ingeniero de software con una maestría en inteligencia artificial.
                Actualmente trabajo como QA Engineer en multiples aplicaciones: 
                Aplicaciones de escritorio, desarrollo web, firmware y plataformas móviles.
                Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@! """)
    )
