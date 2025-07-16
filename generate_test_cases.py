# CLI script to generate boundary test cases for form inputs

def generate_test_cases(min_length, max_length, required=True):
    valid = []
    invalid = []

    valid.append("a" * min_length)
    if max_length - min_length > 1:
        mid = (min_length + max_length) // 2
        valid.append("b" * mid)
    valid.append("c" * max_length)

    if required:
        invalid.append("")
    if min_length > 0:
        invalid.append("x" * (min_length - 1))
    invalid.append("z" * (max_length + 1))

    return {"valid": valid, "invalid": invalid}

if __name__ == "__main__":
    min_len = int(input("Enter minimum length: "))
    max_len = int(input("Enter maximum length: "))
    req = input("Is field required? (yes/no): ").strip().lower() in ["yes", "y"]

    cases = generate_test_cases(min_len, max_len, req)
    print("\nValid Cases:", cases["valid"])
    print("Invalid Cases:", cases["invalid"])