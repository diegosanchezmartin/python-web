import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="Diego Sánchez Martín", size="6")
    )
