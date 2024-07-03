import reflex as rx

def link_button() -> rx.Component:
    return rx.vstack(
        rx.button("LinkedIn")
    )