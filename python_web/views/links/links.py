import reflex as rx
from python_web.components.link_button import link_button
from python_web.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("¡Conecta conmigo!"),
        link_button(
            "LinkedIn", 
            "Perfil profesional de LinkedIn", 
            "https://www.linkedin.com/in/diegosanchezmartin/"
        ),
        link_button(
            "GitHub", 
            "Repositorio de proyectos en GitHub", 
            "https://github.com/diegosanchezmartin"
        ),
        title("Conoce mi historia"),
        link_button(
            "Sobre mi", 
            "Pagina web personal", 
            "https://www.google.es"
            ),
        title("Recursos disponibles"),
        link_button(
            "Descargar CV", 
            "Enlace para descargar mi CV", 
            "https://www.google.es"
        ),
        width="100%",
        spacing="2"
    )