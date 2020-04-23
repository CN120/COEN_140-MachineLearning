import math, time
n = 500
start = time.perf_counter()
x = math.factorial(n)
end = time.perf_counter()
#print(str(n)+"!","=",str(x))
print("Calculating", str(n) + "!", "took", str(end-start), "seconds")
