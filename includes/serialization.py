import os

import json
from decimal import Decimal
from datetime import datetime

from pathlib import Path




class SerializeDeserializeInJSON:

    def __init__(self):
        self.file_name = "serialized_files" + os.sep + "default.json"
        self.data = {}

    def set_serialization_file_name(self, file_name):
        self.file_name = file_name

    def set_serialization_data(self, data):
        self.data = data

    def set_data_format_encoder(self, data_format_encoder_class):
        self.data_format_encoder_class = data_format_encoder_class

    def set_data_format_decoder(self, data_format_decoder_class):
        self.data_format_decoder_class = data_format_decoder_class

    def serialize_in_json(self):
        file_exists = self.check_file_exists()
        if file_exists == False:
            output_file = Path(self.file_name)
            output_file.parent.mkdir(exist_ok=True, parents=True)
        json_data = json.dumps(self.data, cls=self.data_format_encoder_class)
        with open(self.file_name, 'x') as file_object:
            json.dump(json_data, file_object)

    def deserialize_from_json(self):
        deserialized_data = {}
        file_exists = self.check_file_exists()
        if file_exists == True:
            with open(self.file_name, mode='r') as file_object:
                deserialized_data = json.loads(file_object.read(), cls=self.data_format_decoder_class) #
        return deserialized_data

    def check_file_exists(self):
        check = os.path.isfile(self.file_name)
        return check



class TypeToJSONEncoder(json.JSONEncoder):

    def default(self, data_object):
        if isinstance(data_object, Decimal):
            return str(data_object)
        elif isinstance(data_object, datetime):
            return data_object.isoformat()
        elif isinstance(data_object, set):
            return list(data_object)
        else:
            return super().default(data_object)




class TypeToJSONDecoder(json.JSONDecoder):

    date_time_map = {'date', 'datetime', 'day', 'hour', 'minutes', 'month', 'seconds', 'time', 'year'}
    num_type_data = {'fraction', 'decimal', 'complex'}

    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook,strict=False, *args, **kwargs)

    def object_hook(self, obj):
        if '_type' not in obj:
            return obj
        get_type = obj['_type']
        if get_type in self.date_time_map: # check if _type is a datetime type
            obj['value'] = self.date_deserialize(obj['value'], get_type)
        elif get_type in self.num_type_data:  # Checks for fractions, decimal and complex
            try:
                obj['value'] = self.eva_data(obj['value'])
            except ValueError as err:
                print('object_hook ---> in num_type_data eval', err)
        elif get_type == '_set':
            obj['value'] = set(obj['value'])
        return obj

    @staticmethod
    def eva_data(obj):
        """Eval fractions, Decimals and complex num types"""
        return eval(obj)

    @staticmethod
    def date_deserialize(obj, _type):

        # TODO deserialize date with other format types, for instance 2020/11/17
        if _type == 'date':
            try:
                if isinstance(obj, list):  # Date can be [2020, 11, 17] or '2020-11-17)
                    obj = date(*[int(item) for item in obj])
                else:
                    obj = date(*[int(item) for item in obj.split('-')])
            except ValueError as err:
                print('data_serialize -- data', err)

        elif _type == 'datetime':
            try:
                obj = datetime.strptime(str(obj), '%Y-%m-%d %H:%M:%S')
            except ValueError as err:
                try:
                    obj = datetime.fromisoformat(str(obj))
                except ValueError as err:
                    print('data_serialize -- datatime', err)
        return obj
