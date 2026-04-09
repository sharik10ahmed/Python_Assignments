import numpy as np

def show_menu():
    print("\n=== NUMPY ARRAY OPERATIONS ===")
    print("a. Create array filled with 1's")
    print("b. Find max/min from array")
    print("c. Dot product of 2 arrays")
    print("d. Reshape 1D array to 2D")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Enter choice (a/b/c/d/0): ").lower()
    
    if choice == '0':
        print("Goodbye!")
        break
    
    elif choice == 'a':
        size = int(input("Enter array size: "))
        arr = np.ones(size, dtype=int)
        print(f"Array of 1's: {arr}")
    
    elif choice == 'b':
        size = int(input("Enter array size: "))
        elements = list(map(int, input("Enter elements: ").split()))
        arr = np.array(elements)
        print(f"Array: {arr}")
        print(f"Maximum: {np.max(arr)}")
        print(f"Minimum: {np.min(arr)}")
    
    elif choice == 'c':
        print("Enter first array elements: ", end="")
        arr1 = np.array(list(map(int, input().split())))
        print("Enter second array elements: ", end="")
        arr2 = np.array(list(map(int, input().split())))
        result = np.dot(arr1, arr2)
        print(f"Dot product: {result}")
    
    