class Solution {
    public int[] runningSum(int[] nums) {
        int size = nums.length;
        int[]sum = new int[size];

        for (int i=0; i<size; i++){
            int total = 0;
            for (int j = 0; j<=i ; j++){
                if(size == 1){
                    total = nums[i];
                    break;
                }
                total += nums[j];
            }
            sum[i] = total;
        }
        return sum;
    }
}