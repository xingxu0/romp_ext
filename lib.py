# before function converts actual coefficient to magnitude (bits requried to represent this coefficient)
def get_bits(i_num):
	num = abs(i_num)
	if num == 0:
		return 0
	bits = 1
	while (num>>1):
		bits += 1
		num >>= 1
	return bits
