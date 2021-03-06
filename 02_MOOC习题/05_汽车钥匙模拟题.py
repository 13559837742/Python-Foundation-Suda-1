"""
模拟整个借还过程
• N个元素的数组表示钥匙盒状态
    • 元素值分别初始化成1-N
• 遍历K条借还记录
    • 借出-把保存该钥匙的元素置成0
    • 返还-把数组第1个为0的元素置成当前钥匙编号
• 顺序输出钥匙盒中的数组中的每个元素

两个注意事项：
1. 返还时刻=借用时刻+使用时间
2. K条记录不能保证有序返还和借用，需要排序
"""