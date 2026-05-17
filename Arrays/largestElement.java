import java.util.*;

public class largestElement {

    static int largestBrute(int[] arr) {
        Arrays.sort(arr);

        return arr[arr.length - 1];
    }



    static int findLargest(int[] arr){
        
        int max = 0;

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > arr[max]) {
                max = i;
            }
        }

        return arr[max];
    }

    public static void main(String[] args) {
        int[] arr = { 8, 10, 5, 7, 9 };   
        System.out.println(findLargest(arr));
        System.out.println(largestBrute(arr));
    }
}