class Solution {
    public List<String> summaryRanges(int[] nums) {
        int n = nums.length;
        ArrayList<String> answer = new ArrayList<>();
        
        if (n == 0) {
            return answer;     
        }

        if (n == 1) {
            answer.add(Integer.toString(nums[0]));
            return answer;
        }

        int startNum = nums[0];
        
        for (int i = 0; i < n - 1; i++) {
    
            if (nums[i] + 1 != nums[i + 1]) {
                if (startNum == nums[i]) {
                    answer.add(Integer.toString(startNum));
                    startNum = nums[i + 1];
                } else {
                    answer.add(Integer.toString(startNum) + "->" + Integer.toString(nums[i]));
                    startNum = nums[i + 1];
                }
            }

            if (i + 1 == n - 1) {
                if (startNum == nums[i + 1]) {
                    answer.add(Integer.toString(startNum));
                } else {
                    answer.add(Integer.toString(startNum) + "->" + Integer.toString(nums[i + 1]));
                }
            }
        }
        return answer;
    }
}