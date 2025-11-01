
# main.py
"""
Basic Python sample script for testing version control and cloud deployment.
"""

def greet_user(name: str) -> str:
    """Return a greeting message for the given user name."""
    return f"Hello, {name}! Welcome to the Python Cloud Repo Test."

##newly added-one
def greet_user(country: str) -> str:
    """Return a greeting message for the given user name."""
    return f"Hello, {country}! Welcome to the Python Cloud Repo Test."

def add_numbers(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b

def main():
    print("=== Python Cloud Repo Test ===")
    user_name = input("Enter your name: ")
    print(greet_user(user_name))

    # Basic arithmetic test
    num1 = 10
    num2 = 20
    print(f"\nAdding numbers: {num1} + {num2} = {add_numbers(num1, num2)}")

if __name__ == "__main__":
    main()
