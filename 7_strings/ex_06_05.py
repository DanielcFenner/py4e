text = "X-DSPAM-Confidence:    0.8475"
index = text.find('0')
float = float(text[index:len(text)])
print(float)