import java.lang.*;
import java.util.*;
class Solution {
    static boolean flag;
    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];
        int idx = 0;
        for(long num : numbers){
            String binary = Long.toBinaryString(num);
            int digit = 1;
            while(true){
                if(Math.pow(2, digit) - 1 >= binary.length()){
                    break;
                }
                digit++;
            }
            long pohawLen = (long)Math.pow(2, digit) - 1;
            while(pohawLen > binary.length()){
                binary = "0" + binary;
            }
            flag = true;
            check(binary);
            if(flag){
                answer[idx] = 1;
            }
            answer[idx] = flag ? 1 : 0;
            idx+=1;
        }
        return answer;
    }
    public static void check(String binary){
        if(!flag){
            return;
        }
        int mid = binary.length() / 2;
        if(binary.length() == 1){
            return;
        }
        if(binary.charAt(mid) == '0'){
            char[] list = binary.toCharArray();
            for(char c : list){
                if(c == '1'){
                    flag = false;
                    return;
                }
            }
        }
        if(binary.length() >= 3){
            check(binary.substring(0, mid));
            check(binary.substring(mid + 1));
        }
    }
}