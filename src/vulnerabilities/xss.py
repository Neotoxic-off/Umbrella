import re

from models.basemodel import BaseModel

from src.invoker import Invoker
from src.scrapper import Scrapper

class XSS(BaseModel):
    def __init__(self):
        super().__init__("XSS")

        self.scrapper: Scrapper = Scrapper()

    def check(self, html: str):
        pattern = re.compile(
            r"<\s*script[^>]*>(.*?)<\s*/\s*script\s*>",
            re.IGNORECASE | re.DOTALL
        )
        result = pattern.findall(html)

        return (result != None)
