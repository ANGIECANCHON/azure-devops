import click

@click.command(help="this is just a hello app, no more")
@click.option("--name", prompt="I need your name", help="Need your name")
@click.option("--color", prompt="I need your color", help="this is your color")
def hello(name, color):
    if name == "Thor":
        click.echo("youre are always red")
        click.echo(click.style(f"hello world {name}", fg="red"))
    else:
        click.echo(f"Your color is {color}!")
        click.echo(click.style(f"Hello {name}!", fg=color))

if __name__ == "__main__":
    hello()
