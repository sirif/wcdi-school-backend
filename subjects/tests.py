from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from dictionaries.models import DictFirstNameModel, DictSecondNameModel
from subjects.models.teacher_model import TeacherModel


class SubjectAPITest(TestCase):
    def setUp(self) -> None:
        # создание необходимых объектов перед запуском тестов
        self.first_name1 = DictFirstNameModel.objects.create(name='Иван')
        self.second_name1 = DictSecondNameModel.objects.create(name='Иванович')

        self.first_name2 = DictFirstNameModel.objects.create(name='Петр')
        self.second_name2 = DictSecondNameModel.objects.create(name='Петрович')

        self.teacher = TeacherModel.objects.create(first_name=self.first_name1, second_name=self.second_name2)

    def test_post_teacher(self):
        # https://djangodoc.ru/3.1/ref/urlresolvers/
        # для работы reverse нужно указать в urls basename
        url = reverse('teacher-list')
        teacher_data = {
            'first_name': self.first_name1.pk,
            'second_name': self.second_name2.pk
                        }
        response = self.client.post(url, data=teacher_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TeacherModel.objects.count(), 2)

    def test_post_wrong_data(self):
        url = '/subjects/teacher/'
        teacher_data = {
            'first_name': 'Олег',
            'sector_item': 'Олегович'
                        }
        response = self.client.post(url, data=teacher_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(TeacherModel.objects.count(), 1)
