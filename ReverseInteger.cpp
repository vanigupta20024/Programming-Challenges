class Solution {
public:
    int reverse(long int x) {
        
        // if already 0, return
        if(x == 0) return x;
        int sign=0;
        
        // to store sign of input integer
        if(x < 0){
            sign=1;
            x = -x;
        }
        
        // to count trailing zeros
        // which can be discarded on reversing
        if(x % 10 == 0){
            while((x % 10) == 0){
                x /= 10;
            }
        }
        
        long long int num=0,x1=x;
        
        // taking a number from end and
        // adding new integers from back
        while(x1 > 0){
            num = (num*10)+(x1 % 10);
            x1 /= 10;
        }
        
        // Given conditions:
        //  integer range: [−2^31,  2^(31 − 1)]
        if(num > INT_MAX) return 0;
        if(num < INT_MIN) return 0;
        
        if(sign == 1) num = -num;
        
        return num;
    }
};
