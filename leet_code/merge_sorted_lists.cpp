/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* p0 = nullptr;
        ListNode* p1 = l1;
        ListNode* p2 = l2;
        ListNode* head;
        
        if (!p1)
            return p2;
        if (!p2)
            return p1;
        //we know we have both heads
        if (p1->val < p2->val){
            head = p1;
            p0 = p1;
            p1 = p1->next;
        }else{
            head = p2;
            p0 = p2;
            p2 = p2->next;
        }
        
        while (p1 and p2){
            
            if (p1->val < p2->val){
                p0->next = p1;
                p0 = p1;
                p1 = p1->next;
                
            }else{
                p0->next = p2;
                p0 = p2;
                p2 = p2->next;
            }
        }
        if (!p1)
            p0->next = p2;
        
        if (!p2)
            p0->next = p1;
        return head;
    }
};