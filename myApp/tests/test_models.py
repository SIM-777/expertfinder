from django.test import TestCase
from myApp.models import expert, expert_report
from django.contrib.auth.models import User

class ExpertModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.expert = expert.objects.create(
            user=self.user,
            expert_name='John Doe',
            expert_id='123',
            expert_affiliation='University XYZ',
            expert_interests=['Interest 1', 'Interest 2'],
            expert_thumbnail='thumbnail.jpg',
            expert_citations=10
        )

    def test_expert_creation(self):
        self.assertEqual(self.expert.expert_name, 'John Doe')
        self.assertEqual(self.expert.expert_id, '123')
        self.assertEqual(self.expert.expert_affiliation, 'University XYZ')
        self.assertEqual(self.expert.expert_interests, ['Interest 1', 'Interest 2'])
        self.assertEqual(self.expert.expert_thumbnail, 'thumbnail.jpg')
        self.assertEqual(self.expert.expert_citations, 10)
        self.assertEqual(str(self.expert), 'John Doe')

    def test_expert_unique_together(self):
        with self.assertRaises(Exception):
            expert.objects.create(
                user=self.user,
                expert_name='Jane Doe',
                expert_id='123',
                expert_affiliation='University ABC',
                expert_interests=['Interest 3', 'Interest 4'],
                expert_thumbnail='thumbnail2.jpg',
                expert_citations=5
            )

class ExpertReportModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.expert = expert.objects.create(
            user=self.user,
            expert_name='John Doe',
            expert_id='123',
            expert_affiliation='University XYZ',
            expert_interests=['Interest 1', 'Interest 2'],
            expert_thumbnail='thumbnail.jpg',
            expert_citations=10
        )
        self.expert_report = expert_report.objects.create(
            expert=self.expert,
            interests='Interest 1, Interest 2',
            links='link1, link2'
        )

    def test_expert_report_creation(self):
        self.assertEqual(self.expert_report.expert, self.expert)
        self.assertEqual(self.expert_report.interests, 'Interest 1, Interest 2')
        self.assertEqual(self.expert_report.links, 'link1, link2')
        self.assertEqual(str(self.expert_report), f'Expert Report {self.expert_report.id}')
        