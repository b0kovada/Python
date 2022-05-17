from diak import Diak
from typing import *
import io
import os

class DiakIO:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def read(fileName: str) -> List[Diak]:
        oneLine:str = None
        allLines:List[str]=[]
        
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))#visszaadja azt a mappát amiben dolgozunk
            path: str = os.path.join(here, fileName)#összefűzi a mappát a mi fájlnevünkkel 

            with open(path,encoding='latin-1', mode="r") as file:
                for line in file:
                    oneLine = line.strip()
                    allLines.append(oneLine)
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")
        
        diakok: List[Diak] = []
        diak: Diak = None
        
        adatok: List[str] = []
        
        nev: str = None
        atlag: float = None

        for line in allLines:
            adatok = line.split('\t')

            nev = adatok[0]
            atlag = float(adatok[1])

            diak = Diak(nev, atlag)
            diakok.append(diak)

        return diakok