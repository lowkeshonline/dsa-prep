public class InsertionSort {

    public static void insertionSort(int[] arr) {
        
        for (int i = 1; i < arr.length; i++) {
            int j = i;
            while( j > 0 && arr[j] < arr[j - 1]) {
                int temp = arr[j];
                arr[j] = arr[j - 1];
                arr[j - 1] = temp;
                j--;
            }
        }

        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
    

    public static void main(String[] args) {
        
        int [] arr = { 3, 5, 1, 2, 4};

        insertionSort(arr);
    }
}
