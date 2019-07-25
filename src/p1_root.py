def isqrt(n):
    # Handle negative numbers
    if n < 0:
        return None
    # Handle base case
    if n < 2:
        return n

    shift = 2
    n_shifted = n >> shift
    # We check for n_shifted being n, since some implementations perform shift operations modulo the word size.
    while n_shifted != 0 and n_shifted != n:
        shift = shift + 2
        n_shifted = n >> shift
    shift = shift - 2

    # Find digits of result.
    result = 0
    while shift >= 0:
        result = result << 1
        candidate_result = result + 1
        if candidate_result * candidate_result <= (n >> shift):
            result = candidate_result
        shift = shift - 2

    return result


print("Pass" if (3 == isqrt(9)) else "Fail")
print("Pass" if (0 == isqrt(0)) else "Fail")
print("Pass" if (4 == isqrt(16)) else "Fail")
print("Pass" if (1 == isqrt(1)) else "Fail")
print("Pass" if (5 == isqrt(27)) else "Fail")

print("Pass" if (isqrt(-25) is None) else "Fail")  # negative number are invalid
print("Pass" if (10000 == isqrt(100000000)) else "Fail")  # negative number are invalid
print("Pass" if (10000 == isqrt(100000001)) else "Fail")  # negative number are invalid
print("Pass" if (100000000 == (isqrt(10000000000000000))) else "Fail")  # negative number are invalid
