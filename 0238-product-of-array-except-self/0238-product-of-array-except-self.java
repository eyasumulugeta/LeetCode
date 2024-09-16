class Solution {
    public int[] productExceptSelf(int[] nums) {
        int size = nums.length;
        int[] product = new int[size];
        
        // Calculating the prefix product
        product[0] = 1;
        for(int i = 1; i < size; i++){
            product[i] = product[i - 1] * nums[i - 1];
        }

        // Calculating the suffix product and the final product of prefix and suffix
        int suffixProduct = 1;
        for(int i = size - 1; i >= 0; i--){
            product[i] *= suffixProduct;
            suffixProduct *= nums[i];
        }
        return product;
    }
}