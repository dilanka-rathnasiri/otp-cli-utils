import typer

app = typer.Typer()


@app.command()
def validate():
    print("Valid")


def main():
    app()


if __name__ == "__main__":
    main()
