public class BuildArrayFromPermutation {

    static int[] bruteForceSolution (int[] nums) {

        int[] res = new int[nums.length];
        
        for (int i = 0; i < nums.length; i++) {
            res[i] = nums[nums[i]];
        }

        return res;

    }

    static int[] optimalSolution(int[] nums) {

        for (int i = 0; i < nums.length; i++) {
            nums[i] = nums[i] + nums.length * (nums[nums[i]] % nums.length);
        }

        for (int i = 0; i < nums.length; i++) {
            nums[i] = nums[i] / nums.length;
        }
        return nums;
    }
    public static void main(String[] args) {
        
        int[] nums = { 0,2,1,5,3,4 };

        // int[] res = bruteForceSolution(nums);

        int[] res = optimalSolution(nums);

        for (int e : res) {
            System.out.print(e + " ");
        }
    }
}
