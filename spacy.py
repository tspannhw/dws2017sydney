import spacy
nlp = spacy.load('en')
doc5 = nlp(u"Timothy Spann is studying at Princeton University in New Jersey.")
# Named Entity Recognizer (NER)
for ent in doc5.ents:
        print ent, ent.label, ent.label_
