import java.util.Scanner;

public class RunningSumOfArray {


    // 1480. Running Sum of 1d Array

    public static int[] solve (int[] arr) {

        //Traverse the array

        // Start from Index 1 because we are accessing i'th previous element which will cause ArrayOutOfBound exc if we start from 0

        for (int i = 1; i < arr.length; i++) {

            // For every i. i = itself + it's previous element
            arr[i] = arr[i] + arr[i - 1];
        }

        return arr;
    } 

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[5];

        solve(arr);
    }
}
