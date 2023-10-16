from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DOCXimporter import DOCXimporter
from .CSVimporter import CSVimporter
from .PDFimporter import PDFimporter
from .TXTimporter import TXTimporter


class Ingestor(IngestorInterface):
    importers = [DOCXimporter, CSVimporter, PDFimporter, TXTimporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
