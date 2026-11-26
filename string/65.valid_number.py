"""
Given a string s, return whether s is a valid number.
For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".
Formally, a valid number is defined using one of the following definitions:
An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.
A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.
The digits are defined as one or more digits.

Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false

Constraints:
1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""


"""
Thought Process:
    1. Track state with four flags across one linear scan:
       - `seen_digit`: At least one digit appeared in the base (mantissa).
       - `seen_dot`: A decimal point '.' has already appeared.
       - `seen_exp`: An exponent marker ('e' or 'E') has already appeared.
       - `seen_digit_after_exp`: At least one digit appeared after 'e'/'E'
         (initialized to True before any exponent is seen).
    2. Validate each character against positional rules:
       - Digit ('0'-'9'): Set `seen_digit = True`; if `seen_exp` is True,
         set `seen_digit_after_exp = True`.
       - Sign ('+' or '-'): Valid ONLY at index 0 or immediately following
         'e'/'E' (`s[i - 1] in "eE"`).
       - Dot ('.'): Valid ONLY if neither a dot nor an exponent has appeared
         yet (`not seen_dot and not seen_exp`), since exponents must be integers.
       - Exponent ('e' or 'E'): Valid ONLY if a base digit was already seen
         and no exponent has appeared yet (`seen_digit and not seen_exp`);
         reset `seen_digit_after_exp = False` to require exponent digits.
       - Any other character: Return False immediately.
    3. Final check: Return `seen_digit and seen_digit_after_exp`.

Complexity:
    Time: O(n) — single linear pass over `s`.
    Space: O(1) — only four boolean flags used.
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exp = False
        seen_digit_after_exp = True

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                if seen_exp:
                    seen_digit_after_exp = True
            elif char in "+-":
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif char == ".":
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif char in "eE":
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit_after_exp = False
            else:
                return False

        return seen_digit and seen_digit_after_exp
