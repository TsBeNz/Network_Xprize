import routeros_api
import json

connect_object = []

def convert_to_dict(inputs = ""):
    inputs = str(inputs).replace("[","").replace("]","").replace("b","").replace("'",'"')
    inputs = json.loads(inputs)
    return inputs

def connect_router():
    global start
    connection = routeros_api.RouterOsApiPool('192.168.100.1',port=3311, username='TsBeNz', password='BANZbanz25',plaintext_login=True)
    connect_object.append(connection)
    api = connection.get_api()
    while True:
        data = convert_to_dict(str(api.get_resource('/').call('ping', { 'address': '192.168.100.208', 'count': '1'})))
        if data["received"] == '0':
            print("time out")
        else:
             print(data["time"])


if __name__ == '__main__':
    try:
        connect_router()
    except KeyboardInterrupt:
        connect_object[0].disconnect()
        print("\nShutdown ...\n")