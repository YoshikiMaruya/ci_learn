# Yoshiki Maruya
"""This is a test program."""

prices = [3000,2500,10500,4300]
paymentList = list(map(lambda price:price * 1.08 , prices))

print(paymentList)
