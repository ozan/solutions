
def count(text, pattern):
    count = 0
    for i in range(len(text)):
        for j in range(len(pattern)):
            if i + j >= len(text) or text[i+j] != pattern[j]:
                break
        else:
            count += 1
    return count


assert count('GCGCG', 'GCG') == 2
assert count('CGATATATCCATAG', 'ATA') == 3
print('ok')
