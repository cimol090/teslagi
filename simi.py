import urllib
import json

url = "http://sandbox.api.simsimi.com/request.p"
key = "3e2c4618-7b9f-4dba-b79d-453f66589c37"
lc = "id"
ft = "1.0"

def simi(text):
	param = {
			'key':key,
			'lc':lc,
			'ft':ft,
			'text':text
			}
	query = urllib.parse.urlencode(param)
	resp = urllib.request.urlopen("%s?%s" % (url, query)).read().decode()
	try:
		response = json.loads(resp)
		if response["msg"].strip().lower() == "ok.":
			return response["response"].strip()
		else:
			return response["msg"].strip()
	except Exception as e:
		return str(e)
