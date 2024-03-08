from models.basemodel import BaseModel

from src.arguments import Arguments
from src.invoker import Invoker

from src.vulnerabilities.xss import XSS

class Core:
    def __init__(self):
        self.arguments: Arguments = Arguments()
        self.invoker: Invoker = Invoker()

        self.vulnerabilities: list[BaseModel] = [
            XSS()
        ]

        self.__run__()

    def __run__(self):
        status = False
        r = self.invoker.invoke(
            method = "GET",
            url = self.arguments.get("website"),
            params = [],
            headers = {},
            data = {},
            auth = {}
        )

        for vulnerability in self.vulnerabilities:
            status = vulnerability.check(r.text)
            print(f"Exploit {vulnerability.name}: {status}")
