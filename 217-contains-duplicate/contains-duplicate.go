func containsDuplicate(nums []int) bool {
    hash := make(map[int]int)
        
    for _, val := range nums {
        if _, exist := hash[val]; exist {
            return true
        }
        hash[val] = 1
    }
    return false
}