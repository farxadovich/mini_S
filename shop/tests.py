from django.test import TestCase
from shop.models import Mahsulot, Toifa
from django.test import Client
from django.urls import reverse


class ModelTestCase(TestCase):
    def setUp(self):
        Toifa.objects.create(nomi='Yangi')
        Toifa.objects.create(nomi='Testoviy')


        Mahsulot.objects.create(
            nomi='mahsulot',
            narx=12.5,
            tarif='lorem ipsum set dolor amet',
            toifasi=Toifa.objects.get(nomi='Yangi')
        )
        Mahsulot.objects.create(
            nomi='mahsulot2',
            narx=8.24,
            tarif='Lorem ipsum',
            toifasi=Toifa.objects.get(nomi='Testoviy'),
            soni=5,

        )
    def test_model_created(self):
        t1 = Toifa.objects.get(nomi='Yangi')
        t2 = Toifa.objects.get(nomi='Testoviy')
        m1 = Mahsulot.objects.get(nomi='mahsulot 1')
        m2 = Mahsulot.objects.get(nomi='mahsulot 2')
        self.assertEqual(t1.nomi, 'Yangi')
        self.assertEqual(t2.nomi, 'Testoviy')
        self.assertEqual(m1.toifasi, t1)
        self.assertEqual(m2.toifasi, t2)
        self.assertEqual(m1.soni, 10)
        self.assertEqual(m2.soni, 5)


class ViewsTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('shop:index'))
        self.assertEqual(response.status_code, 200)

        Toifa.objects.create(nomi='Yangi')
        Toifa.objects.create(nomi='Testoviy')



        Mahsulot.objects.create(
            nomi='mahsulot',
            narx=12.5,
            tarif='lorem ipsum set delor amet',
            toifasi=Toifa.objects.get(nomi='Yangi'),

        )

        Mahsulot.objects.create(
            nomi='mahsulot2',
            narx=8.24,
            tarif='lorem ipsum',
            toifasi=Toifa.objects.get(nomi='Testoviy'),
            soni=5,

        )
        response = self.client.get(reverse('shop:index'))
        self.assertEqual(response.status_code, 200)
