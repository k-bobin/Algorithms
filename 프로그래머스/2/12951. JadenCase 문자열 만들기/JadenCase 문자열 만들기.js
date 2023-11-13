function solution(s) {
    const answer = s.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase());
    return answer.join(' ');
}