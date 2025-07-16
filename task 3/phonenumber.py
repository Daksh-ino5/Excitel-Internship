import re

text = "Device: 00:1A:2B:3C:4D:5E"
macs = re.findall(r"(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}", text)
print(macs)