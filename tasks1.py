import math
from collections import deque
import random
from interface import Algorithm

class TwoNumberSum(Algorithm):
    """
    This algorithm finds two numbers in an array that add up to a given target sum. It takes an array
    of distinct integers and a target value, then searches for a pair of numbers that sum to the target.
    It works by iterating through the array and checking if the difference (target minus the current number)
    exists elsewhere in the array. If a pair is found, it returns them in an array. If no pair is found,
    it returns an empty array. To avoid using the same number twice, it removes half the target sum from
    consideration if it exists (e.g., if target is 10, it skips using 5 twice). Since there’s at most one
    pair, it stops after finding the first match.
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        arr = kwargs.get('arr')
        a = kwargs.get('target')
        outcome = []
        if a/2 in arr:
            arr.remove(a/2)
        for i in arr:
            if i >= 0 and (a - i) in arr:
                if [i, a - i] not in outcome and [a - i, i] not in outcome:
                    outcome.append([i, a - i])
            elif i < 0 and (a + i) in arr:
                if [i, a + i] not in outcome and [a + i, i] not in outcome:
                    outcome.append([i, a - i])
        return outcome[0] if outcome else []
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = kwargs.get('arr')
        a = kwargs.get('target')
        outcome = []
        if a/2 in arr:
            arr.remove(a/2)
        for i in arr:
            if i >= 0 and (a - i) in arr:
                if [i, a - i] not in outcome and [a - i, i] not in outcome:
                    outcome.append([i, a - i])
            elif i < 0 and (a + i) in arr:
                if [i, a + i] not in outcome and [a + i, i] not in outcome:
                    outcome.append([i, a - i])
        return outcome[0] if outcome else []

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"arr": [3, 5, -4, 8, 11, 1, -1, 6], "target": 10},
                "expected": [-1, 11]
            },
            {
                "inputs": {"arr": [4, 6], "target": 10},
                "expected": [4, 6]
            },
            {
                "inputs": {"arr": [1, 2, 3, 4], "target": 10},
                "expected": []
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(**inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class MoveZeros(Algorithm):
    """
    This algorithm takes an array of integers and moves all zeros to the end while keeping the
    order of non-zero elements the same. It works by iterating through the array, and whenever
    it finds a zero, it removes that zero from its current position and adds it to the end.
    Since this happens in-place, the array itself is modified step-by-step. Non-zero elements
    stay in their original order because we only shift zeros, leaving everything else untouched.
    By the end, all zeros are grouped at the tail of the array.
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        arr = args[0]
        for i in arr:
            if i == 0:
                arr.remove(i)
                arr.append(0)
        return arr
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        for i in arr:
            if i == 0:
                arr.remove(i)
                arr.append(0)
        return arr

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"arr": [0, 1, 0, 3, 12]},
                "expected": [1, 3, 12, 0, 0]
            },
            {
                "inputs": {"arr": [1, 2, 3]},
                "expected": [1, 2, 3]
            },
            {
                "inputs": {"arr": [0, 0, 0, 1]},
                "expected": [1, 0, 0, 0]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            arr_copy = inputs["arr"].copy()
            result = cls.execute(arr=arr_copy)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class FindThreeLargestNumber(Algorithm):
    """
    This algorithm finds the three largest numbers in an array of integers and returns them in a
    sorted array (smallest to largest). It works by repeatedly finding the maximum value in the
    input array, adding it to a new list, and removing it from the original array. This process
    repeats three times to get the top three numbers. If the array has fewer than three elements,
    it raises an error. Since it picks the maximum each time, it naturally handles duplicates
    (e.g., if the largest number appears multiple times, it’ll use it). Finally, it sorts the
    result so the output is in ascending order, as required.
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        arr = args[0]
        n = 3
        if len(arr) < n:
            raise ValueError("Array input has to have at least 3 elements")
        largest_arr = []
        for i in range(n):
            maximum = max(arr)
            largest_arr.append(maximum)
            arr.remove(maximum)
        return sorted(largest_arr)
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        n = 3
        if len(arr) < n:
            raise ValueError("Array input has to have at least 3 elements")
        largest_arr = []
        for i in range(n):
            maximum = max(arr)
            largest_arr.append(maximum)
            arr.remove(maximum)
        return sorted(largest_arr)

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"arr": [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]},
                "expected": [18, 141, 541]
            },
            {
                "inputs": {"arr": [10, 10, 10, 5, 2]},
                "expected": [10, 10, 10]
            },
            {
                "inputs": {"arr": [1, 2, 3, 4, 5]},
                "expected": [3, 4, 5]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            arr_copy = inputs["arr"].copy()  # Avoid modifying original input
            result = cls.execute(arr_copy)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class BestTimeToBuyAndSellStocks(Algorithm):
    """
    This algorithm calculates the maximum profit you can make by buying and selling a stock once.
    It takes an array of daily stock prices and finds the best opportunity to buy low and sell high
    later. It keeps track of the lowest price seen so far (the best time to buy) and the maximum
    profit possible (the biggest difference between a later price and that minimum). It scans the
    array once, updating the minimum price whenever a lower one is found, and updating the profit
    if a higher sell price after the minimum yields a bigger gain. If no profit is possible (e.g.,
    prices only decrease), it returns 0.
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        arr = args[0]
        min_price = float('inf')
        max_profit = 0

        for day, price in enumerate(arr):
            if price < min_price:
                print(price, min_price)
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        min_price = float('inf')
        max_profit = 0

        for day, price in enumerate(arr):
            if price < min_price:
                print(price, min_price)
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"arr": [7, 1, 5, 3, 6, 4]},
                "expected": 5
            },
            {
                "inputs": {"arr": [7, 6, 4, 3, 1]},
                "expected": 0
            },
            {
                "inputs": {"arr": [2, 4, 1]},
                "expected": 2
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["arr"])
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class ContainsDuplicates(Algorithm):
    """
    This algorithm checks if an array of integers has any duplicate values. It uses a set to keep
    track of numbers it has seen so far. It goes through the array one number at a time: if the
    current number is already in the set, it means we’ve found a duplicate, so it returns true.
    If it gets through the whole array without finding any repeats, it returns false. The set
    makes this fast because checking if a number is already there is super quick, and it only
    needs to scan the array once.
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        arr = args[0]
        checked_nums = set()
        for num in arr:
            if num in checked_nums:
                return True
            checked_nums.add(num)
        return False
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        checked_nums = set()
        for num in arr:
            if num in checked_nums:
                return True
            checked_nums.add(num)
        return False

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"arr": [1, 2, 3, 1]},
                "expected": True
            },
            {
                "inputs": {"arr": [1, 2, 3, 4]},
                "expected": False
            },
            {
                "inputs": {"arr": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]},
                "expected": True
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["arr"])
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class ValidateSubsequence(Algorithm):
    """
    This algorithm checks if one array is a subsequence of another. A subsequence means the numbers
    in the second array appear in the same order within the first array, but they don’t have to be
    next to each other. It works by stepping through the main array and keeping a pointer for the
    sequence. Each time it finds a match with the current sequence number, it moves the pointer
    forward. If the pointer reaches the end of the sequence, it means all numbers were found in
    order, so it returns true. If it finishes the main array without finding all sequence numbers,
    it returns false. It’s simple and only needs one pass through the main array.
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        arr1 = args[0]
        arr2 = args[1]
        length = len(arr2)
        k = 0
        for v in arr1:
            if arr2[k] == v:
                k += 1
            if k == length:
                return True
        return False
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr1 = args[0]
        arr2 = args[1]
        length = len(arr2)
        k = 0
        for v in arr1:
            if arr2[k] == v:
                k += 1
            if k == length:
                return True
        return False

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"arr": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, -1, 10]},
                "expected": True
            },
            {
                "inputs": {"arr": [1, 2, 3, 4], "sequence": [1, 3, 4]},
                "expected": True
            },
            {
                "inputs": {"arr": [5, 1, 22, 25, 6, -1, 8, 10], "sequence": [1, 6, 10, -1]},
                "expected": False
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["arr"], inputs["sequence"])
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class PalindromeCheck(Algorithm):
    """
    This algorithm checks if a given string is a palindrome, meaning it reads the same forward and
    backward (like 'racecar' or 'abcdcba'). It works by converting the input to a string (just in
    case it’s not already one), then comparing it to its reverse. The reverse is created using a
    simple slice trick that steps backward through the string. If they match, it returns true; if
    not, it returns false. It’s a quick and straightforward way to test for palindromes in one line!
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        txt = args[0]
        return str(txt) == txt[::-1]
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        txt = args[0]
        return str(txt) == txt[::-1]

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"txt": "abcdcba"},
                "expected": True
            },
            {
                "inputs": {"txt": "hello"},
                "expected": False
            },
            {
                "inputs": {"txt": "racecar"},
                "expected": True
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["txt"])
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class CaesarCipherEncryptor(Algorithm):
    """
    This algorithm encrypts a string using a Caesar cipher, shifting each letter by a given number
    of positions (the key) in the alphabet. It goes through the string letter by letter. If the
    letter is alphabetic, it checks if it’s uppercase or lowercase to set the starting point (A=65
    or a=97 in ASCII). Then it shifts the letter by the key, wrapping around the alphabet using
    modulo 26, and converts the result back to a character. Non-alphabetic characters are ignored.
    The result is a new string with all letters shifted, preserving their original case.
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        txt = args[0]
        k = args[1]
        encrypted_text = ""
        for letter in txt:
            if letter.isalpha():
                if letter.isupper():
                    start_point = 65
                else:
                    start_point = 96

                encrypted_text += chr(((ord(letter) - start_point + k) % 26) + start_point)

        return encrypted_text
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        txt = args[0]
        k = args[1]
        encrypted_text = ""
        for letter in txt:
            if letter.isalpha():
                if letter.isupper():
                    start_point = 65
                else:
                    start_point = 96

                encrypted_text += chr(((ord(letter) - start_point + k) % 26) + start_point)

        return encrypted_text

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"txt": "xyz", "k": 2},
                "expected": "zab"
            },
            {
                "inputs": {"txt": "abc", "k": 1},
                "expected": "bcd"
            },
            {
                "inputs": {"txt": "xyz", "k": 26},
                "expected": "xyz"
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["txt"], inputs["k"])
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class FirstNonRepeatingCharacter(Algorithm):
    """
    This algorithm finds the first character in a string that doesn’t repeat. It uses a dictionary
    to count how many times each character appears. It first goes through the string, building the
    dictionary: if a character is new, it gets a count of 1; if it’s already there, the count goes
    up. Then it checks the dictionary for the first character with a count of 1 and returns that
    character. If every character repeats, it doesn’t return anything.
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        txt = args[0]
        letter_dict = dict()
        for char in txt:
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1

        for char, count in letter_dict.items():
            if count == 1:
                return txt.index(char)
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        txt = args[0]
        letter_dict = dict()
        for char in txt:
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1

        for char, count in letter_dict.items():
            if count == 1:
                return txt.index(char)

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"txt": "abcdcaf"},
                "expected": "b"
            },
            {
                "inputs": {"txt": "aabbcc"},
                "expected": None
            },
            {
                "inputs": {"txt": "leetcode"},
                "expected": "l"
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["txt"])
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class ValidAnagram(Algorithm):
    """
    This algorithm checks if two strings are anagrams—meaning they have the same letters with the
    same counts, just in a different order. It first checks if the strings have the same length;
    if not, they can’t be anagrams, so it returns false. Then it builds a dictionary counting how
    many times each character appears in the first string. Next, it goes through the second string,
    reducing the count for each character. If a character isn’t in the dictionary or its count goes
    below zero, it returns false. Finally, it checks if all counts are zero (all letters used up);
    if so, it returns true. It’s a clean way to confirm the strings are rearrangements of each other!
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        s = args[0]
        t = args[1]
        if len(s) != len(t):
            return False

        char_count = dict()
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        for count in char_count.values():
            if count != 0:
                return False

        return True
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]
        t = args[1]
        if len(s) != len(t):
            return False

        char_count = dict()
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        for count in char_count.values():
            if count != 0:
                return False

        return True

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"s": "anagram", "t": "nagaram"},
                "expected": True
            },
            {
                "inputs": {"s": "rat", "t": "car"},
                "expected": False
            },
            {
                "inputs": {"s": "a", "t": "a"},
                "expected": True
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["s"], inputs["t"])
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class BinarySearch(Algorithm):
    """
    This algorithm uses binary search to find a target integer in a sorted array. It starts by
    setting two pointers: one at the beginning (left) and one at the end (right) of the array.
    It then repeatedly calculates the middle point and compares the middle element to the target.
    If they match, it returns the middle index. If the middle element is too small, it moves the
    left pointer past the middle; if too large, it moves the right pointer before the middle.
    This cuts the search space in half each time until the target is found or the pointers cross,
    meaning the target isn’t there, so it returns -1. It’s super fast for sorted data!
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        arr = args[0]
        target = args[1]

        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1

        return -1
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        target = args[1]

        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1

        return -1

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"arr": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 33},
                "expected": 3
            },
            {
                "inputs": {"arr": [1, 2, 3, 4, 5], "target": 6},
                "expected": -1
            },
            {
                "inputs": {"arr": [1], "target": 1},
                "expected": 0
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["arr"], inputs["target"])
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class FindClosestValueInBST(Algorithm):
    """
    This algorithm finds the value in a Binary Search Tree (BST) that’s closest to a given target
    integer. It uses a recursive helper function that traverses the tree, keeping track of the
    closest value seen so far. Starting at the root, it compares the target to the current node’s
    value: if the difference is smaller than the current closest, it updates the closest value.
    If the target equals the node’s value, it returns that (since it’s exact). Otherwise, it
    decides to go left (if target is smaller) or right (if target is larger), using the BST
    property to narrow the search. If it hits a null node, it returns the closest value found.
    It’s efficient because it only explores one path down the tree!
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        tree = args[0]
        target = args[1]

        def helper(node, target, closest):
            if node is None: 
                return closest

            if abs(target - node.value) < abs(target - closest):
                closest = node.value

            if node.value == target:
                return closest

            if target < node.value:
                return helper(node.left, target, closest)
            else:
                return helper(node.right, target, closest)

        return helper(tree, target, tree.value)
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        tree = args[0]
        target = args[1]

        def helper(node, target, closest):
            if node is None:
                return closest

            if abs(target - node.value) < abs(target - closest):
                closest = node.value

            if node.value == target:
                return closest

            if target < node.value:
                return helper(node.left, target, closest)
            else:
                return helper(node.right, target, closest)

        return helper(tree, target, tree.value)

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        # Assuming a simple Node class with value, left, right
        class Node:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        bst = Node(10)
        bst.left = Node(5)
        bst.right = Node(15)
        bst.left.left = Node(2)
        bst.left.right = Node(7)
        bst.right.left = Node(13)
        bst.right.right = Node(22)

        return [
            {
                "inputs": {"tree": bst, "target": 12},
                "expected": 13
            },
            {
                "inputs": {"tree": bst, "target": 6},
                "expected": 7
            },
            {
                "inputs": {"tree": bst, "target": 23},
                "expected": 22
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["tree"], inputs["target"])
            results.append(f"Test {i}: Inputs={{'tree': BST, 'target': {inputs['target']}}}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class BSTTraversal(Algorithm):
    """
    This algorithm performs three types of traversals on a Binary Search Tree (BST): in-order,
    pre-order, and post-order. It uses recursive helper functions for each traversal type. In-order
    visits the left subtree, then the root, then the right subtree, giving a sorted order for a BST.
    Pre-order visits the root first, then left, then right, showing the tree’s structure top-down.
    Post-order visits left, then right, then the root, useful for bottom-up processing. The main
    function runs all three traversals, collects the results in separate arrays, and returns them
    as a formatted string. It’s a handy way to see all traversal results at once!
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        tree = args[0]
        inorder_array = []
        preorder_array = []
        postorder_array = []
        cls.inOrderTraverse(tree, inorder_array)
        cls.postOrderTraverse(tree, postorder_array)
        cls.preOrderTraverse(tree, preorder_array)
        return f"inorder: {inorder_array}, postorder: {postorder_array}, preorder: {preorder_array}"

    def inOrderTraverse(cls, tree, array):
        if tree is not None:
            cls.inOrderTraverse(tree.left, array)  # Traverse left subtree
            array.append(tree.value)  # Visit root
            cls.inOrderTraverse(tree.right, array)  # Traverse right subtree
        return array

    def preOrderTraverse(cls, tree, array):
        if tree is not None:
            array.append(tree.value)  # Visit root
            cls.preOrderTraverse(tree.left, array)  # Traverse left subtree
            cls.preOrderTraverse(tree.right, array)  # Traverse right subtree
        return array

    def postOrderTraverse(cls, tree, array):
        if tree is not None:
            cls.postOrderTraverse(tree.left, array)  # Traverse left subtree
            cls.postOrderTraverse(tree.right, array)  # Traverse right subtree
            array.append(tree.value)  # Visit root
        return array
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        tree = args[0]
        inorder_array = []
        preorder_array = []
        postorder_array = []
        cls.inOrderTraverse(tree, inorder_array)
        cls.postOrderTraverse(tree, postorder_array)
        cls.preOrderTraverse(tree, preorder_array)
        return f"inorder: {inorder_array}, postorder: {postorder_array}, preorder: {preorder_array}"

    @classmethod
    def inOrderTraverse(cls, tree, array):
        if tree is not None:
            cls.inOrderTraverse(tree.left, array)  # Traverse left subtree
            array.append(tree.value)  # Visit root
            cls.inOrderTraverse(tree.right, array)  # Traverse right subtree
        return array

    @classmethod
    def preOrderTraverse(cls, tree, array):
        if tree is not None:
            array.append(tree.value)  # Visit root
            cls.preOrderTraverse(tree.left, array)
            cls.preOrderTraverse(tree.right, array)
        return array

    @classmethod
    def postOrderTraverse(cls, tree, array):
        if tree is not None:
            cls.postOrderTraverse(tree.left, array)
            cls.postOrderTraverse(tree.right, array)
            array.append(tree.value)
        return array

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):

        class Node:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        bst = Node(10)
        bst.left = Node(5)
        bst.right = Node(15)
        bst.left.left = Node(2)
        bst.left.right = Node(7)
        bst.right.left = Node(13)
        bst.right.right = Node(22)

        return [
            {
                "inputs": {"tree": bst},
                "expected": "inorder: [2, 5, 7, 10, 13, 15, 22], postorder: [2, 7, 5, 13, 22, 15, 10], preorder: [10, 5, 2, 7, 15, 13, 22]"
            },
            {
                "inputs": {"tree": Node(1)},
                "expected": "inorder: [1], postorder: [1], preorder: [1]"
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["tree"])
            results.append(f"Test {i}: Inputs={{'tree': BST}}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class ValidateBST(Algorithm):
    """
    This algorithm checks if a Binary Search Tree (BST) is valid by ensuring every node follows
    the BST property: its value must be greater than all nodes in its left subtree and less than
    or equal to all nodes in its right subtree. It uses a recursive helper function that tracks
    the valid range for each node’s value, starting with negative infinity to positive infinity
    at the root. For each node, it checks if the value is within the allowed range. Then it
    recursively validates the left subtree (with an updated max value) and the right subtree
    (with an updated min value). If any node fails or if the tree is empty (None), it returns
    true for empty and false for invalid. It’s a clever way to enforce BST rules!
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        tree = args[0]

        def validateHelper(node, minValue, maxValue):
            if node is None:
                return True

            if node.value <= minValue or node.value > maxValue:
                return False

            return (validateHelper(node.left, minValue, node.value - 1) and
                    validateHelper(node.right, node.value, maxValue))

        return validateHelper(tree, float('-inf'), float('inf'))
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        tree = args[0]

        def validateHelper(node, minValue, maxValue):
            if node is None:
                return True

            if node.value <= minValue or node.value > maxValue:
                return False

            return (validateHelper(node.left, minValue, node.value - 1) and
                    validateHelper(node.right, node.value, maxValue))

        return validateHelper(tree, float('-inf'), float('inf'))

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):

        class Node:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        valid_bst = Node(10)
        valid_bst.left = Node(5)
        valid_bst.right = Node(15)
        valid_bst.left.left = Node(2)
        valid_bst.left.right = Node(7)
        valid_bst.right.left = Node(13)
        valid_bst.right.right = Node(22)


        invalid_bst = Node(10)
        invalid_bst.left = Node(5)
        invalid_bst.right = Node(15)
        invalid_bst.left.left = Node(2)
        invalid_bst.left.right = Node(12)
        invalid_bst.right.left = Node(13)
        invalid_bst.right.right = Node(22)

        return [
            {
                "inputs": {"tree": valid_bst},
                "expected": True
            },
            {
                "inputs": {"tree": invalid_bst},
                "expected": False
            },
            {
                "inputs": {"tree": None},
                "expected": True
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["tree"])
            results.append(f"Test {i}: Inputs={{'tree': BST}}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class MaximumDepthOfBinaryTree(Algorithm):
    """
    This algorithm calculates the maximum depth of a binary tree, which is the longest path from
    the root to any leaf node. It uses a recursive approach: if the tree is empty (None), the depth
    is 0. Otherwise, it finds the depth of the left subtree and the right subtree by calling itself
    on each child. The maximum depth is then the larger of the two subtree depths plus 1 (to count
    the current node). It’s a simple yet effective way to measure how deep the tree goes!
    """
    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        tree = args[0]
        return cls.maxDepth(tree)

    def maxDepth(cls, root):
        if root is None:
            return 0

        left_depth = cls.maxDepth(root.left)
        right_depth = cls.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        tree = args[0]
        return cls.maxDepth(tree)

    @classmethod
    def maxDepth(cls, root):
        if root is None:
            return 0

        left_depth = cls.maxDepth(root.left)
        right_depth = cls.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        # Assuming a simple Node class
        class Node:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        tree1 = Node(3)
        tree1.left = Node(9)
        tree1.right = Node(20)
        tree1.right.left = Node(15)
        tree1.right.right = Node(7)

        tree2 = Node(1)

        return [
            {
                "inputs": {"tree": tree1},
                "expected": 3
            },
            {
                "inputs": {"tree": tree2},
                "expected": 1
            },
            {
                "inputs": {"tree": None},
                "expected": 0
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["tree"])
            results.append(f"Test {i}: Inputs={{'tree': BinaryTree}}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class NthFibonacci(Algorithm):
    """
    The Fibonacci sequence is defined as follows:
    - The first number is 0
    - The second number is 1
    - The nth number is the sum of the (n-1)th and (n-2)th numbers

    Given an integer n, this algorithm returns the nth Fibonacci number.

    Example:
    Input: n = 6
    Output: 5 (Sequence: 0, 1, 1, 2, 3, 5)
    """

    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        n = args[0]
        a = 0
        b = 1
        idx = n - 1
        for _ in range(idx):
            c = a
            a = a + b
            b = c
        return a
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        n = kwargs.get('n')
        a = 0
        b = 1
        idx = n - 1
        for _ in range(idx):
            c = a
            a = a + b
            b = c
        return a

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {"inputs": {"n": 6}, "expected": 5},
            {"inputs": {"n": 1}, "expected": 0},
            {"inputs": {"n": 2}, "expected": 1},
            {"inputs": {"n": 10}, "expected": 34}
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(**inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class MinimumCoinsForChange(Algorithm):
    """
    Given an array of positive integers representing coin denominations and a target amount,
    this algorithm returns the smallest number of coins needed to make change.
    If it's impossible to make change for the target amount, it returns -1.

    Example:
    Input: n = 7, denoms = [1, 5, 10]
    Output: 3 (2x1 + 1x5)
    """

    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        coins = args[0]
        target = args[1]
        return cls.min_coins(coins, target)

    def min_coins(cls, coins, target):
        if target == 0:
            return 0
        if target < 0:
            return -1

        min_coins = float('inf')

        for coin in coins:
            result = cls.min_coins(coins, target - coin)
            if result != -1:
                current_coins = 1 + result
                min_coins = min(min_coins, current_coins)

        return min_coins if min_coins != float('inf') else -1
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        coins = kwargs.get('denoms')
        target = kwargs.get('n')
        return cls.min_coins(coins, target)

    @classmethod
    def min_coins(cls, coins, target):
        if target == 0:
            return 0
        if target < 0:
            return -1

        min_coins = float('inf')

        for coin in coins:
            result = cls.min_coins(coins, target - coin)
            if result != -1:
                current_coins = 1 + result
                min_coins = min(min_coins, current_coins)

        return min_coins if min_coins != float('inf') else -1

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {"inputs": {"n": 7, "denoms": [1, 5, 10]}, "expected": 3},
            {"inputs": {"n": 0, "denoms": [1, 2, 3]}, "expected": 0},
            {"inputs": {"n": 11, "denoms": [1, 2, 5]}, "expected": 3},
            {"inputs": {"n": 3, "denoms": [2, 4]}, "expected": -1}
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(**inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class ClimbingStairs(Algorithm):
    """
    You are climbing a staircase that takes 'n' steps to reach the top.
    Each time, you can either climb 1 or 2 steps.
    This algorithm returns the number of distinct ways to climb to the top.

    Example:
    Input: n = 3
    Output: 3
    Explanation:
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    """

    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        n = args[0]
        return cls.climbing(n)

    def climbing(cls, n):
        if n == 0:
            return 0
        if n < 0:
            return -1

        return cls.climbing(n - 1) + cls.climbing(n - 2)
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        n = kwargs.get('n')
        return cls.climbing(n)

    @classmethod
    def climbing(cls, n):
        if n <= 0:
            return 0 if n == 0 else -1

        memo = {0: 1, 1: 1}
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {"inputs": {"n": 3}, "expected": 3},
            {"inputs": {"n": 4}, "expected": 5},
            {"inputs": {"n": 5}, "expected": 8},
            {"inputs": {"n": 1}, "expected": 1}
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(**inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class MaximumSubarray(Algorithm):
    """
    Given an integer array nums, this algorithm finds the contiguous subarray
    (containing at least one number) that has the largest sum and returns its sum.

    Example:
    Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6 (subarray [4, -1, 2, 1])
    """

    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        arr = args[0]
        max_sum = float("-inf")
        current_sum = 0
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = kwargs.get('nums')
        max_sum = float("-inf")
        current_sum = 0
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {"inputs": {"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4]}, "expected": 6},
            {"inputs": {"nums": [1]}, "expected": 1},
            {"inputs": {"nums": [5, 4, -1, 7, 8]}, "expected": 23},
            {"inputs": {"nums": [-1, -2, -3, -4]}, "expected": -1}
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(**inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class HouseRobber(Algorithm):
    """
    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed, but adjacent houses
    have security systems that will alert the police if both are robbed.

    This algorithm determines the maximum amount of money you can rob
    tonight without alerting the police.

    Example:
    Input: nums = [1, 2, 3, 1]
    Output: 4 (Rob house 1 (money = 1) and then rob house 3 (money = 3))
    """

    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        arr = args[0]
        opt2 = 0
        opt1 = arr[0]
        for i in range(1, len(arr)):
            current = max(arr[i] + opt2, opt1)
            opt2 = opt1
            opt1 = current
        return opt1
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        nums = kwargs.get('nums')
        if not nums:
            return 0

        opt2, opt1 = 0, 0
        for num in nums:
            current = max(num + opt2, opt1)
            opt2 = opt1
            opt1 = current
        return opt1

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {"inputs": {"nums": [1, 2, 3, 1]}, "expected": 4},
            {"inputs": {"nums": [2, 7, 9, 3, 1]}, "expected": 12},
            {"inputs": {"nums": [5, 1, 1, 5]}, "expected": 10},
            {"inputs": {"nums": [0]}, "expected": 0},
            {"inputs": {"nums": []}, "expected": 0}
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(**inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class MinimumWaitingTime(Algorithm):
    """
    Calculates the minimum total waiting time for queries by processing shorter queries first.
    The optimal strategy is to sort the queries in ascending order and sum the waiting times.
    Waiting time for each query is the sum of durations of all previous queries.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        arr = sorted(args[0], reverse=True)
        min_sum = 0
        for i, v in enumerate(arr):
            min_sum += i * v
        return min_sum
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = sorted(args[0], reverse=True)
        min_sum = 0
        for i, v in enumerate(arr):
            min_sum += i * v
        return min_sum

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"queries": [3, 2, 1, 2, 6]},
                "expected": 17
            },
            {
                "inputs": {"queries": [5]},
                "expected": 0
            },
            {
                "inputs": {"queries": [1, 4, 5]},
                "expected": 5  # (0) + (1) + (1+4) = 5
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["queries"])
            results.append(
                f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class ClassPhotos(Algorithm):
    """
    Determines if class photos can be arranged with one color in front row and the other in back row,
    where every back row student must be strictly taller than the front row student directly in front.
    The solution sorts both groups and checks if one group can be placed entirely in front of the other.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        arr1 = sorted(args[0])
        arr2 = sorted(args[1])
        for i in range(len(arr1)):
            if arr1[i] < arr2[i]:
                continue
            if i == 0 and arr1[i] > arr2[i]:
                arr1, arr2 = arr2, arr1
                continue
            else:
                return False
        else:
            return True
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr1 = sorted(args[0])
        arr2 = sorted(args[1])
        for i in range(len(arr1)):
            if arr1[i] < arr2[i]:
                continue
            if i == 0 and arr1[i] > arr2[i]:
                arr1, arr2 = arr2, arr1
                continue
            else:
                return False
        else:
            return True

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"red_shirt_heights": [5, 8, 1, 3, 4], "blue_shirt_heights": [6, 9, 2, 4, 5]},
                "expected": True
            },
            {
                "inputs": {"red_shirt_heights": [6], "blue_shirt_heights": [6]},
                "expected": False
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["red_shirt_heights"], inputs["blue_shirt_heights"])
            results.append(
                f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class TandemBicycle(Algorithm):
    """
    Calculates either the maximum or minimum possible total speed of tandem bicycle pairs.
    The speed of each tandem bicycle is determined by the faster rider of the pair.
    When 'fastest' is True, pairs the fastest riders together to maximize total speed.
    When 'fastest' is False, pairs the fastest riders with slowest riders to minimize total speed.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        flag = args[2]
        arr1 = sorted(args[0])
        arr2 = sorted(args[1]) if not flag else sorted(args[1], reverse=True)
        max_sum = 0
        for i in range(len(arr1)):
            max_sum += max(arr1[i], arr2[i])
        return max_sum
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        flag = args[2]
        arr1 = sorted(args[0])
        arr2 = sorted(args[1]) if not flag else sorted(args[1], reverse=True)
        max_sum = 0
        for i in range(len(arr1)):
            max_sum += max(arr1[i], arr2[i])
        return max_sum

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"red_shirt_speeds": [5, 5, 3, 9, 2],
                          "blue_shirt_speeds": [3, 6, 7, 2, 1],
                          "fastest": True},
                "expected": 32
            },
            {
                "inputs": {"red_shirt_speeds": [5, 5, 3, 9, 2],
                          "blue_shirt_speeds": [3, 6, 7, 2, 1],
                          "fastest": False},
                "expected": 25
            },
            {
                "inputs": {"red_shirt_speeds": [1, 2, 1, 9, 12, 3],
                          "blue_shirt_speeds": [3, 3, 4, 6, 1, 2],
                          "fastest": True},
                "expected": 37
            },
            {
                "inputs": {"red_shirt_speeds": [10],
                           "blue_shirt_speeds": [10],
                           "fastest": True},
                "expected": 10
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["red_shirt_speeds"],
                               inputs["blue_shirt_speeds"],
                               inputs["fastest"])
            results.append(
                f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class ValidStartingCity(Algorithm):
    """
    Finds the valid starting city in a circular route where:
    - Cities are connected in a circle with given distances between them
    - Each city provides a certain amount of fuel
    - The car has a specific miles-per-gallon (MPG) rating
    - The solution identifies the unique city where you can complete the circuit
    Algorithm works by tracking fuel surplus/deficit at each city and finding the point
    where running deficit is minimized (which must be the valid starting city).
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        distances = args[0]
        gallons = args[1]
        consumption = args[2]
        gallons_left_after_travel = [v - distances[i] / consumption for i, v in enumerate(gallons)]
        valid_index = None
        current_sum = 0
        for i in range(len(gallons)):
            curr_diff = gallons_left_after_travel[i]
            if current_sum <= 0 <= curr_diff:
                valid_index = i
                current_sum = curr_diff
                continue
            current_sum += gallons_left_after_travel[i]
        return valid_index
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        distances = args[0]
        gallons = args[1]
        consumption = args[2]
        gallons_left_after_travel = [v - distances[i] / consumption for i, v in enumerate(gallons)]
        valid_index = None
        current_sum = 0
        for i in range(len(gallons)):
            curr_diff = gallons_left_after_travel[i]
            if current_sum <= 0 <= curr_diff:
                valid_index = i
                current_sum = curr_diff
                continue
            current_sum += gallons_left_after_travel[i]
        return valid_index

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "distances": [5, 25, 15, 10, 15],
                    "fuel": [1, 2, 1, 0, 3],
                    "mpg": 10
                },
                "expected": 4
            },
            {
                "inputs": {
                    "distances": [10, 20, 10, 15, 5],
                    "fuel": [1, 2, 1, 0, 3],
                    "mpg": 10
                },
                "expected": 4
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(
                inputs["distances"],
                inputs["fuel"],
                inputs["mpg"]
            )
            results.append(
                f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class TaskAssignment(Algorithm):
    """
    Optimally assigns tasks to workers such that the maximum task pair duration is minimized.
    Each worker gets exactly two tasks. The optimal strategy is to pair the shortest and longest tasks,
    then move inward. This ensures no single worker is overloaded with two long tasks.
    Returns list of task index pairs that each worker should complete.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        k = args[1]
        assign = [[i, v] for i, v in enumerate(args[0])]
        assign.sort(key=lambda x: x[-1])
        task_list = []
        j = 1
        for i in range(k):
            task_list.append([assign[i][0], assign[-j][0]])
            j += 1
        return task_list
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        k = args[1]
        assign = [[i, v] for i, v in enumerate(args[0])]
        assign.sort(key=lambda x: x[-1])
        task_list = []
        j = 1
        for i in range(k):
            task_list.append([assign[i][0], assign[-j][0]])
            j += 1
        return task_list

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "tasks": [1, 3, 5, 3, 1, 4],
                    "k": 3
                },
                "expected": [[0, 2], [4, 5], [1, 3]]
            },
            {
                "inputs": {
                    "tasks": [1, 2, 2, 1],
                    "k": 2
                },
                "expected": [[0, 3], [1, 2]]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["tasks"], inputs["k"])
            results.append(
                f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class BooleanExpressions(Algorithm):
    """
    Evaluates complex boolean expressions with nested logical operators (!, &, |).
    Handles expressions in prefix notation with arbitrary nesting depth.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        string = args[0]
        operators = []
        values = []

        i = 0
        while i < len(string):
            letter = string[i]
            if letter == "t":
                values.append(True)
                i += 1
            elif letter == "f":
                values.append(False)
                i += 1
            elif letter in ("!", "|", "&"):
                operators.append(letter)
                i += 2  # skip operator and opening "("
            elif letter == ")":
                op = operators.pop()
                if op == "!":
                    val = values.pop()
                    values.append(not val)
                elif op == "&":
                    result = True
                    while values and isinstance(values[-1], bool):
                        result &= values.pop()
                    values.append(result)
                elif op == "|":
                    result = False
                    while values and isinstance(values[-1], bool):
                        result |= values.pop()
                    values.append(result)
                i += 1
            else:
                i += 1
        return values[0]
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        string = args[0]
        operators = []
        values = []

        i = 0
        while i < len(string):
            letter = string[i]
            if letter == "t":
                values.append(True)
                i += 1
            elif letter == "f":
                values.append(False)
                i += 1
            elif letter in ("!", "|", "&"):
                operators.append(letter)
                i += 2  # skip operator and opening "("
            elif letter == ")":
                op = operators.pop()
                if op == "!":
                    val = values.pop()
                    values.append(not val)
                elif op == "&":
                    result = True
                    while values and isinstance(values[-1], bool):
                        result &= values.pop()
                    values.append(result)
                elif op == "|":
                    result = False
                    while values and isinstance(values[-1], bool):
                        result |= values.pop()
                    values.append(result)
                i += 1
            else:
                i += 1
        return values[0]

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"expression": "t"},
                "expected": True
            },
            {
                "inputs": {"expression": "!(t)"},
                "expected": False
            },
            {
                "inputs": {"expression": "|(f,t)"},
                "expected": True
            },
            {
                "inputs": {"expression": "&(t,f)"},
                "expected": False
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["expression"])
            results.append(
                f"Test {i}: Input={inputs['expression']}, Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class SlidingPuzzle(Algorithm):
    """
    Solves the 2x3 sliding puzzle by finding the minimum number of moves to reach the solved state.
    The solved state is [[1,2,3],[4,5,0]] where 0 represents the empty space.
    Uses BFS to explore all possible moves from the current state, tracking visited states to avoid cycles.
    Returns the minimum move count or -1 if unsolvable.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        board = args[0]
        curr_map = {
            "0": [1, 3],
            "1": [0, 2, 4],
            "2": [1, 5],
            "3": [0, 4],
            "4": [1, 3, 5],
            "5": [2, 4],
        }

        curr_repr = "".join([str(i) for row in board for i in row])
        waiting = deque([(curr_repr.index("0"), curr_repr, 0)])
        checked_states = {curr_repr}
        while waiting:
            i, current, l = waiting.popleft()
            if current == "123450":
                return l
            curr_arr = list(current)
            for k in curr_map[str(i)]:
                new_arr = curr_arr.copy()
                new_arr[i], new_arr[k] = curr_arr[k], curr_arr[i]
                new_repr = "".join(new_arr)
                if new_repr not in checked_states:
                    waiting.append((k, new_repr, l + 1))
                    checked_states.add(new_repr)
        return -1
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        board = args[0]
        curr_map = {
            "0": [1, 3],
            "1": [0, 2, 4],
            "2": [1, 5],
            "3": [0, 4],
            "4": [1, 3, 5],
            "5": [2, 4],
        }

        curr_repr = "".join([str(i) for row in board for i in row])
        waiting = deque([(curr_repr.index("0"), curr_repr, 0)])
        checked_states = {curr_repr}
        while waiting:
            i, current, l = waiting.popleft()
            if current == "123450":
                return l
            curr_arr = list(current)
            for k in curr_map[str(i)]:
                new_arr = curr_arr.copy()
                new_arr[i], new_arr[k] = curr_arr[k], curr_arr[i]
                new_repr = "".join(new_arr)
                if new_repr not in checked_states:
                    waiting.append((k, new_repr, l + 1))
                    checked_states.add(new_repr)
        return -1

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"board": [[4, 1, 2], [5, 0, 3]]},
                "expected": 5
            },
            {
                "inputs": {"board": [[1, 2, 3], [4, 5, 0]]},
                "expected": 0
            },
            {
                "inputs": {"board": [[1, 2, 3], [5, 4, 0]]},
                "expected": -1
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["board"])
            results.append(
                f"Test {i}: Input={inputs['board']}, Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class FreqStacks:
    """
    Implements a frequency stack where pop() returns the most frequent element,
    and in case of ties, returns the element closest to the top.
    Uses two class-level structures:
    - obj: maintains the order of pushed elements
    - dct: tracks frequency counts of elements
    """
    obj = []
    nums = [4,5,7]
    dct = dict()
    result = []
    class_name = "FreqStacks"
    @classmethod
    def execute(cls, *args, **kwargs):
        if args[0] != cls.class_name:
            return "Invalid class name as first element of array, make sure it is 'FreqStacks' "
        arr = args[0][1:]
        pops = arr.count("pop")
        pushes = arr.count("push")
        cls.result.append("null")
        for _ in range(pushes):
            res = cls.push()
            cls.result.append(res)
        for _ in range(pops):
            res = cls.pop()
            cls.result.append(res)
        return cls.result

    @classmethod
    def pop(cls):
        max_count = max(cls.dct.values())
        max_numbers = [num for num, count in cls.dct.items() if count == max_count]
        for num in cls.obj[::-1]:
            if num in max_numbers:
                cls.obj.remove(num)
                return num
        return

    @classmethod
    def push(cls):
        num = random.choice(cls.nums)
        cls.obj.append(num)
        if num not in cls.dct:
            cls.dct[num] = 0
        cls.dct[num] += 1
        return "null"

    def __repr__(self):
        print(self.result)

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def run_test(cls):
        return "No tests available for this algorithm"
    @classmethod
    def get_test_cases(cls):
        return "No test cases available for this algorithm"
    @classmethod
    def get_source_code(cls):
        return "Too complicated, please visit the code itself! Sorry"

class PutMarbles(Algorithm):
    """
    Calculates the difference between maximum and minimum possible scores when dividing marbles into k bags.
    The score is determined by the sum of first and last marble in each bag.
    Key insight: The difference depends only on the k-1 split points between bags.
    Optimal solution comes from sorting all possible split point values.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        k = args[1]
        if len(arr) == k or k == 1:
            return 0

        weight_sum = [arr[i]+arr[i+1] for i in range(len(arr)-1)]
        weight_sum.sort()

        return sum(weight_sum[-(k-1):]) - sum(weight_sum[:k-1])
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        k = args[1]
        if len(arr) == k or k == 1:
            return 0

        weight_sum = [arr[i]+arr[i+1] for i in range(len(arr)-1)]
        weight_sum.sort()

        return sum(weight_sum[-(k-1):]) - sum(weight_sum[:k-1])

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "weights": [1, 3, 5, 1],
                    "k": 2
                },
                "expected": 4
            },
            {
                "inputs": {
                    "weights": [1, 3],
                    "k": 2
                },
                "expected": 0
            },
            {
                "inputs": {
                    "weights": [1, 4, 2, 5, 2],
                    "k": 3
                },
                "expected": 3
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["weights"], inputs["k"])
            results.append(
                f"Test {i}: Weights={inputs['weights']}, k={inputs['k']}, "
                f"Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class SplitArray(Algorithm):
    """
    Splits an array into k non-empty contiguous subarrays to minimize the largest sum among them.
    Uses binary search to efficiently find the minimum possible maximum subarray sum.
    The algorithm checks feasibility of a candidate sum by counting how many subarrays it would require.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        k = args[1]

        def min_sub_needed(max_bearable_sum):
            curr_sum = 0
            splits_needed = 1
            sum_sub_max = 0
            for num in arr:
                next_sum = curr_sum + num
                if next_sum <= max_bearable_sum:
                    curr_sum = next_sum
                else:
                    sum_sub_max = max(sum_sub_max, curr_sum)
                    curr_sum = num
                    splits_needed += 1
                    if splits_needed > k:
                        return False, None
            sum_sub_max = max(sum_sub_max, curr_sum)
            return True, sum_sub_max
        left = max(arr)
        right = sum(arr)
        min_big_split_sum = right
        iteration = 0
        while left <= right:
            iteration += 1
            if iteration == 1:
                max_bearable_sum = (right + left) // k
            else:
                max_bearable_sum = (right + left) // 2

            flag, sum_sub_max = min_sub_needed(max_bearable_sum)
            if flag:
                min_big_split_sum = min(min_big_split_sum, sum_sub_max)
                right = sum_sub_max - 1
            else:
                left = max_bearable_sum + 1

        return min_big_split_sum
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        k = args[1]

        def min_sub_needed(max_bearable_sum):
            curr_sum = 0
            splits_needed = 1
            sum_sub_max = 0
            for num in arr:
                next_sum = curr_sum + num
                if next_sum <= max_bearable_sum:
                    curr_sum = next_sum
                else:
                    sum_sub_max = max(sum_sub_max, curr_sum)
                    curr_sum = num
                    splits_needed += 1
                    if splits_needed > k:
                        return False, None
            sum_sub_max = max(sum_sub_max, curr_sum)
            return True, sum_sub_max
        left = max(arr)
        right = sum(arr)
        min_big_split_sum = right
        iteration = 0
        while left <= right:
            iteration += 1
            if iteration == 1:
                max_bearable_sum = (right + left) // k
            else:
                max_bearable_sum = (right + left) // 2

            flag, sum_sub_max = min_sub_needed(max_bearable_sum)
            if flag:
                min_big_split_sum = min(min_big_split_sum, sum_sub_max)
                right = sum_sub_max - 1
            else:
                left = max_bearable_sum + 1

        return min_big_split_sum

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "nums": [7, 2, 5, 10, 8],
                    "k": 2
                },
                "expected": 18
            },
            {
                "inputs": {
                    "nums": [1, 2, 3, 4, 5],
                    "k": 2
                },
                "expected": 9
            },
            {
                "inputs": {
                    "nums": [1, 4, 4],
                    "k": 3
                },
                "expected": 4
            },
            {
                "inputs": {
                    "nums": [10, 2, 3, 9],
                    "k": 2
                },
                "expected": 14
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["nums"], inputs["k"])
            results.append(
                f"Test {i}: nums={inputs['nums']}, k={inputs['k']}, "
                f"Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()
class Parenthesis(Algorithm):
    """
    Generates all combinations of well-formed parentheses for a given n.
    Uses backtracking to build valid combinations by:
    - Only adding '(' if we haven't used all opening parentheses
    - Only adding ')' if we have more opening than closing parentheses
    This ensures we only generate valid balanced parentheses combinations.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        n = args[0]
        result = []

        def tracking(current, open_count, close_count):
            if open_count == n and close_count == n:
                result.append(current)
                return

            if open_count < n:
                tracking(current + '(', open_count + 1, close_count)
            if close_count < open_count:
                tracking(current + ')', open_count, close_count + 1)

        tracking("", 0, 0)
        return result
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        n = args[0]
        result = []

        def tracking(current, open_count, close_count):
            if open_count == n and close_count == n:
                result.append(current)
                return

            if open_count < n:
                tracking(current + '(', open_count + 1, close_count)
            if close_count < open_count:
                tracking(current + ')', open_count, close_count + 1)

        tracking("", 0, 0)
        return result

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"n": 3},
                "expected": ["((()))","(()())","(())()","()(())","()()()"]
            },
            {
                "inputs": {"n": 1},
                "expected": ["()"]
            },
            {
                "inputs": {"n": 2},
                "expected": ["(())","()()"]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["n"])
            # Sort both results and expected for comparison since order doesn't matter
            sorted_result = sorted(result)
            sorted_expected = sorted(test["expected"])
            results.append(
                f"Test {i}: n={inputs['n']}\n"
                f"Result: {sorted_result}\n"
                f"Expected: {sorted_expected}\n"
                f"Match: {sorted_result == sorted_expected}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class RobotPaths(Algorithm):
    """
    Calculates the number of unique paths a robot can take from top-left to bottom-right
    in an m x n grid, moving only right or down.
    Uses dynamic programming with space optimization to efficiently compute the result.
    The solution builds upon the observation that each cell's path count is the sum of
    paths from the cell above and the cell to the left.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        m = args[0]
        n = args[1]
        top_row = [1] * n

        for _ in range(m - 1):
            current_row = [1] * n
            for i in range(1, n):
                current_row[i] = current_row[i - 1] + top_row[i]
            top_row = current_row

        return top_row[-1]
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        m = args[0]
        n = args[1]
        top_row = [1] * n

        for _ in range(m - 1):
            current_row = [1] * n
            for i in range(1, n):
                current_row[i] = current_row[i - 1] + top_row[i]
            top_row = current_row

        return top_row[-1]

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"m": 3, "n": 2},
                "expected": 3
            },
            {
                "inputs": {"m": 3, "n": 7},
                "expected": 28
            },
            {
                "inputs": {"m": 1, "n": 1},
                "expected": 1
            },
            {
                "inputs": {"m": 7, "n": 3},
                "expected": 28
            },
            {
                "inputs": {"m": 3, "n": 3},
                "expected": 6
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["m"], inputs["n"])
            results.append(
                f"Test {i}: m={inputs['m']}, n={inputs['n']}, "
                f"Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class TrainTicket(Algorithm):
    """
    Calculates the minimum cost for train travel using 1-day, 7-day, and 30-day passes.
    Uses dynamic programming to track the optimal cost at each travel day, considering:
    - The cost of buying a 1-day pass for the current day
    - The cost of buying a 7-day pass covering up to 7 days back
    - The cost of buying a 30-day pass covering up to 30 days back
    Returns the minimum total cost for all travel days.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        days = args[0]
        costs = args[1]
        n = len(days)
        ticket_7 = 0
        ticket_30 = 0
        observe_arr = [0] * n

        for i in range(n):
            while days[i] - days[ticket_7] >= 7:
                ticket_7 += 1
            while days[i] - days[ticket_30] >= 30:
                ticket_30 += 1

            cost_1 = (observe_arr[i - 1] if i > 0 else 0) + costs[0]
            cost_7 = (observe_arr[ticket_7 - 1] if ticket_7 > 0 else 0) + costs[1]
            cost_30 = (observe_arr[ticket_30 - 1] if ticket_30 > 0 else 0) + costs[2]
            observe_arr[i] = min(cost_1, cost_7, cost_30)
        return observe_arr[n - 1]
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        days = args[0]
        costs = args[1]
        n = len(days)
        ticket_7 = 0
        ticket_30 = 0
        observe_arr = [0] * n

        for i in range(n):
            while days[i] - days[ticket_7] >= 7:
                ticket_7 += 1
            while days[i] - days[ticket_30] >= 30:
                ticket_30 += 1

            cost_1 = (observe_arr[i - 1] if i > 0 else 0) + costs[0]
            cost_7 = (observe_arr[ticket_7 - 1] if ticket_7 > 0 else 0) + costs[1]
            cost_30 = (observe_arr[ticket_30 - 1] if ticket_30 > 0 else 0) + costs[2]
            observe_arr[i] = min(cost_1, cost_7, cost_30)
        return observe_arr[n - 1]

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "days": [1, 4, 6, 7, 8, 20],
                    "costs": [2, 7, 15]
                },
                "expected": 11
            },
            {
                "inputs": {
                    "days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
                    "costs": [2, 7, 15]
                },
                "expected": 17
            },
            {
                "inputs": {
                    "days": [1, 2, 3, 4, 6, 8, 9, 10, 13, 14, 16, 17, 19, 21, 24, 26, 27, 28],
                    "costs": [3, 14, 50]
                },
                "expected": 30
            },
            {
                "inputs": {
                    "days": [1, 30, 60, 90, 120],
                    "costs": [2, 7, 15]
                },
                "expected": 10
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["days"], inputs["costs"])
            results.append(
                f"Test {i}: Days={inputs['days']}, Costs={inputs['costs']}, "
                f"Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class SwitchPairNodes(Algorithm):
    """
    Swaps every two adjacent nodes in a linked list by modifying node pointers.
    Uses a dummy node approach to handle edge cases and pointer manipulation.
    The algorithm works by:
    1. Creating a dummy node pointing to the head
    2. Iterating through pairs of nodes
    3. Swapping each pair by adjusting their next pointers
    4. Maintaining the connection to the previous pair
    Returns the modified list as an array for easier verification.
    """
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        lst = args[0]
        if len(lst) == 0:
            return lst
        head = cls.create_linked_list(lst)
        temp = cls.ListNode(0, head)
        previous, current = temp, head

        while current and current.next:
            next_prev = current.next.next
            second = current.next
            second.next = current
            current.next = next_prev
            previous.next = second
            previous = current
            current = next_prev

        result_head = temp.next
        result_list = []
        current = result_head
        while current:
            result_list.append(current.val)
            current = current.next

        return result_list
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        lst = args[0]
        if len(lst) == 0:
            return lst
        head = cls.create_linked_list(lst)
        temp = cls.ListNode(0, head)
        previous, current = temp, head

        while current and current.next:
            next_prev = current.next.next
            second = current.next
            second.next = current
            current.next = next_prev
            previous.next = second
            previous = current
            current = next_prev

        result_head = temp.next
        result_list = []
        current = result_head
        while current:
            result_list.append(current.val)
            current = current.next

        return result_list

    @classmethod
    def create_linked_list(cls, lst):
        if not lst:
            return None

        head = cls.ListNode(lst[0])
        current = head

        for val in lst[1:]:
            current.next = cls.ListNode(val)
            current = current.next

        return head

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"list": [1, 2, 3, 4]},
                "expected": [2, 1, 4, 3]
            },
            {
                "inputs": {"list": [1]},
                "expected": [1]
            },
            {
                "inputs": {"list": [1, 2, 3, 4, 5]},
                "expected": [2, 1, 4, 3, 5]
            },
            {
                "inputs": {"list": []},
                "expected": []
            },
            {
                "inputs": {"list": [1, 2, 3]},
                "expected": [2, 1, 3]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["list"])
            results.append(
                f"Test {i}: Input={inputs['list']}, Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class AddNodeNumbers(Algorithm):
    """
    We create two linked lists with arguments (lists) provided. We introduce dummy node to create new
    linked list crawling with current variable. we sum up each node from linked list 1 and linked list2
    respectively as l1 and l2. we simply sum and adding carry to each node pair sum and adding digit
    into new (result) linked list as it already represents the number in the result sum. we continue the loop
    unless there are nodes into the linked lists (l1 or l2) or the remaining carry
    """
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        l1 = args[0]
        l2 = args[1]

        head1 = cls.create_linked_list(l1)
        head2 = cls.create_linked_list(l2)

        dummy = cls.ListNode(0)
        current = dummy
        carry = 0

        while head1 or head2 or carry:
            val1 = head1.val if head1 else 0
            val2 = head2.val if head2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = cls.ListNode(digit)
            current = current.next

            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None

        result_head = dummy.next
        return cls.linked_list_to_list(result_head)
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        l1 = args[0]
        l2 = args[1]

        head1 = cls.create_linked_list(l1)
        head2 = cls.create_linked_list(l2)

        dummy = cls.ListNode(0)
        current = dummy
        carry = 0

        while head1 or head2 or carry:
            val1 = head1.val if head1 else 0
            val2 = head2.val if head2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = cls.ListNode(digit)
            current = current.next

            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None

        result_head = dummy.next
        return cls.linked_list_to_list(result_head)

    @classmethod
    def create_linked_list(cls, lst):
        if not lst:
            return None

        head = cls.ListNode(lst[0])
        current = head

        for val in lst[1:]:
            current.next = cls.ListNode(val)
            current = current.next

        return head

    @classmethod
    def linked_list_to_list(cls, head):
        result_list = []
        current = head
        while current:
            result_list.append(current.val)
            current = current.next
        return result_list

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "l1": [2, 4, 3],
                    "l2": [5, 6, 4]
                },
                "expected": [7, 0, 8]
            },
            {
                "inputs": {
                    "l1": [0],
                    "l2": [0]
                },
                "expected": [0]
            },
            {
                "inputs": {
                    "l1": [9, 9, 9, 9, 9, 9, 9],
                    "l2": [9, 9, 9, 9]
                },
                "expected": [8, 9, 9, 9, 0, 0, 0, 1]
            },
            {
                "inputs": {
                    "l1": [5],
                    "l2": [5]
                },
                "expected": [0, 1]
            },
            {
                "inputs": {
                    "l1": [1, 8],
                    "l2": [0]
                },
                "expected": [1, 8]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["l1"], inputs["l2"])
            results.append(
                f"Test {i}: l1={inputs['l1']}, l2={inputs['l2']}, "
                f"Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class MakeStringsAnagrams(Algorithm):
    """
    We create two empy lists for strings s and t which contains 26 elements matching the lowercase
    alphabet length. then we do two iterations one for s and one for t. in each iteration we update
    corresponding empty list with numbers of how many times each character is represented into the string
    we use built-in ord function to return character's index on ascii table and by subtracting index of
    "a" character which is the first character we simply update any element of the corresponding arrays
    with length of 26
    Finally we introduce new iteration where we sum up absolute values of differences in counts for each
    character in s and t strings and summing it up into variable split_num. This gives us numbers how many
    changes is needed to make s anagram of t and t anagram of s. As it counted anagram making in vice versa
    way we divide it by two, and it represents the real number of how many steps is needed to make s and t
    anagrams
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]
        t = args[1]
        if len(s) != len(t):
            return -1
        t, s = t.lower(), s.lower()
        s_char_count = [0] * 26
        t_char_count = [0] * 26

        for char in t:
            t_char_count[ord(char) - ord("a")] += 1

        for char in s:
            s_char_count[ord(char) - ord("a")] += 1

        split_num = 0
        for i in range(26):
            split_num += abs(s_char_count[i] - t_char_count[i])

        result = split_num / 2
        return result
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]
        t = args[1]
        if len(s) != len(t):
            return -1
        t, s = t.lower(), s.lower()
        s_char_count = [0] * 26
        t_char_count = [0] * 26

        for char in t:
            t_char_count[ord(char) - ord("a")] += 1

        for char in s:
            s_char_count[ord(char) - ord("a")] += 1

        split_num = 0
        for i in range(26):
            split_num += abs(s_char_count[i] - t_char_count[i])

        result = split_num / 2
        return result

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "s": "bab",
                    "t": "aba"
                },
                "expected": 1
            },
            {
                "inputs": {
                    "s": "leetcode",
                    "t": "practice"
                },
                "expected": 5
            },
            {
                "inputs": {
                    "s": "anagram",
                    "t": "mangaar"
                },
                "expected": 0
            },
            {
                "inputs": {
                    "s": "xxyyzz",
                    "t": "xxyyzz"
                },
                "expected": 0
            },
            {
                "inputs": {
                    "s": "friend",
                    "t": "family"
                },
                "expected": 4
            },
            {
                "inputs": {
                    "s": "abc",
                    "t": "def"
                },
                "expected": 3
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["s"], inputs["t"])
            results.append(
                f"Test {i}: s='{inputs['s']}', t='{inputs['t']}', "
                f"Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class PartitionString(Algorithm):
    """
    We create hashmap  in last_pos_char variable where we store characters as keys, and it's the largest
    index into the s string (argument).
    Next step is defining start and end variables to track at which index to split the string and
    keep length of the slice into the result array and move on to another split
    Solution has the greedy pattern, "end = max(end, last_pos_char[char])" this pattern is choosing maximum
    between current maximum (previous largest index of the character) and the largest index of current character
    in the iteration. if idx and end will match it means there are repeated characters up to "end" index
    and none of them is repeated in rest of the string so we calculate the length with "end - start + 1"
    +1 because we use 0 indexing. Then we redefine start as end+1 as it's new starting point of string
    where previous characters are not repeated. We continue iterations until we check all the letters to
    find valid slices. Finally, we return result array representing lengths of string slices
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]
        last_pos_char = {}
        for idx, char in enumerate(s):
            last_pos_char[char] = idx

        start = 0
        end = 0
        result = []
        for idx, char in enumerate(s):
            end = max(end, last_pos_char[char])
            if idx == end:
                result.append(end - start + 1)
                start = end + 1

        return result
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]
        last_pos_char = {}
        for idx, char in enumerate(s):
            last_pos_char[char] = idx

        start = 0
        end = 0
        result = []
        for idx, char in enumerate(s):
            end = max(end, last_pos_char[char])
            if idx == end:
                result.append(end - start + 1)
                start = end + 1

        return result

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "s": "ababcbacadefegdehijhklij"
                },
                "expected": [9, 7, 8]
            },
            {
                "inputs": {
                    "s": "ababcc"
                },
                "expected": [4, 2]
            },
            {
                "inputs": {
                    "s": "eccbbbbdec"
                },
                "expected": [10]
            },
            {
                "inputs": {
                    "s": "a"
                },
                "expected": [1]
            },
            {
                "inputs": {
                    "s": "abcde"
                },
                "expected": [1, 1, 1, 1, 1]
            },
            {
                "inputs": {
                    "s": "aabbccdd"
                },
                "expected": [2, 2, 2, 2]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["s"])
            results.append(
                f"Test {i}: s='{inputs['s']}', Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class NumberOfSubs(Algorithm):
    """
    We create lis "count" of three default 0 elements as we need to track only "a", "b", "c" into
    valid strings. We create "left" variables to slide over the string everytime we check all possible
    valid options for any occurrence of a, b and c in a substring. While loop checks if we have valid sbustring
    and if we do have it we subtract current index from length of the original string, and it represents the
    value of all possible valid substring for the current selection, to be clear it means the current selection
    and all the characters after the current selection. Then we empty the first character from count to move
    tracker to one position from left to right and wait the subtracted character to appear again and validate
    the substring and do the same with the res variable
    after we iterate on full string res value will return all possible valid substrings
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]
        count = [0] * 3
        left = 0
        res = 0
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1

            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                res += len(s) - i
                count[ord(s[left]) - ord("a")] -= 1
                left += 1
        return res
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]
        count = [0] * 3
        left = 0
        res = 0
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1

            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                res += len(s) - i
                count[ord(s[left]) - ord("a")] -= 1
                left += 1
        return res

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "s": "abcabc"
                },
                "expected": 10
            },
            {
                "inputs": {
                    "s": "aaacb"
                },
                "expected": 3
            },
            {
                "inputs": {
                    "s": "abc"
                },
                "expected": 1
            },
            {
                "inputs": {
                    "s": "aabbcc"
                },
                "expected": 8
            },
            {
                "inputs": {
                    "s": "aaabbbccc"
                },
                "expected": 0
            },
            {
                "inputs": {
                    "s": "ababababab"
                },
                "expected": 0
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["s"])
            results.append(
                f"Test {i}: s='{inputs['s']}', Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class QueryNums(Algorithm):
    """
    First we create dictionary and during iteration on nums array if we find x value into nums array
    we keep it as a key and value is represented as a list of indices where x is occurred in the array.
    Then we iterate over queries array and checking ith index of x occurrence into nums array, but now we
    check it into dictionary where value is a list of indices. We search with "i-1" because the list of
    indices into dictionary is a 0 index list. If exception occurs we will append result list "-1" and skip
    the other part of the iteration "continue". if corresponding index is found we append index to "res" array
    and finally after iteration we return the res array
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        nums = args[0]
        queries = args[1]
        x = args[2]
        dct = {}
        for i, v in enumerate(nums):
            if v == x:
                if v not in dct:
                    dct[v] = [i]
                else:
                    dct[v].append(i)
        res = []
        for i in queries:
            try:
                idx = dct[x][i - 1]
            except:
                res.append(-1)
                continue
            res.append(idx)
        return res
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        nums = args[0]
        queries = args[1]
        x = args[2]
        dct = {}
        for i, v in enumerate(nums):
            if v == x:
                if v not in dct:
                    dct[v] = [i]
                else:
                    dct[v].append(i)
        res = []
        for i in queries:
            try:
                idx = dct[x][i - 1]
            except:
                res.append(-1)
                continue
            res.append(idx)
        return res

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "nums": [1, 3, 1, 7],
                    "queries": [1, 3, 2, 4],
                    "x": 1
                },
                "expected": [0, -1, 2, -1]
            },
            {
                "inputs": {
                    "nums": [5, 5, 5, 5, 5],
                    "queries": [1, 3, 5, 7],
                    "x": 5
                },
                "expected": [0, 2, 4, -1]
            },
            {
                "inputs": {
                    "nums": [2, 4, 6, 8],
                    "queries": [1, 2],
                    "x": 1
                },
                "expected": [-1, -1]
            },
            {
                "inputs": {
                    "nums": [1, 2, 1, 2, 1, 2, 1],
                    "queries": [1, 2, 3, 4],
                    "x": 1
                },
                "expected": [0, 2, 4, 6]
            },
            {
                "inputs": {
                    "nums": [1, 1, 1, 1],
                    "queries": [5],
                    "x": 1
                },
                "expected": [-1]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["nums"], inputs["queries"], inputs["x"])
            results.append(
                f"Test {i}: nums={inputs['nums']}, queries={inputs['queries']}, x={inputs['x']}, "
                f"Result={result}, Expected={test['expected']}"
            )
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class AirplaneSeats(Algorithm):
    """
    If first person will picks up someone's seat lets assume the person mth seat everyone from first
    person up to mth person will get their own seat. Then mth person will sit another person's seat
    and between them people will get their own seat. So we have new sub-problems whenever we reach
    person who will be forced to take a random seat
    So with probability formula it comes that P(n) = 1/n * (P(n-1) + P(n-2) + .... + P(1)) which translates to
    n * P(n) = P(n-1) + P(n-1) + .... + P(n) and also (n-1) * P(n-1) = P(n-1) + P(n-2) + .... + P(1)
    if we subtract both sides we will get P(n) = P(n-1) = 1/2 only when n > 2 otherwise we will fail in
    equation P(2) = 1/2, P(1) = 1, P(2) != P(1)
    Finally we get that after n > 1 probability will always return 1/2

    """

    SOURCE_CODE = """
    def execute(cls, *args, **kwargs):
        n = args[0]
        return 0.5 if n > 1 else 1
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        n = args[0]
        return 0.5 if n > 1 else 1

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": [1],
                "expected": 1
            },
            {
                "inputs": [2],
                "expected": 0.5
            },
            {
                "inputs": [3],
                "expected": 0.5
            },
            {
                "inputs": [10],
                "expected": 0.5
            },
            {
                "inputs": [100],
                "expected": 0.5
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(*inputs)
            results.append(
                f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}, {'PASS' if result == test['expected'] else 'FAIL'}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class PartitionPalindromes(Algorithm):
    """
    We start from 0 index in string if there is a valid palindrome we add it to "length" and recursively
    call the same function again with a new starting index "tracker(end+1, length) (start = end + 1)"
    e.g 'aabc'. start = 0 substring = 'a' valid_palindrome = True, appending 'a' to length and recursively
    moving to end + 1 index, and we pass it as start parameter into tracker so in this case it will be 1
    and so on...
    We are removing last added substring to try other partitions and when start will reach the length
    of the string itself it will append all collection of lengths into the result variable, and we finally
    return it
    """

    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]
        def valid_palindrome(sub_s):
            return sub_s == sub_s[::-1]

        def tracker(start, length):
            if start == len(s):
                result.append(length[:])
                return
            for end in range(start, len(s)):
                substring = s[start:end+1]
                if valid_palindrome(substring):
                    length.append(substring)
                    tracker(end+1, length)
                    length.pop()

        result = []
        tracker(0, [])

        return result
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]

        def valid_palindrome(sub_s):
            return sub_s == sub_s[::-1]

        def tracker(start, length):
            if start == len(s):
                result.append(length[:])
                return
            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if valid_palindrome(substring):
                    length.append(substring)
                    tracker(end + 1, length)
                    length.pop()

        result = []
        tracker(0, [])

        return result

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": ["aab"],
                "expected": [["a", "a", "b"], ["aa", "b"]]
            },
            {
                "inputs": ["a"],
                "expected": [["a"]]
            },
            {
                "inputs": [""],
                "expected": [[]]
            },
            {
                "inputs": ["racecar"],
                "expected": [
                    ["r", "a", "c", "e", "c", "a", "r"],
                    ["r", "aceca", "r"],
                    ["racecar"]
                ]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(*inputs)
            # Sort both the result and expected to handle order-independent comparison
            sorted_result = sorted(map(sorted, result))
            sorted_expected = sorted(map(sorted, test["expected"]))
            results.append(
                f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}, {'PASS' if sorted_result == sorted_expected else 'FAIL'}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class RotateIntegers(Algorithm):
    """
    In this algorithm we ignore 0,1 and 8 as they rotate to themselves, logic is based on checking
    if 3,4 or 7 is part of the digit because it will definitely be the invalid number after rotation,
    and we skip this number. We only want to observe if 2|5|6|9 is part of the integer in this case
    if they are given in combination with 0|1|8 final output will be valid because this numbers will
    rotate to themselves and 2|5|6|9 will guarantee us to give different number than current number
    under observation, if we find this kind of number we add 1 to the count and return it at the end
    """

    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        n = args[0]
        count = 0
        for i in range(1, n + 1):
            dgt = str(i)
            if "3" in dgt or "4" in dgt or "7" in dgt:
                continue
            if "2" in dgt or "5" in dgt or "6" in dgt or "9" in dgt:
                count += 1

        return count
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        n = args[0]
        count = 0
        for i in range(1, n + 1):
            dgt = str(i)
            if "3" in dgt or "4" in dgt or "7" in dgt:
                continue
            if "2" in dgt or "5" in dgt or "6" in dgt or "9" in dgt:
                count += 1

        return count

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": [10],
                "expected": 4
            },
            {
                "inputs": [1],
                "expected": 0
            },
            {
                "inputs": [20],
                "expected": 6
            },
            {
                "inputs": [100],
                "expected": 20
            },
            {
                "inputs": [0],
                "expected": 0
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(*inputs)
            results.append(
                f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}, {'PASS' if result == test['expected'] else 'FAIL'}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class MinExtraChars(Algorithm):

    """
    We assume that in given string all the characters are extra and use the dynamic programming
    for finding real minimum extra characters. "dp[0] = 0" it means that if given string is empty
    extra characters are 0.
    Then we iterate for every "i" starting from 1 to the length of the string and update dp[i] with
    previous element +1 as every element represents extra characters up to "ith" index unless we find the match .
    For every iteration we conduct second iteration for every "j" in length of "i" so we are able to check
    every slice in given string separately up to "ith" index. If any slice s[j:i] will match the word in given
    dictionary (word_set) we set extra character number in dp[i] as minimum between currently given dp[i]
    and dp[j] on final iteration dp[n] will have the minimum value for extra character number.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]
        word_set = set(args[1])
        n = len(s)
        dp = [float("inf")] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1

            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        s = args[0]
        word_set = set(args[1])
        n = len(s)
        dp = [float("inf")] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1

            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": ["leetscode", ["leet","code","leetcode"]],
                "expected": 1
            },
            {
                "inputs": ["sayhelloworld", ["hello","world"]],
                "expected": 3
            },
            {
                "inputs": ["dwmodizxvvbosxxw", ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]],
                "expected": 10
            },
            {
                "inputs": ["abcdefg", []],
                "expected": 7
            },
            {
                "inputs": ["abcdefg", ["abcdefg"]],
                "expected": 0
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(*inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}, {'PASS' if result == test['expected'] else 'FAIL'}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class BreakInteger(Algorithm):
    """
    Algorithm is based on mathematical theorem that if we want to maximize multiplication of integers
    which sums up to integer n we have to use integers closest to 3
    In this case we manually return answers up to n == 3. When n > 4 we introduce loop and multiplying
    p dummy variable on 3 everytime we subtract 3 from n. Finally, we multiply p to leftover from n after
    the loop and return the p
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        n = args[0]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 3
        p = 1
        while n > 4:
            p *= 3
            n -= 3
        p *= n
        return p
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        n = args[0]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 3
        p = 1
        while n > 4:
            p *= 3
            n -= 3
        p *= n
        return p

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": [2],
                "expected": 1
            },
            {
                "inputs": [3],
                "expected": 3
            },
            {
                "inputs": [4],
                "expected": 4
            },
            {
                "inputs": [10],
                "expected": 36
            },
            {
                "inputs": [5],
                "expected": 6
            },
            {
                "inputs": [7],
                "expected": 12
            },
            {
                "inputs": [1],
                "expected": 1
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(*inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}, {'PASS' if result == test['expected'] else 'FAIL'}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class PerfectSquare(Algorithm):
    """
    To solve the problem we narrow down the list from which we choose the perfect squares for summing up
    to given n value by flooring square root of n and intuitively only squares of integers less than that
    number can sum up to the given n value. We use helper function for recursively update target value
    by subtracting each element on every iteration, and we add 1 to the count of elements for summing up to
    the target value. Finally, we return the minimum number of elements needed to sum up to the target value.
    """
    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        from math import floor
        import math
        n = args[0]
        sqr = floor(math.sqrt(n))
        nums = [i ** 2 for i in range(1, sqr + 1)]

        def helper(target, arr):
            if target == 0:
                return 0
            if target < 0:
                return -1
            min_num = float("inf")
            for num in arr:
                result = helper(target - num, arr)
                if result != -1:
                    curr_num = result + 1
                    min_num = min(min_num, curr_num)
            return min_num if min_num != float("inf") else -1

        return helper(n, nums)
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        from math import floor
        import math
        n = args[0]
        sqr = floor(math.sqrt(n))
        nums = [i ** 2 for i in range(1, sqr + 1)]

        def helper(target, arr):
            if target == 0:
                return 0
            if target < 0:
                return -1
            min_num = float("inf")
            for num in arr:
                result = helper(target - num, arr)
                if result != -1:
                    curr_num = result + 1
                    min_num = min(min_num, curr_num)
            return min_num if min_num != float("inf") else -1

        return helper(n, nums)

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": [12],
                "expected": 3
            },
            {
                "inputs": [13],
                "expected": 2
            },
            {
                "inputs": [1],
                "expected": 1
            },
            {
                "inputs": [4],
                "expected": 1
            },
            {
                "inputs": [7],
                "expected": 4
            },
            {
                "inputs": [16],
                "expected": 1
            },
            {
                "inputs": [25],
                "expected": 1
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(*inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}, {'PASS' if result == test['expected'] else 'FAIL'}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class Intervals(Algorithm):
    """
    We use dynamic programming for solving this problem. First we create the list containing as much
    -1s as the length of given arr, assuming there is right interval for any given list into arr.
    We iterate over arr setting end value and starting second iteration to find right interval by comparing
    end value of current element to start value of all other elements. We dynamically track previous value
    of start to keep minimum start value as a valid index of right interval of the element. In nested
    loop we skip the step when we hit the ith element and finally if right interval is found we update
    dp's ith index with j index which corresponds the index of the valid right interval for ith element
    in arr
    """

    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        dp = [-1] * (len(arr))

        for i, v in enumerate(arr):
            end = v[1]
            prev_start = float("inf")
            for j in range(len(arr)):
                if j == i:
                    continue
                start = arr[j][0]
                if end <= start < prev_start:
                    prev_start = start
                    dp[i] = j
        return dp
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        arr = args[0]
        dp = [-1] * (len(arr))

        for i, v in enumerate(arr):
            end = v[1]
            prev_start = float("inf")
            for j in range(len(arr)):
                if j == i:
                    continue
                start = arr[j][0]
                if end <= start < prev_start:
                    prev_start = start
                    dp[i] = j
        return dp

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": [[[1,2]]],
                "expected": [-1]
            },
            {
                "inputs": [[[3,4], [2,3], [1,2]]],
                "expected": [-1, 0, 1]
            },
            {
                "inputs": [[[1,12], [2,9], [3,10], [13,14], [15,16], [16,17]]],
                "expected": [3, 3, 3, 4, 5, -1]
            },
            {
                "inputs": [[[4,5], [2,3], [1,2]]],
                "expected": [-1, 0, 1]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(*inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}, {'PASS' if result == test['expected'] else 'FAIL'}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class PushPop(Algorithm):
    """
    We solve the problem with dynamic programming. First we create the list containing as much False
    as the length of given arr. We iterate over array of popped element and keep adding elements from
    pushed array into stack until we add the element which was popped. Then we pop this element from stack
    and compare it with value of current iteration if they match we update the index corresponding to the
    value into pushed array of the dp with value of True
    If finally we will receive the dp full of True's it means push/pop combinations were valid
    """

    SOURCE_CODE = """
    @classmethod
    def execute(cls, *args, **kwargs):
        psh = args[0]
        pp = args[1]
        dp = [False] * (len(psh))
        stack = [psh[0]]
        count = 1
        for i, v in enumerate(pp):
            while v != stack[-1] and count < 5:
                stack.append(psh[count])
                count += 1
            element = stack.pop()
            idx = psh.index(element)
            if element == v:
                dp[idx] = True

        return all(dp) is True
    """

    @classmethod
    def execute(cls, *args, **kwargs):
        psh = args[0]
        pp = args[1]
        print(psh)
        print(pp)
        dp = [False] * (len(psh))
        stack = [psh[0]]
        count = 1
        for i, v in enumerate(pp):
            while stack and v != stack[-1] and count < 5:
                stack.append(psh[count])
                count += 1
            element = stack.pop()
            idx = psh.index(element)
            if element == v:
                dp[idx] = True

        return all(dp) is True

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": [[1,2,3,4,5], [4,5,3,2,1]],
                "expected": True
            },
            {
                "inputs": [[1,2,3,4,5], [4,3,5,1,2]],
                "expected": False
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(*inputs)
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}, {'PASS' if result == test['expected'] else 'FAIL'}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()

class Temperatures(Algorithm):
    """
    We use dynamic programming approach for solving this problem. First we create the list containing as much
    0s as the length of given arr. We iterate over temperatures and append their indices to the stack
    into the iteration we check if the value of temperature on the index which is last appended into stack
    is less than temperature on current iteration. If this condition is met we pop that from stack and
    updating dp's ith index with difference of i and popped index, as it represents how many days after
    will the condition of warmer temperature is met
    """
    SOURCE_CODE = """
        def execute(cls, *args, **kwargs):
            temps = args[0]
            dp = [0] * len(temps)
            stack = []
            for i, v in enumerate(temps):
                while stack and temps[stack[-1]] < v:
                    idx = stack.pop()
                    dp[idx] = i - idx
                stack.append(i)

            return dp
        """
    @classmethod
    def execute(cls, *args, **kwargs):
        temps = args[0]
        dp = [0] * len(temps)
        stack = []
        for i, v in enumerate(temps):
            while stack and temps[stack[-1]] < v:
                idx = stack.pop()
                dp[idx] = i - idx
            stack.append(i)

        return dp

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"temps": [73, 74, 75, 71, 69, 72, 76, 73]},
                "expected": [1, 1, 4, 2, 1, 1, 0, 0]  # Expected per task, but code differs
            },
            {
                "inputs": {"temps": [30, 40, 50, 60]},
                "expected": [1, 1, 1, 0]
            },
            {
                "inputs": {"temps": [30, 20, 10]},
                "expected": [0, 0, 0]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["temps"])
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class Circular(Algorithm):
    """
    First we create class MyCircularQueue which initiates empty stack and k value which is the size of the queue
    for enqueue method we check if there is a place into the queue if it does, we append value to queue and
    subtract 1 from k as there is 1 less place into the queue size of k
    On dequeue method we check if there is any element present into queue, if it does, we pop it from queue
    Front and Rear methods are respectively returning first and last element of the queue (Because of FIFO) from
    the queue if there is any element into queue
    Isempty and isfull methods are respectively returning boolean values weather there is no elements in queue
    or there is no more free space into queue
    Finally with execute function we iterate over the input to match methods with corresponding values, execute
    them and append results sequentially into the empty list. We return the list as the answer
    """
    SOURCE_CODE = """ 
        class MyCircularQueue:
        def __init__(self, k: int):
            self.q = []
            self.k = k

        def enQueue(self, value):
            if self.k > 0:
                self.q.append(value)
                self.k -= 1
                return True
            return False

        def deQueue(self):
            if self.q:
                self.q.pop(0)
                self.k += 1
                return True
            return False

        def Front(self):
            if self.q:
                return self.q[0]
            return -1

        def Rear(self):
            if self.q:
                return self.q[-1]
            return -1

        def isEmpty(self):
            if not self.q:
                return True
            return False

        def isFull(self):
            if self.k == 0:
                return True
            return False

    @classmethod
    def execute(cls, *args, **kwargs):
        arr1 = args[0]  # Commands
        arr2 = args[1]  # Values
        lst = ["null"]
        k = arr2[0][0]
        obj = cls.MyCircularQueue(k)
        for i, args in zip(arr1[1:], arr2[1:]):
            method = getattr(obj, i, None)
            if method:
                result = method(*args)
                if result is not None:
                    lst.append(result)
        return lst
    """

    class MyCircularQueue:
        def __init__(self, k: int):
            self.q = []
            self.k = k

        def enQueue(self, value):
            if self.k > 0:
                self.q.append(value)
                self.k -= 1
                return True
            return False

        def deQueue(self):
            if self.q:
                self.q.pop(0)
                self.k += 1
                return True
            return False

        def Front(self):
            if self.q:
                return self.q[0]
            return -1

        def Rear(self):
            if self.q:
                return self.q[-1]
            return -1

        def isEmpty(self):
            if not self.q:
                return True
            return False

        def isFull(self):
            if self.k == 0:
                return True
            return False

    @classmethod
    def execute(cls, *args, **kwargs):
        arr1 = args[0]  # Commands
        arr2 = args[1]  # Values
        lst = ["null"]
        k = arr2[0][0]
        obj = cls.MyCircularQueue(k)
        for i, args in zip(arr1[1:], arr2[1:]):
            method = getattr(obj, i, None)
            if method:
                result = method(*args)
                if result is not None:
                    lst.append(result)
        return lst

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {
                    "arr1": ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"],
                    "arr2": [[3], [1], [2], [3], [4], [], [], [], [4], []]
                },
                "expected": ["null", True, True, True, False, 3, True, True, True, 4]
            },
            {
                "inputs": {
                    "arr1": ["MyCircularQueue", "enQueue", "deQueue", "isEmpty"],
                    "arr2": [[1], [1], [], []]
                },
                "expected": ["null", True, True, True]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["arr1"], inputs["arr2"])
            results.append(f"Test {i}: Inputs={{'arr1': {inputs['arr1']}, 'arr2': {inputs['arr2']}}}, Result={result}, Expected={test['expected']}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()


class ExecuteOperators(Algorithm):
    """
    We use recursive approach for solving this problem. We iterate on string and keep the character on each
    iteration if we hit the opearot -, + or * then we take an action and divide string into two parts
    left site of the operator and right side of the operator, and we recursively execute same operations
    for left and right side of the substrings. Then we iterate over s1 and s2 (nested) and checking operator
    on each iteration and executing the operation between the integer values of i and j respectively
    from 1st and 2nd substring. We add result into empty list res and return it at the end
    """
    SOURCE_CODE = """ 
    @classmethod
    def execute(cls, *args, **kwargs):
        string = args[0]
        res = []
        for i in range(len(string)):
            op = string[i]
            if op == "-" or op == "+" or op == "*":
                sub_exp1 = string[0:i]
                sub_exp2 = string[i+1:]
                s1 = cls.execute(sub_exp1)
                s2 = cls.execute(sub_exp2)
                for i in s1:
                    for j in s2:
                        if op == "*":
                            res.append(int(i) * int(j))
                        if op == "+":
                            res.append(int(i) + int(j))
                        if op == "-":
                            res.append(int(i) - int(j))
        if len(res) == 0:
            res.append(int(string))
        return res
    """
    @classmethod
    def execute(cls, *args, **kwargs):
        string = args[0]
        res = []
        for i in range(len(string)):
            op = string[i]
            if op == "-" or op == "+" or op == "*":
                sub_exp1 = string[0:i]
                sub_exp2 = string[i+1:]
                s1 = cls.execute(sub_exp1)
                s2 = cls.execute(sub_exp2)
                for i in s1:
                    for j in s2:
                        if op == "*":
                            res.append(int(i) * int(j))
                        if op == "+":
                            res.append(int(i) + int(j))
                        if op == "-":
                            res.append(int(i) - int(j))
        if len(res) == 0:
            res.append(int(string))
        return res

    @classmethod
    def get_documentation(cls):
        return cls.__doc__

    @classmethod
    def get_test_cases(cls):
        return [
            {
                "inputs": {"string": "2-1-1"},
                "expected": [0, 2]  # Order doesn’t matter
            },
            {
                "inputs": {"string": "2*3-4*5"},
                "expected": [10, -34, -14, -10, 10]  # All possible results
            },
            {
                "inputs": {"string": "5"},
                "expected": [5]
            }
        ]

    @classmethod
    def run_test(cls):
        test_cases = cls.get_test_cases()
        results = []
        for i, test in enumerate(test_cases, 1):
            inputs = test["inputs"]
            result = cls.execute(inputs["string"])
            result.sort()
            expected = sorted(test["expected"])
            results.append(f"Test {i}: Inputs={inputs}, Result={result}, Expected={expected}")
        return "\n".join(results)

    @classmethod
    def get_source_code(cls):
        return cls.SOURCE_CODE.strip()



