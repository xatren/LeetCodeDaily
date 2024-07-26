/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int GoodNodes(TreeNode root) {
        int CountGoodNodes(TreeNode node, int maxSoFar) {
            if (node == null) return 0;
            
            int goodNodeCount = 0;
            if (node.val >= maxSoFar) {
                goodNodeCount = 1;
            }
            
            int newMaxSoFar = Math.Max(maxSoFar, node.val);
            
            goodNodeCount += CountGoodNodes(node.left, newMaxSoFar);
            goodNodeCount += CountGoodNodes(node.right, newMaxSoFar);
            
            return goodNodeCount;
        }
        
        return CountGoodNodes(root, root.val);
    }
}
