public class CyclicSort {

    public static void cyclicSort(int[] arr) { 

        int i = 0;

        while(i < arr.length) {
            int index = arr[i] - 1;
    
            if (arr[index] != arr[i]) {
                int temp = arr[index];
                arr[index] = arr[i];
                arr[i] = temp;
            } else {
                i++;
            }
        }
        

        for (int e : arr) {
            System.out.print(e + " ");
        }
    }
    
    public static void main(String[] args) {
        int [] arr = { 3, 5, 2, 1, 4};

        cyclicSort(arr);
    }
}
