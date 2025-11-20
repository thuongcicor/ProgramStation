@echo off
rem -----------------------------------------
set Firmware=%~dp0firmwares\EF1078-HMI-SW-VB0-05-005_CUBE.hex
set ExternalLoader=%~dp0firmwares\EF1078_FLM_MT29F1G08_CUBE.stldr
set ProgMode=SWD
set ProgSN=001A003C544B500120343637
rem -----------------------------------------
C:
cd "Program Files\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin"
::STM32_Programmer_CLI.exe -c port=SWD sn=362C150D1116303030303032 -ob RDP=0xAA -e all -w C:\data\FW\SURF-KM_2022_12_01_110139_PR.FULL.hex -ob RDP=0xBB
STM32_Programmer_CLI.exe -c port=%ProgMode% sn=%ProgSN% -ob BOOT_CM4_ADD0=0x810 BOOT_CM7_ADD0=0x811 -ob RDP=0xAA -rdu -d %Firmware% -el %ExternalLoader%
::STM32_Programmer_CLI.exe -c port=%ProgMode% -rdu -d %Firmware% -el %ExternalLoader%
::pause




