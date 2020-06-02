text = "X-DSPAM-Confidence:    0.8475"
spos = text.find(':')
#epos = text.find('5')
data = text[spos+1 : ]
print(data)
num = float(data)
print(data)