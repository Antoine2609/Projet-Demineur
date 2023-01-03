# importation des bibliothèques et des modules indispensables
import pygame

# class Case du projet démineur
class Case:
    def __init__(self):
        self._mine = False
        self._case_recouverte = True
        self._drapeau = False
    
    def get_mine(self) -> bool:
        return self._mine

    def set_mine(self):
        self._mine = True  

    def get_case_recouverte(self) -> bool:
        return self._case_recouverte
    
    def set_case_decouverte(self):
        '''
        méthode permettant de découvrir la case si elle ne possède pas de drapeau
        '''
        if not self._drapeau:
            self._case_recouverte = False

    def get_drapeau(self) -> bool:
        return self._drapeau

    def set_drapeau(self):
        '''
        méthode permettant d'inverser la valeur que prend le drapeau si la case n'est pas découverte
        '''
        if self.get_case_recouverte():
            self._drapeau = not self._drapeau


