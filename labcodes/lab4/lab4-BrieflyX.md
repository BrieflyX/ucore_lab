# Lab4 Report
# 裴中煜 2012010685

## 练习1

context 用于保存程序运行的上下文，其中的成员变量是8个寄存器的值，用于进程切换时保存与回复现场。

tf这个trapframe结构表示进程的中断帧结构，本实验中在创建init_main函数的内核线程时初始化了它的中断帧，记录了内核的代码段与数据段等参数，指定了线程运行的入口地址。

## 练习2

是的，ucore可以保证每个进程的pid唯一。在proc.c中定义了MAX_PROCESS与MAX_PID宏，而MAX_PID是MAX_PROCESS的2倍，在get_pid函数中，每次遍历整个进程链表确保每个现有进程的pid与选中的last_pid不同。另外将MAX_PID设为MAX_PROCESS的2倍，且将next_safe和last_pid作为静态变量记录上次pid的分配状态都可以加速这个唯一性寻找的过程。

## 练习3

1.2个内核线程，idleproc与initproc.

2.这2条语句用于关闭中断和恢复中断，在lab4中，ucore在向终端输出字符、分配物理页帧、释放页、进程调度时都会先关闭终端，操作完成后再开启中断。
