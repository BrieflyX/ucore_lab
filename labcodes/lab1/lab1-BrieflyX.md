# Lab1 Report
# 裴中煜 2012010685

## 练习1

1. 执行 make "V=" 命令后得到的输出
```
    + cc kern/init/init.c
    gcc -Ikern/init/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/init/init.c -o obj/kern/init/init.o
    kern/init/init.c:95:1: warning: ‘lab1_switch_test’ defined but not used [-Wunused-function]
    + cc kern/libs/readline.c
    gcc -Ikern/libs/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/libs/readline.c -o obj/kern/libs/readline.o
    + cc kern/libs/stdio.c
    gcc -Ikern/libs/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/libs/stdio.c -o obj/kern/libs/stdio.o
    + cc kern/debug/kdebug.c
    gcc -Ikern/debug/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/debug/kdebug.c -o obj/kern/debug/kdebug.o
    + cc kern/debug/kmonitor.c
    gcc -Ikern/debug/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/debug/kmonitor.c -o obj/kern/debug/kmonitor.o
    + cc kern/debug/panic.c
    gcc -Ikern/debug/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/debug/panic.c -o obj/kern/debug/panic.o
    + cc kern/driver/clock.c
    gcc -Ikern/driver/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/driver/clock.c -o obj/kern/driver/clock.o
    + cc kern/driver/console.c
    gcc -Ikern/driver/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/driver/console.c -o obj/kern/driver/console.o
    + cc kern/driver/intr.c
    gcc -Ikern/driver/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/driver/intr.c -o obj/kern/driver/intr.o
    + cc kern/driver/picirq.c
    gcc -Ikern/driver/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/driver/picirq.c -o obj/kern/driver/picirq.o
    + cc kern/trap/trap.c
    gcc -Ikern/trap/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/trap/trap.c -o obj/kern/trap/trap.o
    + cc kern/trap/trapentry.S
    gcc -Ikern/trap/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/trap/trapentry.S -o obj/kern/trap/trapentry.o
    + cc kern/trap/vectors.S
    gcc -Ikern/trap/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/trap/vectors.S -o obj/kern/trap/vectors.o
    + cc kern/mm/pmm.c
    gcc -Ikern/mm/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Ikern/debug/ -Ikern/driver/ -Ikern/trap/ -Ikern/mm/ -c kern/mm/pmm.c -o obj/kern/mm/pmm.o
    + cc libs/printfmt.c
    gcc -Ilibs/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/  -c libs/printfmt.c -o obj/libs/printfmt.o
    + cc libs/string.c
    gcc -Ilibs/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/  -c libs/string.c -o obj/libs/string.o
    + ld bin/kernel
    ld -m    elf_i386 -nostdlib -T tools/kernel.ld -o bin/kernel  obj/kern/init/init.o obj/kern/libs/readline.o obj/kern/libs/stdio.o obj/kern/debug/kdebug.o obj/kern/debug/kmonitor.o obj/kern/debug/panic.o obj/kern/driver/clock.o obj/kern/driver/console.o obj/kern/driver/intr.o obj/kern/driver/picirq.o obj/kern/trap/trap.o obj/kern/trap/trapentry.o obj/kern/trap/vectors.o obj/kern/mm/pmm.o  obj/libs/printfmt.o obj/libs/string.o
    + cc boot/bootasm.S
    gcc -Iboot/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Os -nostdinc -c boot/bootasm.S -o obj/boot/bootasm.o
    + cc boot/bootmain.c
    gcc -Iboot/ -fno-builtin -Wall -ggdb -m32 -gstabs -nostdinc  -fno-stack-protector -Ilibs/ -Os -nostdinc -c boot/bootmain.c -o obj/boot/bootmain.o
    + cc tools/sign.c
    gcc -Itools/ -g -Wall -O2 -c tools/sign.c -o obj/sign/tools/sign.o
    gcc -g -Wall -O2 obj/sign/tools/sign.o -o bin/sign
    + ld bin/bootblock
    ld -m    elf_i386 -nostdlib -N -e start -Ttext 0x7C00 obj/boot/bootasm.o obj/boot/bootmain.o -o obj/bootblock.o
    'obj/bootblock.out' size: 492 bytes
    build 512 bytes boot sector: 'bin/bootblock' success!
    dd if=/dev/zero of=bin/ucore.img count=10000
    10000+0 records in
    10000+0 records out
    5120000 bytes (5.1 MB) copied, 0.0160878 s, 318 MB/s
    dd if=bin/bootblock of=bin/ucore.img conv=notrunc
    1+0 records in
    1+0 records out
    512 bytes (512 B) copied, 1.6295e-05 s, 31.4 MB/s
    dd if=bin/kernel of=bin/ucore.img seek=1 conv=notrunc
    146+1 records in
    146+1 records out
    74862 bytes (75 kB) copied, 0.000183689 s, 408 MB/s
```

