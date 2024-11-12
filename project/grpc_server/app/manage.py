import typer
import unittest
import os

from test import manual_test
from server import server


app = typer.Typer()

@app.command()
def runserver(port: int):
    server.serve(port)

@app.command()
def manual_test_csv():
    manual_test.test_csv()

@app.command()
def manual_test_influx():
    manual_test.test_influx()

@app.command()
def run_all_tests():
    os.system('pytest')


if __name__ == "__main__":
    app()