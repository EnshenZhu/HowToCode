// Write a function named as the find_sum(),
// which takes the root as the input and return the sum of the tree
public class Main {

    public static class Node {
        int data;
        Node left;
        Node right;

        Node(int inputData) {
            this.data = inputData;
        }
    }

    public static int find_sum(Node root) {
        if (root == null) {
            return 0;
        } else {
            return root.data + find_sum(root.left) + find_sum(root.right);
        }
    }

    public static void main(String[] args) {
        // Our example tree looks like this:
        //         2
        //       /   \
        //      3     4
        //     / \   / \
        //    5   6 7   8

        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        Node node6 = new Node(6);
        Node node7 = new Node(7);
        Node node8 = new Node(8);

        node2.left = node3;
        node2.right = node4;

        node3.left = node5;
        node3.right = node6;

        node4.left = node7;
        node4.right = node8;

        System.out.println("Sum of all values of this tree is (should print 35):");
        System.out.println(find_sum(node2));

        System.out.println("Sum of all values of this tree (start from node 3) is (should print 14):");
        System.out.println(find_sum(node3));

        System.out.println("Sum of all values of this tree (start from node 4) is (should print 19):");
        System.out.println(find_sum(node4));
    }
}