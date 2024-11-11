import typer
import unittest

from test import manual_test
from server import server


app = typer.Typer()

@app.command()
def runserver(port: int):
    server.serve(port)

@app.command()
def test_csv_nima():
    manual_test.test_csv()

@app.command()
def test_influx_data_loader():
    manual_test.test_influx()

@app.command()
def run_all_tests():
    # Discover and load all tests in the current directory
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern='test*.py')

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Check if any tests failed or encountered errors
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print(f"{len(result.failures)} test(s) failed.")
        print(f"{len(result.errors)} test(s) had errors.")


if __name__ == "__main__":
    app()