from diak import Diak
from typing import *

class Osztaly:
    
    @staticmethod
    def atlag(diakok: List[Diak]) -> float:
        osszeg: float = 0
        atlag: float = 0

        for diak in diakok:
            osszeg += diak.atlag

        atlag = osszeg / len(diakok)

        return atlag

    @staticmethod
    def legjobbak(diakok: List[Diak]) -> List[Diak]:
        joDiakok: List[Diak] = [diakok[0]]
        
        
        for i in range(1, len(diakok), 1):
            if(diakok[i].atlag >= joDiakok[0].atlag):
                joDiakok.append(diakok[i])
              

            elif(diakok[i].atlag > joDiakok[0].atlag):
                joDiakok.clear()
                joDiakok.append(diakok[i])


        return joDiakok