从输出可以看出首先编译链接了所有kernel的源码文件，然后编译了工具程序sign.c，用这个程序生成了bin/bootblock文件，随后使用dd命令对kernel，bootblock这2个文件进行打包，将它们都写入ucore.img文件中。
从makefile的代码来看，生成的UCOREIMG的方法是

```
    $(UCOREIMG): $(kernel) $(bootblock)
        $(V)dd if=/dev/zero of=$@ count=10000
        $(V)dd if=$(bootblock) of=$@ conv=notrunc
        $(V)dd if=$(kernel) of=$@ seek=1 conv=notrunc
```

它依赖于kernel与bootblock的生成。
生成kernel的方法是

```
    $(kernel): $(KOBJS)
        @echo + ld $@
        $(V)$(LD) $(LDFLAGS) -T tools/kernel.ld -o $@ $(KOBJS)
        @$(OBJDUMP) -S $@ > $(call asmfile,kernel)
        @$(OBJDUMP) -t $@ | $(SED) '1,/SYMBOL TABLE/d; s/ .* / /; /^$$/d' > $(call symfile,kernel)
```

关键在于输出中的链接指令

```
    ld -m elf_i386 -nostdlib -T tools/kernel.ld -o bin/kernel ...
    参数含义:
        -m elf_i386 使用i386的链接方式
        -nostdlib 不使用标准库
        -T 使用连接脚本tools/kernel.ld
```

生成bootblock的方法是

```
    $(bootblock): $(call toobj,$(bootfiles)) | $(call totarget,sign)
        @echo + ld $@
        $(V)$(LD) $(LDFLAGS) -N -e start -Ttext 0x7C00 $^ -o $(call toobj,bootblock)
        @$(OBJDUMP) -S $(call objfile,bootblock) > $(call asmfile,bootblock)
        @$(OBJCOPY) -S -O binary $(call objfile,bootblock) $(call outfile,bootblock)
        @$(call totarget,sign) $(call outfile,bootblock) $(bootblock)
```

关键也在于其中的链接命令

```
    ld -m elf_i386 -nostdlib -N -e start -Ttext 0x7C00 obj/boot/bootasm.o obj/boot/bootmain.o -o obj/bootblock.o
    参数含义:
        -m elf_i386 使用i386的链接方式
        -nostdlib 不使用标准库
        -N 把text和data节设置为可读写
        -e start 指定入口点
        -Ttext 指定节在输出文件中的绝对地址
```

最后的dd命令

```
    dd if=/dev/zero of=bin/ucore.img count=10000
    dd if=bin/bootblock of=bin/ucore.img conv=notrunc
    dd if=bin/kernel of=bin/ucore.img seek=1 conv=notrunc
```

if为输入文件，of为输出文件，count为复制区块的大小，默认每块是512bytes故10000块是5.1MB空间。第1个dd从/dev/zero产生'\x00'字符输出到ucore.img，第2个dd将bootblock的512bytes写入ucore.img中，最后一个dd的seek=1偏移1个块，即将kernel写在ucore.img中bootblock之后的位置。

上述过程完成后就生成了ucore.img。

2. 阅读sign.c的代码可以看出，其开辟了512字节的buffer并写入最多510字节，而最后两个字节一定被填充为0x55与0xAA，这就是符合规范的主引导扇区特征。

## 练习2

1. 删除tools/gdbinit中的最后一行continue，让qemu直接断在入口处，即CPU加电后的第一条指令0xfff0处。在执行"make debug"后看到gdb的调试窗口中显示PC为0xfff0。

2. 在gdbinit中删除其他断点，同时加入2行指令，让kernel断在0x7c00处，同时在gdb连接后让kernel运行起来直到断点处。

```
    b *0x7c00
    c
```

运行gdb后程序显示PC为0x7c00，说明断点正常，然后执行x /5i $eip查看指令，得到
```
    Breakpoint 1, 0x00007c00 in ?? ()
    (gdb) x /5i $eip
    => 0x7c00:      cli    
       0x7c01:      cld    
       0x7c02:      xor    %eax,%eax
       0x7c04:      mov    %eax,%ds
       0x7c06:      mov    %eax,%es
```

3. 在上一步断在0x7c00处时，实际已经处在bootasm.S的入口处，此时直接输入x /20i $eip指令，即可看到接下来的20条指令。与bootasm.S比较，发现与文件中的指令一致。

4. 在gdbinit中写入如下指令
```
    file bin/kernel
    target remote:1234
    b kern_init
    c
```
让程序在kern_init函数入口处设置断点停止，然后可以使用n命令一条一条代码向下执行，可以看到console初始化的过程以及屏幕上显示出"(THU.CST) os is loading ..."，一直到最后的while(1)，程序就进入循环。

