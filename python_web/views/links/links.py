import reflex as rx
from python_web.components.link_button import link_button
from python_web.components.title import title
from python_web.styles.styles import Size as Size

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
        title("Contacto"),
        link_button(
            "Email", 
            "Contacta por correo", 
            f"mailto:sanchhez08@gmail.com"
        ),
        width="100%",
        spacing="2",
        padding_bottom = Size.SMALL.value,
    )