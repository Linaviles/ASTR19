import numpy as np
from tabulate import tabulate
import math
x=np.linspace(0, (math.pi * 2) , 10000)
y= np.sin(x)
data = [(a,b) for a, b in zip(x,y)]
table_header = ["x", "sin(x)"]
python_table = tabulate(data, tablefmt = "grid", headers = table_header, floatfmt=".3f")



def main():
	print(python_table)
	

if __name__ == "__main__":
	main()