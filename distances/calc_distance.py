import Levenshtein
import numpy

class OCRDistance():
    def similarity(self, string1, string2, maximal):
        distance = Levenshtein.distance(string1, string2)
        if distance < maximal:
            return distance
        return -1


    def find_similarities(self, allexames, imagefound):
        arrayfound = imagefound.split('\n')
        finalresult = ""

        for found in arrayfound:
            bestresult = ""
            bestdistance = 10
            found = found.strip()
            if found == "":
                continue

            for exames in allexames:
                localresult = self.similarity(found,exames.strip(),12)
                if localresult != -1 and localresult <= bestdistance:
                    bestdistance = localresult
                    bestresult = exames

            if bestresult != "":
                finalresult = finalresult + bestresult + "\n"

        return finalresult


allexames = numpy.array([
    "ACIDO FOLICO, PESQUISA E/OU DOSAGEM NOS ERITROCITOS",
    "CALCIO",
    "FERRO SERICO",
    "MAGNESIO",
    "TRANSFERRINA",
    "VITAMINA D 25 HIPROXI",
    "VITAMINA D3",
    "FERRITINA",
    "FOLICULO ESTIMULANTE",
    "HORMONIO LUTEINIZANTE",
    "PROLACTINA",
    "SULFATO DE DEMIDROEPIANDROSTERONA",
    "T4 LIVRE",
    "TESTOSTERONA LIVRE",
    "TESTOSTERONA TOTAL",
    "TIREOESTIMULANTE",
    "HORMONIO (TSH)"
])

imagefound = """Deep Studio Informática Ltda.
                Teste de receituário de examas

                Para Sr. Edson Arintura

                ACIDO FOLICO, PESQUISA E/OU DOSAGEM NOS ERITROCITOS
                CALEIO
                FERRO SÉERICO
                MAGNESIO
                TRANSFERRINA
                VITAMINA D 25 HIPROXI, PESQUISA E/OU DOSAGEM (VITAMINA D3)
                FERRITINA
                FOLICULO ESTIMULANTE, HHORMONTO (FSH)
                RORMUNIO LUTEINIZANTE. 1H
                PROLACTINA '
                . SULFATO DE DEMIDROEPIANDROSTERONA 1S
                T4A LIVRE
                TESTOSTERONA LIVRE
                TESTOSTERONA TOTÁL: .
                TIREOESTIMULANTE, HORMONIO (TSH)

                Edson Toit anmu;
                Rafael Coeir
                Flavio de Moras"""

distance = OCRDistance()
result = distance.find_similarities(allexames, imagefound)
print(result)