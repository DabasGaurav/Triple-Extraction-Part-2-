from openie import StanfordOpenIE

text="""it features both original and existing music tracks.
it is the worst reviewed film in the franchise.
but she injures quicksilver and accidentally kills mystique before flying away.
military forces tasked with her arrest.
the train is attacked by vuk and her d'bari forces.
kota eberhardt portrays telepath selene gallio,
singer did not return to direct the sequel, x-men:
the last stand, which was written by penn and simon kinberg.
jessica chastain was also potentially being considered for the same character.
mauro fiore served as cinematographer.
filming was completed on october 14, 2017."""

with StanfordOpenIE() as client:

    print('Text: %s.' % text)
    for triple in client.annotate(text):
        print('|-', triple)
    
    corpus=text
    
    triples_corpus = client.annotate(corpus[0:50000])
    
    print('Corpus: %s [...].' % corpus[0:80])
    print('Found %s triples in the corpus.' % len(triples_corpus))
    
    for triple in triples_corpus[:3]:
        print('|-', triple)
        
 
    
    
    
        