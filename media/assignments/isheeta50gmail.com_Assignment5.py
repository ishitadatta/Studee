var countBits = function(n) {
    const res = []
    let index = 0 
    while (index <= n){
        let temp = count1s(index)
        res.push(temp)
        index++
    }
    return res
};
const count1s = function(n){
    let res = 0
    while (n > 0){
        res += (1&n)
        n >>= 1
    }
    return res
}