#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sesiunea 27: Exerciții LeetCode Comentate în Python (Partea 1).

Modul axat pe implementarea și documentarea primelor 8 probleme LeetCode.
Complexitățile asimptotice sunt explicate în docstrings.
"""


class ListNode:
    """Definiție standard pentru un nod dintr-o listă simplu înlănțuită."""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def two_sum(nums, target):
    """Găsește indicii a două numere care adunate dau valoarea target.

    O(N) Timp, O(N) Spațiu.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def is_palindrome(x):
    """Verifică dacă un număr întreg este palindrom.

    O(N) Timp, O(N) Spațiu.
    """
    text_numar = str(x)
    return text_numar == text_numar[::-1]


def roman_to_int(s):
    """Convertește un șir de caractere romane în întreg.

    O(N) Timp, O(1) Spațiu.
    """
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    lungime = len(s)
    for i in range(lungime):
        if i + 1 < lungime and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total


def is_valid(s):
    """Verifică dacă parantezele din șir sunt închise corect.

    O(N) Timp, O(N) Spațiu (utilizează Stack).
    """
    stiva = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping:
            top_element = stiva.pop() if stiva else "#"
            if mapping[char] != top_element:
                return False
        else:
            stiva.append(char)
    return not stiva


def merge_two_lists(l1, l2):
    """Unește două liste înlănțuite sortate.

    O(N + M) Timp, O(1) Spațiu.
    """
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next


def remove_duplicates(nums):
    """Elimină duplicatele dintr-o listă sortată in-place.

    O(N) Timp, O(1) Spațiu.
    """
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


def max_profit(prices):
    """Calculează profitul maxim din acțiuni.

    O(N) Timp, O(1) Spațiu.
    """
    min_price = float("inf")
    profit_maxim = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > profit_maxim:
            profit_maxim = price - min_price
    return profit_maxim


def climb_stairs(n):
    """Calculează modurile unice de a urca o scară cu n trepte.

    O(N) Timp, O(1) Spațiu.
    """
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def max_sub_array(nums):
    """Găsește suma maximă a unui subtablou contiguu (Kadane).

    O(N) Timp, O(1) Spațiu.
    """
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global


def length_of_last_word(s):
    """Returnează lungimea ultimului cuvânt dintr-un șir text.

    O(N) Timp, O(N) Spațiu.
    """
    cuvinte = s.strip().split(" ")
    return len(cuvinte[-1])


def plus_one(digits):
    """Adăugă o unitate numărului reprezentat ca o listă de cifre.

    O(N) Timp, O(1) Spațiu.
    """
    for i in reversed(range(len(digits))):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


def move_zeroes(nums):
    """Mută toate elementele de 0 la sfârșitul listei in-place.

    O(N) Timp, O(1) Spațiu.
    """
    pozitie_curenta = 0
    for num in nums:
        if num != 0:
            nums[pozitie_curenta] = num
            pozitie_curenta += 1
    while pozitie_curenta < len(nums):
        nums[pozitie_curenta] = 0
        pozitie_curenta += 1


def fizz_buzz(n):
    """Returnează o listă de stringuri conform regulilor FizzBuzz.

    O(N) Timp, O(N) Spațiu.
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def is_anagram(s, t):
    """Verifică dacă două șiruri de caractere sunt anagrame.

    O(N log N) Timp, O(N) Spațiu.
    """
    return sorted(s) == sorted(t)


def binary_search(nums, target):
    """Caută un număr țintă într-o listă sortată binar.

    O(log N) Timp, O(1) Spațiu.
    """
    stanga, dreapta = 0, len(nums) - 1
    while stanga <= dreapta:
        mijloc = (stanga + dreapta) // 2
        if nums[mijloc] == target:
            return mijloc
        elif nums[mijloc] < target:
            stanga = mijloc + 1
        else:
            dreapta = mijloc - 1
    return -1


# ------------------------------------------------------------------
# BLOCUL PRINCIPAL DE TESTARE ȘI EXECUȚIE COMPLET
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Execuție Teste Algoritmice: Sesiunea 27 ===")

    # Test 1 - 4
    print("1. Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("2. Is Palindrome (121):", is_palindrome(121))
    print("3. Roman to Int ('IV'):", roman_to_int("IV"))
    print("4. Is Valid Parentheses ('()[]{}'):", is_valid("()[]{}"))

    # Test 5
    nod_a = ListNode(1, ListNode(3))
    nod_b = ListNode(2, ListNode(4))
    lista_unita = merge_two_lists(nod_a, nod_b)
    print("5. Merge Lists (Primul element unit):", lista_unita.val)

    # Test 6 - 11
    print("6. Remove Duplicates:", remove_duplicates([1, 1, 2]))
    print("7. Max Profit Stock:", max_profit([7, 1, 5, 3, 6, 4]))
    print("8. Climb Stairs (5 trepte):", climb_stairs(5))
    print("9. Max Subarray Sum:", max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("10. Length of Last Word:", length_of_last_word("Hello World"))
    print("11. Plus One ([9, 9]):", plus_one([9, 9]))

    # Test 12
    vector_zero = [0, 1, 0, 3, 12]
    move_zeroes(vector_zero)
    print("12. Move Zeroes:", vector_zero)

    # Test 13 - 15
    print("13. FizzBuzz (Primele 5 elemente):", fizz_buzz(5))
    print("14. Is Anagram:", is_anagram("anagram", "nagaram"))
    print("15. Binary Search (Indice pentru 4):", binary_search([1, 2, 3, 4, 5, 6], 4))
