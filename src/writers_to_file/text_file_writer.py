from .ifilewriter import IFileWriter


class TextFileWriter(IFileWriter):
    def write(self, data: str, path: str, format: str) -> None:
        with open(f"{path}.{format}", "w") as file:
            file.write(data)
