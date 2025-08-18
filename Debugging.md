```
display/i $pc
monitor reset halt
break 
continue
step
delete
monitor cortex_m vector_catch all
bt
```


If I run the code step by step it all works perfectly... If I hit continue it never seems to go anywhere and hits a hard fault... time to figure out why :D 


```
#3  0x100406d6 in SystemInit () at ../Core/Src/system_stm32wl3x.c:280

        mainRegulator = 4294967295
        smpsOutVoltage = 0
        lsiBw = 4294967295
        hsiCalib = 4294967295

        i = 0 '\000'
```


```
/* Set all the interrupt with low priority */

/*for (i=0; i<32; i++)

{

NVIC_SetPriority((IRQn_Type)i, IRQ_LOW_PRIORITY);

}*/
```

It just flashed wrong.............


```
/Applications/STM32CubeIDE.app/Contents/Eclipse/plugins/com.st.stm32cube.ide.mcu.externaltools.openocd.macos64_2.4.200.202505051030/tools/bin/openocd "-f" "BlinkSTM32WL3x Debug.cfg" "-s" "/Users/marcelgietzmann-sanders/STM32CubeIDE/workspace_1.17.0/BlinkSTM32WL3x" "-s" "/Applications/STM32CubeIDE.app/Contents/Eclipse/plugins/com.st.stm32cube.ide.mcu.debug.openocd_2.3.100.202501240831/resources/openocd/st_scripts" "-c" "hla_serial 1B1215157416303030303032" "-c" "gdb_report_data_abort enable" "-c" "gdb_port 3333" "-c" "tcl_port 6666" "-c" "telnet_port 4444"


gdb BlinkSTM32WL3x.elf

STM32_Programmer_CLI --connect port=SWD -r8 0x10041638 64
STM32_Programmer_CLI -c port=SWD -d ~/STM32CubeIDE/workspace_1.17.0/BlinkSTM32WL3x/Debug/BlinkSTM32WL3x.elf

STM32_Programmer_CLI --connect port=SWD --erase all
```

I have at this point learned loads. I know how to use the debugger, I know roughly how to setup the chip. I have manually changed the linker and the startup. And I know how to walk through gdp pretty darn well. Unfortunately I don't know what to do about this instability I'm experiencing in both the flashing and the hard faults. I have browsed loads of documentation to no avail (everything suggests I'm doing the right thing) and the debugger is giving me no further clues. Furthermore given the edits I've had to make to the MX generated software I don't know if something is just not getting configured correctly or some shit like that. 

So we're going to start with a nucleo board that is already pre-built and that we can then blink an LED on. That way I at least know the software is correct. I will also at that point have a working circuit too. Then I'll do this in reverse order - create a circuit that is very very similar (if not exactly the same) and work my backwards from that to a circuit I could easily use. To do this I'll need to build a new kicad project that can take the slightly larger MCUs I'll be dealing with here. And I'll need to identify how each of the circuits are working on the nucleo board so I can replicate those as well. 

But that'll be for another day. I think at this point the chances of my figuring all of this out by August 22nd are very slim. So I will switch over to just focusing on the paper and doing little bits of this if I have leftover time. 

- [ ] Fully understand the circuitry of the nucleo board
- [ ] Program it to blink
- [ ] Build a bare metal version
- [ ] Program it to blink
- [ ] Learn wtf went wrong here... (I'm very curious to see if the linker will be better for this one)

So I need to go from the opposite direction - from something that works to something that doesn't. 