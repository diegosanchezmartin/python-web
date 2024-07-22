import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    ZERO = "0epx !important"
    TINY="0.2em"
    SMALL="0.5em"
    INTERMEDIATE = "0.70em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em",
    ICON="12em",

# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "size": "5",
        "color": TextColor.HEADER.value,
        "font_family": Font.DEFAULT.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
        },
        "cursor": "pointer",
        
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family = Font.LOGO.value,
)

title_style = dict(
    width="100%",
    padding_top=Size.SMALL.value,
)

button_title_style = dict(
    font_family = Font.TITLE.value,
    font_size = Size.DEFAULT.value,
    color = TextColor.HEADER.value,
)

button_body_style = dict(
    font_family = Font.DEFAULT.value,
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value,
)