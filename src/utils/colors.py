DARK_BLACK = "#1e1e1e"
LIGHT_BLACK = "#2b2b2b"
ACCENT = "#FFDB58"
TEXT_LIGHT = "#FFFFFF"
DARK_GRAY = "#444"
TEXT_DARK = "lightgrey"


def hex_to_rgb(hex_color):
    """Convert hex color to RGB string like '255, 255, 0'."""
    hex_color = hex_color.lstrip("#")
    return ", ".join(str(int(hex_color[i : i + 2], 16)) for i in (0, 2, 4))


def get_conditional_color(
    value, min_val, max_val, base_hex_color, return_opacity=False
):
    """
    Given a value and its min/max range, return an rgba color string
    with opacity scaled between 0.1 and 1.0 based on the value.

    base_rgb should be a string like '255, 255, 0' for yellow.
    """
    base_rgb = hex_to_rgb(base_hex_color)

    norm = (value - min_val) / (max_val - min_val) if max_val != min_val else 1
    opacity = 0.1 + 0.9 * norm
    rgba_str = f"rgba({base_rgb}, {opacity:.2f})"
    if return_opacity:
        return rgba_str, opacity
    else:
        return rgba_str
