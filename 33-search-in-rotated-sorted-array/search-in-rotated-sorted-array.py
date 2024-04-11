class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # def binary_search(arr, low, high, x):
        #     if high >= low:
        #         mid = (high + low) // 2
        #         if arr[mid] == x:
        #             return mid
        #         elif arr[mid]>x:
        #             if arr[low]>arr[high]:
        #                 if arr[low]<=x:
        #                     return binary_search(arr,low,mid-1,x)
        #                 else:
        #                     return binary_search(arr,mid+1,high,x)
        #             else:
        #                 return binary_search(arr,low,mid-1,x)
        #         else:
        #             if arr[low]>arr[high]:
        #                 if arr[high]>=x:
        #                     return binary_search(arr,mid+1,high,x)
        #                 else:
        #                     return binary_search(arr,low,mid-1,x)
        #             else:
        #                 return binary_search(arr,mid+1,high,x)
        #     else:
        #         return -1
        # return binary_search(nums, 0, len(nums)-1, target)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1