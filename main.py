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
                    A(Img(src="icon-projetor-02.png", width="200"), href="#"),
                    A(Img(src="icon-projetor-03.png", width="200"), href="#"),
                    A(Img(src="icon-projetor-03.png", width="200"), href="#"),
                    A(Img(src="icon-projetor-05.png", width="200"), href="#"),
                    A(Img(src="icon-projetor-06.png", width="200"), href="#"),
                    A(Img(src="icon-projetor-07.png", width="200"), href="#"),
                ),
                Group(
                    A(Img(src="icon-projetor-08.png", width="200"), href="#"),
                    A(Img(src="icon-projetor-09.png", width="200"), href="#"),
                    A(Img(src="icon-tv-01.png", width="200"), href="#"),
                    A(Img(src="icon-tv-02.png", width="200"), href="#"),
                    A(Img(src="icon-linguas.png", width="200"), href="#"),
                    A(Img(src="icon-fisica.png", width="200"), href="#"),
                ),
                Group(
                    A(Img(src="icon-matematica.png", width="200"), href="#"),
                    A(Img(src="icon-biologia.png", width="200"), href="#"),
                    A(Img(src="icon-quimica.png", width="200"), href="#"),
                    A(Img(src="icon-auditorio.png", width="200"), href="#"),
                    A(Img(src="icon-biblioteca.png", width="200"), href="#"),
                    A(Img(src="icon-quadra.png", width="200"), href="#"),
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


@rt("/agendar")
def get():
    return Titled("Agendar recurso")


serve()
