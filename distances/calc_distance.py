import Levenshtein
import numpy

class OCRDistance():
    def similarity(self, string1, string2, maximal):
        distance = Levenshtein.distance(string1, string2)
        if distance < maximal:
            return distance
        return -1

    def distance(self, found, exames, bestdistance, bestresult):
        localresult = self.similarity(found,exames,10)
        if localresult != -1 and localresult <= bestdistance:
            bestdistance = localresult
            bestresult = exames
        return bestdistance, bestresult

    def calculate(self, allexames, found):
            bestresult = ""
            bestdistance = 999
            for exames in allexames:
                bestdistance, bestresult = self.distance(found,exames.strip(), bestdistance, bestresult)
                bestdistance, bestresult = self.distance(found,exames.strip().split("-")[0], bestdistance, bestresult)
                bestdistance, bestresult = self.distance(found,exames.strip().split(",")[0], bestdistance, bestresult)

            return bestresult


    def find_similarities(self, allexames, imagefound):
        arrayfound = imagefound.split('\n')
        finalresult = ""

        for found in arrayfound:
            found = found.strip()
            if found == "":
                continue
            bestresult = self.calculate(allexames, found)

            if bestresult == "":
                bestresult = self.calculate(allexames, found.split("-")[0])

            if bestresult == "":
                bestresult = self.calculate(allexames, found.split(",")[0])

            if bestresult != "":
                finalresult = finalresult + bestresult + "\n"

        return finalresult


allexames = numpy.array([
    "ACIDO FOLICO, PESQUISA E/OU DOSAGEM NOS ERITROCITOS",
    "FERRO SERICO",
    "MAGNESIO",
    "TRANSFERRINA",
    "VITAMINA D3",
    "HORMONIO LUTEINIZANTE",
    "PROLACTINA",
    "SULFATO DE DEMIDROEPIANDROSTERONA",
    "T4 LIVRE",
    "TESTOSTERONA LIVRE",
    "TESTOSTERONA TOTAL",
    "COLESTEROL (HDL) - PESQUISA E/OU DOSAGEM",
    "COLESTEROL TOTAL - PESQUISA E/OU DOSAGEM",
    "FOSFATASE ALCALINA - PESQUISA E/OU DOSAGEM"
    "GAMA-GLUTAMIL TRANSFERASE (GAMA GT) - PESQUISA E/OU DOSAGEM",
    "TGO - TRANSAMINASE OXALACETICA (AMINO TRANSFERASE ASPARTATO) - PESQUISA E/OU DOSAGEM",
    "TGP - TRANSAMINASE PIRUVICA (AMINO TRANSFERASE DE ALANINA) - PESQUISA E/OU DOSAGEM",
    "TRIGLICERIDEOS - PESQUISA E/OU DOSAGEM",
    "ACIDO URICO - PESQUISA E/OU DOSAGEM",
    "CREATININA - PESQUISA E/OU DOSAGEM",
    "CREATINO FOSFOQUINASE TOTAL (CK) - PESQUISA E/OU DOSAGEM",
    "GLICOSE - PESQUISA E/OU DOSAGEM",
    "HEMOGLOBINA GLICADA (FRACAO A1C) - PESQUISA E/OU DOSAGEM",
    "VITAMINA D 25 HIDROXI, PESQUISA E/OU DOSAGEM (VITAMINA D3)",
    "HEMOGRAMA COM CONTAGEM DE PLAQUETAS OU FRACOES (ERITROGRAMA, LEUCOGRAMA, PLAQUETAS)",
    "ROTINA DE URINA (CARACTERES FISICOS, ELEMENTOS ANORMAIS E SEDIMENTOSCOPIA)",
    "POTASSIO - PESQUISA E/OU DOSAGEM",
    "PROTEINA C REATIVA, QUANTITATIVA - PESQUISA E/OU DOSAGEM",
    "AMILASE - PESQUISA E/OU DOSAGEM",
    "CALCIO - PESQUISA E/OU DOSAGEM",
    "ELETROFERESE DE PROTEINAS",
    "LIPASE - PESQUISA E/OU DOSAGEM",
    "ANTICOAGULANTE LUPICO, PESQUISA",
    "HEMOSSEDIMENTACAO, (VHS) - PESQUISA E/OU DOSAGEM",
    "ANTI-RO/SSA - PESQUISA E/OU DOSAGEM",
    "FATOR ANTINUCLEO, (FAN) - PESQUISA E/OU DOSAGEM",
    "HEPATITE B - HBSAG (AU, ANTIGENO AUSTRALIA) - PESQUISA E/OU DOSAGEM",
    "HEPATITE C - ANTI-HCV - PESQUISA E/OU DOSAGEM",
    "CORTISOL - PESQUISA E/OU DOSAGEM",
    "FERRITINA - PESQUISA E/OU DOSAGEM",
    "TIREOESTIMULANTE, HORMONIO (TSH) - PESQUISA E/OU DOSAGEM",
    "VITAMINA B12 - PESQUISA E/OU DOSAGEM",
    "CULTURA, URINA COM CONTAGEM DE COLONIAS",

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