import random
def objective_function(x):
       return -x**2 + 10*x + 25

def hill_climbing(max_iterations=1000, step_size=0.1):
    current_solution = random.uniform(-10, 10)  
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
       
        neighbor_solution = current_solution + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor_solution)

    
        if neighbor_value > current_value:
            current_solution = neighbor_solution
            current_value = neighbor_value

    return current_solution, current_value

if __name__ == "__main__":
    best_solution, best_value = hill_climbing()
    print("Best solution:", best_solution)
    print("Best value:", best_value)
