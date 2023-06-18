import os
import json
from urllib.parse import urlsplit, parse_qsl
from serpapi import GoogleSearch
def Dummy():    # dummy function to test the search functionaility by returning raw json data
    result={
        "experts":[
  {
    "thumbnail": "https://scholar.googleusercontent.com/citations?view_op=small_photo&user=JicYPdAAAAAJ&citpid=2",
    "name": "Geoffrey Hinton",
    "link": "https://scholar.google.com/citations?hl=en&user=JicYPdAAAAAJ",
    "author_id": "JicYPdAAAAAJ",
    "email": "Verified email at cs.toronto.edu",
    "affiliations": "Emeritus Prof. Comp Sci, U.Toronto & Engineering Fellow, Google",
    "cited_by": 638900,
    "interests": [
      {
        "title": "machine learning",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Amachine_learning",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:machine_learning"
      },
      {
        "title": "psychology",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Apsychology",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:psychology"
      },
      {
        "title": "artificial intelligence",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Aartificial_intelligence",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:artificial_intelligence"
      },
      {
        "title": "cognitive science",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Acognitive_science",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:cognitive_science"
      },
      {
        "title": "computer science",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Acomputer_science",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:computer_science"
      }
    ]
  },
  {
    "thumbnail": "https://scholar.googleusercontent.com/citations?view_op=small_photo&user=kukA0LcAAAAJ&citpid=3",
    "name": "Yoshua Bengio",
    "link": "https://scholar.google.com/citations?hl=en&user=kukA0LcAAAAJ",
    "author_id": "kukA0LcAAAAJ",
    "email": "Verified email at umontreal.ca",
    "affiliations": "Professor of computer science, University of Montreal, Mila, IVADO, CIFAR",
    "cited_by": 605714,
    "interests": [
      {
        "title": "Machine learning",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Amachine_learning",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:machine_learning"
      },
      {
        "title": "deep learning",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Adeep_learning",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:deep_learning"
      },
      {
        "title": "artificial intelligence",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Aartificial_intelligence",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:artificial_intelligence"
      }
    ]
  }
        ]
    }
    
    return result
def getExperts(query:str):
   #c7522e1e379906672ad08268ac5d1c4363828bfacb8e59607ad09df75685ff01
   #"0aaf3529a32d8651f58e5608a11880d8132d27caf2f2e8ecdb1764ad7b75179a"
    params = {
        "api_key": ("0aaf3529a32d8651f58e5608a11880d8132d27caf2f2e8ecdb1764ad7b75179a"),                   # SerpApi API key
        "engine": "google_scholar_profiles",               # profile results search engine
        "mauthors":  query  # search query
    }
    search = GoogleSearch(params)

    profile_results_data = []
    
    if not ("error" in search.get_dict()):
      print(search.get_dict())
      profiles_is_present = True
      while profiles_is_present:
          profile_results = search.get_dict()
          for profile in profile_results["profiles"]:
              thumbnail = profile["thumbnail"]
              name = profile["name"]
              link = profile["link"]
              author_id = profile["author_id"]
              affiliations = profile["affiliations"]
              email = profile.get("email")
              cited_by = profile.get("cited_by")
              interests = profile.get("interests")

              profile_results_data.append({
                  "thumbnail": thumbnail,
                  "name": name,
                  "link": link,
                  "author_id": author_id,
                  "email": email,
                  "affiliations": affiliations,
                  "cited_by": cited_by,
                  "interests": interests
              })

          if "next" in profile_results.get("serpapi_pagination", {}):
              # splits URL in parts as a dict() and update search "params" variable to a new page that will be passed to GoogleSearch()
              search.params_dict.update(dict(parse_qsl(urlsplit(profile_results.get("serpapi_pagination").get("next")).query)))
          else:
              profiles_is_present = False

    
    return ({'experts':profile_results_data})


def getOrganicResult():  
  data=[]  
  for result in soup.select('.gs_r.gs_or.gs_scl'):
        title = result.select_one('.gs_rt').text
        title_link = result.select_one('.gs_rt a')['href']
        publication_info = result.select_one('.gs_a').text
        snippet = result.select_one('.gs_rs').text
        cited_by = result.select_one('#gs_res_ccl_mid .gs_nph+ a')['href']
        try:
            pdf_link = result.select_one('.gs_or_ggsm a:nth-child(1)')['href']
        except: 
            pdf_link = None

        data.append({
            'title': title,
            'title_link': title_link,
            'publication_info': publication_info,
            'snippet': snippet,
            'cited_by': f'https://scholar.google.com{cited_by}',
            'related_articles': f'https://scholar.google.com{related_articles}',
            'all_article_versions': f'https://scholar.google.com{all_article_versions}',
            "pdf_link": pdf_link
        })

def generate_report(name,affiliations):
  params = {
  "engine": "google",
  "q": name+" "+ affiliations,
  #"api_key": "c7522e1e379906672ad08268ac5d1c4363828bfacb8e59607ad09df75685ff01"
  "api_key": ("0aaf3529a32d8651f58e5608a11880d8132d27caf2f2e8ecdb1764ad7b75179a"),
  
      }

  search = GoogleSearch(params)
  organic_results = search.get_dict()
  return {"report":organic_results}
  
  
def Ranker(json_data):
    sorted_result = sorted(json_data, key=lambda x: x["cited_by"], reverse=True)
    for expert in sorted_result:
     print(f"Name: {expert['name']}, Cited By: {expert['cited_by']}")
    params = {
        "api_key": ("c7522e1e379906672ad08268ac5d1c4363828bfacb8e59607ad09df75685ff01"),                   # SerpApi API key
        "engine": "google_scholar_profiles",               # profile results search engine
        "mauthors":  query  # search query
    }
    profile_results_data = []
    
    if not ("error" in search.get_dict()):
      print(search.get_dict())
      profiles_is_present = True
      while profiles_is_present:
          profile_results = search.get_dict()
          for profile in profile_results["profiles"]:
              cited_by = profile.get("cited_by")
              profile_results_data.append({
                  
                  "cited_by": cited_by,
                  
              })

          if "next" in profile_results.get("serpapi_pagination", {}):
              # splits URL in parts as a dict() and update search "params" variable to a new page that will be passed to GoogleSearch()
              search.params_dict.update(dict(parse_qsl(urlsplit(profile_results.get("serpapi_pagination").get("next")).query)))
          else:
              profiles_is_present = False
      return profile_results_data

        
