// function solution(n, wires) {
//     const total = {};
//     for (let i = 1; i <= n; i++) total[i] = []
//     wires.forEach(([frm,to])=>{
//         total[frm].push(to);
//         total[to].push(frm);
//     })
//     const answer = [];
//     wires.forEach(([frm,to])=>{
//         total[frm] = total[frm].filter((end)=> end !== to);
//         total[to] = total[to].filter((end)=> end !== frm);
//         const visited = new Array(n).fill(false);
//         const q = [];
//         q.push(frm)
//         let miniAnswer = 0
        
//         while (q.length > 0){
//             const now = q.shift();
//             visited[now-1] = true;
//             miniAnswer += 1;
//             total[now].forEach((v)=>{
//                 if (visited[v-1] === false){
//                     q.push(v)
//                 }
//             })
//         }
        
//         answer.push(Math.abs((n-(miniAnswer)) - (miniAnswer)))
        
//         total[frm].push(to)
//         total[to].push(frm)
//     })
//     return answer.sort((a,b)=>a-b)[0]
// }

// console.log(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
// console.log(solution(4,[[1,2],[2,3],[3,4]]))
// console.log(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))


// const getDistance = (nowNumber, targetNumber) => {
//     const position = [
//         [3,1],
//         [0,0], [0,1], [0,2],
//         [1,0], [1,1], [1,2],
//         [2,0], [2,1], [2,2],
//         [3,0], [3,2]
//     ];
//     const [targetX,targetY] = position[targetNumber];
//     const [nowX,nowY] = position[nowNumber];
    
//     return Math.abs(nowX - targetX) + Math.abs(nowY - targetY);
// }

// function solution(numbers, hand) {
//     const left = [1,4,7];
//     const right = [3,6,9];
//     let leftposition = 10;
//     let rightposition = 11;
//     let answer = '';
    
//     numbers.forEach((number) => {
//         if (left.includes(number)) {
//             answer += 'L';
//             leftposition = number;
//         } else if (right.includes(number)) {
//             answer += 'R';
//             rightposition = number;
//         } else {
//             const a = getDistance(leftposition, number);
//             const b = getDistance(rightposition, number);
//             if (a > b) {
//                 answer += 'R'
//                 rightposition = number;
//             } else if (a < b) {
//                 answer += 'L'
//                 leftposition = number;
//             } else {
//                 if (hand === 'left') {
//                     answer += 'L'
//                     leftposition = number;
//                 } else {
//                     answer += 'R'
//                     rightposition = number;
//                 }
//             }
//         }
        
        
//     })
//     return answer;
// }

// function solution(participant, completion) {
//     const now = {};
//     let answer = '';
//     participant.forEach((v) => {
//         if (now[v] === undefined){
//             now[v] = 1
//         } else {
//             now[v] += 1
//         }
//     })
//     completion.forEach((v) => {
//         now[v] -= 1
//     })
    
//     Object.keys(now).forEach((v) => {
//         if (now[v] !== 0){
//             answer = v 
//         }
//     })
//     return answer;
// }

// function solution(strings, n) {
//     const total = {};
//     strings.forEach((string) => {
//         if (total[string[n]]) {
//             total[string[n]].push(string)
//         }else {
//             total[string[n]] = [string]
//         }
//     })
//     let answer = []
//     Object.keys(total).sort().forEach((key) => answer = [...answer, ...total[key].sort()])
//     return answer;
// }


// function solution(a, b) {
//     let answer = 0
//     a.forEach((v,i) => {
//         answer += v * b[i]
//     })
//     return answer;
// }

// function solution(s){
//     let count = 0;
//     s.toUpperCase().split('').forEach((v) => {
//         if (v === 'P') count += 1;
//         else if (v === 'Y') count -= 1;
//     })
//     return !!!count;
// }

// function solution(seoul) {
//     return `김서방은 ${seoul.findIndex((v) => v.includes('Kim'))}에 있다`
// }

// function solution(n) {
//     let answer = '';
//     new Array(n).fill(0).forEach((v,i) => {
//       if ((i+1) % 2 === 0)  {
//           answer += '박'
//       } else {
//           answer += '수'
//       }
//     })
//     return answer;
// }

// function solution(arr1, arr2) {
//     const answer = [];
//     arr1.forEach((v,i) => {
//         const a = []
//         v.forEach((V,I) => {
//             a.push(V + arr2[i][I])
//         })
//         answer.push(a)
//     })
//     return answer;
// }

// function isThereZero(obj){
//     if (Object.values(obj).includes(0)) return true;
//     return false;
// }

// function solution(n) {
//     for (let i = 1; i <= n; i++) {
//         if (n % i === 1) {
//             return i
//         }
//     }
// }

// const isNaNInS = (s) => s.split('').find((v) => isNaN(parseInt(v)))

// function solution(s) {
//     if (s.length !== 4 && s.length !== 6) {
//         return false;
//     } else {
//         if (isNaNInS(s)) {
//             return false
//         } else {
//             return true
//         }
//     }
// }

// function solution(s) {
//     return parseInt(s)
// }