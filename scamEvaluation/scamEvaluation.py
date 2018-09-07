import csv
import spacy

from .collocation import Collocation

from .wordIsMixOfConfusableAndLatinLetters import wordIsMixOfConfusableAndLatinLetters

class ScamEvaluation:
    def __init__(self):
        self._nlp = spacy.load('en')
        self._collocationGroups = {}
        
    def scamLevel(self, doc):
        parsedDoc = self._nlp(doc)
        if self._checkConfusionBetweenLatinLettersAndSpecialSymbols(parsedDoc):
            return 1.0
        return 0
        tokens = []
        lemmatizedTokens = []
        for token in parsedDoc:
            tokens.append(token.text)
            lemmatizedTokens.append(token.lemma_)
        
        lemmatizedScamLevel = self._scamLevelByKeyPhrases(lemmatizedTokens)
        return lemmatizedScamLevel
        
        #scamLevel = self._scamLevelByKeyPhrases(tokens)
        #return max(lemmatizedScamLevel, scamLevel)

    # Private functions:
    
    def _checkConfusionBetweenLatinLettersAndSpecialSymbols(self, parsedDoc):
        for token in parsedDoc:
            if wordIsMixOfConfusableAndLatinLetters(token.text):
                return True
        return False
        
    def _scamLevelByKeyPhrases(self, tokens):
        scamlevel = 0.0
        closedPositions = set()
        groupSizes = list(self._collocationGroups.keys())
        groupSizes.sort()
        groupNum = len(groupSizes) - 1
        while groupNum > 0:
            for cw in self._collocationGroups[groupNum]:
                diapasons = cw["collocation"].search(tokens, closedPositions)
                if len(diapasons) != 0:
                    scamlevel += cw["weight"]
            groupNum -= 1
        return scamlevel
    
    # Setters and getters:
    
    def addCollocation(self, collocation, weight):
        length = collocation.getCollocationSize()
        if length not in self._collocationGroups:
            self._collocationGroups[length] = []
        self._collocationGroups[length].append({"collocation" : collocation, "weight" : weight})
    
    # Fields:
    
    _nlp = None
    _collocationGroups = None
    
    