import java.util.Scanner;
class Solution {

  public static List<List<Integer>> combine(int n, int k) {
    List<List<Integer>> result = new ArrayList<>();
    exploreCombinations(n, k, 1, new ArrayList<Integer>(), result);
    return result;
  }

  private static void exploreCombinations(int n, int k, int offset,
                                          List<Integer> snippet,
                                          List<List<Integer>> result) {
        if (snippet.size() == k) {
        result.add(new ArrayList<>(snippet));
        return;
    }
    final int spaceLeftInSnippet = k - snippet.size();
    for (int i = offset; i <= n && spaceLeftInSnippet <= n - i + 1 ; ++i) {
        snippet.add(i);
        exploreCombinations(n, k, i + 1, snippet , result);
        snippet.remove(snippet.size() - 1);
    }
  }

  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int k=sc.nextInt();
    combine(n,k);
  }
}
