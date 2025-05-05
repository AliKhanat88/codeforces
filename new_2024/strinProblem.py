import sys
input = sys.stdin.readline

def solve(s):
    n = len(s)
    count = 0
    for i in range(len(s)):
        if s[i] != "a":
            count += 1
    
    if count == 0:
        print(n - 1)
        return n - 1

    
    dividers = []
    for i in range(1, count):
        if count % i == 0:
            dividers.append(i)
    before = 0
    after = 0
    for i in range(n):
        if s[i] == "a":
            before += 1
        else:
            break

    for i in range(n-1, -1, -1):
        if s[i] == "a":
            after += 1
        else:
            break
    
    if count == 1:
        print((before + 1) * (after + 1))
        return (before + 1) * (after + 1)
    # print(dividers)
    # print(before, after)
    ans = 0
    for num in dividers:
        temp_count = 0
        temp_stack = []
        for i in range(before, n - after):
            if s[i] == "a" and temp_count < num:
                temp_stack.append("a")
            elif s[i] != "a" and temp_count < num:
                temp_count += 1
                temp_stack.append(s[i])
            else:
                break
        mat = "".join(temp_stack)
        # print(mat)
        
        temp_before = before
        temp_after = after
        temp_mid = 9999999999999999999999999
        j = 0
        temp_count = 0
        first = True
        can = True
        for i in range(before, n - after):
            if j == 0 and s[i] == "a":
                temp_count += 1
                continue
            if j == 0 and s[i] != "a" and not first:
                temp_mid = min(temp_mid, temp_count)
                temp_count = 0
            if j == 0 and s[i] != "a" and first:
                first = False
            if mat[j] != s[i]:
                can = False
                break
            j = (j + 1) % len(mat)
        # print(can, num, mat, temp_before, temp_after)
        if can:
            if temp_mid >= temp_after:
                temp = min(temp_before, temp_mid - temp_after)
                ans = ans + (temp_after+1) * (temp+1)
                start_ar = min(temp_mid - temp, temp_after)
                last_term = max(0, start_ar - (temp_before - temp) + 1)
                # print(start_ar, last_term)
                ans += ((start_ar + last_term) * (start_ar - last_term + 1)) // 2
            else:
                start_ar = temp_mid + 1
                last_term = max(0, start_ar - temp_before)
                # print(start_ar, last_term, before, after)
                ans += ((start_ar + last_term) * (start_ar - last_term + 1)) // 2
    print(ans + (before+1) * (after + 1))
    return ans + (before+1) * (after + 1)

            

def count_valid_substrings(s):
    n = len(s)
    seti = set()
    
    # Iterate over all possible substrings t
    for start in range(n):
        for end in range(start + 1, n + 1):
            t = s[start:end]
            if t == "a":  # Skip "a" as t
                continue
            
            # Check if s can be partitioned into t and "a"
            i = 0
            has_t = False
            valid = True
            while i < n:
                if s[i:i+len(t)] == t:  # Match substring t
                    has_t = True
                    i += len(t)
                elif s[i] == "a":  # Match "a"
                    i += 1
                else:  # Invalid partition
                    valid = False
                    break
    
            # If valid partition and at least one t exists
            if valid and has_t:
                seti.add(s[start:end])
                # count += 1
    
    return len(seti)

# # # Example usage
# s = "aaaaaa"
# print(count_valid_substrings(s))  # Output the number of valid substrings t   

for t in range(int(input())):
    s = input().strip()
    solve(s)

from random import randint, choice
def checker(n):

    
    for i in range(10000000):
        s = []
        for j in range(n):
            s.append(chr(choice([ord("a"), randint(ord("a"), ord("z"))])))
        s = "".join(s)
        if solve(s) != count_valid_substrings(s):
            print("Found")
            print(s)
            print(solve(s))
            print(count_valid_substrings(s))
            break

# checker(10)


