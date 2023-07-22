// VLR -> Pre-order Traversal -> root-left-right

import java.util.*;

public class Main {
    public static void main(String[] args) {
        TreeNode Node4 = new TreeNode(4, null, null);
        TreeNode Node5 = new TreeNode(5, null, null);
        TreeNode Node6 = new TreeNode(6, null, null);
        TreeNode Node7 = new TreeNode(7, null, null);

        TreeNode Node2 = new TreeNode(2, Node4, Node5);
        TreeNode Node3 = new TreeNode(3, Node6, Node7);

        TreeNode Node1 = new TreeNode(1, Node2, Node3);

        preorderTraversal(Node1);
    }

    // conduct the breath-first traversal to imply the pre-order traversal
    public static void preorderTraversal(TreeNode head) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(head);

        while (!queue.isEmpty()) {
            TreeNode current = queue.poll();
            System.out.println(current.val);

            if (current.left != null) {
                queue.add(current.left);
            }

            if (current.right != null) {
                queue.add(current.right);
            }
        }
    }
}