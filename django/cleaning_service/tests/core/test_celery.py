from django.test import TestCase
from api.tasks import create_users


class TestCreateUsers(TestCase):
    def setUp(self):
        self.task = create_users.apply_async(args=[1])
        self.results = self.task.get()

    def test_task_state(self):
        self.assertEqual(self.task.state, 'SUCCESS')

    def test_create_users(self):
        self.assertEqual(self.results, 1)
