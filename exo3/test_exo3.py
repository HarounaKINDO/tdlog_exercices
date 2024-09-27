import unittest
from exo3 import processLines

class TestExo3(unittest.TestCase):
    def test_input_1(self):
        # Lire les données d'entrée depuis le fichier input1.txt
        with open("sample/input1.txt") as input1:
            lines = input1.readlines()

        # Lire la sortie attendue depuis le fichier output1.txt
        with open("sample/output1.txt") as output1:
            expected = output1.read().strip()  # .strip() pour enlever les espaces ou nouvelles lignes

        # Vérifier si le résultat est correct
        self.assertEqual(expected, processLines(lines))

    def test_input_2(self):
        # Lire les données d'entrée depuis le fichier input2.txt
        with open("sample/input2.txt") as input2:
            lines = input2.readlines()

        # Lire la sortie attendue depuis le fichier output2.txt
        with open("sample/output2.txt") as output2:
            expected = output2.read().strip()  # .strip() pour enlever les espaces ou nouvelles lignes

        # Vérifier si le résultat est correct
        self.assertEqual(expected, processLines(lines))

if __name__ == "__main__":
    unittest.main()
