// function solution(n, record) {
//     let server = new Array(n);
//     for (var i = 0; i < server.length; i++) {
//         server[i] = new Array(5);
//     }

//     record.map((item) => {
//         [serverNumber, nickName] = item.split(" ");

//         if (server[Number(serverNumber) - 1].includes(nickName)) {
//             return
//         }

//         if (server[Number(serverNumber) - 1].length === 5) {
//             server[Number(serverNumber) - 1].shift();
//             server[Number(serverNumber) - 1].push(nickName);
//         } else {
//             server[Number(serverNumber) - 1].push(nickName);
//         }
//     })
//     var answer = server.flat();
//     return answer;
// }

// solution(4, ["1 a", "1 b", "1 abc", "3 b", "3 a", "1 abcd", "1 abc", "1 aaa", "1 a", "1 z", "1 q", "3 k", "3 q", "3 z", "3 m", "3 b"])

// function solution(m, v) {
//     let tetris = [v[0]];

//     v.map((item, index) => {
//         if (index === 0) {
//             return;
//         }

//         //거꾸로 검사한다
//         let tetrisLength = tetris.length
//         for (let i = (tetrisLength - 1); i >= 0; i--) {
//             let space = m - tetris[i]

//             // 공간이 없어서 어딘가에 두어야 한다.
//             if (space < item) {
//                 if (i === tetrisLength - 1) {
//                     tetris[i + 1] = item;
//                 } else {
//                     tetris[i + 1] += item;
//                 }
//                 break;
//             }

//             // 계속 공간이 있으면!!?
//             if (i === 0) {
//                 tetris[0] += item
//             }
//         }
//     });
//     var answer = tetris.length;
//     return answer;
// }

solution(4, [2, 3, 1])