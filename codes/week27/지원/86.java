/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode node = head;

        ListNode head1 = null;
        ListNode tail1 = null;
        ListNode head2 = null;
        ListNode tail2 = null;

        while (node != null) {
            if (node.val < x) {
                if (head1 == null) {
                    head1 = node;
                    tail1 = node;
                } else {
                    tail1.next = node;
                    tail1 = node;
                }
            } else {
                if (head2 == null) {
                    head2 = node;
                    tail2 = node;
                } else {
                    tail2.next = node;
                    tail2 = node;
                }
            }

            // 연결이 유지된 복사본 할당
            ListNode next = node.next;

            // 연결 끊기 <- tail1, tail2에 할당될때 순환 구조가 유지될 수 있기 때문
            node.next = null;

            node = next;
        }

        if (tail1 == null) {
            return head2;
        } else {
            tail1.next = head2;
        }

        return head1;
    }
}