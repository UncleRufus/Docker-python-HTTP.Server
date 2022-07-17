# Imports
import json
from typing import Dict
import requests

class RequestManager:
    def __init__(self, model):
        self.model=model

    def get_list_record(self):
        return self.model.objects.all()

    def get_target_record(self, pk):
        return self.model.objects.get(pk=pk)

    def create_record(self, request):
        new_record = self.model.objects.create(
            cmd=self.make_local_request()['cmd'],
            code=self.make_local_request()['code'],
        )
        new_record.save()
        return new_record

    def make_local_request(self) -> Dict:
        try:
            local_request = requests.get('http://host.docker.internal:9999/get_pwd/', timeout=60, verify=False)
            parsed_request = json.loads(local_request.text)
            return parsed_request
        except Exception:
            parsed_request = {
                'cmd': 'Нет ответа от локального сервера',
                'code': '404'
            }
            return parsed_request
