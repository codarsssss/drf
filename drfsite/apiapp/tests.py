from collections import OrderedDict

from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase

from .models import Data


class RequestTests(APITestCase):
    def test_create_post(self):
        data_version = {"id": "aaaa1232", "software": "samba", "version": "1.2.3"}
        response = self.client.post("/version/", data_version)
        self.assertEquals(response.data, data_version)

    def test_create_post2(self):
        data_version = {"id": "", "software": "samba", "version": "1.2.3"}
        response = self.client.post("/version/", data_version)
        self.assertEquals(response.data, {'id': [ErrorDetail(string='Это поле не может быть пустым.', code='blank')]} )

    def test_create_post3(self):
        data_version = {"id": "aaaa1232", "version": "1.2.3"}
        response = self.client.post("/version/", data_version)
        self.assertEquals(response.data, {'software': [ErrorDetail(string='Обязательное поле.', code='required')]})

    def test_create_post4(self):
        data_version = {"id": "aaaa1232", "software": "samba"}
        response = self.client.post("/version/", data_version)
        self.assertEquals(response.data, {"version":["Обязательное поле."]})

    def test_create_and_get(self):
        data_version = {"id": "aaaa1232", "software": "samba", "version": "1.2.3"}
        response = self.client.post("/version/", data_version, format='json')
        self.assertEquals(response.data, data_version)
        self.assertEquals(response.status_code, 201)

    def test_create_and_patch_version(self):
        data_version = {"id": "aaaa1232", "software": "samba", "version": "1.2.3"}
        response = self.client.post("/version/", data_version)
        new_data = {"version": "2.0.0"}
        response = self.client.patch(f"/version/{data_version['id']}/", new_data, format='json')
        self.assertEquals(response.data, {"id": "aaaa1232", "software": "samba", "version": "2.0.0"})

    def test_create_and_delete(self):
        data_version = {"id": "aaaa1232", "software": "samba", "version": "1.2.3"}
        response = self.client.post("/version/", data_version)
        response = self.client.delete(f"/version/{data_version['id']}/")
        self.assertEquals(response.status_code, 204)

    def test_create_and_get_versions(self):
        data_version = {"id": "aaaa1232", "software": "samba", "version": "1.2.3"}

        response = self.client.get('/versions/')
        self.assertEquals(response.data, [])

        response = self.client.post("/version/", data_version)
        response = self.client.get('/versions/')
        self.assertEquals(response.data, [OrderedDict([('id', 'aaaa1232'), ('software', 'samba'), ('version', '1.2.3')])])
