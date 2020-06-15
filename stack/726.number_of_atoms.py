"""
Given a chemical formula (given as a string), return the count of each atom.
An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input: 
formula = "H2O"
Output: "H2O"
Explanation: 
The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input: 
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: 
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input: 
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: 
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Note:
All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
"""

import string


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula = "(" + formula + ")"
        cnt = {}
        stk = []
        group = []
        i = 0

        while i < len(formula):
            if formula[i] == "(":
                stk.append(formula[i])
            elif formula[i].isalpha():
                atom = formula[i]

                while i < len(formula) and formula[i + 1] in string.ascii_lowercase:
                    atom += formula[i + 1]
                    i += 1

                stk.append((atom, 1))
            elif formula[i].isdigit():
                m = formula[i]

                while i < len(formula) - 1 and formula[i + 1].isdigit():
                    m += formula[i + 1]
                    i += 1

                if not group:
                    top, n = stk.pop()
                    stk.append((top, n * int(m)))
                else:
                    stk += [(x, n * int(m)) for x, n in group]
                    group.clear()
            elif formula[i] == ")":
                while stk and stk[-1] != "(":
                    atom, n = stk.pop()
                    group.append((atom, n))

                if stk and stk[-1] == "(":
                    stk.pop()

            i += 1

        while group:
            atom, n = group.pop()
            cnt[atom] = cnt.get(atom, 0) + n

        res = ""

        for atom in sorted(cnt):
            res += atom
            res += str(cnt[atom]) if cnt[atom] != 1 else ""

        return res
