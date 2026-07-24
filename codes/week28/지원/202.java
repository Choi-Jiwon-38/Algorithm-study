class Solution {
    public boolean isHappy(int n) {
        Set<Integer> trace = new HashSet<>();

        while (true) {
            int sum = 0;

            while (n > 0) {
                int lastNum = n % 10;
                sum += lastNum * lastNum;
                n /= 10;
            }    
        
            if (sum == 1) {
                return true;
            }

            if (trace.contains(sum)) {
                return false;
            } else {
                trace.add(sum);
            }

            n = sum;
        }
    }
}
