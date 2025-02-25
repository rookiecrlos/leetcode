def areOccurrencesEqual(self, s: str) -> bool:
    hashMap = {}

    for c in s:
        if c in hashMap:
            hashMap[c] += 1
        else:
            hashMap[c] = 1

    return len(set(hashMap.values())) == 1
