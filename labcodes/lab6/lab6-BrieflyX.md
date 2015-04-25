# lab6 Report
# 裴中煜 2012010685

## 练习1

1. sched_class与RR调度算法

sched_class定义如下
```
struct sched_class {
    // the name of sched_class
    const char *name;
    // Init the run queue
    void (*init)(struct run_queue *rq);
    // put the proc into runqueue, and this function must be called with rq_lock
    void (*enqueue)(struct run_queue *rq, struct proc_struct *proc);
    // get the proc out runqueue, and this function must be called with rq_lock
    void (*dequeue)(struct run_queue *rq, struct proc_struct *proc);
    // choose the next runnable task
    struct proc_struct *(*pick_next)(struct run_queue *rq);
    // dealer of the time-tick
    void (*proc_tick)(struct run_queue *rq, struct proc_struct *proc);
};
```
可以看出，init函数为初始化进程运行队列，可在sched_init中调用。enqueue将进程放入运行队列中，在进程的need_resched=1时调用，进程放弃时间片进入等待下一次调度。dequeue将进程移出队列，进程将马上被执行。pick_next用于选取下一个执行的进程，在schedule函数中调用，与具体算法有关。proc_tick函数在每个clock tick调用，用于为进程计时，以便于及时知道进程的时间片用完。

RR调度算法的实现比较简单，在进程进入队列时的enqueue操作中，为每个进程设置time_slice，在进程运行时proc_tick函数中会不断递减time_slice的值，当其值减为0时，则将need_resched置为1，这样在schedule函数中该进程就会被收回CPU使用权，进入run_list队列的尾部。然后pick_next选择下一个进程。选择进程时仅仅将队列中最前面的进程弹出即可，队列的选择方式与FIFO一样。

2. 多级反馈队列调度算法设计

需要多个队列来支持MLFQ算法，这些队列可以用一个总的链表管理queue_list，链表的每一个元素都是某一个队列的头指针即另一个链表的头部，链表的顺序就是队列优先级的顺序。每次挑选进程时遍历链表，从高优先级到低优先级查看队列中是否存在进程，如果有进程就执行，并记录下进程所处的队列指针。在进程用完固定的时间片后如果还没有结束，就将进程放置到下一级队列的尾部，由于每级队列的时间片大小不同，此时赋予进程的time_slice的值也是不同的，这可以在队列结构中增加一个元素来指定。

## 练习2

在有了优先队列结构的支持下，stride调度算法的实现也并不困难。重写sched_class中相应的函数即可。

stride_init:初始化运行队列，将专用的lab6_run_pool设置好。

stride_enqueue:将进程的lab6_run_pool插入队列中，使用优先队列的接口。同时检查进程的时间片使用情况。

stride_dequeue:将进程移出优先队列。

stride_pick_next:由于优先队列的结构特性，可以直接从头部取出stride值最小的进程，同时更新stride的值，加上的pass值为BIG_STRIDE / priority。

stride_proc_tick:与RR的设计相同。

关于32位无符号整数溢出导致stride判断不准的问题，实验指导书中已经给出了解决方案。在代码中，将BIG_STRIDE设置为0x7FFFFFFF，这样stride的差一定在BIG_STRIDE的范围内，而在比较stride的代码中
```
int32_t c = p->lab6_stride - q->lab6_stride;
if (c > 0) return 1;
else if (c == 0) return 0;
else return -1;
```
这里的c是32位的有符号数，也就是说如果2个stride的差值大于BIG_STRIDE的0x7FFFFFFF时，c就会变为负数，这个时候就说明有个stride的数值已经发生了溢出，但是这样也能被正确地识别出来。

## 与参考答案的不同

这次的代码有些地方存在一定的问题，可能是之前实验的代码问题，也许是实验框架自身的设计问题。

首先是trap.c中，注释给出的处理时间中断的地方需要更新
```
...
/* LAB6 YOUR CODE */
/* you should upate you lab5 code
 * IMPORTANT FUNCTIONS:
 * sched_class_proc_tick
 */
ticks ++;
...
```
再看sched.c中的定义
```
static void
sched_class_proc_tick(struct proc_struct *proc) {
...
```
sched_class_proc_tick函数是一个静态函数，C中的静态函数只能在本文件(sched.c)中使用，而trap.c中却让我们调用这是行不通的。而且答案中并没有调用这个函数，甚至lab5中的代码也被删除了。

然后是对nr_process全局变量的处理，之前的实验中在多个地方都对nr_process进行的修改，导致对这个变量的维护有一些混乱，后来查看答案后，明确只在set_links和remove_links中进行修改，否则在init_main的最后有一句assert(nr_process==2)就无法通过了。

## 实验中的知识点

实验中比较重要的地方就是调度的时机，这在代码中有很好的体现，在什么位置调用了sched_class中的什么函数，进程的在什么状态应该进入队列，在什么状态应该从队列中剔除，都能在代码中找到答案。

## 原理课中的知识点

原理课中比较重要的就是各种各样的调度算法的含义以及比较，这在实验中不太能全部实现出来否则就要把所有的算法都实现一边，代码量较大。