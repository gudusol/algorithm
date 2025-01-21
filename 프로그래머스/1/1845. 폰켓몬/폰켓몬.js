function solution(nums) {
    const hashMap = {};
    nums.forEach((num) => {
        if(hashMap.hasOwnProperty(num)){
            hashMap[num] += 1;
        } else {
            hashMap[num] = 1;
        }
    })
    const maxLen = nums.length / 2
    const hashMapLen = Object.keys(hashMap).length;
    return hashMapLen >= maxLen ? maxLen : hashMapLen;
}