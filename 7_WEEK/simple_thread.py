import threading

def prt_square(num):
    print(f"Square: {num**2}")

def prt_cube(num):
    print(f"Cube: {num**3}")

t1 = threading.Thread(target=prt_square, args=(10,))
t2 = threading.Thread(target=prt_cube, args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")