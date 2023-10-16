from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVimporter(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            body = row['body']
            if not body.startswith('"') and not body.endswith('"'):
                body = f'"{body}"'
            new_quote = QuoteModel(body, row['author'])
            quotes.append(new_quote)

        return quotes
