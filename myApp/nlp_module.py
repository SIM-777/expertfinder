import spacy
from spacy import displacy
from myApp.Expert import *

NER = spacy.load("en_core_web_sm")
social_medias=["twitter","linkedin","springer","researchgate"]




def extract_report(dict):
    extracted_social_media_links=[]
    report=[]
    raw_data=dict
    data= raw_data["report"]
    organic_results=data["organic_results"]
    for organic_result in organic_results:
        title=organic_result["title"]
        displayed_link=organic_result["displayed_link"]
        for social_media in social_medias:
            if social_media in displayed_link:
                 extracted_social_media_links.append(organic_result)
                 organic_results.remove(organic_result)
        processed_title=NER(title)
        for word in processed_title.ents:
            if(word.label_=="ORG" or word.label_=="PERSON"):
                report.append(
                    organic_result
                                    
                )
                break 
    #report.append({"social_medias":extracted_social_media_links})      
    return {"reports": report,"social_medias":extracted_social_media_links}    



def extract_keywords():
   pass