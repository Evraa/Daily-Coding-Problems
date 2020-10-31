/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    // void print_all(Node* head){
    //     Node* ptr = head;
    //     while(ptr)
    //     {
    //         cout <<ptr->val<< " ";
    //         ptr = ptr->next;
    //     }
    //     cout <<"\n\n";
    // }
    Node* copyRandomList(Node* head) {
        if(!head)
            return head;
        Node* ptr = head;
        while (ptr){
            Node* tmp= new Node(ptr->val);
            tmp->next = ptr->next;
            ptr->next =tmp;
            ptr = tmp->next;
            
        }
        // print_all(head);
        ptr = head;
        Node* new_head = ptr->next;
        while(ptr){
            if (ptr->random){
                ptr->next->random = ptr->random->next;
            }
            ptr = ptr->next->next;
        }
        // print_all(head);
        // head->next = new_head->next;
        
        ptr = new_head;
        Node* ptr_2 = head;
        while(ptr->next){
            ptr_2->next = ptr_2->next->next;
            ptr->next = ptr->next->next;
            
            ptr = ptr->next;
            ptr_2 = ptr_2->next;
        }
        ptr_2->next = nullptr;
        return new_head;
    }
};