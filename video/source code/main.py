from datetime import datetime

import redis
import marshmallow as ma
import json

class Freeze:
    def __init__(self, freeze_path: str, camera_name: str):
        self.freeze_path = freeze_path
        self.camera_name = camera_name
        self.date_time = datetime.now()

    def __repr__(self) -> str:
        return f'Freeze({self.freeze_path}, {self.camera_name})'

class FreezeSchema(ma.Schema):
    freeze_path = ma.fields.String()
    camera_name = ma.fields.String()
    date_time = ma.fields.DateTime()



def main(freeze: Freeze):
    freeze_schema = FreezeSchema()
    print(freeze1)
    with redis.Redis(host='localhost', port=6379, db=0) as redis_client:
        redis_client.lpush('freezes', json.dumps(freeze_schema.dump(freeze)))
        desicion = input('Подтвердите, что это является корректным (y/n)')
        if desicion == 'y':
            print('Сообщение сформировано')
            print('Занесено в базу данных')
        redis_client.rpop('freezes')

freeze1 = Freeze('path1', 'camera1')
main(freeze1)

