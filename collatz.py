import random
#generates a list of booleans. True means 3n+1, False means n/2. n/2 must follow 3n+1 (therefore False must follow True) as there
#is no number n such that 3n+1 is an even number
def generate_iterations(num):
    output = [bool(random.getrandbits(1)) for _ in range(num)]
    for i in range(len(output)):
        if output[i] and i!=len(output)-1:
            output[i+1] = False
    return output
#this applies the list of operations to a number n
def generate_coefficients(iterations):
    n_coefficient = 1
    constant = 0
    for iteration in iterations:
        if iteration:
            n_coefficient *= 3
            constant = (constant*3)+1
        else:
            n_coefficient /= 2
            constant /= 2
    return n_coefficient, constant
#solves the equation by setting it equal to n. For example, if 3n+1=n, n=-0.5. We multiply by 1000 here to avoid floating point
#errors
def solve_n(n_coefficient, constant):
    return constant*1000/(1000-(n_coefficient*1000))
#this puts all of the functions together. We also check that the number is a positive number
def generate_looping_numbers(num, coefficient_num):
    output = [None]*num
    for i in range(num):
        iterations = generate_iterations(coefficient_num)
        coefficients = generate_coefficients(iterations)
        x = solve_n(coefficients[0], coefficients[1])
        if abs(x) == x and float(int(x)) == x:
            output[i]=(round(x, 1))
    return sorted(list(set([j for i, j in enumerate(output) if j!=None])))

#first input is the number of attempts, second input is the number of iterations of the collatz conjecture applied
#for example, 4 -> 2 -> 1 is 3 iterations
print(generate_looping_numbers(100, 3))

#given the output of this program, I'd like to make a conjecture that there is no number that loops in the collatz function
#above 4 (assuming that we don't end when the number reaches 1, otherwise there are likely none)