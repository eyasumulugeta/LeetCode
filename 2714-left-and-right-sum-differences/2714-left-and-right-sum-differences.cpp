class Solution {
    int array_size = 0;
    public:
        vector<int> leftRightDifference(vector<int>& nums) {
            array_size = nums.size();
            int* leftSum = new int[array_size];
            int* rightSum= new int[array_size];
            vector<int> answer(array_size);
        
            leftSum = calculateLeftSum(nums);
            rightSum = calculateRightSum(nums);
            
            for(int i = 0; i<array_size; i++)
            {
                answer[i] = (leftSum[i] - rightSum[i]) >= 0 ? (leftSum[i] - rightSum[i]) : -1*(leftSum[i] - rightSum[i]);
            }    
    return answer;    
        }

    int* calculateLeftSum(vector<int>& nums)
    {
        int sum = 0;
        int* leftSum = new int[array_size];
        
        for(int i = 0; i < array_size; i++)
        {
            sum = 0;
            for(int j = i; j >= 0; j --){
                if(j-1 >=0)
                {
                    sum+= nums[j-1];
                }
            }
            leftSum[i] = sum;   
        }
        return leftSum;
    }

    int* calculateRightSum(vector<int>& nums)
    {
        int sum = 0;
        int* rightSum = new int[array_size];
        
        for(int i = 0; i < array_size; i++)
        {
            sum = 0;
            for(int j = i; j < array_size; j ++){
                if(j+1 < array_size)
                {
                    sum+= nums[j+1];
                }
            }
            rightSum[i] = sum;   
        }
        return rightSum;
    }
};