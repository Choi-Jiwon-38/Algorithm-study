"""
주차별 알고리즘 문제 자동 선정 및 PR 생성 스크립트
- LeetCode 75 + Top Interview 150 풀(Easy/Medium, 189문제)에서 선정
- 기존 PR 본문을 스캔해 중복 출제 방지
- Easy 2문제 / Medium 2문제 유형 무관 랜덤 선정
- week{N} 브랜치 생성 → README.md 커밋 → PR 오픈
"""

import os
import random
import base64
import requests
import re
from datetime import datetime

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ.get("GITHUB_REPOSITORY", "Choi-Jiwon-38/Algorithm-study")
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}
NUM_PROBLEMS = 4
ASSIGNEES = REVIEWERS = ["Choi-Jiwon-38", "AIJeongwon", "jinh-636"]


def make_url(slug):
    return f"https://leetcode.com/problems/{slug}/"


# ═══════════════════════════════════════════════════════════════════════════════
# 문제 풀: LeetCode 75 + Top Interview 150 (중복 제거 후 185문제)
# source: "LC75" | "TI150" | "both"
# ═══════════════════════════════════════════════════════════════════════════════
PROBLEM_POOL_RAW = [
    # ── Array & String ──────────────────────────────────────────────────────────
    {"id": "1",    "title": "Two Sum",                                          "slug": "two-sum",                                                "difficulty": "Easy",   "tags": ["Array", "Hash Table"],              "source": "TI150"},
    {"id": "6",    "title": "Zigzag Conversion",                                "slug": "zigzag-conversion",                                      "difficulty": "Medium", "tags": ["String"],                           "source": "TI150"},
    {"id": "12",   "title": "Integer to Roman",                                 "slug": "integer-to-roman",                                       "difficulty": "Medium", "tags": ["String", "Math"],                   "source": "TI150"},
    {"id": "13",   "title": "Roman to Integer",                                 "slug": "roman-to-integer",                                       "difficulty": "Easy",   "tags": ["String", "Math"],                   "source": "TI150"},
    {"id": "14",   "title": "Longest Common Prefix",                            "slug": "longest-common-prefix",                                  "difficulty": "Easy",   "tags": ["String"],                           "source": "TI150"},
    {"id": "26",   "title": "Remove Duplicates from Sorted Array",              "slug": "remove-duplicates-from-sorted-array",                    "difficulty": "Easy",   "tags": ["Array", "Two Pointers"],            "source": "TI150"},
    {"id": "27",   "title": "Remove Element",                                   "slug": "remove-element",                                         "difficulty": "Easy",   "tags": ["Array", "Two Pointers"],            "source": "TI150"},
    {"id": "28",   "title": "Find the Index of First Occurrence in a String",   "slug": "find-the-index-of-the-first-occurrence-in-a-string",     "difficulty": "Easy",   "tags": ["String"],                           "source": "TI150"},
    {"id": "45",   "title": "Jump Game II",                                     "slug": "jump-game-ii",                                           "difficulty": "Medium", "tags": ["Array", "Greedy"],                  "source": "TI150"},
    {"id": "55",   "title": "Jump Game",                                        "slug": "jump-game",                                              "difficulty": "Medium", "tags": ["Array", "Greedy"],                  "source": "TI150"},
    {"id": "58",   "title": "Length of Last Word",                              "slug": "length-of-last-word",                                    "difficulty": "Easy",   "tags": ["String"],                           "source": "TI150"},
    {"id": "66",   "title": "Plus One",                                         "slug": "plus-one",                                               "difficulty": "Easy",   "tags": ["Array", "Math"],                    "source": "TI150"},
    {"id": "67",   "title": "Add Binary",                                       "slug": "add-binary",                                             "difficulty": "Easy",   "tags": ["Bit Manipulation", "String"],       "source": "TI150"},
    {"id": "80",   "title": "Remove Duplicates from Sorted Array II",           "slug": "remove-duplicates-from-sorted-array-ii",                 "difficulty": "Medium", "tags": ["Array", "Two Pointers"],            "source": "TI150"},
    {"id": "88",   "title": "Merge Sorted Array",                               "slug": "merge-sorted-array",                                     "difficulty": "Easy",   "tags": ["Array", "Two Pointers"],            "source": "TI150"},
    {"id": "121",  "title": "Best Time to Buy and Sell Stock",                  "slug": "best-time-to-buy-and-sell-stock",                        "difficulty": "Easy",   "tags": ["Array", "DP"],                      "source": "TI150"},
    {"id": "122",  "title": "Best Time to Buy and Sell Stock II",               "slug": "best-time-to-buy-and-sell-stock-ii",                     "difficulty": "Medium", "tags": ["Array", "Greedy"],                  "source": "TI150"},
    {"id": "134",  "title": "Gas Station",                                      "slug": "gas-station",                                            "difficulty": "Medium", "tags": ["Array", "Greedy"],                  "source": "TI150"},
    {"id": "151",  "title": "Reverse Words in a String",                        "slug": "reverse-words-in-a-string",                              "difficulty": "Medium", "tags": ["String", "Two Pointers"],           "source": "both"},
    {"id": "169",  "title": "Majority Element",                                 "slug": "majority-element",                                       "difficulty": "Easy",   "tags": ["Array", "Hash Table"],              "source": "TI150"},
    {"id": "189",  "title": "Rotate Array",                                     "slug": "rotate-array",                                           "difficulty": "Medium", "tags": ["Array"],                            "source": "TI150"},
    {"id": "238",  "title": "Product of Array Except Self",                     "slug": "product-of-array-except-self",                           "difficulty": "Medium", "tags": ["Array", "Prefix Sum"],              "source": "both"},
    {"id": "274",  "title": "H-Index",                                          "slug": "h-index",                                                "difficulty": "Medium", "tags": ["Array", "Sorting"],                 "source": "TI150"},
    {"id": "334",  "title": "Increasing Triplet Subsequence",                   "slug": "increasing-triplet-subsequence",                         "difficulty": "Medium", "tags": ["Array", "Greedy"],                  "source": "LC75"},
    {"id": "345",  "title": "Reverse Vowels of a String",                       "slug": "reverse-vowels-of-a-string",                             "difficulty": "Easy",   "tags": ["String", "Two Pointers"],           "source": "LC75"},
    {"id": "380",  "title": "Insert Delete GetRandom O(1)",                     "slug": "insert-delete-getrandom-o1",                             "difficulty": "Medium", "tags": ["Array", "Hash Table"],              "source": "TI150"},
    {"id": "392",  "title": "Is Subsequence",                                   "slug": "is-subsequence",                                         "difficulty": "Easy",   "tags": ["String", "Two Pointers"],           "source": "both"},
    {"id": "443",  "title": "String Compression",                               "slug": "string-compression",                                     "difficulty": "Medium", "tags": ["Array", "Two Pointers"],            "source": "LC75"},
    {"id": "605",  "title": "Can Place Flowers",                                "slug": "can-place-flowers",                                      "difficulty": "Easy",   "tags": ["Array", "Greedy"],                  "source": "LC75"},
    {"id": "1071", "title": "Greatest Common Divisor of Strings",               "slug": "greatest-common-divisor-of-strings",                     "difficulty": "Easy",   "tags": ["String", "Math"],                   "source": "LC75"},
    {"id": "1431", "title": "Kids With the Greatest Number of Candies",         "slug": "kids-with-the-greatest-number-of-candies",               "difficulty": "Easy",   "tags": ["Array"],                            "source": "LC75"},
    {"id": "1768", "title": "Merge Strings Alternately",                        "slug": "merge-strings-alternately",                              "difficulty": "Easy",   "tags": ["String", "Two Pointers"],           "source": "LC75"},
    # ── Two Pointers ────────────────────────────────────────────────────────────
    {"id": "11",   "title": "Container With Most Water",                        "slug": "container-with-most-water",                              "difficulty": "Medium", "tags": ["Array", "Two Pointers"],            "source": "both"},
    {"id": "15",   "title": "3Sum",                                             "slug": "3sum",                                                   "difficulty": "Medium", "tags": ["Array", "Two Pointers"],            "source": "TI150"},
    {"id": "125",  "title": "Valid Palindrome",                                 "slug": "valid-palindrome",                                       "difficulty": "Easy",   "tags": ["String", "Two Pointers"],           "source": "TI150"},
    {"id": "167",  "title": "Two Sum II - Input Array Is Sorted",               "slug": "two-sum-ii-input-array-is-sorted",                       "difficulty": "Medium", "tags": ["Array", "Two Pointers"],            "source": "TI150"},
    {"id": "283",  "title": "Move Zeroes",                                      "slug": "move-zeroes",                                            "difficulty": "Easy",   "tags": ["Array", "Two Pointers"],            "source": "LC75"},
    {"id": "1679", "title": "Max Number of K-Sum Pairs",                        "slug": "max-number-of-k-sum-pairs",                              "difficulty": "Medium", "tags": ["Array", "Hash Table"],              "source": "LC75"},
    # ── Sliding Window ──────────────────────────────────────────────────────────
    {"id": "3",    "title": "Longest Substring Without Repeating Characters",   "slug": "longest-substring-without-repeating-characters",         "difficulty": "Medium", "tags": ["String", "Sliding Window"],         "source": "TI150"},
    {"id": "209",  "title": "Minimum Size Subarray Sum",                        "slug": "minimum-size-subarray-sum",                              "difficulty": "Medium", "tags": ["Array", "Sliding Window"],          "source": "TI150"},
    {"id": "643",  "title": "Maximum Average Subarray I",                       "slug": "maximum-average-subarray-i",                             "difficulty": "Easy",   "tags": ["Array", "Sliding Window"],          "source": "LC75"},
    {"id": "1004", "title": "Max Consecutive Ones III",                         "slug": "max-consecutive-ones-iii",                               "difficulty": "Medium", "tags": ["Array", "Sliding Window"],          "source": "LC75"},
    {"id": "1456", "title": "Maximum Number of Vowels in a Substring of Given Length", "slug": "maximum-number-of-vowels-in-a-substring-of-given-length", "difficulty": "Medium", "tags": ["String", "Sliding Window"], "source": "LC75"},
    {"id": "1493", "title": "Longest Subarray of 1's After Deleting One Element", "slug": "longest-subarray-of-1s-after-deleting-one-element",   "difficulty": "Medium", "tags": ["Array", "Sliding Window", "DP"],    "source": "LC75"},
    # ── Prefix Sum ──────────────────────────────────────────────────────────────
    {"id": "724",  "title": "Find Pivot Index",                                 "slug": "find-pivot-index",                                       "difficulty": "Easy",   "tags": ["Array", "Prefix Sum"],              "source": "LC75"},
    {"id": "1732", "title": "Find the Highest Altitude",                        "slug": "find-the-highest-altitude",                              "difficulty": "Easy",   "tags": ["Array", "Prefix Sum"],              "source": "LC75"},
    # ── HashMap / HashSet ───────────────────────────────────────────────────────
    {"id": "49",   "title": "Group Anagrams",                                   "slug": "group-anagrams",                                         "difficulty": "Medium", "tags": ["Array", "Hash Table"],              "source": "TI150"},
    {"id": "128",  "title": "Longest Consecutive Sequence",                     "slug": "longest-consecutive-sequence",                           "difficulty": "Medium", "tags": ["Array", "Hash Table"],              "source": "TI150"},
    {"id": "202",  "title": "Happy Number",                                     "slug": "happy-number",                                           "difficulty": "Easy",   "tags": ["Math", "Hash Table"],               "source": "TI150"},
    {"id": "205",  "title": "Isomorphic Strings",                               "slug": "isomorphic-strings",                                     "difficulty": "Easy",   "tags": ["String", "Hash Table"],             "source": "TI150"},
    {"id": "219",  "title": "Contains Duplicate II",                            "slug": "contains-duplicate-ii",                                  "difficulty": "Easy",   "tags": ["Array", "Hash Table"],              "source": "TI150"},
    {"id": "242",  "title": "Valid Anagram",                                    "slug": "valid-anagram",                                          "difficulty": "Easy",   "tags": ["String", "Hash Table"],             "source": "TI150"},
    {"id": "290",  "title": "Word Pattern",                                     "slug": "word-pattern",                                           "difficulty": "Easy",   "tags": ["String", "Hash Table"],             "source": "TI150"},
    {"id": "383",  "title": "Ransom Note",                                      "slug": "ransom-note",                                            "difficulty": "Easy",   "tags": ["String", "Hash Table"],             "source": "TI150"},
    {"id": "1207", "title": "Unique Number of Occurrences",                     "slug": "unique-number-of-occurrences",                           "difficulty": "Easy",   "tags": ["Array", "Hash Table"],              "source": "LC75"},
    {"id": "1657", "title": "Determine if Two Strings Are Close",               "slug": "determine-if-two-strings-are-close",                     "difficulty": "Medium", "tags": ["String", "Hash Table"],             "source": "LC75"},
    {"id": "2215", "title": "Find the Difference of Two Arrays",                "slug": "find-the-difference-of-two-arrays",                      "difficulty": "Easy",   "tags": ["Array", "Hash Table"],              "source": "LC75"},
    {"id": "2352", "title": "Equal Row and Column Pairs",                       "slug": "equal-row-and-column-pairs",                             "difficulty": "Medium", "tags": ["Array", "Hash Table"],              "source": "LC75"},
    # ── Stack ───────────────────────────────────────────────────────────────────
    {"id": "20",   "title": "Valid Parentheses",                                "slug": "valid-parentheses",                                      "difficulty": "Easy",   "tags": ["Stack", "String"],                  "source": "TI150"},
    {"id": "71",   "title": "Simplify Path",                                    "slug": "simplify-path",                                          "difficulty": "Medium", "tags": ["Stack", "String"],                  "source": "TI150"},
    {"id": "150",  "title": "Evaluate Reverse Polish Notation",                 "slug": "evaluate-reverse-polish-notation",                       "difficulty": "Medium", "tags": ["Stack", "Array"],                   "source": "TI150"},
    {"id": "155",  "title": "Min Stack",                                        "slug": "min-stack",                                              "difficulty": "Medium", "tags": ["Stack", "Design"],                  "source": "TI150"},
    {"id": "394",  "title": "Decode String",                                    "slug": "decode-string",                                          "difficulty": "Medium", "tags": ["Stack", "String"],                  "source": "both"},
    {"id": "735",  "title": "Asteroid Collision",                               "slug": "asteroid-collision",                                     "difficulty": "Medium", "tags": ["Stack", "Array"],                   "source": "LC75"},
    {"id": "2390", "title": "Removing Stars From a String",                     "slug": "removing-stars-from-a-string",                           "difficulty": "Medium", "tags": ["Stack", "String"],                  "source": "LC75"},
    # ── Queue ───────────────────────────────────────────────────────────────────
    {"id": "649",  "title": "Dota2 Senate",                                     "slug": "dota2-senate",                                           "difficulty": "Medium", "tags": ["Queue", "Greedy"],                  "source": "LC75"},
    {"id": "933",  "title": "Number of Recent Calls",                           "slug": "number-of-recent-calls",                                 "difficulty": "Easy",   "tags": ["Queue", "Data Stream"],             "source": "LC75"},
    # ── Linked List ─────────────────────────────────────────────────────────────
    {"id": "2",    "title": "Add Two Numbers",                                  "slug": "add-two-numbers",                                        "difficulty": "Medium", "tags": ["Linked List", "Math"],              "source": "TI150"},
    {"id": "19",   "title": "Remove Nth Node From End of List",                 "slug": "remove-nth-node-from-end-of-list",                       "difficulty": "Medium", "tags": ["Linked List", "Two Pointers"],      "source": "TI150"},
    {"id": "21",   "title": "Merge Two Sorted Lists",                           "slug": "merge-two-sorted-lists",                                 "difficulty": "Easy",   "tags": ["Linked List"],                      "source": "TI150"},
    {"id": "61",   "title": "Rotate List",                                      "slug": "rotate-list",                                            "difficulty": "Medium", "tags": ["Linked List", "Two Pointers"],      "source": "TI150"},
    {"id": "82",   "title": "Remove Duplicates from Sorted List II",            "slug": "remove-duplicates-from-sorted-list-ii",                  "difficulty": "Medium", "tags": ["Linked List"],                      "source": "TI150"},
    {"id": "86",   "title": "Partition List",                                   "slug": "partition-list",                                         "difficulty": "Medium", "tags": ["Linked List", "Two Pointers"],      "source": "TI150"},
    {"id": "92",   "title": "Reverse Linked List II",                           "slug": "reverse-linked-list-ii",                                 "difficulty": "Medium", "tags": ["Linked List"],                      "source": "TI150"},
    {"id": "138",  "title": "Copy List with Random Pointer",                    "slug": "copy-list-with-random-pointer",                          "difficulty": "Medium", "tags": ["Linked List", "Hash Table"],        "source": "TI150"},
    {"id": "141",  "title": "Linked List Cycle",                                "slug": "linked-list-cycle",                                      "difficulty": "Easy",   "tags": ["Linked List", "Two Pointers"],      "source": "TI150"},
    {"id": "146",  "title": "LRU Cache",                                        "slug": "lru-cache",                                              "difficulty": "Medium", "tags": ["Linked List", "Design"],            "source": "TI150"},
    {"id": "206",  "title": "Reverse Linked List",                              "slug": "reverse-linked-list",                                    "difficulty": "Easy",   "tags": ["Linked List"],                      "source": "both"},
    {"id": "328",  "title": "Odd Even Linked List",                             "slug": "odd-even-linked-list",                                   "difficulty": "Medium", "tags": ["Linked List"],                      "source": "LC75"},
    {"id": "2095", "title": "Delete the Middle Node of a Linked List",          "slug": "delete-the-middle-node-of-a-linked-list",                "difficulty": "Medium", "tags": ["Linked List", "Two Pointers"],      "source": "LC75"},
    {"id": "2130", "title": "Maximum Twin Sum of a Linked List",                "slug": "maximum-twin-sum-of-a-linked-list",                      "difficulty": "Medium", "tags": ["Linked List", "Two Pointers"],      "source": "LC75"},
    # ── Binary Tree ─────────────────────────────────────────────────────────────
    {"id": "98",   "title": "Validate Binary Search Tree",                      "slug": "validate-binary-search-tree",                            "difficulty": "Medium", "tags": ["Tree", "DFS"],                      "source": "TI150"},
    {"id": "100",  "title": "Same Tree",                                        "slug": "same-tree",                                              "difficulty": "Easy",   "tags": ["Tree", "DFS"],                      "source": "TI150"},
    {"id": "101",  "title": "Symmetric Tree",                                   "slug": "symmetric-tree",                                         "difficulty": "Easy",   "tags": ["Tree", "DFS"],                      "source": "TI150"},
    {"id": "102",  "title": "Binary Tree Level Order Traversal",                "slug": "binary-tree-level-order-traversal",                      "difficulty": "Medium", "tags": ["Tree", "BFS"],                      "source": "TI150"},
    {"id": "103",  "title": "Binary Tree Zigzag Level Order Traversal",         "slug": "binary-tree-zigzag-level-order-traversal",               "difficulty": "Medium", "tags": ["Tree", "BFS"],                      "source": "TI150"},
    {"id": "104",  "title": "Maximum Depth of Binary Tree",                     "slug": "maximum-depth-of-binary-tree",                           "difficulty": "Easy",   "tags": ["Tree", "DFS"],                      "source": "both"},
    {"id": "105",  "title": "Construct Binary Tree from Preorder and Inorder Traversal", "slug": "construct-binary-tree-from-preorder-and-inorder-traversal", "difficulty": "Medium", "tags": ["Tree", "DFS"],         "source": "TI150"},
    {"id": "106",  "title": "Construct Binary Tree from Inorder and Postorder Traversal", "slug": "construct-binary-tree-from-inorder-and-postorder-traversal", "difficulty": "Medium", "tags": ["Tree", "DFS"],       "source": "TI150"},
    {"id": "108",  "title": "Convert Sorted Array to Binary Search Tree",       "slug": "convert-sorted-array-to-binary-search-tree",             "difficulty": "Easy",   "tags": ["Tree", "Divide & Conquer"],         "source": "TI150"},
    {"id": "112",  "title": "Path Sum",                                         "slug": "path-sum",                                               "difficulty": "Easy",   "tags": ["Tree", "DFS"],                      "source": "TI150"},
    {"id": "114",  "title": "Flatten Binary Tree to Linked List",               "slug": "flatten-binary-tree-to-linked-list",                     "difficulty": "Medium", "tags": ["Tree", "DFS"],                      "source": "TI150"},
    {"id": "117",  "title": "Populating Next Right Pointers in Each Node II",   "slug": "populating-next-right-pointers-in-each-node-ii",         "difficulty": "Medium", "tags": ["Tree", "BFS"],                      "source": "TI150"},
    {"id": "129",  "title": "Sum Root to Leaf Numbers",                         "slug": "sum-root-to-leaf-numbers",                               "difficulty": "Medium", "tags": ["Tree", "DFS"],                      "source": "TI150"},
    {"id": "173",  "title": "Binary Search Tree Iterator",                      "slug": "binary-search-tree-iterator",                            "difficulty": "Medium", "tags": ["Tree", "Stack", "Design"],          "source": "TI150"},
    {"id": "199",  "title": "Binary Tree Right Side View",                      "slug": "binary-tree-right-side-view",                            "difficulty": "Medium", "tags": ["Tree", "BFS"],                      "source": "both"},
    {"id": "222",  "title": "Count Complete Tree Nodes",                        "slug": "count-complete-tree-nodes",                              "difficulty": "Easy",   "tags": ["Tree", "Binary Search"],            "source": "TI150"},
    {"id": "226",  "title": "Invert Binary Tree",                               "slug": "invert-binary-tree",                                     "difficulty": "Easy",   "tags": ["Tree", "DFS"],                      "source": "TI150"},
    {"id": "230",  "title": "Kth Smallest Element in a BST",                   "slug": "kth-smallest-element-in-a-bst",                          "difficulty": "Medium", "tags": ["Tree", "DFS"],                      "source": "TI150"},
    {"id": "236",  "title": "Lowest Common Ancestor of a Binary Tree",          "slug": "lowest-common-ancestor-of-a-binary-tree",                "difficulty": "Medium", "tags": ["Tree", "DFS"],                      "source": "both"},
    {"id": "437",  "title": "Path Sum III",                                     "slug": "path-sum-iii",                                           "difficulty": "Medium", "tags": ["Tree", "DFS", "Prefix Sum"],        "source": "LC75"},
    {"id": "450",  "title": "Delete Node in a BST",                             "slug": "delete-node-in-a-bst",                                   "difficulty": "Medium", "tags": ["Tree", "DFS"],                      "source": "LC75"},
    {"id": "530",  "title": "Minimum Absolute Difference in BST",               "slug": "minimum-absolute-difference-in-bst",                     "difficulty": "Easy",   "tags": ["Tree", "DFS"],                      "source": "TI150"},
    {"id": "637",  "title": "Average of Levels in Binary Tree",                 "slug": "average-of-levels-in-binary-tree",                       "difficulty": "Easy",   "tags": ["Tree", "BFS"],                      "source": "TI150"},
    {"id": "700",  "title": "Search in a Binary Search Tree",                   "slug": "search-in-a-binary-search-tree",                         "difficulty": "Easy",   "tags": ["Tree", "DFS"],                      "source": "LC75"},
    {"id": "1161", "title": "Maximum Level Sum of a Binary Tree",               "slug": "maximum-level-sum-of-a-binary-tree",                     "difficulty": "Medium", "tags": ["Tree", "BFS"],                      "source": "LC75"},
    {"id": "1372", "title": "Longest ZigZag Path in a Binary Tree",             "slug": "longest-zigzag-path-in-a-binary-tree",                   "difficulty": "Medium", "tags": ["Tree", "DFS", "DP"],                "source": "LC75"},
    {"id": "1448", "title": "Count Good Nodes in Binary Tree",                  "slug": "count-good-nodes-in-binary-tree",                        "difficulty": "Medium", "tags": ["Tree", "DFS"],                      "source": "LC75"},
    # ── Graph ───────────────────────────────────────────────────────────────────
    {"id": "130",  "title": "Surrounded Regions",                               "slug": "surrounded-regions",                                     "difficulty": "Medium", "tags": ["Graph", "DFS"],                     "source": "TI150"},
    {"id": "133",  "title": "Clone Graph",                                      "slug": "clone-graph",                                            "difficulty": "Medium", "tags": ["Graph", "DFS"],                     "source": "TI150"},
    {"id": "200",  "title": "Number of Islands",                                "slug": "number-of-islands",                                      "difficulty": "Medium", "tags": ["Graph", "DFS", "BFS"],              "source": "TI150"},
    {"id": "207",  "title": "Course Schedule",                                  "slug": "course-schedule",                                        "difficulty": "Medium", "tags": ["Graph", "Topological Sort"],        "source": "TI150"},
    {"id": "210",  "title": "Course Schedule II",                               "slug": "course-schedule-ii",                                     "difficulty": "Medium", "tags": ["Graph", "Topological Sort"],        "source": "TI150"},
    {"id": "399",  "title": "Evaluate Division",                                "slug": "evaluate-division",                                      "difficulty": "Medium", "tags": ["Graph", "DFS"],                     "source": "both"},
    {"id": "433",  "title": "Minimum Genetic Mutation",                         "slug": "minimum-genetic-mutation",                               "difficulty": "Medium", "tags": ["Graph", "BFS"],                     "source": "TI150"},
    {"id": "547",  "title": "Number of Provinces",                              "slug": "number-of-provinces",                                    "difficulty": "Medium", "tags": ["Graph", "Union Find"],              "source": "LC75"},
    {"id": "841",  "title": "Keys and Rooms",                                   "slug": "keys-and-rooms",                                         "difficulty": "Medium", "tags": ["Graph", "DFS"],                     "source": "LC75"},
    {"id": "909",  "title": "Snakes and Ladders",                               "slug": "snakes-and-ladders",                                     "difficulty": "Medium", "tags": ["Graph", "BFS"],                     "source": "TI150"},
    {"id": "994",  "title": "Rotting Oranges",                                  "slug": "rotting-oranges",                                        "difficulty": "Medium", "tags": ["Graph", "BFS"],                     "source": "LC75"},
    {"id": "1466", "title": "Reorder Routes to Make All Paths Lead to the City Zero", "slug": "reorder-routes-to-make-all-paths-lead-to-the-city-zero", "difficulty": "Medium", "tags": ["Graph", "DFS"],             "source": "LC75"},
    {"id": "1926", "title": "Nearest Exit from Entrance in Maze",               "slug": "nearest-exit-from-entrance-in-maze",                     "difficulty": "Medium", "tags": ["Graph", "BFS"],                     "source": "LC75"},
    # ── Heap / Priority Queue ───────────────────────────────────────────────────
    {"id": "215",  "title": "Kth Largest Element in an Array",                  "slug": "kth-largest-element-in-an-array",                        "difficulty": "Medium", "tags": ["Heap", "Array"],                    "source": "both"},
    {"id": "373",  "title": "Find K Pairs with Smallest Sums",                  "slug": "find-k-pairs-with-smallest-sums",                        "difficulty": "Medium", "tags": ["Heap", "Array"],                    "source": "TI150"},
    {"id": "2336", "title": "Smallest Number in Infinite Set",                  "slug": "smallest-number-in-infinite-set",                        "difficulty": "Medium", "tags": ["Heap", "Design"],                   "source": "LC75"},
    {"id": "2462", "title": "Total Cost to Hire K Workers",                     "slug": "total-cost-to-hire-k-workers",                           "difficulty": "Medium", "tags": ["Heap", "Two Pointers"],             "source": "LC75"},
    {"id": "2542", "title": "Maximum Subsequence Score",                        "slug": "maximum-subsequence-score",                              "difficulty": "Medium", "tags": ["Heap", "Greedy"],                   "source": "LC75"},
    # ── Binary Search ───────────────────────────────────────────────────────────
    {"id": "33",   "title": "Search in Rotated Sorted Array",                   "slug": "search-in-rotated-sorted-array",                         "difficulty": "Medium", "tags": ["Binary Search", "Array"],           "source": "TI150"},
    {"id": "34",   "title": "Find First and Last Position of Element in Sorted Array", "slug": "find-first-and-last-position-of-element-in-sorted-array", "difficulty": "Medium", "tags": ["Binary Search", "Array"],   "source": "TI150"},
    {"id": "35",   "title": "Search Insert Position",                           "slug": "search-insert-position",                                 "difficulty": "Easy",   "tags": ["Binary Search", "Array"],           "source": "TI150"},
    {"id": "69",   "title": "Sqrt(x)",                                          "slug": "sqrtx",                                                  "difficulty": "Easy",   "tags": ["Binary Search", "Math"],            "source": "TI150"},
    {"id": "74",   "title": "Search a 2D Matrix",                               "slug": "search-a-2d-matrix",                                     "difficulty": "Medium", "tags": ["Binary Search", "Matrix"],          "source": "TI150"},
    {"id": "153",  "title": "Find Minimum in Rotated Sorted Array",             "slug": "find-minimum-in-rotated-sorted-array",                   "difficulty": "Medium", "tags": ["Binary Search", "Array"],           "source": "TI150"},
    {"id": "162",  "title": "Find Peak Element",                                "slug": "find-peak-element",                                      "difficulty": "Medium", "tags": ["Binary Search", "Array"],           "source": "both"},
    {"id": "374",  "title": "Guess Number Higher or Lower",                     "slug": "guess-number-higher-or-lower",                           "difficulty": "Easy",   "tags": ["Binary Search"],                    "source": "LC75"},
    {"id": "875",  "title": "Koko Eating Bananas",                              "slug": "koko-eating-bananas",                                    "difficulty": "Medium", "tags": ["Binary Search", "Array"],           "source": "LC75"},
    {"id": "2300", "title": "Successful Pairs of Spells and Potions",           "slug": "successful-pairs-of-spells-and-potions",                 "difficulty": "Medium", "tags": ["Binary Search", "Array"],           "source": "LC75"},
    # ── Trie ────────────────────────────────────────────────────────────────────
    {"id": "208",  "title": "Implement Trie (Prefix Tree)",                     "slug": "implement-trie-prefix-tree",                             "difficulty": "Medium", "tags": ["Trie", "Design"],                   "source": "both"},
    {"id": "211",  "title": "Design Add and Search Words Data Structure",       "slug": "design-add-and-search-words-data-structure",             "difficulty": "Medium", "tags": ["Trie", "Design"],                   "source": "TI150"},
    {"id": "1268", "title": "Search Suggestions System",                        "slug": "search-suggestions-system",                              "difficulty": "Medium", "tags": ["Trie", "Binary Search"],            "source": "LC75"},
    # ── Backtracking ────────────────────────────────────────────────────────────
    {"id": "17",   "title": "Letter Combinations of a Phone Number",            "slug": "letter-combinations-of-a-phone-number",                  "difficulty": "Medium", "tags": ["Backtracking", "String"],           "source": "both"},
    {"id": "22",   "title": "Generate Parentheses",                             "slug": "generate-parentheses",                                   "difficulty": "Medium", "tags": ["Backtracking", "String"],           "source": "TI150"},
    {"id": "39",   "title": "Combination Sum",                                  "slug": "combination-sum",                                        "difficulty": "Medium", "tags": ["Backtracking", "Array"],            "source": "TI150"},
    {"id": "46",   "title": "Permutations",                                     "slug": "permutations",                                           "difficulty": "Medium", "tags": ["Backtracking", "Array"],            "source": "TI150"},
    {"id": "77",   "title": "Combinations",                                     "slug": "combinations",                                           "difficulty": "Medium", "tags": ["Backtracking"],                     "source": "TI150"},
    {"id": "79",   "title": "Word Search",                                      "slug": "word-search",                                            "difficulty": "Medium", "tags": ["Backtracking", "Matrix"],           "source": "TI150"},
    {"id": "216",  "title": "Combination Sum III",                              "slug": "combination-sum-iii",                                    "difficulty": "Medium", "tags": ["Backtracking", "Array"],            "source": "LC75"},
    # ── Dynamic Programming ─────────────────────────────────────────────────────
    {"id": "5",    "title": "Longest Palindromic Substring",                    "slug": "longest-palindromic-substring",                          "difficulty": "Medium", "tags": ["DP", "String"],                     "source": "TI150"},
    {"id": "53",   "title": "Maximum Subarray",                                 "slug": "maximum-subarray",                                       "difficulty": "Medium", "tags": ["DP", "Array"],                      "source": "TI150"},
    {"id": "62",   "title": "Unique Paths",                                     "slug": "unique-paths",                                           "difficulty": "Medium", "tags": ["DP", "Math"],                       "source": "LC75"},
    {"id": "63",   "title": "Unique Paths II",                                  "slug": "unique-paths-ii",                                        "difficulty": "Medium", "tags": ["DP", "Matrix"],                     "source": "TI150"},
    {"id": "64",   "title": "Minimum Path Sum",                                 "slug": "minimum-path-sum",                                       "difficulty": "Medium", "tags": ["DP", "Matrix"],                     "source": "TI150"},
    {"id": "70",   "title": "Climbing Stairs",                                  "slug": "climbing-stairs",                                        "difficulty": "Easy",   "tags": ["DP", "Math"],                       "source": "TI150"},
    {"id": "72",   "title": "Edit Distance",                                    "slug": "edit-distance",                                          "difficulty": "Medium", "tags": ["DP", "String"],                     "source": "both"},
    {"id": "97",   "title": "Interleaving String",                              "slug": "interleaving-string",                                    "difficulty": "Medium", "tags": ["DP", "String"],                     "source": "TI150"},
    {"id": "120",  "title": "Triangle",                                         "slug": "triangle",                                               "difficulty": "Medium", "tags": ["DP", "Array"],                      "source": "TI150"},
    {"id": "139",  "title": "Word Break",                                       "slug": "word-break",                                             "difficulty": "Medium", "tags": ["DP", "Hash Table"],                 "source": "TI150"},
    {"id": "198",  "title": "House Robber",                                     "slug": "house-robber",                                           "difficulty": "Medium", "tags": ["DP", "Array"],                      "source": "both"},
    {"id": "300",  "title": "Longest Increasing Subsequence",                   "slug": "longest-increasing-subsequence",                         "difficulty": "Medium", "tags": ["DP", "Array"],                      "source": "TI150"},
    {"id": "322",  "title": "Coin Change",                                      "slug": "coin-change",                                            "difficulty": "Medium", "tags": ["DP", "Array"],                      "source": "TI150"},
    {"id": "714",  "title": "Best Time to Buy and Sell Stock with Transaction Fee", "slug": "best-time-to-buy-and-sell-stock-with-transaction-fee", "difficulty": "Medium", "tags": ["DP", "Greedy"],               "source": "LC75"},
    {"id": "746",  "title": "Min Cost Climbing Stairs",                         "slug": "min-cost-climbing-stairs",                               "difficulty": "Easy",   "tags": ["DP", "Array"],                      "source": "LC75"},
    {"id": "790",  "title": "Domino and Tromino Tiling",                        "slug": "domino-and-tromino-tiling",                              "difficulty": "Medium", "tags": ["DP"],                               "source": "LC75"},
    {"id": "918",  "title": "Maximum Sum Circular Subarray",                    "slug": "maximum-sum-circular-subarray",                          "difficulty": "Medium", "tags": ["DP", "Array"],                      "source": "TI150"},
    {"id": "1137", "title": "N-th Tribonacci Number",                           "slug": "n-th-tribonacci-number",                                 "difficulty": "Easy",   "tags": ["DP", "Math"],                       "source": "LC75"},
    {"id": "1143", "title": "Longest Common Subsequence",                       "slug": "longest-common-subsequence",                             "difficulty": "Medium", "tags": ["DP", "String"],                     "source": "both"},
    # ── Bit Manipulation ────────────────────────────────────────────────────────
    {"id": "136",  "title": "Single Number",                                    "slug": "single-number",                                          "difficulty": "Easy",   "tags": ["Bit Manipulation", "Array"],        "source": "both"},
    {"id": "137",  "title": "Single Number II",                                 "slug": "single-number-ii",                                       "difficulty": "Medium", "tags": ["Bit Manipulation", "Array"],        "source": "TI150"},
    {"id": "190",  "title": "Reverse Bits",                                     "slug": "reverse-bits",                                           "difficulty": "Easy",   "tags": ["Bit Manipulation"],                 "source": "TI150"},
    {"id": "191",  "title": "Number of 1 Bits",                                 "slug": "number-of-1-bits",                                       "difficulty": "Easy",   "tags": ["Bit Manipulation"],                 "source": "TI150"},
    {"id": "201",  "title": "Bitwise AND of Numbers Range",                     "slug": "bitwise-and-of-numbers-range",                           "difficulty": "Medium", "tags": ["Bit Manipulation"],                 "source": "TI150"},
    {"id": "338",  "title": "Counting Bits",                                    "slug": "counting-bits",                                          "difficulty": "Easy",   "tags": ["Bit Manipulation", "DP"],           "source": "both"},
    {"id": "1318", "title": "Minimum Flips to Make a OR b Equal to c",         "slug": "minimum-flips-to-make-a-or-b-equal-to-c",                "difficulty": "Medium", "tags": ["Bit Manipulation"],                 "source": "LC75"},
    # ── Math ────────────────────────────────────────────────────────────────────
    {"id": "9",    "title": "Palindrome Number",                                "slug": "palindrome-number",                                      "difficulty": "Easy",   "tags": ["Math"],                             "source": "TI150"},
    {"id": "50",   "title": "Pow(x, n)",                                        "slug": "powx-n",                                                 "difficulty": "Medium", "tags": ["Math", "Divide & Conquer"],         "source": "TI150"},
    {"id": "172",  "title": "Factorial Trailing Zeroes",                        "slug": "factorial-trailing-zeroes",                              "difficulty": "Medium", "tags": ["Math"],                             "source": "TI150"},
    # ── Matrix ──────────────────────────────────────────────────────────────────
    {"id": "36",   "title": "Valid Sudoku",                                     "slug": "valid-sudoku",                                           "difficulty": "Medium", "tags": ["Matrix", "Hash Table"],             "source": "TI150"},
    {"id": "48",   "title": "Rotate Image",                                     "slug": "rotate-image",                                           "difficulty": "Medium", "tags": ["Matrix"],                           "source": "TI150"},
    {"id": "54",   "title": "Spiral Matrix",                                    "slug": "spiral-matrix",                                          "difficulty": "Medium", "tags": ["Matrix", "Simulation"],             "source": "TI150"},
    {"id": "73",   "title": "Set Matrix Zeroes",                                "slug": "set-matrix-zeroes",                                      "difficulty": "Medium", "tags": ["Matrix"],                           "source": "TI150"},
    {"id": "289",  "title": "Game of Life",                                     "slug": "game-of-life",                                           "difficulty": "Medium", "tags": ["Matrix", "Simulation"],             "source": "TI150"},
    # ── Intervals ───────────────────────────────────────────────────────────────
    {"id": "56",   "title": "Merge Intervals",                                  "slug": "merge-intervals",                                        "difficulty": "Medium", "tags": ["Array", "Sorting"],                 "source": "TI150"},
    {"id": "57",   "title": "Insert Interval",                                  "slug": "insert-interval",                                        "difficulty": "Medium", "tags": ["Array"],                            "source": "TI150"},
    {"id": "228",  "title": "Summary Ranges",                                   "slug": "summary-ranges",                                         "difficulty": "Easy",   "tags": ["Array"],                            "source": "TI150"},
    {"id": "435",  "title": "Non-overlapping Intervals",                        "slug": "non-overlapping-intervals",                              "difficulty": "Medium", "tags": ["Array", "Greedy"],                  "source": "LC75"},
    {"id": "452",  "title": "Minimum Number of Arrows to Burst Balloons",       "slug": "minimum-number-of-arrows-to-burst-balloons",             "difficulty": "Medium", "tags": ["Array", "Greedy"],                  "source": "both"},
    # ── Monotonic Stack ─────────────────────────────────────────────────────────
    {"id": "739",  "title": "Daily Temperatures",                               "slug": "daily-temperatures",                                     "difficulty": "Medium", "tags": ["Stack", "Array"],                   "source": "both"},
    {"id": "901",  "title": "Online Stock Span",                                "slug": "online-stock-span",                                      "difficulty": "Medium", "tags": ["Stack", "Design"],                  "source": "LC75"},
    # ── Divide & Conquer ────────────────────────────────────────────────────────
    {"id": "148",  "title": "Sort List",                                        "slug": "sort-list",                                              "difficulty": "Medium", "tags": ["Linked List", "Divide & Conquer"],  "source": "TI150"},
    {"id": "427",  "title": "Construct Quad Tree",                              "slug": "construct-quad-tree",                                    "difficulty": "Medium", "tags": ["Tree", "Divide & Conquer"],         "source": "TI150"},
]

