#3:03 -> 42
def solution(gems):
    gem_set = set(gems)
    gem_count = len(gem_set)
    gem_freq = {}
    min_len = float('inf')
    answer = []

    left, right = 0, 0

    while right < len(gems):
        if gems[right] in gem_freq:
            gem_freq[gems[right]] += 1
        else:
            gem_freq[gems[right]] = 1

        while len(gem_freq) == gem_count:
            if right - left < min_len:
                min_len = right - left
                answer = [left + 1, right + 1]

            if gems[left] in gem_freq:
                gem_freq[gems[left]] -= 1
                if gem_freq[gems[left]] == 0:
                    del gem_freq[gems[left]]
            left += 1

        right += 1

    return answer

        
            
        
        
        
    
    

        
