import urllib.request, json

print ("Silahkan kirim pesan!")

while(True):
    pesan = input("Anda: ")
    with urllib.request.urlopen("http://sandbox.api.simsimi.com/request.p?key=dd01228d-7068-4d34-a2ea-668fe42560c8&lc=id&ft=1.0&text=%s" % pesan) as url:
    data = json.loads(url.read())

    print ("simsimi: %s" % data['response'])
