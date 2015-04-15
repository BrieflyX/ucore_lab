Lab5 Report
# 裴中煜 2012010685

## 练习1

实现过程：设置trapframe的工作主要就是完成各个段寄存器的初始化，还有初始化进程使用的栈结构以及起始地址等上下文结构。将cs设置为USER_CS，ds,es,ss均设为USER_DS，使其拥有用户特权级。esp为用户栈的顶端，eip为程序的入口地址，eflags寄存器中打开中断位即可。

用户进程执行过程：当进程变为RUNNING态时，proc_run函数会载入进程的kstack和cr3页表，调用switch_to函数进行切换，在switch.S中调用汇编代码。这段代码会将进程当前执行到的eip压栈，然后用一条ret跳转到eip处执行。之前load_icode已经把eip设为了程序的entry处，且已经设置好了用户态的trapframe和对应的段寄存器。这样执行完ret以后跳到用户程序的入口地址执行，其就工作在用户态。

## 练习2

## 练习3
