import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.text("© 2022-2024 <\\\\diegosanchezmartin> by Diego Sánchez Martín. From El Bierzo to the World, with ♥.")
    )