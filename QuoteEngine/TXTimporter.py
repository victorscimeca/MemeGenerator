from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTimporter(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        with open(path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                if line.strip() != "":
                    parse = line.split(' - ')
                    new_quote = QuoteModel(f'"{parse[0]}"', parse[1])
                    quotes.append(new_quote)

        return quotes
