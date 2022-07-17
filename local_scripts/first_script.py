# Imports
import subprocess
from typing import NamedTuple


class DTO(NamedTuple):
    cmd: str
    code: str


def local_execute():
    """
    Выполняет комманду pwd на хосте
    Возвращает строковый результат
    """

    cmd = subprocess.run('pwd', shell=True, encoding='utf-8', executable='/bin/bash', stdout=subprocess.PIPE)

    return DTO(
        cmd=str(cmd.stdout),
        code=str(cmd.returncode)
    )


if __name__=='__main__':
    print(local_execute())
