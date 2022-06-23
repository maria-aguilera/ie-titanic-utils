import pandas as pd


def extract_title(name, separator="."):
    if not separator:
        raise ValueError("Separator cannot be empty")
    fragments = name.split(separator)
    title = fragments[0]
    return title
