import reflex as rx
from python_web.components.link_button import link_button
from python_web.components.link_button_CV import link_button_CV
from python_web.components.title import title
from python_web.styles.styles import Size as Size

def links() -> rx.Component:
    return rx.vstack(
        title("¡Conecta conmigo!"),
        link_button(
            "LinkedIn", 
            "Perfil profesional de LinkedIn", 
            "icons/linkedin.svg",
            "https://www.linkedin.com/in/diegosanchezmartin/"
        ),
        link_button(
            "GitHub", 
            "Repositorio de proyectos en GitHub", 
            "icons/github.svg",
            "https://github.com/diegosanchezmartin"
        ),
        title("Conoce mi historia"),
        link_button(
            "Sobre mi", 
            "Pagina web personal", 
            "icons/hand-solid.svg",
            "http://www.diegosanchezmartin.es"
            ),
        title("Recursos disponibles"),
        link_button_CV(
            "Descargar CV", 
            "Enlace para descargar mi CV", 
            "icons/file-solid.svg",
        ),
        title("Contacto"),
        link_button(
            "Email", 
            "Contacta por correo", 
            "icons/envelope-solid.svg",
            f"mailto:sanchhez08@gmail.com"
        ),
        width="100%",
        spacing="2",
        padding_bottom = Size.SMALL.value,
    )