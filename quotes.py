import random

FILEPATH = "quotes.txt"


class QuotesGenerator:
    """An attempt to build a random quotes generator"""

    def __init__(self):
        self.filepath = FILEPATH

    def read_quotes(self):
        """Read quotes from the database"""
        try:
            with open(file=self.filepath, mode="r") as file:
                quotes = file.readlines()
            # Strip extra whitespace characters from each line
            quotes = [quote.strip() for quote in quotes if quote.strip()]
            return quotes
        except FileNotFoundError:
            return ["ERROR: Quotes database not Found. Did you delete it?"]

    def write_quote(self, quote_text):
        """Write quotes to the database"""
        # open the text file in append mode
        with open(file=self.filepath, mode="a") as file:
            file.write('\n\n' + quote_text)
            return "SUCCESS: Quote written successfully to the Database ✅"

    def get_random_quote(self):
        """Outputs a random quote"""
        quotes = self.read_quotes()

        if quotes:
            return random.choice(quotes)
        else:
            output = """There are no quotes available. \n
            Try adding some to the database"""
            return output

    def list_all_quotes(self):
        """Outputs all quotes available in the database"""
        quotes = self.read_quotes()
        if quotes:
            for idx, quote in enumerate(quotes, start=1):
                print(f"{idx}. {quote}")
        else:
            output = """There are no quotes available. \n
            Try adding some to the database"""
            return output