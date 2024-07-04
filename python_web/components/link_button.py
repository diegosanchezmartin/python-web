import reflex as rx

def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_right",
                    size=10,
                ),
                rx.vstack(
                    rx.text(text),
                    rx.text(text),
                ),
            ),
            width="100%"
        ),
        href=url,
        is_external=True,
        width="100%"
    )