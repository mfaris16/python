import urllib.request, json

print ("Silahkan kirim pesan!")

while(True):
    pesan = input("Anda: ")
    link_json = urllib.request.urlopen("http://sandbox.api.simsimi.com/request.p?key=dd01228d-7068-4d34-a2ea-668fe42560c8&lc=id&ft=1.0&text=%s" % pesan)
    data = json.loads(link_json.read())

    print ("simsimi: %s" % data['response'])
