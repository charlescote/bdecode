import re

class Error(Exception):
	pass

class StringTooSmallError(Error):
	pass

class ValueFormatError(Error):
	pass

class ListFormatError(Error):
	pass

class DictFormatError(Error):
	pass

class IntFormatError(Error):
	pass

def bdecode(data):
	x, _ = _bdecode(data)
	return x

def _bdecode(data):
	firstChar = data[0]
	decimalMatch = re.match('^[0-9]+:', data)
	i = 1

	if firstChar == 'i':
		numStr = ''
		try:
			while data[i] != 'e':
				numStr += data[i]
				i += 1
			return int(numStr), i + 1
		except IndexError:
			raise IntFormatError
	elif decimalMatch:
		length = int(decimalMatch.group(0)[:-1])
		byteStr = data[(len(decimalMatch.group(0))):]
		if length > len(byteStr):
			raise StringTooSmallError
		return byteStr[:length], len(decimalMatch.group(0)) + length
	elif firstChar == 'l':
		list = []
		try:
			while data[i] != 'e':
				firstValue, increment = _bdecode(data[i:])
				list.append(firstValue);
				i += increment
			return list, i + 1
		except IndexError:
			raise ListFormatError
	elif firstChar == 'd':
		dict = {}
		try:
			while data[i] != 'e':
				key, increment = _bdecode(data[i:])
				i += increment
				dict[key], increment = _bdecode(data[i:])
				i += increment
			return dict, i + 1
		except IndexError:
			raise DictFormatError

	raise ValueFormatError