import random
import string

# this funtion returns a random solution 
def generate_random_solution(answer):
    length = len(answer)
    return [random.choice(string.printable)for _ in range(length)]
print(generate_random_solution("Hello World"))


# evaluating a solution for the solution S 
def evaluate(solution,answer):
    target = list(answer)
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s) - ord(t))
    return diff
print(evaluate(['a','s','i','x','t','w',')','s','6','u','t','@'],"Hello,World"))

# to mutate means to change in a small way here we change letter in our string to arrive at best solution 

def mutate_solution(solution):
    index = random.randint(0,len(solution)-1)
    solution[index] = random.choice(string.printable)
solution = ['a','s','i','x','t','w',')','s','6','u','t','@']
mutate_solution(solution)
print(solution)


answer = "Hello,World"
best = generate_random_solution(answer)
best_score =  evaluate(best,answer)

while True:
    print("Best score so far ", best_score,"solution","".join(best))

    if best_score == 0:
        break
    
    new_solution = list(best)
    mutate_solution(new_solution)

    score = evaluate(new_solution,answer)
    while evaluate(new_solution,answer)<best_score:
        best= new_solution
        best_score = best