import reflex as rx
from python_web.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("LinkedIn","https://www.linkedin.com/in/diegosanchezmartin/"),
        link_button("GitHub","https://github.com/diegosanchezmartin"),
        link_button("Sobre mi","https://www.google.es"),
        link_button("Descargar CV", "https://www.google.es"),
        width="100%",
    )