import org.w3c.dom.Node;

public class Main {
    public static void main(String[] args) {
        ListNode Node5 = new ListNode(5, null);
        ListNode Node4 = new ListNode(4, Node5);
        ListNode Node3 = new ListNode(3, Node4);
        ListNode Node2 = new ListNode(2, Node3);
        ListNode Node1 = new ListNode(1, Node2);

        System.out.println(Node2.next.val);
        reverseLinkedList(Node1);
        System.out.println(Node2.next.val);
    }

    public static void reverseLinkedList(ListNode head) {
        ListNode oldPrevious = null, oldNext = null;

        while (head != null) {
            oldNext = head.next;
            head.next = oldPrevious;
            oldPrevious = head;
            head = oldNext;
        }
    }
}