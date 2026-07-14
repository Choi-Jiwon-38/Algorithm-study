class Solution {
    public int search(int[] nums, int target) {
        int s = 0;
        int e = nums.length - 1;
        int m = (s + e) / 2;

        if (nums[s] == target) {
            return s;
        } else if (nums[e] == target) {
            return e;
        } else if (nums[m] == target) {
            return m;
        }

        while (s != m && m != e) {
            if (nums[m] == target) {
                return m;
            }
            if ((nums[s] <= nums[m] && nums[s] <= target && target <= nums[m]) || (nums[m] <= nums[s] && (nums[s] <= target || target <= nums[m]))) {
                e = m;
                m = (s + e) / 2;
            } else {
                s = m;
                m = (s + e) / 2;
            }
        }

        return -1;
    }
}