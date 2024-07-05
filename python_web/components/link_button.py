import reflex as rx
import python_web.styles.styles as styles

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.vstack(
                    rx.spacer(),
                    rx.icon(
                        tag="arrow_right",
                        width=styles.Size.LARGE.value,
                        height=styles.Size.LARGE.value,
                    ),
                    rx.spacer(),
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing="1"
                ),
            ),
        ),
        href=url,
        is_external=True,
        width="100%",
        text_decoration="none"
    )