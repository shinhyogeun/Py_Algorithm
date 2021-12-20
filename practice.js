function isThereZero(obj){
    if (Object.values(obj).includes(0)) return true;
    return false;
}

function solution(gems) {
    const target = {};
    const newz = new Set();
    let answers = [];
    let start = 0;
    let end = -1;
    const a = new Set(gems)
    for (const c of a){
        target[c] = 0
    }
    for (const c of gems){
        if (a.size === newz.size) break;
        end += 1;
        target[c] += 1;
        newz.add(c)
    }
    answers.push([start,end])
    while (end !== gems.length){
        
        while (true){
            target[gems[start]] -= 1
            start += 1
            if (target[gems[start-1]] === 0) break
        }
        answers.push([start-1,end])
        while (end < gems.length) {
            end += 1
            target[gems[end]] += 1
            if (target[gems[end]] === 1) break
        }
    }
    answers = answers.sort((a,b)=>{
        if (a[1] - a[0] - (b[1] - b[0]) !== 0) return a[1] - a[0] - (b[1] - b[0])
        else {
            return a[0] - b[0]
        }
    })
    return [answers[0][0]+1,answers[0][1]+1];
}

// console.log(solution(["A","A","A","B","B"]))
// console.log(solution(["A"]))
// console.log(solution(["A","B","B","B","B","B","B","C","B","A"]))
console.log(solution(["XYZ", "XYZ", "XYZ"]))
console.log(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
console.log(solution(["AA", "AB", "AC", "AA", "AC"]))