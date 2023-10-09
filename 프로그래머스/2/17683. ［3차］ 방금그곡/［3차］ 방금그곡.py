def solution(m, musicinfos):
    answer = []
    
    def convert_mins(s, e):
        sh, sm = map(int, s.split(':'))
        eh, em = map(int, e.split(':'))
        return (eh * 60 + em) - (sh * 60 + sm)
    
    def shap(s):
        s = s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        return s
    
    m = shap(m)
    
    for idx, i in enumerate(musicinfos):
        stimes, etimes, name, melody = i.split(',')
        durations = convert_mins(stimes, etimes)
        
        # 악보를 재생 시간에 맞게 반복
        melody = shap(melody)
        new_m = shap(m)
        
        fullmelody = melody * (durations // len(melody)) + melody[:durations%len(melody)]
        
        if new_m in fullmelody:
            answer.append([name, durations, idx])
        
    if not len(answer):
        return '(None)'
    else:
        answer.sort(key=lambda x: (-x[1], x[2]))
        return answer[0][0]
