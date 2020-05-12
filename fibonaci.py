from marathon import MarathonClient
from marathon.models import MarathonApp
import time
import csv
import json

c = MarathonClient('http://localhost:8080')
print(c.list_tasks())
task_name = ""
fibo_array = [0,1]
for k in c.list_tasks():
	new_string = str(k)
	app_name = new_string.split("'app_id': ")[1].split(", 'health_check_results'")[0]
	app_id = new_string.split("'id': ")[1].split(", 'ports'")[0]
	if 'fibonaccitest' in app_name:
		task_name = app_name
		task_id = app_id

def Fibonacci(num):
	if num<0:
		print("Invalid input")
	elif num<=len(fibo_array):
		return fibo_array[num-1]
	else:
		temp_fib = Fibonacci(num-1)+Fibonacci(num-2) 
		fibo_array.append(temp_fib)
		return temp_fib 

def write_to_file(unique_id,x,total_time,n_value,task_name):
	with open('output_file.csv', mode='a') as output_file:
	    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	    output_writer.writerow([unique_id,x,total_time,n_value,task_name])
  
file = open("/Users/vidipmalhotra/Desktop/newProj5409/random_numbers.txt","r")
contents = file.readlines()
unique_id = 0
for x in contents:
	unique_id += 1
	print(x)
	start = time.time()
	n_value = Fibonacci(int(x))
	end = time.time()
	total_time = end - start
#	total_time = "{:.5f}".format(total_time)
	x = x.strip()
	write_to_file(unique_id,x,total_time,n_value,task_name)