def DummyReport():
  report={"report":{
  "search_metadata":
  {
  "id":
  "644d0649aef264d32181a514",
  "status":
  "Success",
  "json_endpoint":
  "https://serpapi.com/searches/2530e9c79fc1e5fd/644d0649aef264d32181a514.json",
  "created_at":
  "2023-04-29 11:58:01 UTC",
  "processed_at":
  "2023-04-29 11:58:01 UTC",
  "google_url":
  "https://www.google.com/search?q=Alessandro+Orso+Georgia+Institute+of+Technology&oq=Alessandro+Orso+Georgia+Institute+of+Technology&hl=en&gl=us&sourceid=chrome&ie=UTF-8",
  "raw_html_file":
  "https://serpapi.com/searches/2530e9c79fc1e5fd/644d0649aef264d32181a514.html",
  "total_time_taken":
  1.63
  },
  "search_parameters":
  {
  "engine":
  "google",
  "q":
  "Alessandro Orso Georgia Institute of Technology",
  "google_domain":
  "google.com",
  "hl":
  "en",
  "gl":
  "us",
  "device":
  "desktop"
  },
  "search_information":
  {
  "organic_results_state":
  "Results for exact spelling",
  "query_displayed":
  "Alessandro Orso Georgia Institute of Technology",
  "total_results":
  1460000,
  "time_taken_displayed":
  0.37,
  "menu_items":
  [
  {
  "position":
  1,
  "title":
  "News",
  "link":
  "https://www.google.com/search?hl=en&gl=us&q=Alessandro+Orso+Georgia+Institute+of+Technology&tbm=nws&sa=X&ved=2ahUKEwj23eXphM_-AhUcD1kFHQijDPoQ0pQJegQICBAB",
  "serpapi_link":
  "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=Alessandro+Orso+Georgia+Institute+of+Technology&tbm=nws"
  },
  {
  "position":
  2,
  "title":
  "Images",
  "link":
  "https://www.google.com/search?hl=en&gl=us&q=Alessandro+Orso+Georgia+Institute+of+Technology&tbm=isch&sa=X&ved=2ahUKEwj23eXphM_-AhUcD1kFHQijDPoQ0pQJegQIBxAB",
  "serpapi_link":
  "https://serpapi.com/search.json?device=desktop&engine=google_images&gl=us&google_domain=google.com&hl=en&q=Alessandro+Orso+Georgia+Institute+of+Technology"
  },
  {
  "position":
  3,
  "title":
  "Maps",
  "link":
  "https://maps.google.com/maps?hl=en&gl=us&output=search&q=Alessandro+Orso+Georgia+Institute+of+Technology&entry=mc&sa=X&ved=2ahUKEwj23eXphM_-AhUcD1kFHQijDPoQ0pQJegQIBhAB"
  },
  {
  "position":
  4,
  "title":
  "Shopping",
  "link":
  "https://www.google.com/search?hl=en&gl=us&q=Alessandro+Orso+Georgia+Institute+of+Technology&tbm=shop&sa=X&ved=2ahUKEwj23eXphM_-AhUcD1kFHQijDPoQ0pQJegQIBRAB",
  "serpapi_link":
  "https://serpapi.com/search.json?device=desktop&engine=google_shopping&gl=us&google_domain=google.com&hl=en&q=Alessandro+Orso+Georgia+Institute+of+Technology"
  },
  {
  "position":
  5,
  "title":
  "Videos",
  "link":
  "https://www.google.com/search?hl=en&gl=us&q=Alessandro+Orso+Georgia+Institute+of+Technology&tbm=vid&sa=X&ved=2ahUKEwj23eXphM_-AhUcD1kFHQijDPoQ0pQJegQIUhAB",
  "serpapi_link":
  "https://serpapi.com/search.json?device=desktop&engine=google_videos&gl=us&google_domain=google.com&hl=en&q=Alessandro+Orso+Georgia+Institute+of+Technology"
  },
  {
  "position":
  6,
  "title":
  "Books",
  "link":
  "https://www.google.com/search?hl=en&gl=us&q=Alessandro+Orso+Georgia+Institute+of+Technology&tbm=bks&sa=X&ved=2ahUKEwj23eXphM_-AhUcD1kFHQijDPoQ0pQJegQIWxAB"
  },
  {
  "position":
  7,
  "title":
  "Flights",
  "link":
  "https://www.google.com/flights?hl=en&gl=us&output=search&q=Alessandro+Orso+Georgia+Institute+of+Technology&sa=X&ved=2ahUKEwj23eXphM_-AhUcD1kFHQijDPoQ0pQJegQIXBAB"
  },
  {
  "position":
  8,
  "title":
  "Finance",
  "link":
  "https://www.google.com/finance?hl=en&gl=us&output=search&q=Alessandro+Orso+Georgia+Institute+of+Technology&sa=X&ved=2ahUKEwj23eXphM_-AhUcD1kFHQijDPoQ0pQJegQIWhAB"
  }
  ]
  },
  "related_questions":
  [
  {
  "question":
  "How much is the Georgia Tech endowment?",
  "title":
  "$2.97 billion",
  "link":
  "https://en.wikipedia.org/wiki/Georgia_Tech",
  "displayed_link":
  "https://en.wikipedia.org › wiki › Georgia_Tech",
  "thumbnail":
  "https://serpapi.com/searches/644d0649aef264d32181a514/images/9ed8d9d80f6b175a0e7d675a9ca11f4283bde7d07caa8a6dc4192fc95604f519.png",
  "next_page_token":
  "eyJvbnMiOiIxMDA0MSIsImZjIjoiRW9zQkNreEJSWE0zYWs1VFIwbzBhV3hUZDNad1IxTkZaMUpOTW5WT1VGSnpUMlE1TldSRGVqbHFNRmh6VTBoQlUwMVNaVlYzVmsxR05YaEhRV2M1WWpSU2VFSllNRTg0VFZOQk9GSnVXSEJ6RWhkVFoxcE9XbEJoVVVNMWVXVTFUbTlRYVUxaGVUQkJPQm9pUVU4dE1ISnNObXhKUkdKdVIzaFlTMUZrVkZsT2JFbDJRVEJVTFRkWVpUWklVUSIsImZjdiI6IjMiLCJlaSI6IlNnWk5aUGFRQzV5ZTVOb1BpTWF5MEE4IiwicWMiOiJDaTloYkdWemMyRnVaSEp2SUc5eWMyOGdaMlZ2Y21kcFlTQnBibk4wYVhSMWRHVWdiMllnZEdWamFHNXZiRzluZVJBQWZSZHpNVDgiLCJxdWVzdGlvbiI6IkhvdyBtdWNoIGlzIHRoZSBHZW9yZ2lhIFRlY2ggZW5kb3dtZW50PyIsImxrIjoiR2lab2IzY2diWFZqYUNCcGN5QjBhR1VnWjJWdmNtZHBZU0IwWldOb0lHVnVaRzkzYldWdWRBIiwiYnMiOiJjLVBTNFZMM3lDOVh5QzFOemxESUxGWW95VWhWY0VfTkwwclBURlFJU1FXS3BlYWw1SmZucHVhVjJFczhzLVN5NWJJSXowZ3NVVWpKVHkyR3FfUE1LeTdKTENrdFNWWElUd05yeXN2UHlVLXZWQ2d1U0UzT1RNekpyRXBWeU15emw1Z2V3V1hIWlFuV0RyVW9yVFFuUnlFdk1SZXNrWUJwOWhMX3ZMbU11SFRETTRBR2w1U21WQ29BelNHbzU0cWdBQ01BIiwiaWQiOiJmY18xIn0=",
  "serpapi_link":
  "https://serpapi.com/search.json?device=desktop&engine=google_related_questions&google_domain=google.com&next_page_token=eyJvbnMiOiIxMDA0MSIsImZjIjoiRW9zQkNreEJSWE0zYWs1VFIwbzBhV3hUZDNad1IxTkZaMUpOTW5WT1VGSnpUMlE1TldSRGVqbHFNRmh6VTBoQlUwMVNaVlYzVmsxR05YaEhRV2M1WWpSU2VFSllNRTg0VFZOQk9GSnVXSEJ6RWhkVFoxcE9XbEJoVVVNMWVXVTFUbTlRYVUxaGVUQkJPQm9pUVU4dE1ISnNObXhKUkdKdVIzaFlTMUZrVkZsT2JFbDJRVEJVTFRkWVpUWklVUSIsImZjdiI6IjMiLCJlaSI6IlNnWk5aUGFRQzV5ZTVOb1BpTWF5MEE4IiwicWMiOiJDaTloYkdWemMyRnVaSEp2SUc5eWMyOGdaMlZ2Y21kcFlTQnBibk4wYVhSMWRHVWdiMllnZEdWamFHNXZiRzluZVJBQWZSZHpNVDgiLCJxdWVzdGlvbiI6IkhvdyBtdWNoIGlzIHRoZSBHZW9yZ2lhIFRlY2ggZW5kb3dtZW50PyIsImxrIjoiR2lab2IzY2diWFZqYUNCcGN5QjBhR1VnWjJWdmNtZHBZU0IwWldOb0lHVnVaRzkzYldWdWRBIiwiYnMiOiJjLVBTNFZMM3lDOVh5QzFOemxESUxGWW95VWhWY0VfTkwwclBURlFJU1FXS3BlYWw1SmZucHVhVjJFczhzLVN5NWJJSXowZ3NVVWpKVHkyR3FfUE1LeTdKTENrdFNWWElUd05yeXN2UHlVLXZWQ2d1U0UzT1RNekpyRXBWeU15emw1Z2V3V1hIWlFuV0RyVW9yVFFuUnlFdk1SZXNrWUJwOWhMX3ZMbU11SFRETTRBR2w1U21WQ29BelNHbzU0cWdBQ01BIiwiaWQiOiJmY18xIn0%3D"
  },
  {
  "question":
  "What does Georgia Institute of Technology specialize in?",
  "snippet":
  "Tech's engineering and computing Colleges are the largest and among the highest-ranked in the nation. The Institute also offers outstanding programs in business, design, liberal arts, and sciences.",
  "title":
  "About Georgia Tech",
  "link":
  "https://www.gatech.edu/about#:~:text=Tech's%20engineering%20and%20computing%20Colleges,%2C%20liberal%20arts%2C%20and%20sciences.",
  "displayed_link":
  "https://www.gatech.edu › about",
  "next_page_token":
  "eyJvbnMiOiIxMDA0MSIsImZjIjoiRW9zQkNreEJSWE0zYWs1VFIwbzBhV3hUZDNad1IxTkZaMUpOTW5WT1VGSnpUMlE1TldSRGVqbHFNRmh6VTBoQlUwMVNaVlYzVmsxR05YaEhRV2M1WWpSU2VFSllNRTg0VFZOQk9GSnVXSEJ6RWhkVFoxcE9XbEJoVVVNMWVXVTFUbTlRYVUxaGVUQkJPQm9pUVU4dE1ISnNObXhKUkdKdVIzaFlTMUZrVkZsT2JFbDJRVEJVTFRkWVpUWklVUSIsImZjdiI6IjMiLCJlaSI6IlNnWk5aUGFRQzV5ZTVOb1BpTWF5MEE4IiwicWMiOiJDaTloYkdWemMyRnVaSEp2SUc5eWMyOGdaMlZ2Y21kcFlTQnBibk4wYVhSMWRHVWdiMllnZEdWamFHNXZiRzluZVJBQWZSZHpNVDgiLCJxdWVzdGlvbiI6IldoYXQgZG9lcyBHZW9yZ2lhIEluc3RpdHV0ZSBvZiBUZWNobm9sb2d5IHNwZWNpYWxpemUgaW4/IiwibGsiOiJHamQzYUdGMElHUnZaWE1nWjJWdmNtZHBZU0JwYm5OMGFYUjFkR1VnYjJZZ2RHVmphRzV2Ykc5bmVTQnpjR1ZqYVdGc2FYcGxJR2x1IiwiYnMiOiJjLVBTNFZMM3lDOVh5QzFOemxESUxGWW95VWhWY0VfTkwwclBURlFJU1FXS3BlYWw1SmZucHVhVjJFczhzLVN5NWJJSXowZ3NVVWpKVHkyR3FfUE1LeTdKTENrdFNWWElUd05yeXN2UHlVLXZWQ2d1U0UzT1RNekpyRXBWeU15emw1Z2V3V1hIWlFuV0RyVW9yVFFuUnlFdk1SZXNrWUJwOWhMX3ZMbU11SFRETTRBR2w1U21WQ29BelNHbzU0cWdBQ01BIiwiaWQiOiJmY18xIn0=",
  "serpapi_link":
  "https://serpapi.com/search.json?device=desktop&engine=google_related_questions&google_domain=google.com&next_page_token=eyJvbnMiOiIxMDA0MSIsImZjIjoiRW9zQkNreEJSWE0zYWs1VFIwbzBhV3hUZDNad1IxTkZaMUpOTW5WT1VGSnpUMlE1TldSRGVqbHFNRmh6VTBoQlUwMVNaVlYzVmsxR05YaEhRV2M1WWpSU2VFSllNRTg0VFZOQk9GSnVXSEJ6RWhkVFoxcE9XbEJoVVVNMWVXVTFUbTlRYVUxaGVUQkJPQm9pUVU4dE1ISnNObXhKUkdKdVIzaFlTMUZrVkZsT2JFbDJRVEJVTFRkWVpUWklVUSIsImZjdiI6IjMiLCJlaSI6IlNnWk5aUGFRQzV5ZTVOb1BpTWF5MEE4IiwicWMiOiJDaTloYkdWemMyRnVaSEp2SUc5eWMyOGdaMlZ2Y21kcFlTQnBibk4wYVhSMWRHVWdiMllnZEdWamFHNXZiRzluZVJBQWZSZHpNVDgiLCJxdWVzdGlvbiI6IldoYXQgZG9lcyBHZW9yZ2lhIEluc3RpdHV0ZSBvZiBUZWNobm9sb2d5IHNwZWNpYWxpemUgaW4%2FIiwibGsiOiJHamQzYUdGMElHUnZaWE1nWjJWdmNtZHBZU0JwYm5OMGFYUjFkR1VnYjJZZ2RHVmphRzV2Ykc5bmVTQnpjR1ZqYVdGc2FYcGxJR2x1IiwiYnMiOiJjLVBTNFZMM3lDOVh5QzFOemxESUxGWW95VWhWY0VfTkwwclBURlFJU1FXS3BlYWw1SmZucHVhVjJFczhzLVN5NWJJSXowZ3NVVWpKVHkyR3FfUE1LeTdKTENrdFNWWElUd05yeXN2UHlVLXZWQ2d1U0UzT1RNekpyRXBWeU15emw1Z2V3V1hIWlFuV0RyVW9yVFFuUnlFdk1SZXNrWUJwOWhMX3ZMbU11SFRETTRBR2w1U21WQ29BelNHbzU0cWdBQ01BIiwiaWQiOiJmY18xIn0%3D"
  },
  {
  "question":
  "What is the full name of Georgia Institute of Technology?",
  "snippet":
  "During its first 50 years, Tech grew from a narrowly focused trade school to a regionally recognized technological university. In 1948, the School's name was changed to the Georgia Institute of Technology to reflect a growing focus on advanced technological and scientific research.",
  "title":
  "History and Traditions - Georgia Tech",
  "link":
  "https://www.gatech.edu/about/history-traditions#:~:text=During%20its%20first%2050%20years,advanced%20technological%20and%20scientific%20research.",
  "displayed_link":
  "https://www.gatech.edu › about › history-traditions",
  "next_page_token":
  "eyJvbnMiOiIxMDA0MSIsImZjIjoiRW9zQkNreEJSWE0zYWs1VFIwbzBhV3hUZDNad1IxTkZaMUpOTW5WT1VGSnpUMlE1TldSRGVqbHFNRmh6VTBoQlUwMVNaVlYzVmsxR05YaEhRV2M1WWpSU2VFSllNRTg0VFZOQk9GSnVXSEJ6RWhkVFoxcE9XbEJoVVVNMWVXVTFUbTlRYVUxaGVUQkJPQm9pUVU4dE1ISnNObXhKUkdKdVIzaFlTMUZrVkZsT2JFbDJRVEJVTFRkWVpUWklVUSIsImZjdiI6IjMiLCJlaSI6IlNnWk5aUGFRQzV5ZTVOb1BpTWF5MEE4IiwicWMiOiJDaTloYkdWemMyRnVaSEp2SUc5eWMyOGdaMlZ2Y21kcFlTQnBibk4wYVhSMWRHVWdiMllnZEdWamFHNXZiRzluZVJBQWZSZHpNVDgiLCJxdWVzdGlvbiI6IldoYXQgaXMgdGhlIGZ1bGwgbmFtZSBvZiBHZW9yZ2lhIEluc3RpdHV0ZSBvZiBUZWNobm9sb2d5PyIsImxrIjoiR2lsblpXOXlaMmxoSUdsdWMzUnBkSFYwWlNCdlppQjBaV05vYm05c2IyZDVJR1oxYkd3Z2JtRnRaUSIsImJzIjoiYy1QUzRWTDN5QzlYeUMxTnpsRElMRllveVVoVmNFX05MMHJQVEZRSVNRV0twZWFsNUpmbnB1YVYyRXM4cy1TeTViSUl6MGdzVVVqSlR5MkdxX1BNS3k3SkxDa3RTVlhJVHdOcnlzdlB5VS12VkNndVNFM09UTXpKckVwVnlNeXpsNWdld1dYSFpRbldEclVvclRRblJ5RXZNUmVza1lCcDloTF92TG1NdUhURE00QUdsNVNtVkNvQXpTR281NHFnQUNNQSIsImlkIjoiZmNfMSJ9",
  "serpapi_link":
  "https://serpapi.com/search.json?device=desktop&engine=google_related_questions&google_domain=google.com&next_page_token=eyJvbnMiOiIxMDA0MSIsImZjIjoiRW9zQkNreEJSWE0zYWs1VFIwbzBhV3hUZDNad1IxTkZaMUpOTW5WT1VGSnpUMlE1TldSRGVqbHFNRmh6VTBoQlUwMVNaVlYzVmsxR05YaEhRV2M1WWpSU2VFSllNRTg0VFZOQk9GSnVXSEJ6RWhkVFoxcE9XbEJoVVVNMWVXVTFUbTlRYVUxaGVUQkJPQm9pUVU4dE1ISnNObXhKUkdKdVIzaFlTMUZrVkZsT2JFbDJRVEJVTFRkWVpUWklVUSIsImZjdiI6IjMiLCJlaSI6IlNnWk5aUGFRQzV5ZTVOb1BpTWF5MEE4IiwicWMiOiJDaTloYkdWemMyRnVaSEp2SUc5eWMyOGdaMlZ2Y21kcFlTQnBibk4wYVhSMWRHVWdiMllnZEdWamFHNXZiRzluZVJBQWZSZHpNVDgiLCJxdWVzdGlvbiI6IldoYXQgaXMgdGhlIGZ1bGwgbmFtZSBvZiBHZW9yZ2lhIEluc3RpdHV0ZSBvZiBUZWNobm9sb2d5PyIsImxrIjoiR2lsblpXOXlaMmxoSUdsdWMzUnBkSFYwWlNCdlppQjBaV05vYm05c2IyZDVJR1oxYkd3Z2JtRnRaUSIsImJzIjoiYy1QUzRWTDN5QzlYeUMxTnpsRElMRllveVVoVmNFX05MMHJQVEZRSVNRV0twZWFsNUpmbnB1YVYyRXM4cy1TeTViSUl6MGdzVVVqSlR5MkdxX1BNS3k3SkxDa3RTVlhJVHdOcnlzdlB5VS12VkNndVNFM09UTXpKckVwVnlNeXpsNWdld1dYSFpRbldEclVvclRRblJ5RXZNUmVza1lCcDloTF92TG1NdUhURE00QUdsNVNtVkNvQXpTR281NHFnQUNNQSIsImlkIjoiZmNfMSJ9"
  },
  {
  "question":
  "Why study at Georgia Institute of Technology?",
  "snippet":
  "Georgia Tech's engineering and computing Colleges are the largest and among the highest-ranked in the nation, and the Institute also offers outstanding programs in business, design, liberal arts, and sciences.",
  "title":
  "Georgia Institute of Technology",
  "link":
  "https://www.usg.edu/institutions/profile/georgia_institute_of_technology#:~:text=Georgia%20Tech's%20engineering%20and%20computing,%2C%20liberal%20arts%2C%20and%20sciences.",
  "displayed_link":
  "https://www.usg.edu › institutions › profile › georgia_ins...",
  "thumbnail":
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtqg9m0rSfmdpB-gJZ1HbTlbl-Uj9n1ebX7P9lux0Z-A&s",
  "next_page_token":
  "eyJvbnMiOiIxMDA0MSIsImZjIjoiRW9zQkNreEJSWE0zYWs1VFIwbzBhV3hUZDNad1IxTkZaMUpOTW5WT1VGSnpUMlE1TldSRGVqbHFNRmh6VTBoQlUwMVNaVlYzVmsxR05YaEhRV2M1WWpSU2VFSllNRTg0VFZOQk9GSnVXSEJ6RWhkVFoxcE9XbEJoVVVNMWVXVTFUbTlRYVUxaGVUQkJPQm9pUVU4dE1ISnNObXhKUkdKdVIzaFlTMUZrVkZsT2JFbDJRVEJVTFRkWVpUWklVUSIsImZjdiI6IjMiLCJlaSI6IlNnWk5aUGFRQzV5ZTVOb1BpTWF5MEE4IiwicWMiOiJDaTloYkdWemMyRnVaSEp2SUc5eWMyOGdaMlZ2Y21kcFlTQnBibk4wYVhSMWRHVWdiMllnZEdWamFHNXZiRzluZVJBQWZSZHpNVDgiLCJxdWVzdGlvbiI6IldoeSBzdHVkeSBhdCBHZW9yZ2lhIEluc3RpdHV0ZSBvZiBUZWNobm9sb2d5PyIsImxrIjoiR2l4M2FIa2djM1IxWkhrZ1lYUWdaMlZ2Y21kcFlTQnBibk4wYVhSMWRHVWdiMllnZEdWamFHNXZiRzluZVEiLCJicyI6ImMtUFM0VkwzeUM5WHlDMU56bERJTEZZb3lVaFZjRV9OTDByUFRGUUlTUVdLcGVhbDVKZm5wdWFWMkVzOHMtU3k1YklJejBnc1VVakpUeTJHcV9QTUt5N0pMQ2t0U1ZYSVR3TnJ5c3ZQeVUtdlZDZ3VTRTNPVE16SnJFcFZ5TXl6bDVnZXdXWEhaUW5XRHJVb3JUUW5SeUV2TVJlc2tZQnA5aExfdkxtTXVIVERNNEFHbDVTbVZDb0F6U0dvNTRxZ0FDTUEiLCJpZCI6ImZjXzEifQ==",
  "serpapi_link":
  "https://serpapi.com/search.json?device=desktop&engine=google_related_questions&google_domain=google.com&next_page_token=eyJvbnMiOiIxMDA0MSIsImZjIjoiRW9zQkNreEJSWE0zYWs1VFIwbzBhV3hUZDNad1IxTkZaMUpOTW5WT1VGSnpUMlE1TldSRGVqbHFNRmh6VTBoQlUwMVNaVlYzVmsxR05YaEhRV2M1WWpSU2VFSllNRTg0VFZOQk9GSnVXSEJ6RWhkVFoxcE9XbEJoVVVNMWVXVTFUbTlRYVUxaGVUQkJPQm9pUVU4dE1ISnNObXhKUkdKdVIzaFlTMUZrVkZsT2JFbDJRVEJVTFRkWVpUWklVUSIsImZjdiI6IjMiLCJlaSI6IlNnWk5aUGFRQzV5ZTVOb1BpTWF5MEE4IiwicWMiOiJDaTloYkdWemMyRnVaSEp2SUc5eWMyOGdaMlZ2Y21kcFlTQnBibk4wYVhSMWRHVWdiMllnZEdWamFHNXZiRzluZVJBQWZSZHpNVDgiLCJxdWVzdGlvbiI6IldoeSBzdHVkeSBhdCBHZW9yZ2lhIEluc3RpdHV0ZSBvZiBUZWNobm9sb2d5PyIsImxrIjoiR2l4M2FIa2djM1IxWkhrZ1lYUWdaMlZ2Y21kcFlTQnBibk4wYVhSMWRHVWdiMllnZEdWamFHNXZiRzluZVEiLCJicyI6ImMtUFM0VkwzeUM5WHlDMU56bERJTEZZb3lVaFZjRV9OTDByUFRGUUlTUVdLcGVhbDVKZm5wdWFWMkVzOHMtU3k1YklJejBnc1VVakpUeTJHcV9QTUt5N0pMQ2t0U1ZYSVR3TnJ5c3ZQeVUtdlZDZ3VTRTNPVE16SnJFcFZ5TXl6bDVnZXdXWEhaUW5XRHJVb3JUUW5SeUV2TVJlc2tZQnA5aExfdkxtTXVIVERNNEFHbDVTbVZDb0F6U0dvNTRxZ0FDTUEiLCJpZCI6ImZjXzEifQ%3D%3D"
  }
  ],
  "organic_results":
  [
  {
  "position":
  1,
  "title":
  "Alessandro Orso - College of Computing - Georgia Tech",
  "link":
  "https://www.cc.gatech.edu/people/alessandro-orso",
  "displayed_link":
  "https://www.cc.gatech.edu › people › alessandro-orso",
  "date":
  "Oct 7, 2017",
  "snippet":
  "Alessandro Orso is a Professor and Associate School Chair in the College of Computing at the Georgia Institute of Technology. He received his M.S. degree in ...",
  "snippet_highlighted_words":
  [
  "Alessandro Orso",
  "Georgia Institute of Technology"
  ],
  "about_this_result":
  {
  "source":
  {
  "description":
  "The College of Computing is a college of the Georgia Institute of Technology, a public research university in Atlanta, Georgia.",
  "source_info_link":
  "https://www.cc.gatech.edu/people/alessandro-orso",
  "security":
  "secure",
  "icon":
  "https://serpapi.com/searches/644d0649aef264d32181a514/images/22031757ecf65711f2e686f4c7a2eeef3e2cbda90c784c65aefe32f773ff091ce20f30aa1a92f8b8d6fd5104b86b73e9.png"
  }
  },
  "about_page_link":
  "https://www.google.com/search?q=About+https://www.cc.gatech.edu/people/alessandro-orso&tbm=ilp&ilps=ADJL0iy7Rt8t-0PVQXnFCuPVfVxHaze51A",
  "about_page_serpapi_link":
  "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0iy7Rt8t-0PVQXnFCuPVfVxHaze51A&q=About+https%3A%2F%2Fwww.cc.gatech.edu%2Fpeople%2Falessandro-orso",
  "cached_page_link":
  "https://webcache.googleusercontent.com/search?q=cache:q8BdMdsu70EJ:https://www.cc.gatech.edu/people/alessandro-orso&cd=10&hl=en&ct=clnk&gl=us",
  "source":
  "Georgia Tech",
  "related_results":
  [
  {
  "position":
  1,
  "title":
  "Alex Orso - Home Page - College of Computing - Georgia Tech",
  "link":
  "https://www.cc.gatech.edu/home/orso/",
  "displayed_link":
  "https://www.cc.gatech.edu › home › orso",
  "date":
  "Oct 7, 2017",
  "snippet":
  "Bio: Alessandro Orso is a Professor in the School of Computer Science and an Associate Dean in the College of Computing at the Georgia Institute ...",
  "snippet_highlighted_words":
  [
  "Alessandro Orso",
  "Georgia Institute"
  ],
  "about_this_result":
  {
  "source":
  {
  "description":
  "The College of Computing is a college of the Georgia Institute of Technology, a public research university in Atlanta, Georgia.",
  "source_info_link":
  "https://www.cc.gatech.edu/home/orso/",
  "security":
  "secure",
  "icon":
  "https://serpapi.com/searches/644d0649aef264d32181a514/images/22031757ecf65711f2e686f4c7a2eeef4b41e0339c2d51aa4fba156ce58a034a9472f6b7fa2a9981f52acc0c338f0f7643ecd125c81c321d9baf186f59cec19f3dadaf8615f8cae0.png"
  }
  },
  "about_page_link":
  "https://www.google.com/search?q=About+https://www.cc.gatech.edu/home/orso/&tbm=ilp&ilps=ADJL0iyUIkyY9CmDpMaB1m-QZRYNqv_Z8g",
  "about_page_serpapi_link":
  "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0iyUIkyY9CmDpMaB1m-QZRYNqv_Z8g&q=About+https%3A%2F%2Fwww.cc.gatech.edu%2Fhome%2Forso%2F",
  "cached_page_link":
  "https://webcache.googleusercontent.com/search?q=cache:oLPVyvNppSsJ:https://www.cc.gatech.edu/home/orso/&cd=11&hl=en&ct=clnk&gl=us"
  }
  ]
  },
  {
  "position":
  2,
  "title":
  "Alessandro Orso - Georgia Institute of Technology",
  "link":
  "https://www.linkedin.com/in/alexorso",
  "displayed_link":
  "https://www.linkedin.com › alexorso",
  "snippet":
  "Experience · Associate Dean · Professor · Expert Witness.",
  "about_this_result":
  {
  "source":
  {
  "description":
  "LinkedIn is a business and employment-focused social media platform that works through websites and mobile apps. It launched on May 5, 2003. It is now owned by Microsoft.",
  "source_info_link":
  "https://www.linkedin.com/in/alexorso",
  "security":
  "secure",
  "icon":
  "https://serpapi.com/searches/644d0649aef264d32181a514/images/22031757ecf65711f2e686f4c7a2eeef810017625bba058d97faa58dd16994871aae2c69ac7827e34bc3eee5efa0d983.png"
  }
  },
  "about_page_link":
  "https://www.google.com/search?q=About+https://www.linkedin.com/in/alexorso&tbm=ilp&ilps=ADJL0iwqL0o82a1fGs1PPKZq0hjeH26oJw",
  "about_page_serpapi_link":
  "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0iwqL0o82a1fGs1PPKZq0hjeH26oJw&q=About+https%3A%2F%2Fwww.linkedin.com%2Fin%2Falexorso",
  "cached_page_link":
  "/search?hl=en&gl=us&q=related:https://www.linkedin.com/in/alexorso+Alessandro+Orso+Georgia+Institute+of+Technology",
  "source":
  "LinkedIn"
  },
  {
  "position":
  3,
  "title":
  "Alessandro Orso",
  "link":
  "https://scholar.google.com/citations?user=wCfYkMkAAAAJ&hl=en",
  "displayed_link":
  "https://scholar.google.com › citations",
  "snippet":
  "Professor of Computer Science, Georgia Institute of Technology - ‪‪Cited by 13931‬‬ - ‪Software Engineering‬ - ‪Programming Languages‬ - ‪Security‬",
  "snippet_highlighted_words":
  [
  "Georgia Institute of Technology"
  ],
  "about_this_result":
  {
  "source":
  {
  "description":
  "Google Scholar is a freely accessible web search engine that indexes the full text or metadata of scholarly literature across an array of publishing formats and disciplines.",
  "source_info_link":
  "https://scholar.google.com/citations?user=wCfYkMkAAAAJ&hl=en",
  "security":
  "secure",
  "icon":
  "https://serpapi.com/searches/644d0649aef264d32181a514/images/22031757ecf65711f2e686f4c7a2eeefebf226a62fccddbf2eb0e66c50d43dc683d426bbd2c53247142b42e00c110302.png"
  }
  },
  "about_page_link":
  "https://www.google.com/search?q=About+https://scholar.google.com/citations?user%3DwCfYkMkAAAAJ%26hl%3Den&tbm=ilp&ilps=ADJL0ixx5rytKC61P13_u_OeYHZvclg0YQ",
  "about_page_serpapi_link":
  "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0ixx5rytKC61P13_u_OeYHZvclg0YQ&q=About+https%3A%2F%2Fscholar.google.com%2Fcitations%3Fuser%3DwCfYkMkAAAAJ%26hl%3Den",
  "cached_page_link":
  "https://webcache.googleusercontent.com/search?q=cache:81SvMFuxUSQJ:https://scholar.google.com/citations%3Fuser%3DwCfYkMkAAAAJ%26hl%3Den&cd=13&hl=en&ct=clnk&gl=us",
  "source":
  "Google"
  },
  {
  "position":
  4,
  "title":
  "Alessandro Orso | IEEE Xplore Author Details",
  "link":
  "https://ieeexplore.ieee.org/author/37267738200",
  "displayed_link":
  "https://ieeexplore.ieee.org › author",
  "snippet":
  "He is a professor with the School of Computer Science and an associate dean with the College of Computing, the Georgia Institute of Technology. From March 2000, ...",
  "snippet_highlighted_words":
  [
  "Georgia Institute of Technology"
  ],
  "about_this_result":
  {
  "source":
  {
  "description":
  "The Institute of Electrical and Electronics Engineers is a 501 professional association for electronics engineering, electrical engineering, and other related disciplines with its corporate office in New York City and its operations center in Piscataway, New Jersey.",
  "source_info_link":
  "https://ieeexplore.ieee.org/author/37267738200",
  "security":
  "secure",
  "icon":
  "https://serpapi.com/searches/644d0649aef264d32181a514/images/22031757ecf65711f2e686f4c7a2eeef6cd49cf120536421e626ab5991eee391e0ce0b7bddc1b89a148c4fd1528719ee.png"
  }
  },
  "about_page_link":
  "https://www.google.com/search?q=About+https://ieeexplore.ieee.org/author/37267738200&tbm=ilp&ilps=ADJL0ix-jiZvAl3jYl1d6jFbVDsobvTyIw",
  "about_page_serpapi_link":
  "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0ix-jiZvAl3jYl1d6jFbVDsobvTyIw&q=About+https%3A%2F%2Fieeexplore.ieee.org%2Fauthor%2F37267738200",
  "source":
  "Institute of Electrical and Electronics Engineers"
  },
  {
  "position":
  5,
  "title":
  "Alessandro (Alex) Orso",
  "link":
  "https://isr.uci.edu/content/alessandro-alex-orso",
  "displayed_link":
  "https://isr.uci.edu › content › alessandro-alex-orso",
  "snippet":
  "Alessandro Orso is a Professor in the College of Computing at the Georgia Institute of Technology. He received his M.S. degree in Electrical Engineering ...",
  "snippet_highlighted_words":
  [
  "Alessandro Orso",
  "Georgia Institute of Technology"
  ],
  "about_this_result":
  {
  "source":
  {
  "description":
  "The University of California, Irvine is a public land-grant research university in Irvine, California.",
  "source_info_link":
  "https://isr.uci.edu/content/alessandro-alex-orso",
  "security":
  "secure",
  "icon":
  "https://serpapi.com/searches/644d0649aef264d32181a514/images/22031757ecf65711f2e686f4c7a2eeef9b6da904e17756822c922f99186dd3318c338e8116375900cee87a99dbedb1c6.png"
  }
  },
  "about_page_link":
  "https://www.google.com/search?q=About+https://isr.uci.edu/content/alessandro-alex-orso&tbm=ilp&ilps=ADJL0iynaJlEWMxYGerYgHJNIZ2FjBmikQ",
  "about_page_serpapi_link":
  "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0iynaJlEWMxYGerYgHJNIZ2FjBmikQ&q=About+https%3A%2F%2Fisr.uci.edu%2Fcontent%2Falessandro-alex-orso",
  "cached_page_link":
  "https://webcache.googleusercontent.com/search?q=cache:HSbZ9qHCRZwJ:https://isr.uci.edu/content/alessandro-alex-orso&cd=25&hl=en&ct=clnk&gl=us",
  "source":
  "University of California, Irvine"
  },
  {
  "position":
  6,
  "title":
  "Alessandro Orso",
  "link":
  "https://dblp.org/pid/35/805",
  "displayed_link":
  "https://dblp.org › Persons",
  "snippet":
  "List of computer science publications by Alessandro Orso. ... affiliation: Georgia Institute of Technology, Atlanta GA, USA.",
  "snippet_highlighted_words":
  [
  "Alessandro Orso",
  "Georgia Institute of Technology"
  ],
  "about_this_result":
  {
  "source":
  {
  "description":
  "DBLP is a computer science bibliography website. Starting in 1993 at Universität Trier in Germany, it grew from a small collection of HTML files and became an organization hosting a database and logic programming bibliography site.",
  "source_info_link":
  "https://dblp.org/pid/35/805",
  "security":
  "secure",
  "icon":
  "https://serpapi.com/searches/644d0649aef264d32181a514/images/22031757ecf65711f2e686f4c7a2eeef26e3a71d06e14d1396d8fc3a14f3a34e4e848741784d4d7599d96f303f6313b9.png"
  }
  },
  "about_page_link":
  "https://www.google.com/search?q=About+https://dblp.org/pid/35/805&tbm=ilp&ilps=ADJL0ixoHIIftEN3tdR8yB4xJj6pHg5r5g",
  "about_page_serpapi_link":
  "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0ixoHIIftEN3tdR8yB4xJj6pHg5r5g&q=About+https%3A%2F%2Fdblp.org%2Fpid%2F35%2F805",
  "source":
  "DBLP"
  },
  {
  "position":
  7,
  "title":
  "Alex Orso (@alexorso) / Twitter",
  "link":
  "https://twitter.com/alexorso?lang=en",
  "displayed_link":
  "https://twitter.com › alexorso",
  "snippet":
  "The Scientific Software Engineering Center at Georgia Tech seeks software engineers at various seniority levels to build better scientific software.",
  "snippet_highlighted_words":
  [
  "Georgia Tech"
  ],
  "about_this_result":
  {
  "source":
  {
  "description":
  "This result comes from twitter.com",
  "source_info_link":
  "https://twitter.com/alexorso?lang=en",
  "security":
  "secure",
  "icon":
  "https://serpapi.com/searches/644d0649aef264d32181a514/images/22031757ecf65711f2e686f4c7a2eeef812d44916cbf85878c6c735dce288ac38d2579836e69bd3097b498dcbc3bc661.png"
  }
  },
  "about_page_link":
  "https://www.google.com/search?q=About+https://twitter.com/alexorso&tbm=ilp&ilps=ADJL0izyZEvdEjb4kqfXybhokPeZvDTZ8w",
  "about_page_serpapi_link":
  "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0izyZEvdEjb4kqfXybhokPeZvDTZ8w&q=About+https%3A%2F%2Ftwitter.com%2Falexorso",
  "cached_page_link":
  "https://webcache.googleusercontent.com/search?q=cache:KImtEtgboRMJ:https://twitter.com/alexorso%3Flang%3Den&cd=27&hl=en&ct=clnk&gl=us",
  "related_pages_link":
  "https://www.google.com/search?hl=en&gl=us&q=related:https://twitter.com/alexorso%3Flang%3Den+Alessandro+Orso+Georgia+Institute+of+Technology",
  "source":
  "Twitter"
  },
  {
  "position":
  8,
  "title":
  "Alessandro (Alex) Orso, PhD - Atlanta GA",
  "link":
  "https://hip.emory.edu/faculty/bios/orso_alex.html",
  "displayed_link":
  "https://hip.emory.edu › faculty › bios › orso_alex",
  "snippet":
  "... Alessandro (Alex) Orso, PhD. Alessandro (Alex) Orso, PhD. Associate Professor, Georgia Tech College of Computing. Email. orso@cc.gatech.edu. Phone.",
  "snippet_highlighted_words":
  [
  "Alex",
  "Orso",
  "Alex",
  "Orso",
  "Georgia Tech",
  "gatech"
  ],
  "about_this_result":
  {
  "source":
  {
  "description":
  "Emory University is a private research university in Atlanta, Georgia. Founded in 1836 as Emory College by the Methodist Episcopal Church and named in honor of Methodist bishop John Emory, Emory is the second-oldest private institution of higher education in Georgia.",
  "source_info_link":
  "https://hip.emory.edu/faculty/bios/orso_alex.html",
  "security":
  "secure"
  }
  },
  "about_page_link":
  "https://www.google.com/search?q=About+https://hip.emory.edu/faculty/bios/orso_alex.html&tbm=ilp&ilps=ADJL0iyIskRXmqvWegCybSwZmcDUlBGOmg",
  "about_page_serpapi_link":
  "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0iyIskRXmqvWegCybSwZmcDUlBGOmg&q=About+https%3A%2F%2Fhip.emory.edu%2Ffaculty%2Fbios%2Forso_alex.html",
  "cached_page_link":
  "https://webcache.googleusercontent.com/search?q=cache:8vx7sg1ma4UJ:https://hip.emory.edu/faculty/bios/orso_alex.html&cd=28&hl=en&ct=clnk&gl=us",
  "source":
  "Emory University"
  },
  {
  "position":
  9,
  "title":
  "Alessandro Orso Georgia Institute of Technology | GT",
  "link":
  "https://www.researchgate.net/profile/Alessandro_Orso/9",
  "displayed_link":
  "https://www.researchgate.net › ... › College of Computing",
  "snippet":
  "Alessandro ORSO, Professor (Full) | Cited by 8921 | of Georgia Institute of Technology, Georgia (GT) | Read 173 publications | Contact Alessandro ORSO.",
  "snippet_highlighted_words":
  [
  "Alessandro ORSO",
  "Georgia Institute of Technology",
  "Alessandro ORSO"
  ],
  "about_this_result":
  {
  "source":
  {
  "description":
  "ResearchGate is a European commercial social networking site for scientists and researchers to share papers, ask and answer questions, and find collaborators.",
  "source_info_link":
  "https://www.researchgate.net/profile/Alessandro_Orso/9",
  "security":
  "secure",
  "icon":
  "https://serpapi.com/searches/644d0649aef264d32181a514/images/22031757ecf65711f2e686f4c7a2eeef0792aab72d1486f55cd95b08421fa54667ff8d99b1cfba568359c5667b3ba5fb.png"
  }
  },
  "about_page_link":
  "https://www.google.com/search?q=About+https://www.researchgate.net/profile/Alessandro_Orso/9&tbm=ilp&ilps=ADJL0iwGzV3JPZf_94cIVsUgkpOovR7nNg",
  "about_page_serpapi_link":
  "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0iwGzV3JPZf_94cIVsUgkpOovR7nNg&q=About+https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FAlessandro_Orso%2F9",
  "source":
  "ResearchGate"
  }
  ],
  "related_searches":
  [
  {
  "query":
  "alessandro orso rate my professor",
  "link":
  "https://www.google.com/search?hl=en&gl=us&q=Alessandro+Orso+rate+my+Professor&sa=X&ved=2ahUKEwj23eXphM_-AhUcD1kFHQijDPoQ1QJ6BAg8EAE"
  }
  ],
  "pagination":
  {
  "current":
  1,
  "next":
  "https://www.google.com/search?q=Alessandro+Orso+Georgia+Institute+of+Technology&oq=Alessandro+Orso+Georgia+Institute+of+Technology&hl=en&gl=us&start=10&sourceid=chrome&ie=UTF-8",
  "other_pages":
  {
  "https://www.google.com/search?q=Alessandro+Orso+Georgia+Institute+of+Technology&oq=Alessandro+Orso+Georgia+Institute+of+Technology&hl=en&gl=us&start=10&sourceid=chrome&ie=UTF-8",
  "https://www.google.com/search?q=Alessandro+Orso+Georgia+Institute+of+Technology&oq=Alessandro+Orso+Georgia+Institute+of+Technology&hl=en&gl=us&start=20&sourceid=chrome&ie=UTF-8",
  "https://www.google.com/search?q=Alessandro+Orso+Georgia+Institute+of+Technology&oq=Alessandro+Orso+Georgia+Institute+of+Technology&hl=en&gl=us&start=30&sourceid=chrome&ie=UTF-8",
  "https://www.google.com/search?q=Alessandro+Orso+Georgia+Institute+of+Technology&oq=Alessandro+Orso+Georgia+Institute+of+Technology&hl=en&gl=us&start=40&sourceid=chrome&ie=UTF-8"
  }
  },
  "serpapi_pagination":
  {
  "current":
  1,
  "next_link":
  "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=Alessandro+Orso+Georgia+Institute+of+Technology&start=10",
  "next":
  "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=Alessandro+Orso+Georgia+Institute+of+Technology&start=10",
  "other_pages":
  {
  "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=Alessandro+Orso+Georgia+Institute+of+Technology&start=10",
  "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=Alessandro+Orso+Georgia+Institute+of+Technology&start=20",
  "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=Alessandro+Orso+Georgia+Institute+of+Technology&start=30",
  "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=Alessandro+Orso+Georgia+Institute+of+Technology&start=40"
  }
  }
  }}
  return report





















