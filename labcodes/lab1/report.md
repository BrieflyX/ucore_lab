# Lab1 Report
# 裴中煜 2012010685

## 练习1

1. 

2. 阅读sign.c的代码可以看出，其开辟了512字节的buffer并写入最多510字节，而最后两个字节一定被填充为0x55与0xAA，这就是符合规范的主引导扇区特征。

## 练习2

1. 删除tools/gdbinit中的最后一行continue，让qemu直接断在入口处，即CPU加电后的第一条指令0xfff0处。在执行"make debug"后看到gdb的调试窗口中显示PC为0xfff0。

2. 在gdbinit中删除其他断点，同时加入2行指令，让kernel断在0x7c00处，同时在gdb连接后让kernel运行起来直到断点处。

'''
    b *0x7c00
    c
'''

运行gdb后程序显示PC为0x7c00，说明断点正常，然后执行x /5i $eip查看指令，得到
'''
    Breakpoint 1, 0x00007c00 in ?? ()
    (gdb) x /5i $eip
    => 0x7c00:      cli    
       0x7c01:      cld    
       0x7c02:      xor    %eax,%eax
       0x7c04:      mov    %eax,%ds
       0x7c06:      mov    %eax,%es
'''

3. 在上一步断在0x7c00处时，实际已经处在bootasm.S的入口处，此时直接输入x /20i $eip指令，即可看到接下来的20条指令。与bootasm.S比较，发现与文件中的指令一致。

4. 

## 练习3

1. 首先开启A20，在早期PC中，A20物理地址线置为低电平无法访问更高的地址空间，为了访问4G的内存空间，执行以下代码

'''
seta20.1:
    inb $0x64, %al
    testb $0x2, %al
    jnz seta20.1

    movb $0xd1, %al
    outb %al, $0x64

seta20.2:
    inb $0x64, %al
    testb $0x2, %al
    jnz seta20.2

    movb $0xdf, %al
    outb %al, $0x60 
'''

代码在8042空闲之时，将0xd1与0xdf分别送到0x64与0x60端口，这样就开启了A20.

2. 初始化GDT表，在bootasm.S的文件底部已经对BootstrapGDT进行了定义，gdt为表的空间，gdtdesc为表描述符。然后执行代码
'''
lgdt gdtdesc
'''

3. 使能和进入保护模式，使能的方法是将CR0的PE位置置为1即可。进入保护模式，需要先将处理器切换到32位模式，然后初始化段寄存器，并设置堆栈寄存器ebp与esp，最后执行到
'''
call bootmain
'''
转到bootmain.c代码中执行，接下来就是C程序实现的部分。

## 练习4

1. 读取扇区的功能由readsect和readseg函数实现。在readsect函数中，首先等待磁盘准备好，然后向各个控制地址写入对应的数据
'''
outb(0x1F2, 1);
outb(0x1F3, secno & 0xFF);
outb(0x1F4, (secno >> 8) & 0xFF);
outb(0x1F5, (secno >> 16) & 0xFF);
outb(0x1F6, ((secno >> 24) & 0xF) | 0xE0);
outb(0x1F7, 0x20);
'''
0x1F2为1，表示读取1个扇区，0x1F3-0x1F6共同组成LBA参数，其中0x1F6的第4为置0表示disk 0主盘。然后0x1F7置0x20表示读取指令。
再次等待磁盘准备好，然后执行
'''
insl(0x1F0, dst, SECTSIZE / 4);
'''
从0x1F0地址读出需要的数据。readseg调用了readsect，实现了可以从任意位置读取任意长度的数据。

2. 首先读出elfhdr描述结构，然后根据其中指定的偏移量等信息加载proghdr，其中e_phoff即程序段的偏移量，而e_phnum即程序段的数目，从ELF中读出程序放入内存
'''
for (; ph < eph; ph ++) {
    readseg(ph->p_va & 0xFFFFFF, ph->p_memsz, ph->p_offset);
}
'''
最后从e_entry处开始执行，进入kernel代码。

## 练习5
