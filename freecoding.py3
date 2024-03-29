def generate_pyramid(n):
    for i in range(n):
        print(' ' * (n - i -1) + '*' * (2 * i + 1))
generate_pyramid(10)
        
