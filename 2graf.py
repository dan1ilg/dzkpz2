import pulp
import time
start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
problem = pulp.LpProblem('0',pulp.LpMinimize)
problem += x1 +x2+3*x3+4*x4, "Функция цели"
problem += 5*x1- 6*x2+ x3-2*x4 == 2, "1"
problem += 11*x1-14*x2+2*x3-5*x4 == 2, "2"
problem.solve()
print ("Результат:")
for variable in problem.variables():
 print (variable.name, "=", variable.varValue)
print ("Прибыль:")
print (pulp.value(problem.objective))
stop = time.time()
print ("Время :")
print(stop- start)