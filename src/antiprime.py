## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys
def main(x) :
	r = 0
	i = 1
	while i <= x :
		if x % i == 0 :
			r = r + 1
		i = i + 1
	return r

def ap(x):
	divisores = main(x)
	i = 1
	while i < x :
		if main(i) >= divisores :
			return "not anti-prime"
		i = i + 1
	return("anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	num = int(sys.argv[1])
	res = ap(num)
	print(res)
	

	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
