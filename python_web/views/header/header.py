import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Diego Sánchez Martín", size="xl")
    )
