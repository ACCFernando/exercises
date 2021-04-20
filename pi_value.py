import random
from argparse import ArgumentParser

def estimate_pi(n):
    num_points_circle = 0
    num_points_total = 0
    for ponto in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2 #não precisa fazer a raiz, se for maior que 1 a raiz tb será
        if distance <= 1:
            num_points_circle += 1
        num_points_total +=1
        
    return 4*num_points_circle/num_points_total

if __name__=="__main__":
    parser = ArgumentParser(description="Calculate Pi")
    parser.add_argument("integer", metavar="N", type=int,
    help="Insert base number of trials")
    args = parser.parse_args()    
    
    n = args.integer
    pi = estimate_pi(n)
    print(pi)