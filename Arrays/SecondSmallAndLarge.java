import java.util.*;

public class SecondSmallAndLarge {

    static int[] findSecondSmallLarge(int[] nums) {
        if(nums.length < 2) {
            return new int[] {-1};
        }

        Arrays.sort(nums);

        return new int[] {nums[1], nums[nums.length - 2]};
    }

    public static void main(String[] args) {
        int[] nums = {1,2,2};

        int[] result = findSecondSmallLarge(nums);

        for (int e : result) {
            System.out.print( e + " ");
        }
    }
}
