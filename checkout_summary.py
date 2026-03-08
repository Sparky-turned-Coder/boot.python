# This was a Boot.dev Training Ground challenge called "Checkout Summary"


# main.py
def cents_to_dollars(cents):
    dollars = cents * 0.01
    return f"${dollars:.2f}"


def format_checkout_summary(subtotal_cents, tax_percent, tip_percent):
    tax_cents = subtotal_cents * tax_percent // 100
    tip_cents = subtotal_cents * tip_percent // 100
    total_cents = subtotal_cents + tax_cents + tip_cents
    return (
        f"Subtotal: {cents_to_dollars(subtotal_cents)}\n"
        f"Tax ({tax_percent}%): {cents_to_dollars(tax_cents)}\n"
        f"Tip ({tip_percent}%): {cents_to_dollars(tip_cents)}\n"
        f"Total: {cents_to_dollars(total_cents)}"
    )


# main_test.py
# from main import *

run_cases = [
    (
        2599,
        10,
        20,
        "Subtotal: $25.99\nTax (10%): $2.59\nTip (20%): $5.19\nTotal: $33.77",
    ),
    (5000, 8, 0, "Subtotal: $50.00\nTax (8%): $4.00\nTip (0%): $0.00\nTotal: $54.00"),
    (99, 0, 15, "Subtotal: $0.99\nTax (0%): $0.00\nTip (15%): $0.14\nTotal: $1.13"),
]

submit_cases = run_cases + [
    (0, 10, 20, "Subtotal: $0.00\nTax (10%): $0.00\nTip (20%): $0.00\nTotal: $0.00"),
    (1, 99, 99, "Subtotal: $0.01\nTax (99%): $0.00\nTip (99%): $0.00\nTotal: $0.01"),
    (
        123456,
        7,
        18,
        "Subtotal: $1234.56\nTax (7%): $86.41\nTip (18%): $222.22\nTotal: $1543.19",
    ),
]


def format_input(subtotal_cents, tax_percent, tip_percent):
    return (
        f"Subtotal cents: {subtotal_cents}\n"
        f"Tax percent:    {tax_percent}\n"
        f"Tip percent:    {tip_percent}"
    )


def test(subtotal_cents, tax_percent, tip_percent, expected_output):
    print("---------------------------------")
    print("Input:")
    print(format_input(subtotal_cents, tax_percent, tip_percent))
    print("")
    result = format_checkout_summary(subtotal_cents, tax_percent, tip_percent)
    print("Expected:")
    print(expected_output)
    print("")
    print("Actual:")
    print(result)

    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
