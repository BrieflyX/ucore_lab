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