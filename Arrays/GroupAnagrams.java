import java.util.*;

public class GroupAnagrams {

    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            char[] charArray = str.toCharArray();

            Arrays.sort(charArray);
            String key = new String(charArray);

            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            ;

            map.get(key).add(str);
        }

        return new ArrayList<>(map.values());
    }

    public static void main(String[] args) {
        GroupAnagrams solver = new GroupAnagrams();
        String[] input = { "eat", "tea", "tan", "ate", "nat", "bat" };
        System.out.println(solver.groupAnagrams(input));
    }
}