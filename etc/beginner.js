var ex = [1, 2, 3, 4];
//  1. 순서대로 출력한다.
console.log('1. 순서대로 출력 :', ex);
// 2. 역순으로 출력한 다.
console.log('2. 역순으로 출력 : ', ex.reverse());
// 3. 순서대로 출력한다.
var ex = [[1, 2, 3], [4, 5, 6]];
console.log('3. 순서대로 출력 : ', ex.flat(1));
// 4. 순서대로 출력한다.
var ex = [[1], [2, 3], [4, 5, 6]];
console.log('4. 순서대로 출력 :', ex.flat(3));
// 5. 짝수만 탐색하여 출력한다.(if 사용x)
var ex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var ans = [];
for(var i =1; i< ex.length; i+=2){
    ans.push(ex[i])
};

console.log('5. 짝수 탐색 : ', ans);
// 6. 모두 탐색하되 짝수인지 확인하여 출력한다.(if 사용)
for (a of ex)
{if(a%2 ==0 ){
    console.log(a)
}
};
for(var i = 0 ; i < ex.length ;i ++){
    if(arr[i] %2 ==0){
        console.log(arr[i])
    }
}
// 7. 구구단의 모든 경우의 수를 출력한다.
for(var i = 1 ;i < 10;i ++){
    for(var j =1; j<10;j++){
        console.log(i + "*" +j + "=" + i+j )
    }
}
// 8. 행렬 합을 구한다.
var n = [[1, 2], [3, 4]]
var m = [[5, 6], [7, 8]]
function ans(A,B){
    return A.map((a,i) => a.map((b, j) => b + B[i][j]));
  }
var result = [[0, 0], [0, 0]]


// 9. 행렬 곱을 구한다.
var n = [[1, 2, 3], [4, 5, 6]]
var m = [[1, 2], [3, 4], [5, 6]]
var result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]