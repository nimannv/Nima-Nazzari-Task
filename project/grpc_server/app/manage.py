import typer
import unittest
import os

from src.test import manual_test
from src.server import server


app = typer.Typer()

@app.command()
def runserver(port: int):
    try:
        server.serve(port)
    except Exception as e:
        logging.error(f"Failed to run the server on port {port}: {e}", exc_info=True)


@app.command()
def manual_test_csv():
    manual_test.csv_test()

@app.command()
def manual_test_influx():
    manual_test.influx_test()

@app.command()
def test():
    os.system('pytest')


if __name__ == "__main__":
    app()