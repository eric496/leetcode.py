"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix
Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

Example 1:
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:
Input: "/a/./b/../../c/"
Output: "/c"

Example 5:
Input: "/a/../../b/../c//.//"
Output: "/c"

Example 6:
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
"""


"""
Thought Process:
    1. Split on slashes: `path.split("/")` breaks the path into directory
       tokens while turning consecutive, leading, and trailing slashes into
       empty strings `""`.
    2. Simulate directory depth with a stack:
       - Ignore `""` and `"."` (no change in directory).
       - On `".."`: Pop the top directory from `stack` if non-empty (stay at
         root if already empty).
       - On any other token (including `"..."` or `"...."`): Push onto `stack`.
    3. Reconstruct canonical path: Join surviving directories with `"/"` and
       prepend a leading `"/"` (returns `"/"` automatically when `stack` is empty).

Complexity:
    Time: O(n) — splitting, scanning tokens, and joining each take linear time.
    Space: O(n) — for the split token list and directory stack.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        sep = "/"

        for d in path.split(sep):
            if d in ("", "."):
                continue
            elif d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)

        return sep + sep.join(stack) 
