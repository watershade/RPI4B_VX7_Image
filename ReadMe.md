# About RPI4B_VX7_Image
## What is it? 本工程是什么？
本工程是基于WindRiver Labs公开的SDK。他们称作non-commercial license agreement (NCLA)。可以在附录的第一个连接了解我的制作笔记。
整体移植并不困难，但是我还是在最后界面显示的地方卡住了。因为最初我使用HDMI作为信息的显示媒介。发现VxWorks开始启动后，屏幕就没有任何内容显示了。
因为最初串口连接的引脚也因为糊涂搞错了，所以白白折腾了半天时间。最后把HDMI拔掉，然后使用Serial显示，结果满足要求。
这里展示一下移植成功的显示，以增强你的信心。

```shell

 Serial  Port opened


U-Boot 2023.10 (Jan 06 2024 - 19:32:58 +0800)

DRAM:  948 MiB (effective 1.9 GiB)
RPI 4 Model B (0xb03112)
Core:  209 devices, 15 uclasses, devicetree: board
MMC:   mmcnr@7e300000: 1, mmc@7e340000: 0
Loading Environment from FAT... OK
In:    serial,usbkbd
Out:   serial,vidconsole
Err:   serial,vidconsole
Net:   
Warning: ethernet@7d580000 MAC addresses don‘t match:
Address in DT is                dc:a6:32:c8:21:09
Address in environment is       dc:a6:32:07:b3:a4
eth0: ethernet@7d580000
Hit any key to stop autoboot:  0 
15767528 bytes read in 677 ms (22.2 MiB/s)
## Booting kernel from Legacy Image at 00100000 ...
   Image Name:   vxworks
   Image Type:   AArch64 VxWorks Kernel Image (uncompressed)
   Data Size:    15767464 Bytes = 15 MiB
   Load Address: 00100000
   Entry Point:  00100000
   Verifying Checksum ... OK
Working FDT set to 0
   Loading Kernel Image
   !!! WARNING !!! Using legacy DTB
## Starting vxWorks at 0x00100000, device tree at 0x00000000 ...
Instantiating /ram0 as rawFs,  device = 0x1
Formatting /ram0 for HRFS v1.2
Instantiating /ram0 as rawFs, device = 0x1
Formatting...OK.
Target Name: vxTarget 
Instantiating /tmp as rawFs,  device = 0x10001
Formatting /tmp for HRFS v1.2
Instantiating /tmp as rawFs, device = 0x10001
Formatting...OK.
 
 _________            _________
 \........\          /......../
  \........\        /......../
   \........\      /......../
    \........\    /......../
     \........\   \......./
      \........\   \...../              VxWorks SMP 64-bit
       \........\   \.../
        \........\   \./     Release version: 23.09
         \........\   -      Build date: Sep 19 2023 16:16:34
          \........\
           \......./         Copyright Wind River Systems, Inc.
            \...../   -                 1984-2023
             \.../   /.\
              \./   /...\
               -   -------

                   Board: Raspberry Pi 4 Model B - ARMv8
               CPU Count: 4
          OS Memory Size: ~883MB
        ED&R Policy Mode: Deployed
     Debug Agent: Started (always)
         Stop Mode Agent: Not started
              BSP Status: *** UNSUPPORTED ***

Instantiating /ram as rawFs,  device = 0x50001
Formatting /ram for DOSFS
Instantiating /ram as rawFs, device = 0x50001
Formatting...Retrieved old volume params with %38 confidence:
Volume Parameters: FAT type: FAT32, sectors per cluster 0
  0 FAT copies, 0 clusters, 0 sectors per FAT
  Sectors reserved 0, hidden 0, FAT sectors 0
  Root dir entries 0, sysId (null)  , serial number 5b0000
  Label:"           " ...
Disk with 64 sectors of 512 bytes will be formatted with:
Volume Parameters: FAT type: FAT12, sectors per cluster 1
  2 FAT copies, 54 clusters, 1 sectors per FAT
  Sectors reserved 1, hidden 0, FAT sectors 2
  Root dir entries 112, sysId VXDOS12 , serial number 5b0000
  Label:"           " ...
OK.
Thu Jan  1 00:00:01 1970: ipnet[44a0f0]: Error: ipcom_getsockaddrbyaddr failed gw: dhcp

 Adding 22707 symbols for standalone.

-> 
```
后面我也简单的做了几个交互动作：
```shell
-> help

help                           Print this list
dbgHelp                        Print debugger help info
edrHelp                        Print ED&R help info
ioHelp                         Print I/O utilities help info
nfsHelp                        Print nfs help info
netHelp                        Print network help info
rtpHelp                        Print process help info
spyHelp                        Print task histogrammer help info
timexHelp                      Print execution timer help info
h         [n]                  Print (or set) shell history
i         [task]               Summary of tasks’ TCBs
ti        task                 Complete info on TCB for task
sp        adr,args...          Spawn a task, pri=100, opt=0x19, stk=20000
taskSpawn name,pri,opt,stk,adr,args... Spawn a task
tip       "dev=device1#tag=tagStr1", "dev=device2#tag=tagStr2", ...
                               Connect to one or multiple serial lines
td        task                 Delete a task
ts        task                 Suspend a task
tr        task                 Resume a task

Type <CR> to continue, Q<CR> or q<CR> to stop: i

tw        task                 Print pending task detailed info
w         [task]               Print pending task info
d         [adr[,nunits[,width]]] Display memory
m         adr[,width]          Modify memory
mRegs     [reg[,task]]         Modify a task's registers interactively
pc        [task]               Return task's program counter
iam       "user"[,"passwd"]    Set user name and passwd, possibly in
                               an interactive manner
whoami                         Print user name
devs                           List devices
ld        [syms[,noAbort][,"name"]] Load stdin, or file, into memory
                               (syms = add symbols to table:
                               -1 = none, 0 = globals, 1 = all)
lkup      ["substr"]           List symbols in system symbol table
lkAddr    address              List symbol table entries near address
checkStack  [task]             List task stack sizes and usage
printErrno  value              Print the name of a status value
period    secs,adr,args...     Spawn task to call function periodically
repeat    n,adr,args...        Spawn task to call function n times (0=forever)
version                        Print VxWorks version info, and boot line

Type <CR> to continue, Q<CR> or q<CR> to stop: 
shConfig  ["config"]           Display or set shell configuration variables
strFree   [address]            Free strings allocated within the shell (-1=all)

NOTE:  Arguments specifying 'task' can be either task ID or name.

value = 1 = 0x1
-> i

  NAME             TID       PRI   STATUS         PC          ERRNO  CPU #
----------  ---------------- --- ---------- ---------------- ------- -----
tIsr0       ffff80000002cd10   0 PEND       ffffffff807ca5b4       0     -
tJobTask    ffff80000005b820   0 PEND       ffffffff8061c69c       0     -
tExcTask    ffffffff81069fc8   0 PEND       ffffffff807ca5b4       0     -
tLogTask    ffff80000005e010   0 PEND       ffffffff807c7124       0     -
tShell0     ffff8000004a1f30   1 READY      ffffffff807e2b4c       0     1
tHrfsCommi> ffff8000003556b0   2 PEND+T     ffffffff807ca5b4  3d0004     -
tHrfsCommi> ffff8000003e9ec0   2 PEND+T     ffffffff807ca5b4  3d0004     -
tErfTask    ffff80000002a070  10 PEND       ffffffff807cc480       0     -
ipcom_tick> ffff8000004eba40  20 PEND+T     ffffffff807ca5b4       0     -
tVxdbgTask  ffff8000004ec3e0  25 PEND       ffffffff807ca5b4       0     -
tDmaJobTas> ffff80000002b4a0  45 PEND       ffffffff807cb6f8       0     -
tTcfEvents  ffffffff81078e50  49 PEND+T     ffffffff807cd7c4  3d0004     -
tTcf        ffff8000004ee540  49 DELAY      ffffffff807de3cc       0     -
tTcf        ffff8000004426f0  49 PEND       ffffffff807ca5b4       0     -
tTcf        ffff8000004f4010  49 PEND       ffffffff807ca5b4       0     -
tTcf        ffff8000004f4f80  49 PEND       ffffffff807ca5b4       0     -
tTcf        ffff8000004f67b0  49 PEND       ffffffff807ca5b4       0     -
tTcf        ffff8000004f7b80  49 PEND       ffffffff807ca5b4       0     -
tNet0       ffff80000002a910  50 PEND       ffffffff807cb6f8       0     -
tAioIoTask> ffff8000002c3c70  50 PEND       ffffffff807cc480       0     -
tAioIoTask> ffff8000002c4190  50 PEND       ffffffff807cc480       0     -
/sd0XbdSvc  ffff8000003ee010  50 PEND       ffffffff807ca5b4       0     -
tVxcd       ffff8000004264c0  50 PEND       ffffffff807c7124       0     -
tNetConf    ffff80000044a0f0  50 PEND       ffffffff807ca5b4       0     -
ipcom_teln> ffff8000004a2e10  50 PEND       ffffffff807ca5b4       0     -
ipdhcpc     ffff80000044d010  50 PEND+T     ffffffff807ca5b4  3d0004     -
tAnalysisA> ffffffff8100a1d0  50 PEND       ffffffff807cd7c4       0     -
tAioWait    ffff8000002c3590  51 PEND       ffffffff807ca5b4       0     -
tPortmapd   ffff8000004a3950  54 PEND       ffffffff807ca5b4       0     -
xHCD_IH0    ffff800000032400  90 PEND       ffffffff807ca5b4       0     -
sdBusMonit> ffff80000002d790 100 PEND       ffffffff807ca5b4       5     -
BusM A      ffff800000030a90 100 DELAY      ffffffff807de3cc       0     -
BusM B      ffff800000028980 100 DELAY      ffffffff807de3cc       0     -
tUsb2Video  ffff8000004eafe0 100 PEND       ffffffff807c7124       0     -
tUsb2Clr    ffff80000035b250 150 PEND       ffffffff807c7124       0     -
miiBusMoni> ffff8000004417c0 252 DELAY      ffffffff807de3cc       0     -
tIdleTask0  ffffffff813dc000 287 READY      ffffffff807c94b4       0     0
tIdleTask1  ffffffff813e9000 287 READY      ffffffff807c94b4       0     -
tIdleTask2  ffffffff813f6000 287 READY      ffffffff807c94b4       0     2
tIdleTask3  ffffffff81403000 287 READY      ffffffff807c94b4       0     3
value = 0 = 0x0
-> 
```


## 附录
1. Please refer to [my notes](https://watershade.github.io/ROS2/How_To_Install_Vxworks_On_PRI4/) to know how can I generate this images.

2. The official guide page is [here.](https://labs.windriver.com/downloads/wrsdk-vxworks7-docs/2309/README_raspberrypi4b.html)

