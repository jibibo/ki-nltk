import nltk
from nltk import CFG
from nltk.grammar import FeatureGrammar

cfg_1 = CFG.fromstring("""
S -> NP VP
NP -> PRP
PRP -> ‘he’
VP -> VDB PP
VDB -> ‘lived’
PP -> IN NP
IN -> ‘in’
NP -> NN
NN -> ‘africa’
S -> NP VP
NP -> PRP
PRP -> ‘he’
VP -> VDB ADJP ADVP
VBD -> ‘was’
ADJP -> JJ
JJ -> ‘curious’
ADVP -> RB
RB -> ‘again’
S -> NP VP
NP -> DT NN
DT -> ‘the’
NN -> ‘traffic’
VP -> VBD NP PRT
VBD -> ‘got’
NP -> DT JJ
DT -> ‘all’
JJ -> ‘mixed’
PRT -> RP
RP -> ‘up’
S -> NP-TMP NP VP
NP-MP -> DT JJ NN
DT -> ‘the’
JJ -> ‘next’
NN -> ‘morning’
NP -> DT NN
DT -> ‘the’
NN -> ‘man’
VP -> VBD NP
VBD -> ‘telephoned’
NP -> DT NN
DT -> ‘the’
NN -> ‘zoo’
S -> NP VP
NP -> NN
NN -> ‘george’
VP -> VBD VP
VBD -> ‘had’
VP -> VBD NP
VBD -> ‘telephoned’
NP -> DT NN NN
DT -> ‘the’
NN -> ‘fire’
NN -> ‘station’
S -> NP VP
NP -> PRP
PRP -> ‘they’
VP -> VBD SBAR
VBD -> ‘thought’
SBAR -> S
S -> NP VP
NP -> PRP
PRP -> ‘it’
VP -> VBD NP
VBD -> ‘was’
NP -> DT JJ NN
DT -> ‘a’
JJ -> ‘real’
NN -> ‘fire’
S -> NP VP
NP -> NN
NN -> ‘george’
VP -> VBD S
VBD -> ‘tried’
S -> VP
VP -> TO VP
TO -> ‘to’
VP -> VB ADVP
VB -> ‘run’
ADVP -> RB
RB -> ‘away’
S -> NP VP
NP -> DT JJ NN
DT -> ‘a’
JJ -> ‘little’
NN -> ‘girl’
VP -> VBD NP PP
VBD -> ‘bought’
NP -> DT NN
DT -> ‘a’
NN -> ‘balloon’
PP -> IN NP
IN -> ‘for’
NP -> PRP$ NN
PRP$ -> ‘her’
NN -> ‘brother’
S -> NP VP
NP -> DT NNS
DT -> ‘the’
NNS -> ‘houses’
VP -> VBD PP PP
VDB -> ‘looked’
PP -> IN NP
IN -> ‘like’
NP -> NP CC NP
NP -> NN NNS
NN -> ‘toy’
NNS -> ‘houses’
CC -> ‘and’
NP -> DT NNS
DT -> ‘the’
NNS -> ‘people’
PP -> IN NP
IN -> ‘like’
NP -> NNS
NNS -> ‘dolls’
S -> NP VP
NP -> PRP
PRP -> 'he’
VP -> VP CC VP
VP -> VBD PRT
VBD -> ‘looked’
PRT -> RP
RP -> ‘down’
CC -> ‘and’
VP -> VBD NP
VBD -> ‘saw’
NP -> NP COMMA NP
NP -> PRP$ NN
PRP$ -> ‘his’
NN -> ‘friend’
COMMA -> ‘,’
NP -> NP PP
NP -> DT NN
DT -> ‘the’
NN -> ‘man’
PP -> IN NP
IN -> ‘with’
NP -> DT JJ JJ NN
DT -> ‘the’
JJ -> ‘big’
JJ -> ‘yellow’
NN -> ‘hat’
S -> NP VP
NP -> PRP
NP -> PRP
NP -> PRP
NP -> DT NN
VP -> VP CC VP
VP -> VBD NP PRT
VP -> VBD NP PP
PRT -> RP
PP -> IN NP
PRP -> ‘they’ 
PRP ->  ‘him’ 
VBD -> ‘took’
VBD ->  ‘shut’
RP -> ‘away’
CC -> ‘and’
IN -> ‘in’
DT -> ‘a’
NN -> ‘prison’
S -> NP VP
NP -> DT NNS
VP -> VP CC VP
VP -> VBD
VP -> VBD
DT -> ‘the’
NNS -> ‘sailors’
VBD -> ‘looked’
CC -> ‘and’
VBD -> ‘looked’
S -> NP VP
NP -> PRP
VP -> VBD RB VP
VP -> VB SBAR
SBAR -> S 
NP -> PRP
VP -> VBD ADJP
ADJP -> JJ
PRP -> ‘they’
VBD -> ‘did’
RB -> ‘not’
VB -> ‘know’
PRP -> ‘it’
VBD -> ‘was’
JJ -> ‘george’
S -> NP-TMP NP VP
NP-TMP -> DT JJ NN
NP -> DT NN
VP -> VBD NP
NP -> DT NN
DT -> ‘the’
JJ -> ‘next’
NN -> ‘morning’
DT -> ‘the’
NN -> ‘man’
VBD -> ‘telephoned’
DT -> ‘the’
NN -> ‘zoo’
S -> NP VP
NP -> NN
VP -> VBD VP
VP -> VBD NP
NP -> DT NN NN
NN -> ‘george’ 
VBD -> ‘had’
VBD -> ‘telephoned’
DT -> ‘the’
NN -> ‘fire’
NN -> ‘station’
S -> NP VP 
NP -> PRP
VP -> VBD SBAR
SBAR -> S
S -> NP VP
NP -> PRP 
VP -> VBD NP
NP -> DT JJ NN
PRP -> ‘they’
VBD -> ‘thought’
PRP -> ‘it’
VBD -> ‘was’
DT -> ‘a’
JJ -> ‘real’
NN -> ‘fire’
S -> NP VP
NP -> PRP
VP -> VBD SBAR
SBAR -> S
S -> NP VP 
NP -> PRP
VP -> MD VP
VP -> VB NP
NP -> DT JJ JJ NN
RPR -> ‘he’
VBD -> ‘felt’
PRP -> ‘he’
MD -> ‘must’
VB -> ‘have’
DT -> ‘a’
JJ -> ‘bright’
JJ -> ‘red’ 
NN -> ‘balloon’ 
S -> NP VP
NP -> DT NN
VP -> VBD NP 
NP -> NP NN
NP -> NNP POS
NN -> ‘head’
DT -> ‘the’
NN -> ‘hat’
VBD -> ‘covered’
NNP -> ‘george’
POS -> ‘’s’
S -> ADVP NP VP
ADVP -> IN JJ
NP -> PRP
VP -> VBD NP S
NP -> PRP 
S -> VP
VP -> VBG PP
PP -> IN NP
NP -> NP , CC RB NP
NP -> DT NN
NP ->  DT JJ NN
IN -> ‘at’
JJ -> ‘last’
PRP -> ‘they’
VBD -> ‘saw’
PRP -> ‘him’
VBG -> ‘struggling
IN -> ‘in’
DT -> ‘the’
NN -> ‘water’
, -> ‘,’
CC -> ‘and’
RB -> ‘almost’
DT -> ‘all’
JJ -> ‘tired’
NN -> ‘out’
S -> NP VP
VP -> VP CC VP
VP -> VBD NP PRT ADVP
NP -> PRP
PRT -> RP
ADVP -> RB
VP -> VBD NP PP
NP -> PRP
PP -> IN NP
Det -> ‘the’
N -> ‘man’
PRP -> ‘him’
VBD -> ‘picked’
RP -> ‘up’
RB -> ‘quickly’
CC -> ‘and’
VBD -> ‘popped’
PRP -> ‘him’
IN -> ‘into’
Det -> ‘a’
NN -> ‘bag’
S -> NP VP
NP -> NNP
NNP -> ‘George’
VP -> VBD VP
VBD -> ‘was’
VP -> VBN
VBN -> ‘caught'
S -> CC NP VP
NP -> PRP
VP -> VBZ ADJP S
ADJP -> JJ PP
PP -> IN NP
NP -> JJ NNS
S -> VP
VP -> TO VP
VP -> VB
CC -> ‘but’
PRP -> ‘it’
VBZ -> ‘is’
JJ -> ‘easy’
IN -> ‘for’
JJ -> ‘little’
NNS -> ‘monkeys’
TO -> ‘to’
VB -> ‘forget’
S -> PP NP VP
PP -> IN NP
NP -> Det NN
NP -> PRP
VP -> VBD NP
NP -> Det NNS
IN -> ‘on’
Det -> ‘the’
NN -> ‘deck’
PRP -> ‘he’
VBD -> ‘found’
Det -> ‘some’
NNS -> ‘seagulls’
S -> NP VP
NP -> PRP
VP -> VBD SBAR
SBAR -> WHADVP S
WHADVP -> WRB
S -> NP VP
NP -> PRP
VP -> MD VP
VP -> VB
PRP -> ‘he’
VBD -> ‘wondered’
WRB -> ‘how’
PRP -> ‘they’
MD -> ‘could’
VB -> ‘fly’
S -> NP VP
NP -> PRP
VP -> VBD ADJP
ADJP -> RB JJ
PRP -> ‘he’
VBD -> ‘was’
RB -> ‘very’
JJ -> ‘curious’
S -> ADVP NP VP
ADVP -> RB
NP -> PRP
VP -> VBD S
S -> VP
VP -> TO VP
VP -> VB
RB -> ‘finally’
PRP -> ‘he’
VBD -> ‘had’
TO -> ‘to’
VB -> ‘try’
S -> NP VP
NP -> PRP
VP -> VBD ADJP
ADJP -> JJ
PRP -> ‘it’
VBD -> ‘looked’
JJ -> ‘easy’
S -> CC NP VP
NP -> WP
VP -> VBD
CC -> ‘but’
WP -> ‘what’
VBD -> ‘happened’
S -> NP-TMP NP VP
NP-TMP -> CD NN
NP -> NNP
VP -> VBD NP
NP -> Det NN
CD -> ‘one’
NN -> ‘day’
NNP -> ‘George’
VBD -> ‘saw’
Det -> ‘a’
NN -> ‘man’

""")