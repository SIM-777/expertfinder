from django.test import SimpleTestCase
from django.urls import reverse,resolve
from myApp.views import *
from myApp import views
class TestUrls(SimpleTestCase):
    def test_showExperts_url_is_resolved(self):
       url=reverse('showExperts')
       self.assertEquals(resolve(url).func,showExperts)

    def test_GetExperts_url_is_resolved(self):
       url=reverse('GetExperts')
       self.assertEquals(resolve(url).func,GetExperts)

    def test_login_url_is_resolved(self):
       url=reverse('login')
       self.assertEquals(resolve(url).func,redirectlogin) 

    


    def test_manage_results_url_is_resolved(self):
       url=reverse('manage_results')
       self.assertEquals(resolve(url).func,manage_results)   
    
    
    def test_search_experts_db_url_is_resolved(self):
       url=reverse('search_experts_db')
       self.assertEquals(resolve(url).func,search_experts_from_db) 
   
    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, views.search_for_experts)

    

    def test_redirectlogin_url_is_resolved(self):
        url = reverse('redirectlogin')
        self.assertEquals(resolve(url).func, views.redirectlogin)

    def test_save_result_url_is_resolved(self):
        url = reverse('save_result', args=['example_id'])
        self.assertEquals(resolve(url).func, views.save_result)

    def test_expert_bio_url_is_resolved(self):
        url = reverse('expert_bio')
        self.assertEquals(resolve(url).func, views.expert_bio)

    

    def test_view_report_url_is_resolved(self):
        url = reverse('view_report', args=['example_name', 'example_affiliations'])
        self.assertEquals(resolve(url).func, views.view_report)

    def test_delete_result_url_is_resolved(self):
        url = reverse('delete_result', args=['example_id'])
        self.assertEquals(resolve(url).func, views.delete_result)

    def test_logout_user_url_is_resolved(self):
        url = reverse('logout_user')
        self.assertEquals(resolve(url).func, views.logout_user)

   
   


    