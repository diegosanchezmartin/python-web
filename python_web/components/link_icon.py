import reflex as rx
import python_web.styles.styles as styles

def link_icon(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=styles.Size.DEFAULT.value,
            height=styles.Size.DEFAULT.value,
        ),
        href=url,
        is_external=True,
    )