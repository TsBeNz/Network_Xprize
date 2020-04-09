import routeros_api


router = Api('192.168.100.1', user='TsBeNz', password='BANZbanz25',port = 3311)
r = router.talk('/ip/address/print')
print(r)