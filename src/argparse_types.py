import argparse
import os

from settings import settings


class ArgparseType:
    @staticmethod
    def students_filename(arg: str) -> str:
        if not os.path.isfile(arg):
            raise argparse.ArgumentTypeError(
                "Путь к файлу студентов некорректен")
        return arg

    @staticmethod
    def rooms_filename(arg: str) -> str:
        if not os.path.isfile(arg):
            raise argparse.ArgumentTypeError("Путь к файлу комнат некорректен")
        return arg

    @staticmethod
    def file_format(arg: str) -> str:
        if arg not in settings.available_serializers.keys():
            raise argparse.ArgumentTypeError("Формат файла некорректен")
        return arg
