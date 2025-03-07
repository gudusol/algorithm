function solution(distance, rocks, n) {
    const rocksArr = rocks.sort((a, b) => a - b);
    rocksArr.push(distance);

    let lo = 0;
    let hi = distance;
    
    while (lo <= hi) {
        let mid = Math.round((lo + hi) / 2);
        let remove = 0;
        let cur = 0;

        for (let rock of rocksArr) {
            if (rock - cur < mid) {
                remove += 1;
            } else {
                cur = rock;
            }
        }
        
        if (n < remove) {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return hi;
}