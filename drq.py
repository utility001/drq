import click
import commands


@click.group()
@click.version_option("0.1.0", prog_name="drq")
def main():
    """
    This cli tool is used to get random quotes
    """


main.add_command(commands.get_random)
main.add_command(commands.list_all)
main.add_command(commands.add_new)


if __name__ == "__main__":
    main()