#{'report': [{'position': 1, 'title': 'Yann LeCun', 'link': 'https://en.wikipedia.org/wiki/Yann_LeCun', 'displayed_link': 'https://en.wikipedia.org › wiki › Yann_LeCun', 'snippet': 'He is the Silver Professor of the Courant Institute of Mathematical Sciences at New York University and Vice-President, Chief AI Scientist at Meta.', 'snippet_highlighted_words': ['Silver Professor', 'Courant Institute', 'New York', 'Chief AI Scientist'], 'sitelinks': {'inline': [{'title': 'ESIEE Paris', 'link': 'https://en.wikipedia.org/wiki/ESIEE_Paris'}, {'title': 'DjVu', 'link': 'https://en.wikipedia.org/wiki/DjVu'}, {'title': 'Soisy-sous-Montmorency', 'link': 'https://en.wikipedia.org/wiki/Soisy-sous-Montmorency'}, {'title': 'Léon Bottou', 'link': 'https://en.wikipedia.org/wiki/L%C3%A9on_Bottou'}]}, 'about_this_result': {'keywords': ['yann', 'lecun', 'chief', 'ai', 'scientist', 'facebook', 'silver', 'professor', 'courant', 'institute', 'new', 'york'], 'languages': ['English'], 'regions': ['United States']}, 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:4d8mUyF0fZ0J:https://en.wikipedia.org/wiki/Yann_LeCun&cd=10&hl=en&ct=clnk&gl=us', 'related_pages_link': 'https://www.google.com/search?q=related:https://en.wikipedia.org/wiki/Yann_LeCun+Yann+LeCun+Chief+AI+Scientist+at+Facebook+%26+Silver+Professor+at+the+Courant+Institute,+New+York+%E2%80%A6', 'source': 'Wikipedia'}, 
#{'position': 2, 'title': 'Yann LeCun', 'link': 'https://ai.facebook.com/people/yann-lecun/', 'displayed_link': 'https://ai.facebook.com › people › yann-lecun', 'snippet': 'Yann is the Chief AI Scientist for Facebook AI Research (FAIR), joining Facebook in December 2013. He is also a Silver Professor at New York University...', 'snippet_highlighted_words': ['Yann', 'Chief AI Scientist', 'Facebook AI', 'Facebook', 'Silver Professor', 'New York'], 'about_this_result': {'keywords': ['yann', 'lecun', 'chief', 'ai', 'scientist', 'facebook', 'silver', 'professor', 'courant', 'institute', 'new', 'york'], 'languages': ['English'], 'regions': ['United States']}, 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:DiV6HaabHGwJ:https://ai.facebook.com/people/yann-lecun/&cd=11&hl=en&ct=clnk&gl=us', 'source': 'Facebook', 'related_results': [{'position': 1, 'title': 'Yann LeCun - Meta Research - Facebook', 'link': 'https://research.facebook.com/people/lecun-yann/', 'displayed_link': 'https://research.facebook.com › people › lecun-yann', 'snippet': 'I am Chief AI Scientist for Meta AI Research (FAIR), joining Meta in December 2013. I am also a Silver Professor at New York University on a part time basis ...', 'snippet_highlighted_words': ['Chief AI Scientist', 'AI', 'Silver Professor', 'New York'], 'about_this_result': {'keywords': ['yann', 'lecun', 'chief', 'ai', 'scientist', 'facebook', 'silver', 'professor', 'courant', 'institute', 'new', 'york'], 'languages': ['English'], 'regions': ['United States']}, 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:FYBmumLNjRYJ:https://research.facebook.com/people/lecun-yann/&cd=12&hl=en&ct=clnk&gl=us'}]}, {'position': 3, 'title': "Yann LeCun's Home Page", 'link': 'http://yann.lecun.com/', 'displayed_link': 'http://yann.lecun.com', 'snippet': 'Yann LeCun, VP and Chief AI Scientist, Facebook Silver Professor of Computer Science, Data Science, Neural Science, and Electrical and Computer Engineering, ...', 'snippet_highlighted_words': ['Yann LeCun', 'Chief AI Scientist', 'Facebook Silver Professor', 'Science', 'Science', 'Science'], 'about_this_result': {'keywords': ['yann', 'lecun', 'chief', 
#'ai', 'scientist', 'facebook', 'silver', 'professor', 'courant', 'institute', 'new', 'york'], 'related_keywords': ['science'], 'languages': ['English'], 'regions': ['United States']}, 'cached_page_link': 'http://webcache.googleusercontent.com/search?q=cache:xyNIEaNRIOgJ:yann.lecun.com/&cd=25&hl=en&ct=clnk&gl=us', 'related_pages_link': 'https://www.google.com/search?q=related:yann.lecun.com/+Yann+LeCun+Chief+AI+Scientist+at+Facebook+%26+Silver+Professor+at+the+Courant+Institute,+New+York+%E2%80%A6', 'source': 'lecun.com'}, {'position': 4, 'title': 'Yann LeCun', 'link': 'https://engineering.nyu.edu/faculty/yann-lecun', 'displayed_link': 'https://engineering.nyu.edu › faculty › yann-lecun', 'snippet': 'Yann LeCun is Director of AI Research at Facebook, and Silver Professor of Data ... at New 
#York University, affiliated with the NYU Center for Data Science, ...', 'snippet_highlighted_words': ['Yann LeCun', 'AI', 'Facebook', 'Silver Professor', 'New York', 'Center', 'Science'], 'about_this_result': {'keywords': ['yann', 'lecun', 'ai', 'facebook', 'silver', 'professor', 'courant', 'institute', 'new', 'york'], 'related_keywords': ['science', 'faculty', 'center', 'school'], 'languages': ['English'], 'regions': ['United States']}, 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:Ftt9E2OOUK4J:https://engineering.nyu.edu/faculty/yann-lecun&cd=26&hl=en&ct=clnk&gl=us', 'source': 'New York University'}, {'position': 5, 'title': 'Yann LeCun - VP & Chief AI Scientist at Meta - Facebook', 'link': 'https://www.linkedin.com/in/yann-lecun', 'displayed_link': 'https://www.linkedin.com › yann-lecun', 'about_this_result': {'keywords': ['yann', 'lecun', 'chief', 'ai', 'scientist', 'facebook', 'professor', 'institute', 'new', 'york'], 'languages': ['English'], 'regions': ['United States']}, 'rich_snippet_list': ['VP & Chief AI Scientist at Meta', 'VP & Chief AI Scientist', 'Director of AI Research', 'Professor', 'Co-founder, Advisor', 'Cofounder and Chief Scientist', 'Owner'], 'missing': ['Silver', 'Courant'], 'source': 'LinkedIn'}, {'position': 7, 'title': 'Yann LeCun', 'link': 'https://www.simonsfoundation.org/people/yann-lecun/', 'displayed_link': 'https://www.simonsfoundation.org › people › yann-le...', 'snippet': 'Yann LeCun is Vice President and Chief AI Scientist at Facebook and Silver Professor at New York University affiliated with the Courant Institute and the ...', 'snippet_highlighted_words': ['Yann LeCun', 'Chief AI Scientist', 'Facebook', 'Silver Professor', 'New York', 'Courant Institute'], 'about_this_result': {'keywords': ['yann', 'lecun', 'chief', 'ai', 'scientist', 'facebook', 'silver', 'professor', 'courant', 'institute', 'new', 'york'], 'languages': ['English'], 'regions': ['United States']}, 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:LxboOpZHFK0J:https://www.simonsfoundation.org/people/yann-lecun/&cd=29&hl=en&ct=clnk&gl=us', 'source': 'Simons Foundation'}, {'position': 8, 'title': 'Yann LeCun | Speaking Fee | Booking Agent', 'link': 'https://www.allamericanspeakers.com/speakers/425979/Yann-LeCun', 'displayed_link': 'https://www.allamericanspeakers.com › Speakers', 'snippet': 'VP & Chief AI Scientist at Meta; Silver Professor at NYU; Founding Director of Facebook AI Research & the NYU Center for Data Science · New York, NY, USA · Live ...', 'snippet_highlighted_words': ['Chief AI Scientist', 'Silver Professor', 'Facebook AI', 'Center', 'Science', 'New York', 'NY'], 'about_this_result': {'keywords': ['yann', 'lecun', 'chief', 'ai', 'scientist', 'facebook', 'silver', 'professor', 'courant', 'institute', 'new', 'york'], 'related_keywords': ['science', 'center', 'ny'], 'languages': ['English'], 'regions': ['United States']}, 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:wUKXfJ4ipEEJ:https://www.allamericanspeakers.com/speakers/425979/Yann-LeCun&cd=30&hl=en&ct=clnk&gl=us', 'source': 'All American Speakers Bureau'}, {'position': 9, 'title': "Intel's Artificial Intelligence Podcast", 'link': 'https://www.intel.com/content/www/us/en/artificial-intelligence/podcast-episodes/artificial-intelligence-podcast-episode-8.html', 'displayed_link': 'https://www.intel.com › content › www › podcast-episodes', 'snippet': 'Yann LeCun is Chief AI Scientist at Facebook, and Silver Professor of Dara Science, Computer Science, Neural Science, and Electrical Engineering at New York ...', 'snippet_highlighted_words': ['Yann LeCun', 'Chief AI Scientist', 'Facebook', 'Silver Professor', 'Science', 'Science', 'Science', 'New York'], 'about_this_result': {'keywords': ['yann', 'lecun', 'chief', 'ai', 'scientist', 'facebook', 'silver', 'professor', 'courant', 'institute', 'new', 'york'], 'related_keywords': ['artificial intelligence', 'science'], 'languages': ['English'], 'regions': ['United States']}, 'source': 'Intel'}, {'social_media': [{'position': 5, 'title': 'Yann LeCun - VP & Chief AI Scientist at Meta - Facebook', 'link': 'https://www.linkedin.com/in/yann-lecun', 'displayed_link': 'https://www.linkedin.com › yann-lecun', 'about_this_result': {'keywords': ['yann', 'lecun', 'chief', 'ai', 'scientist', 'facebook', 'professor', 'institute', 'new', 'york'], 'languages': ['English'], 'regions': ['United States']}, 'rich_snippet_list': ['VP & Chief AI 
##Scientist at Meta', 'VP & Chief AI Scientist', 'Director of AI Research', 'Professor', 'Co-founder, 
#Advisor', 'Cofounder and Chief Scientist', 'Owner'], 'missing': ['Silver', 'Courant'], 'source': 'LinkedIn'}]}], 'expert_information': {'thumbnail': 'https://scholar.googleusercontent.com/citations?view_op=small_photo&user=WLN3QrAAAAAJ&citpid=2', 'name': 'Yann LeCun', 'link': 'https://scholar.google.com/citations?hl=en&user=WLN3QrAAAAAJ', 'author_id': 'WLN3QrAAAAAJ', 'email': 'Verified email at cs.nyu.edu', 'affiliations': 'Chief AI Scientist at Facebook & Silver Professor at the Courant Institute, New York …', 'cited_by': 301663, 'interests': [{'title': 'AI', 'serpapi_link': 'https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Aai', 'link': 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:ai'}, {'title': 'machine learning', 'serpapi_link': 'https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Amachine_learning', 'link': 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:machine_learning'}, {'title': 'computer vision', 'serpapi_link': 'https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Acomputer_vision', 'link': 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:computer_vision'}, {'title': 'robotics', 'serpapi_link': 'https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Arobotics', 'link': 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:robotics'}, {'title': 'image compression', 'serpapi_link': 'https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Aimage_compression', 'link': 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:image_compression'}]}}}
