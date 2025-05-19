import os

base_dir = os.path.dirname(os.path.abspath(__file__))
myprints_dir = os.path.join(base_dir, "MyPrints")

print("Base dir:", base_dir)
print("MyPrints dir:", myprints_dir)

print("\nFiles in base dir:")
print(os.listdir(base_dir))

print("\nFiles in MyPrints:")
print(os.listdir(myprints_dir))
