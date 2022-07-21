import json
class ReadJson:
    def read_json(self):
         with open('../data/calc.json', 'r', encoding='utf-8') as f:
             return json.load(f)


if __name__ == "__main__":
    datas = ReadJson().read_json()

    arr = []
    for data in datas.values():

        arr.append((data['a'], data['b'], data['expect']))

    print(arr)



