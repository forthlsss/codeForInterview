#### 题目
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
#### 题解
 1. 把复制的结点链接在原始链表的每一对应结点后面
![image](https://uploadfiles.nowcoder.com/images/20160726/737942_1469488971641_84B136C6E4052690517046794A4F80B0)
 2. 把复制的结点的random指针指向被复制结点的random指针的下一个结点
![image](https://uploadfiles.nowcoder.com/images/20160726/737942_1469488996797_F052D5F977FA4E843FE926BA3200084A)
3. 拆分成两个链表，奇数位置为原链表，偶数位置为复制链表，注意复制链表的最后一个结点的next指针不能跟原链表指向同一个空结点None，next指针要重新赋值None(判定程序会认定你没有完成复制）
![image](https://uploadfiles.nowcoder.com/images/20160726/737942_1469489231960_95E2453212A43966E21F1ABC09A80999)
