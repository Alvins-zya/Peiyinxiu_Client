import json
import unittest


class TestFile(unittest.TestCase):

    def test_with_temp(self):
        file_name = './temp_file.json'
        with open(file_name, 'r', encoding='utf-8') as file_obj:
            for line in file_obj.readlines():
                print(line)

    def test_with_read_lines(self):
        file_name = './temp_file.json'
        with open(file_name, 'r', encoding='utf-8') as file_obj:
            file_str = str(file_obj.readlines())
            file_str.replace(r"\n'", '')
            print(file_str)

    def test_with_write_file_in_json(self):
        json_date = [
            {
                "uuid": {
                    "":""
                },
                "test2":"value2"
            },
            {
                "test1": "value1",
                "test2": "value2"
            },
        ]
        file_name = './temp_file.json'
        with open(file_name, 'a', encoding='utf-8') as file_obj:
            json.dump(json_date, file_obj)
            # json_date = json.load(file_obj)
            print(json_date)

    def test_with_read_file_in_json(self):
        """
        从文件中获取
        :return:
        """
        file_name = './temp_file.json'
        with open(file_name, 'r', encoding='utf-8') as file_obj:
            json_date = json.load(file_obj)
            print(json_date)

