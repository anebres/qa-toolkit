# Reusable utility functions

def assert_equal(expected, actual):
    if expected == actual:
        return "PASS"
    else:
        return f"FAIL: Expected {expected}, got {actual}"

def has_duplicates(items):
    return len(items) != len(set(items))

def find_empty_fields(data):
    return [k for k, v in data.items() if not v.strip()]

# def find_empty_fields(data):
#     return [k for k, v in data.items() if is_field_empty(v)]

def is_valid_email(email):
    import re
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def is_field_empty(value):
    return not value or not value.strip()

def find_missing(expected_list, actual_list):
    return list(set(expected_list) - set(actual_list))

def find_unexpected(actual_list, expected_list):
    return list(set(actual_list) - set(expected_list))

def diff_dict(expected, actual):
    return {
        key: (expected.get(key), actual.get(key))
        for key in expected.keys() | actual.keys()
        if expected.get(key) != actual.get(key)
    }

def normalize_whitespace(text):
    return " ".join(text.strip().split())

def capitalize_each_word(text):
    return " ".join(word.capitalize() for word in text.split())

def log_result(test_name, result):
    print(f"{test_name}: {'✔ PASS' if result == 'PASS' else '✖ FAIL'}")

def summarize_results(results):
    passed = results.count("PASS")
    failed = results.count("FAIL")
    return f"Summary: {passed} passed, {failed} failed"

def generate_test_strings(min_length, max_length, required=True):
    valid = ["a" * min_length, "b" * ((min_length + max_length) // 2), "c" * max_length]
    invalid = []
    if required:
        invalid.append("")
    if min_length > 0:
        invalid.append("x" * (min_length - 1))
    invalid.append("z" * (max_length + 1))
    return {"valid": valid, "invalid": invalid}