import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH = "600px"

# Sizes
class Spacer(Enum):
    SMALL="0.5em"
    DEFAULT="1em"
    BIG="2em"

# Styles

BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Spacer.SMALL.value,
        "border_radius": Spacer.DEFAULT.value
    }
}