# 중복 id 제거 (dict 순서 유지)
seen = set()
PROBLEM_POOL = []
for p in PROBLEM_POOL_RAW:
    if p["id"] not in seen:
        seen.add(p["id"])
        PROBLEM_POOL.append(p)


# ── GitHub API 헬퍼 ──────────────────────────────────────────────────────────

def get_current_week_number():
    url = f"https://api.github.com/repos/{REPO}/commits?per_page=1&sha=main"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        try:
            last_link = resp.links.get("last", {}).get("url")
            if last_link:
                r2 = requests.get(last_link, headers=HEADERS)
                if r2.status_code == 200:
                    d = r2.json()[-1]["commit"]["committer"]["date"]
                    first_dt = datetime.fromisoformat(d.replace("Z", "+00:00"))
                    now = datetime.now(first_dt.tzinfo)
                    return max(1, (now - first_dt).days // 7 + 1)
        except Exception:
            pass
    return datetime.now().isocalendar()[1]


def get_used_problem_ids():
    """기존 PR 본문에서 이미 출제된 LeetCode slug → id 매핑으로 추출"""
    used = set()
    slug_to_id = {p["slug"]: p["id"] for p in PROBLEM_POOL}
    page = 1
    while True:
        resp = requests.get(
            f"https://api.github.com/repos/{REPO}/pulls?state=all&per_page=100&page={page}",
            headers=HEADERS,
        )
        if resp.status_code != 200 or not resp.json():
            break
        for pr in resp.json():
            body = pr.get("body", "") or ""
            for slug in re.findall(r"leetcode\.com/problems/([\w-]+)/", body):
                if slug in slug_to_id:
                    used.add(slug_to_id[slug])
        if "next" not in resp.links:
            break
        page += 1
    return used


def select_problems(used_ids):
    """유형 상관없이 Easy 2문제, Medium 2문제를 랜덤 선정"""
    available = [p for p in PROBLEM_POOL if p["id"] not in used_ids]
    if len(available) < NUM_PROBLEMS:
        print("⚠️  전체 풀 소진 — 초기화 후 재선정")
        available = list(PROBLEM_POOL)

    easy   = [p for p in available if p["difficulty"] == "Easy"]
    medium = [p for p in available if p["difficulty"] == "Medium"]

    selected = []
    # Easy 2문제 랜덤
    if len(easy) >= 2:    selected += random.sample(easy,   2)
    elif easy:            selected += easy
    # Medium 2문제 랜덤
    if len(medium) >= 2:  selected += random.sample(medium, 2)
    elif medium:          selected += medium

    # 풀이 부족한 경우 나머지로 채우기
    remaining = [p for p in available if p not in selected]
    while len(selected) < NUM_PROBLEMS and remaining:
        pick = random.choice(remaining)
        selected.append(pick)
        remaining.remove(pick)

    return selected[:NUM_PROBLEMS]


# ── 브랜치 / README / PR ────────────────────────────────────────────────────

def get_week_numbers_from_branches():
    """열려있는 브랜치에서 week* 번호 목록 반환"""
    weeks = []
    page = 1
    while True:
        resp = requests.get(
            f"https://api.github.com/repos/{REPO}/branches?per_page=100&page={page}",
            headers=HEADERS,
        )
        if resp.status_code != 200 or not resp.json():
            break
        for b in resp.json():
            m = re.match(r"week(\d+)$", b["name"])
            if m:
                weeks.append(int(m.group(1)))
        if "next" not in resp.links:
            break
        page += 1
    return weeks


def get_week_numbers_from_main():
    """main 브랜치의 codes/ 디렉토리에서 week* 번호 목록 반환"""
    weeks = []
    resp = requests.get(
        f"https://api.github.com/repos/{REPO}/contents/codes",
        headers=HEADERS,
    )
    if resp.status_code != 200:
        return weeks
    for item in resp.json():
        if item["type"] == "dir":
            m = re.match(r"week(\d+)$", item["name"])
            if m:
                weeks.append(int(m.group(1)))
    return weeks


def get_next_week_number():
    """
    1순위: 열려있는 브랜치의 week* 최댓값 + 1
    2순위: 없으면 main의 codes/week* 디렉토리 최댓값 + 1
    """
    weeks = get_week_numbers_from_branches()
    if not weeks:
        print("ℹ️  열린 week 브랜치 없음 → main 디렉토리에서 주차 감지")
        weeks = get_week_numbers_from_main()
    return max(weeks) + 1 if weeks else 14


def get_main_sha():
    resp = requests.get(
        f"https://api.github.com/repos/{REPO}/git/ref/heads/main",
        headers=HEADERS,
    )
    resp.raise_for_status()
    return resp.json()["object"]["sha"]


def branch_exists(branch):
    return requests.get(
        f"https://api.github.com/repos/{REPO}/git/ref/heads/{branch}",
        headers=HEADERS,
    ).status_code == 200


def create_branch(branch, sha):
    requests.post(
        f"https://api.github.com/repos/{REPO}/git/refs",
        headers=HEADERS,
        json={"ref": f"refs/heads/{branch}", "sha": sha},
    ).raise_for_status()


def get_file_sha(path, branch):
    resp = requests.get(
        f"https://api.github.com/repos/{REPO}/contents/{path}?ref={branch}",
        headers=HEADERS,
    )
    return resp.json().get("sha") if resp.status_code == 200 else None


def commit_readme(week, branch, problems):
    lines = [f"# {week}주차 알고리즘 문항\n"]
    for p in problems:
        lines.append(f"* [{p['title']}]({make_url(p['slug'])})")
    content = "\n".join(lines) + "\n"

    path = f"codes/week{week}/README.md"
    payload = {
        "message": f"chore: [Week {week}] README 추가",
        "content": base64.b64encode(content.encode()).decode(),
        "branch": branch,
    }
    existing_sha = get_file_sha(path, branch)
    if existing_sha:
        payload["sha"] = existing_sha
    requests.put(
        f"https://api.github.com/repos/{REPO}/contents/{path}",
        headers=HEADERS,
        json=payload,
    ).raise_for_status()
    return path


def pr_exists(head):
    resp = requests.get(
        f"https://api.github.com/repos/{REPO}/pulls?state=open&head={REPO.split('/')[0]}:{head}",
        headers=HEADERS,
    )
    return resp.status_code == 200 and len(resp.json()) > 0


def create_pr(week, branch, problems):
    rows = ""
    for i, p in enumerate(problems, 1):
        rows += f"| {i} | [{p['title']}]({make_url(p['slug'])}) |\n"

    body = f"""## {week}주차 알고리즘 스터디 문제

> 매주 일요일 스터디 전까지 풀이를 올려주세요! 🚀

### 📋 이번 주 문제 목록

| # | 문제 |
|---|------|
{rows}
### 📁 풀이 파일 경로

```
codes/week{week}/본인이름/문제제목.py (또는 .cpp, .c)
```

### ✅ 체크리스트

- [ ] 박정원
- [ ] 진현
- [ ] 최지원

---
*이 PR은 GitHub Actions에 의해 자동 생성되었습니다.*
"""

    resp = requests.post(
        f"https://api.github.com/repos/{REPO}/pulls",
        headers=HEADERS,
        json={
            "title": f"[Week {week}] 주차별 문제",
            "body": body,
            "head": branch,
            "base": "main",
        },
    )
    resp.raise_for_status()
    pr = resp.json()

    # Reviewer 지정 (pulls API)
    requests.post(
        f"https://api.github.com/repos/{REPO}/pulls/{pr['number']}/requested_reviewers",
        headers=HEADERS,
        json={"reviewers": REVIEWERS},
    )
    # Assignee 지정 (issues API — PR assignee는 이 엔드포인트로만 가능)
    requests.post(
        f"https://api.github.com/repos/{REPO}/issues/{pr['number']}/assignees",
        headers=HEADERS,
        json={"assignees": ASSIGNEES},
    )
    return pr


def main():
    print(f"📚 문제 풀 크기: {len(PROBLEM_POOL)}문제 (LC75 + TI150, Easy/Medium)")

    # ── 1. 주차 결정 ───────────────────────────────────────────────────────────
    week = get_next_week_number()
    branch = f"week{week}"
    print(f"📅 {week}주차 / 브랜치: {branch}")

    # ── 2. 중복 방지: 기존 PR에서 출제된 문제 조회 ────────────────────────────
    used_ids = get_used_problem_ids()
    print(f"📖 이미 출제된 문제: {len(used_ids)}개")

    # ── 3. 문제 선정 ───────────────────────────────────────────────────────────
    problems = select_problems(used_ids)
    print("🎲 선정된 문제:")
    for p in problems:
        print(f"   [{p['difficulty']:6s}] #{p['id']:4s} {p['title']} ({p['source']})")

    # ── 4. 브랜치 생성 ─────────────────────────────────────────────────────────
    if branch_exists(branch):
        print(f"⚠️  브랜치 이미 존재, 스킵")
    else:
        create_branch(branch, get_main_sha())
        print(f"✅ 브랜치 생성 완료")

    # ── 5. README 커밋 ─────────────────────────────────────────────────────────
    readme_path = commit_readme(week, branch, problems)
    print(f"📄 {readme_path} 커밋 완료")

    # ── 6. PR 생성 ─────────────────────────────────────────────────────────────
    if pr_exists(branch):
        print(f"⚠️  PR 이미 존재, 스킵")
    else:
        pr = create_pr(week, branch, problems)
        print(f"🚀 PR 생성 완료: {pr['html_url']}")

    print("\n🎉 전체 완료!")


if __name__ == "__main__":
    main()
