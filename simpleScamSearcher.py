import csv
import spacy

from scamEvaluation.scamEvaluation import ScamEvaluation
from scamEvaluation.collocation import Collocation

class SimpleScamSearcher:
    def __init__(self):
        self._scamEvaluator = ScamEvaluation()
        self._nlp = spacy.load('en')
        
        # Устанавливаем словосочетания, которые хотим искать в тексте
        # если коэффициент в строке self._scamEvaluator.addCollocation(collocation, 0.5) положительный,
        # то нахождение данного словосочетания увеличивате уровень скамности иначе понижает
        # Positive collocations:

        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giving away btc")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giving btc away")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("btc giving away")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("btc away giving")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("away btc giving")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("away giving btc")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)

        
        
        
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giving away bitcoin")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giving bitcoin away")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("bitcoin giving away")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("bitcoin away giving")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("away bitcoin giving")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("away giving bitcoin")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        
        
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giving away eth")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giving eth away")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("eth giving away")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("eth away giving")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("away eth giving")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("away giving eth")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        
        
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giving away etherium")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giving etherium away")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("etherium giving away")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("etherium away giving")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("away etherium giving")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("away giving etherium")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
       

        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giveaway btc")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("btc giveaway")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giveaway bitcoin")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("bitcoin giveaway")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)

        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giveaway eth")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("eth giveaway")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("giveaway etherium")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        collocation.setMaxDistance(1)
        tokens = self._nlp("etherium giveaway")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("airdrop")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.3)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("multiply your investment")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 1.0)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("profit")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.4)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("profit up to")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.7)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("get up to")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.7)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("multiplied")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.3)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("triple")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.2)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("double")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.2)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("invest")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.3)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("reward")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.4)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("just send")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 1.0)
        
        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("send just")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 1.0)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("can earn")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.8)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("special bonus")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.8)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("free")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, 0.5)

        # Negative collocations:

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("scam")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, -1.0)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("dumm")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, -1.0)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("dumn")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, -1.0)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("stole")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, -1.0)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("awful")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, -1.0)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("fraud")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, -1.0)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("phishing")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, -1.0)

        separateLemmatizedWords = []
        collocation = Collocation()
        tokens = self._nlp("not trust")
        for token in tokens:
            separateLemmatizedWords.append(token.lemma_)
        collocation.setWords(separateLemmatizedWords)
        self._scamEvaluator.addCollocation(collocation, -1.0)
        
    def documentScamLevel(self, doc):
        return self._scamEvaluator.scamLevel(doc)
    
    def documentListScamLevels(self, docs):
        res = []
        for doc in docs:
            res.append(self.documentScamLevel(doc))
            
        return res
    
    # Fields:
    
    _scamEvaluator = None
    _nlp = None
    
    