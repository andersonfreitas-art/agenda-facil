from fasthtml.common import *
from pages import home

app, rt = fast_app(
    debug=True,
    static_path="assets",
    pico=True,
    live=True,
)

home = home.page


@rt("/")
def get():
    return home


@rt("/{name}")
def get(name: str):
    return Titled(f"Seja bem vindo {name}", "É bom te ver aqui.")


serve()
