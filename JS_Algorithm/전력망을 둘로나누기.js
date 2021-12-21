function solution(n, wires) {
    const total = {};
    for (let i = 1; i <= n; i++) total[i] = []
    wires.forEach(([frm,to])=>{
        total[frm].push(to);
        total[to].push(frm);
    })
    const answer = [];
    wires.forEach(([frm,to])=>{
        total[frm] = total[frm].filter((end)=> end !== to);
        total[to] = total[to].filter((end)=> end !== frm);
        const visited = new Array(n).fill(false);
        const q = [];
        q.push(frm)
        let miniAnswer = 0
        
        while (q.length > 0){
            const now = q.shift();
            visited[now-1] = true;
            miniAnswer += 1;
            total[now].forEach((v)=>{
                if (visited[v-1] === false){
                    q.push(v)
                }
            })
        }
        
        answer.push(Math.abs((n-(miniAnswer)) - (miniAnswer)))
        
        total[frm].push(to)
        total[to].push(frm)
    })
    return answer.sort((a,b)=>a-b)[0]
}

console.log(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
console.log(solution(4,[[1,2],[2,3],[3,4]]))
console.log(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))