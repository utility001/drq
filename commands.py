import click
from quotes import QuotesGenerator

q = QuotesGenerator()


@click.command()
def get_random():
    """Get random quote from the database"""
    quote = q.get_random_quote()
    click.secho(quote, fg='green')


@click.command()
def list_all():
    """List all the quotes available in the database"""
    quotes = q.list_all_quotes()
    click.secho(quotes, fg='blue')


@click.command()
def add_new():
    """
    Add a new quote to the database.

    This command prompts you to enter a quote and then saves it to the quote database. 
    """
    to_add = click.prompt("Enter quote")
    add = q.write_quote(to_add)
    click.secho(add)