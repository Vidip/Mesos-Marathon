from marathon import MarathonClient
from marathon.models import MarathonApp

cursor = MarathonClient('http://localhost:8080')
cursor.create_app('fibonacitest', MarathonApp(cmd="python3 /Users/vidipmalhotra/Desktop/newProj5409/user2/fibonaci.py;sleep 200", mem=16, cpus=1))
print(cursor.list_tasks())

cursor1 = MarathonClient('http://localhost:8080')
cursor1.create_app('factorialtest', MarathonApp(cmd="python3 /Users/vidipmalhotra/Desktop/newProj5409/user1/factorial_task.py;sleep 200", mem=16, cpus=1))
print(cursor1.list_tasks())