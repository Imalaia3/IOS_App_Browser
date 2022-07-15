from PIL import Image
from io import BytesIO
import base64

import json
appsjson = json.loads(open("apps.json").read())



entry = appsjson["App"]["Ipas"]

def readall(entrypoint):
	outp = []
	for i in range(len(entrypoint)):
		v = []
		v.append(entrypoint[i]["bundleid"])
		v.append(i)
		outp.append(v)

	return outp


def getinfo(idx,entrypoint):
	
	app = entrypoint[idx]

	return [app["appsize"],app["bundleid"],app["docsize"],app["imagesize"], app["name"]]


def getimage(idx, entrypoint):
	app = entrypoint[idx]
	return app["imagedata"]


def generalinfo():
	point = appsjson["App"]
	return [point["count"], point["file"], point["totalsize"]]


def handleimgs(index):
	out = getimage(index, entry)
	im = Image.open(BytesIO(base64.b64decode(out)))
	im.show()

print('Searching apps.json. Current entrypoint = apps.json["App"]["Ipas"]')

allapps = readall(entry)

for app in allapps:
	print("Index: " + str(app[1]) + " | Bundle ID: " + app[0] + "|\n")

info = generalinfo()
print("Number Of Apps: " + str(info[0]) + "\nLast Cached Filepath: " + info[1]+"\nTotal App Size: " + str(info[2]))


while True:

	v = int(input("Browse Entries:\n"))
	print(getinfo(v, entry))
	l = str(input("Open Image? (Y/n):\n"))
	if l == "" or l == "y" or l == "Y":
		handleimgs(v)
	else:
		pass
	
	
