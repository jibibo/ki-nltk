import nltk
from nltk import CFG
from nltk.grammar import FeatureGrammar

cfg_1 = CFG.fromstring("""
    S -> NP VP
    NP -> 

""")