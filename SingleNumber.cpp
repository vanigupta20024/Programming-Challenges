// Given a non-empty array of integers, every element appears 
// twice except for one. Find that single one.
// Example 1:
//    Input: [4,1,2,1,2]
//    Output: 4

// Level - Easy
// Easiest Approch:

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int x=0;
        
        /* 
            XOR is basically subtraction:
            7 ^ 7 = 0
            7 ^ 5 = 2 and so on..
            Also,
            any number when XORed with 0, returns itself. So we populate the
            integer x with first number and perform XOR will numbers.
            The remaining number will be the one that does not cancel itself.
        */
        
        for(int i=0;i<nums.size();i++){
            x ^= nums[i];
        }
        return x;
    }
};
