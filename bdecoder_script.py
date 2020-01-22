from bencode import bdecoder

while True:
	bencoded = input("Enter your bencoded string ('exit' to close the script): ")
	if bencoded == 'exit':
		break;
	else:
		try:
			bdecoded = bdecoder.bdecode(bencoded)
			print("Decoded: " + str(bdecoded))
		except bdecoder.StringTooSmallError:
			print("Your string has fewer characters than the leading integer indicates.")
		except bdecoder.IntFormatError:
			print("Your integer is badly formatted (correct format: 'i<number>e').")
		except bdecoder.ListFormatError:
			print("Your list is badly formatted (correct format: 'l<elements>e')")
		except bdecoder.DictFormatError:
			print("Your dictionary is badly formatted (correct format: 'd<key-value pairs>e')")
		except bdecoder.ValueFormatError:
			print("Your value or one of its elements is badly formatted.")
