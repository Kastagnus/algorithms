from tasks1 import TwoNumberSum, MoveZeros, FindThreeLargestNumber, BestTimeToBuyAndSellStocks, ContainsDuplicates, \
    PalindromeCheck, ValidateSubsequence, CaesarCipherEncryptor, FirstNonRepeatingCharacter, ValidAnagram, \
    FindClosestValueInBST, BSTTraversal, ValidateBST, MaximumDepthOfBinaryTree, NthFibonacci, MinimumCoinsForChange, \
    ClimbingStairs, MinimumWaitingTime, ClassPhotos, ValidStartingCity, TaskAssignment, BooleanExpressions, FreqStacks, \
    TrainTicket, SwitchPairNodes, AddNodeNumbers, MakeStringsAnagrams, PartitionString, NumberOfSubs, QueryNums, \
    PartitionPalindromes, MinExtraChars, BreakInteger, PerfectSquare, Intervals, PushPop, Temperatures, Circular, \
    ExecuteOperators, BinarySearch, MaximumSubarray, HouseRobber, TandemBicycle, SlidingPuzzle, PutMarbles, SplitArray, \
    Parenthesis, RobotPaths, AirplaneSeats, RotateIntegers


class AlgorithmManager:
    def __init__(self):
        self.algorithms = {}

    def add_algorithm(self, name, algorithm):
        normalized_name = name.replace(" ", "_").lower()
        self.algorithms[normalized_name] = algorithm

    def execute_algorithm(self, name, *args, **kwargs):
        normalized_name = name.replace(" ", "_").lower()
        if normalized_name in self.algorithms:
            algorithm = self.algorithms[normalized_name]
            return algorithm.execute(*args, **kwargs)
        else:
            raise NameError(f"Algorithm '{normalized_name}' not found")

    def get_algorithm_documentation(self, name):
        normalized_name = name.replace(" ", "_").lower()
        if normalized_name in self.algorithms:
            algorithm = self.algorithms[normalized_name]
            return algorithm.get_documentation()

    def get_algorithm_names(self):
        return list(self.algorithms.keys())
    def get_algorithm_source_code(self, name):
        normalized_name = name.replace(" ", "_").lower()
        if normalized_name in self.algorithms:
            algorithm = self.algorithms[normalized_name]
            return algorithm.get_source_code()
    def run_tests(self, name):
        normalized_name = name.replace(" ", "_").lower()
        if normalized_name in self.algorithms:
            algorithm = self.algorithms[normalized_name]
            return algorithm.run_test()
        else:
            raise NameError(f"Algorithm '{normalized_name}' not found")


manager =  AlgorithmManager()
manager.add_algorithm("Two Number Sum", TwoNumberSum)
manager.add_algorithm("Move Zeros", MoveZeros)
manager.add_algorithm("Find Three Largest Number", FindThreeLargestNumber)
manager.add_algorithm("Best Time to Buy and Sell Stock", BestTimeToBuyAndSellStocks)
manager.add_algorithm("Contains Duplicates", ContainsDuplicates)
manager.add_algorithm("Validate Subsequence", ValidateSubsequence)
manager.add_algorithm("Palindrome Check", PalindromeCheck)
manager.add_algorithm("Caesar Cipher Encryptor", CaesarCipherEncryptor)
manager.add_algorithm("First Non Repeating Character", FirstNonRepeatingCharacter)
manager.add_algorithm("Valid Anagram", ValidAnagram)
manager.add_algorithm("Binary Search", BinarySearch)
manager.add_algorithm("Find Closest Value in BST", FindClosestValueInBST)
manager.add_algorithm("BST Traversal", BSTTraversal)
manager.add_algorithm("Validate BST", ValidateBST)
manager.add_algorithm("Maximum Depth of Binary Tree", MaximumDepthOfBinaryTree)
manager.add_algorithm("Nth Fibonacci", NthFibonacci)
manager.add_algorithm("Minimum Coins For Change", MinimumCoinsForChange)
manager.add_algorithm("Climbing Stairs", ClimbingStairs)
manager.add_algorithm("Maximum Subarray", MaximumSubarray)
manager.add_algorithm("House Robber", HouseRobber)
manager.add_algorithm("Minimum Waiting Time", MinimumWaitingTime)
manager.add_algorithm("Class Photos", ClassPhotos)
manager.add_algorithm("Tandem Bicycle", TandemBicycle)
manager.add_algorithm("Valid Starting City", ValidStartingCity)
manager.add_algorithm("Task Assignment", TaskAssignment)
manager.add_algorithm("Boolean Expressions", BooleanExpressions)
manager.add_algorithm("Sliding Puzzle", SlidingPuzzle)
manager.add_algorithm("FreqStacks", FreqStacks)
manager.add_algorithm("Put Marbles", PutMarbles)
manager.add_algorithm("Split Array", SplitArray)
manager.add_algorithm("Parenthesis", Parenthesis)
manager.add_algorithm("Robot Paths", RobotPaths)
manager.add_algorithm("Train Tickets", TrainTicket)
manager.add_algorithm("Switch Pair Nodes", SwitchPairNodes)
manager.add_algorithm("Add Node Numbers", AddNodeNumbers)
manager.add_algorithm("Make Strings Anagrams", MakeStringsAnagrams)
manager.add_algorithm("Partition String", PartitionString)
manager.add_algorithm("Number Of Valid Substrings", NumberOfSubs)
manager.add_algorithm("Query Nums", QueryNums)
manager.add_algorithm("Airplane Seats", AirplaneSeats)
manager.add_algorithm("Partition Palindrome", PartitionPalindromes)
manager.add_algorithm("Rotate Integers", RotateIntegers)
manager.add_algorithm("Minimum Extra Characters", MinExtraChars)
manager.add_algorithm("Break Integer", BreakInteger)
manager.add_algorithm("Perfect Square", PerfectSquare)
manager.add_algorithm("Intervals", Intervals)
manager.add_algorithm("Push and Pop", PushPop)
manager.add_algorithm("Temperatures", Temperatures)
manager.add_algorithm("Circular Queue", Circular)
manager.add_algorithm("Execute Operators", ExecuteOperators)

