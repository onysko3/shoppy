from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Category,Item


class ItemTests(TestCase):

    def setUp(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            password='pass123',
        )
        self.category = Category.objects.create(
            title='Mobile Phone',
            description='mobile phone, cellular phone, cell phone, cellphone, handphone, or hand phone',
        )
        self.item = Item.objects.create(
            user=user,
            title='iphone 5s',
            body='as new',
            price='10',
            location='U.S.',
            category=self.category,
        )

    def test_item_listing(self):
        self.assertEqual(f'{self.item.title}', 'iphone 5s')
        self.assertEqual(f'{self.item.body}', 'as new')
        self.assertEqual(f'{self.item.price}', '10')
        self.assertEqual(f'{self.item.location}', 'U.S.')

    def test_item_list_view(self):
        response = self.client.get(reverse('items:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'iphone 5s')
        self.assertTemplateUsed(response, 'items/list.html')

    def test_item_detail_view(self):
        response = self.client.get(self.item.get_absolute_url())
        no_response = self.client.get('/items/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'iphone 5s')
        self.assertTemplateUsed(response, 'items/detail.html')