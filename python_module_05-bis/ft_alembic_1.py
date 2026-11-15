import alchemy

print("=== Alembic 1 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print()
print("Now show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth: ", end="", flush=True)
# create_earth exists in alchemy/elements.py, but alchemy/__init__.py
# never brings it into the package namespace: the next line must fail.
print(f"{alchemy.create_earth()}")
