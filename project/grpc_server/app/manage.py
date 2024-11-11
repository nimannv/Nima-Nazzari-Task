import typer

from test.test import test_csv, influx_test
from server import server


app = typer.Typer()

@app.command()
def runserver():
    server.serve()

@app.command()
def test_csv_data_loader():
    test_csv()

@app.command()
def test_influx_data_loader():
    influx_test()


if __name__ == "__main__":
    app()