## 练习3

1. 首先开启A20，在早期PC中，A20物理地址线置为低电平无法访问更高的地址空间，为了访问4G的内存空间，执行以下代码

```
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
```

代码在8042空闲之时，将0xd1与0xdf分别送到0x64与0x60端口，这样就开启了A20.

2. 初始化GDT表，在bootasm.S的文件底部已经对BootstrapGDT进行了定义，gdt为表的空间，gdtdesc为表描述符。然后执行代码
```
lgdt gdtdesc
```

3. 使能和进入保护模式，使能的方法是将CR0的PE位置置为1即可。进入保护模式，需要先将处理器切换到32位模式，然后初始化段寄存器，并设置堆栈寄存器ebp与esp，最后执行到
```
call bootmain
```
转到bootmain.c代码中执行，接下来就是C程序实现的部分。

## 练习4

1. 读取扇区的功能由readsect和readseg函数实现。在readsect函数中，首先等待磁盘准备好，然后向各个控制地址写入对应的数据
```
outb(0x1F2, 1);
outb(0x1F3, secno & 0xFF);
outb(0x1F4, (secno >> 8) & 0xFF);
outb(0x1F5, (secno >> 16) & 0xFF);
outb(0x1F6, ((secno >> 24) & 0xF) | 0xE0);
outb(0x1F7, 0x20);
```
0x1F2为1，表示读取1个扇区，0x1F3-0x1F6共同组成LBA参数，其中0x1F6的第4为置0表示disk 0主盘。然后0x1F7置0x20表示读取指令。
再次等待磁盘准备好，然后执行
```
insl(0x1F0, dst, SECTSIZE / 4);
```
从0x1F0地址读出需要的数据。readseg调用了readsect，实现了可以从任意位置读取任意长度的数据。

2. 首先读出elfhdr描述结构，然后根据其中指定的偏移量等信息加载proghdr，其中e_phoff即程序段的偏移量，而e_phnum即程序段的数目，从ELF中读出程序放入内存
```
for (; ph < eph; ph ++) {
    readseg(ph->p_va & 0xFFFFFF, ph->p_memsz, ph->p_offset);
}
```
最后从e_entry处开始执行，进入kernel代码。

## 练习5

因为函数调用时需要将ebp和eip分别压栈以保存栈帧结构和返回地址，故根据当前的ebp值就可以一直迭代栈中的调用链，每次在栈中读出每个函数调用时的ebp和eip即可，根据kdebug.c中给出的注释完成代码。执行make qemu得到以下输出
```
ebp:0x00007b18 eip:0x0010095c args:0x00010094 0x00000000 0x00007b48 0x0010007f
    kern/debug/kdebug.c:307: print_stackframe+22
ebp:0x00007b28 eip:0x00100c53 args:0x00000000 0x00000000 0x00000000 0x00007b98
    kern/debug/kmonitor.c:125: mon_backtrace+10
ebp:0x00007b48 eip:0x0010007f args:0x00000000 0x00007b70 0xffff0000 0x00007b74
    kern/init/init.c:48: grade_backtrace2+19
ebp:0x00007b68 eip:0x001000a0 args:0x00000000 0xffff0000 0x00007b94 0x00000029
    kern/init/init.c:53: grade_backtrace1+27
ebp:0x00007b88 eip:0x001000bc args:0x00000000 0x00100000 0xffff0000 0x00100043
    kern/init/init.c:58: grade_backtrace0+19
ebp:0x00007ba8 eip:0x001000dc args:0x00000000 0x00000000 0x00000000 0x00103240
    kern/init/init.c:63: grade_backtrace+26
ebp:0x00007bc8 eip:0x00100050 args:0x00000000 0x00000000 0x00010094 0x00000000
    kern/init/init.c:28: kern_init+79
ebp:0x00007bf8 eip:0x00007d66 args:0xc031fcfa 0xc08ed88e 0x64e4d08e 0xfa7502a8
    <unknow>: -- 0x00007d65 --
```

最后一行的<unknow>是堆栈初始化后首次使用的函数，在bootasm.S的最后使用了call bootmain调用bootmain.c中的bootmain函数。
此时ebp被保存下来，bootmain函数的ebp即为0x7bf8，而调用它的地址eip为0x7d66是call bootmain这条指令所在的位置。

## 练习6

1. 从vector.S文件对各个中断向量的初始化可以看出，汇编代码执行了2次pushl操作，一共将8字节的数据压栈，故中断向量表一个表项长度为8 byte。其中第2-3byte指的是段号，0-1字节和6-7字节指的是段内偏移，由此可以确定中断例程的入口地址。

2. 见代码

3. 见代码
