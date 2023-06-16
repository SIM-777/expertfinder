from django.test import TestCase,Client
from django.urls import reverse
from myApp.models import *
import json
class TestViews(TestCase):
    def setUp(self):
         client=Client()
    def test_showExperts(self):
         
         response=self.client.post(reverse("showExperts"),{'query':'Dummy','university_name':'Dummy_name','citation_num':0})
         self.assertEquals(response.status_code,302)

         

    def test_expert_report(self):
         response=self.client.get(reverse('expert_bio'))
         self.assertEquals(response.status_code,200)
         self.assertTemplateUsed(response,'bio.html')     
    

    def test_manage_results(self):
         response=self.client.get(reverse('manage_results'))
         self.assertEquals(response.status_code,302)  

    def test_search_experts_from_db(self):
         response=self.client.get(reverse("search_experts_db")) 
         self.assertEquals(response.status_code,302) 

    def test_save_result(self):
        response=self.client.get(reverse("save_result",args=['dummy'])) 
        self.assertEquals(response.status_code,302) 
    
    def test_delete_result(self):
        response=self.client.get(reverse("delete_result",args=['dummy'])) 
        self.assertEquals(response.status_code,302)