from fasthtml.common import *

app, rt = fast_app(
    debug=False,
    static_path="assets",
    pico=True,
    live=False,
)


@rt("/")
def get():
    page = (
        Title("Agenda Fácil"),
        Header(
            Hgroup(
                H1("Agenda Fácil 📅"),
                Nav(
                    Ul(Li(Strong("EEEP Sandra Carvalho Costa"))),
                    Ul(Li(A("Conta", cls="contrast")), Li(A("Sair", cls="contrast"))),
                ),
                Hr(),
            ),
            cls="container",
        ),
        Main(
            Section(
                Group(
                    Img(src="icon-projetor.png", width="50"),
                    Img(src="icon-projetor.png", width="50"),
                    Img(src="icon-projetor.png", width="50"),
                    Img(src="icon-projetor.png", width="50"),
                    Img(src="icon-projetor.png", width="50"),
                    Img(src="icon-projetor.png", width="50"),
                ),
                Group(
                    Img(src="icon-projetor.png", width="50"),
                    Img(src="icon-tv.png", width="50"),
                    Img(src="icon-tv.png", width="50"),
                    Img(src="icon-linguas.png", width="50"),
                    Img(src="icon-fisica.png", width="50"),
                    Img(src="icon-matematica.png", width="50"),
                ),
                Group(
                    Img(src="icon-biologia.png", width="50"),
                    Img(src="icon-quimica.png", width="50"),
                    Img(src="icon-auditorio.png", width="50"),
                    Img(src="icon-biblioteca.png", width="50"),
                    Img(src="icon-quadra.png", width="50"),
                ),
            ),
            cls="container",
        ),
        Footer(
            Hr(),
            Small("© Agenda Fácil 2024 · Por Anderson Freitas"),
            cls="container",
        ),
    )
    return page


serve()
