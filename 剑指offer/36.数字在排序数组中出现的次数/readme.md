#### 题目
统计一个数字在排序数组中出现的次数。
#### 思路
确实是单纯的统计一个数字出现的次数,那可以遍历统计,不过就没啥意思了,所以考察的应该是查找,所以可以\
整体用二分法，找到头和尾。\
因为data中都是整数，所以可以稍微变一下，不是搜索k的两个位置，而是搜索k-0.5和k+0.5\
这两个数应该插入的位置，然后相减即可。
#### 代码1
由于数组是排序数组，而且都是整数。因此不用查找k的左右位置，只需要找到k-0.5和k+0.5的插入位置，然后左右相减即可。既然是排序数组，那么就可以用二分法查找。
#### 代码2
直接找k出现的最左边，和最右边的位置，然后相减。仍然是二分查找k
