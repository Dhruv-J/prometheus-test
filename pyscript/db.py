from prometheus_client import start_http_server, Gauge
import random
import time

avgGPA = Gauge('avg_student_gpa', 'This gauge measures the average student\'s GPA.')
numStudents = Gauge('num_students', 'This gauge measures the number of students enrolled in a certain class.')
numProfs = Gauge('num_professors', 'This gauge measures the number of professors teaching a certain class')
avgAge = Gauge('avg_student_age', 'This gauge measures the average student\'s age.')

def generateRand():
    avgGPA.set(round(random.uniform(2, 4), 1))
    numStudents.set(random.randint(1, 250))
    numProfs.set(random.randint(1, 5))
    avgAge.set(random.randint(18, 22))

start_http_server(8000)
print('Server started!')
while True:
    generateRand()
    time.sleep(2.5)
