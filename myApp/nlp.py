#from keybert import KeyBERT
#from keyphrase_vectorizers import KeyphraseCountVectorizer
import yake

# docs = ["implementing security in distributed systems"]
# vectorizer = KeyphraseCountVectorizer()
#vectorizer.fit_transform(docs).toarray()
#kw_model = KeyBERT()
#keywords = kw_model.extract_keywords(docs, vectorizer=KeyphraseCountVectorizer())
#print(keywords)
def ExtractKeywords(doc):
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(doc)
