import pandas as pd

def extract_title(name):
    fragments = name.split(".")
    title = fragments[0]
    return title


