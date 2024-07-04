import reflex as rx
import datetime

def footer() -> rx.Component:
    current_year = datetime.datetime.now().year
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.link(
            "© 2022-" + format(current_year) + "<\\\\diegosanchezmartin> by Diego Sánchez Martín.",
            href="https://www.google.es",
            is_external=True),
        rx.text("From El Bierzo to the World, with ♥.")
    )