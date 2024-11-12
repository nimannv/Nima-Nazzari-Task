import typer
import unittest
import uvicorn
import os

app = typer.Typer()

@app.command()
def runserver(port: int):
    uvicorn.run("src.main:app", host="0.0.0.0", port=port, reload=False, log_level="debug")

@app.command()
def test():
    os.system('pytest')

if __name__ == "__main__":
    app()