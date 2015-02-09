key = "849e027f476027a394edd656eaef4842"
key2 = "d676cf6e1e0ceb8fd14e8cb69acd812d"
key3 = "1adecee8a60444738f280aad1cd87d0e"


keylist = [key, key2, key3]

n = 0

"""
while n < 3:
	print keylist[n]
	n = n + 1
"""

while True:
	if n%2 == 0:
		apikey = keylist[0]
		n = n + 1
	elif n%2 == 1:
		apikey = keylist[1]
		n = n+1

	print n
	print apikey



#prints the values for key,key2, and key3