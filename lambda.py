def function_1(x) : return x **	2 
def function_2(x) : return x **	3
def function_3(x) : return x **	4
callbacks = [function_1 , function_2 , function_3] 
print("\nNamed Functions:") 
for function in	callbacks : print("Result:",function(3)) 
callbacks=\ 
[lambda	x:x**2,lambdax:x**3,lambdax:x**4]
print("\nAnonymous Functions:") 
for function in	callbacks: 
print("Result:",function(3))
