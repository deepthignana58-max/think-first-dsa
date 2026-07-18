PROBLEMS = [
    {
        "id": 1,
        "title": "Two Sum",
        "topic": "Arrays + Hashing",
        "statement": "Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Assume exactly one solution exists.",
        "example": "Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]  (because nums[0] + nums[1] = 9)",
        "ideal_approach": "Use a hashmap to store each number and its index as you iterate. For each number, check if (target - number) already exists in the hashmap. This gives O(n) time instead of the brute force O(n^2) nested loop approach."
    },
    {
        "id": 2,
        "title": "Reverse a Linked List",
        "topic": "Linked List",
        "statement": "Given the head of a singly linked list, reverse the list and return the new head.",
        "example": "Input: 1 -> 2 -> 3 -> 4 -> None\nOutput: 4 -> 3 -> 2 -> 1 -> None",
        "ideal_approach": "Use three pointers: previous, current, and next. Iterate through the list, and for each node, reverse its 'next' pointer to point to 'previous', then move all three pointers forward. Previous ends up as the new head."
    },
    {
        "id": 3,
        "title": "Valid Parentheses",
        "topic": "Stack",
        "statement": "Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid (every opening bracket has a matching closing bracket in the correct order).",
        "example": "Input: \"{[()]}\"\nOutput: true\nInput: \"{[(])}\"\nOutput: false",
        "ideal_approach": "Use a stack. Push opening brackets onto the stack. When you see a closing bracket, check if it matches the top of the stack (pop and compare). If it doesn't match, or the stack is empty when you expect a match, the string is invalid. At the end, the stack must be empty."
    },
    {
        "id": 4,
        "title": "Binary Search",
        "topic": "Searching",
        "statement": "Given a sorted array of integers and a target value, return the index of the target if found, otherwise return -1. Must run in O(log n) time.",
        "example": "Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4",
        "ideal_approach": "Use two pointers, low and high, marking the search range. Repeatedly check the middle element: if it equals the target, return its index. If it's smaller than target, search the right half (move low). If larger, search the left half (move high). Repeat until found or the range is empty."
    },
    {
        "id": 5,
        "title": "Fibonacci with Memoization",
        "topic": "Recursion + Dynamic Programming",
        "statement": "Given an integer n, return the nth Fibonacci number efficiently (avoid recomputation).",
        "example": "Input: n = 10\nOutput: 55",
        "ideal_approach": "Use recursion with a memoization cache (dictionary) to store already-computed Fibonacci values. Before computing fib(n), check if it's already in the cache. This reduces time complexity from exponential O(2^n) to linear O(n)."
    }
]