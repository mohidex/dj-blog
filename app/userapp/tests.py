from django.test import TestCase
from django.core import mail
from django.utils import timezone
from .models import User
from django.db.utils import IntegrityError


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(
            username="john_doe",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            is_staff=False,
            is_active=True,
            date_joined=timezone.now(),
            password="password"
        )
        User.objects.create(
            username="alex_zoe",
            first_name="Alex",
            last_name="Zoe",
            email="alex_zoe@example.com",
            password="password"
        )

    def tearDown(self):
        # Clean up any resources after each test case is run
        pass

    def test_user_creation(self):
        user = User.objects.get(username='john_doe')
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john@example.com")
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertIsNotNone(user.date_joined)

    def test_user_creation_with_default(self):
        user = User.objects.get(username='alex_zoe')
        self.assertEqual(user.username, "alex_zoe")
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertIsNotNone(user.date_joined)

    def test_username_uniqueness(self):
        # Attempt to create another instance with the same unique value
        with self.assertRaises(IntegrityError) as context:
            User.objects.create(
                username="alex_zoe",
                first_name="Alexis",
                last_name="Zoe",
                email="alexis_zoe@example.com",
                password="password"
            )

        # Verify that the IntegrityError exception is raised
        self.assertIn(
            'duplicate key value violates unique constraint',
            str(context.exception)
        )

    def test_email_uniqueness(self):
        # Attempt to create another instance with the same unique value
        with self.assertRaises(IntegrityError) as context:
            User.objects.create(
                username="alexis_zoe",
                first_name="Alexis",
                last_name="Zoe",
                email="alex_zoe@example.com",
                password="password"
            )

        # Verify that the IntegrityError exception is raised
        self.assertIn(
            'duplicate key value violates unique constraint',
            str(context.exception)
        )

    def test_username_uniqueness_with_case_insensitive(self):
        # Attempt to create another instance with the same unique value
        with self.assertRaises(IntegrityError) as context:
            User.objects.create(
                username="John_Doe",
                first_name="John",
                last_name="Doe",
                email="johny@example.com",
                password="password"
            )
        # Verify that the IntegrityError exception is raised
        self.assertIn(
            'duplicate key value violates unique constraint',
            str(context.exception)
        )

    def test_username_uniqueness_with_case_insensitive_v2(self):
        # Attempt to create another instance with the same unique value
        with self.assertRaises(IntegrityError) as context:
            User.objects.create(
                username="john_Doe",
                first_name="John",
                last_name="Doe",
                email="johny@example.com",
                password="password"
            )
        # Verify that the IntegrityError exception is raised
        self.assertIn(
            'duplicate key value violates unique constraint',
            str(context.exception)
        )

    def test_email_uniqueness_with_case_insensitive(self):
        # Attempt to create another instance with the same unique value
        with self.assertRaises(IntegrityError) as context:
            User.objects.create(
                username="John_Doe",
                first_name="John",
                last_name="Doe",
                email="joHn@example.com",
                password="password"
            )
        # Verify that the IntegrityError exception is raised
        self.assertIn(
            'duplicate key value violates unique constraint',
            str(context.exception)
        )

    def test_username_search_insensitivity(self):
        user1 = User.objects.get(username='john_Doe')
        user2 = User.objects.get(username='John_doe')
        self.assertEqual(user1, user2)
        self.assertEqual(user1.username, 'john_doe')
        self.assertEqual(user2.username, 'john_doe')
    
    def test_username_changing_insensitivity(self):
        user1 = User.objects.get(username='john_Doe')
        user1.username = 'JOHN_DOE'
        user1.save()
        user2 = User.objects.get(username='john_doe')
        self.assertEqual(user1, user2)

    def test_email_search_insensitivity(self):
        user1 = User.objects.get(email='John@Example.COM')
        user2 = User.objects.get(email='john@EXample.com')
        self.assertEqual(user1, user2)
        self.assertEqual(user1.email, 'john@example.com')
        self.assertEqual(user2.email, 'john@example.com')
