import urllib, json

print ("Silahkan kirim pesan!")

while(True):
    pesan = raw_input("Anda: ")
    url = "http://sandbox.api.simsimi.com/request.p?key=dd01228d-7068-4d34-a2ea-668fe42560c8&lc=id&ft=1.0&text=%s" % pesan
    link_json = urllib.urlopen(url)
    data = json.loads(link_json.read())

    print "simsimi: %s" % data['response']
