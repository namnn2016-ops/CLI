import typer
import random
app = typer.Typer()
@app.command()
def hello(name = typer.Option("bạn")):
    typer.echo(f"hello {name}!")
@app.command()
def about():
    typer.echo("Đây là CLI của Nam.")
@app.command()
def version():
    typer.echo("1.0.0")
@app.command()
def login():
    typer.echo("Đăng nhập thành công.")
@app.command()
def logout():
    typer.echo("Đã đăng xuất.")
@app.command()
def add(a:int, b:int):
    typer.echo(a + b)
@app.command()
def multiply(a:int, b:int):
    typer.echo(a * b)
@app.command()
def age(name, age:int):
    typer.echo(f"Xin chào {name}, bạn {age} tuổi.")
@app.command()
def calc(a:int, b:int):
    typer.echo(f"{a} + {b} = {a + b}")
    typer.echo(f"{a} - {b} = {a - b}")
    typer.echo(f"{a} * {b} = {a * b}")
    typer.echo(f"{a} / {b} = {a / b}")
@app.command()
def me():
    typer.echo("Tên: Nam \n Tuổi: 10 \n Sở thích: Học CLI")
@app.command()
def bmi(weight: float = typer.Option(...), height: float = typer.Option(...)):
    typer.echo(weight / (height ** 2))
@app.command()
def rectangle(width: int = typer.Option(...), height: int = typer.Option(...)):
    typer.echo(f"Chiều dài: {height}\nChiều rộng: {width}\nDiện tích: {height * width}\nChu vi: {(height + width) * 2}")
@app.command()
def info(name = typer.Option("Nam"), age: int = typer.Option(10), hobby = typer.Option("Học CLI"), country = typer.Option("Việt Nam")):
    typer.echo(f"Tên: {name}\nTuổi: {age}\nSở thích: {hobby}\nQuốc gia: {country}")
@app.command(name="random")
def random_naumber():
    typer.echo(random.randint(1, 100))
if __name__ == "__main__":
    app()