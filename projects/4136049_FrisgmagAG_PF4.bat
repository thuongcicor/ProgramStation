@echo off
rem -----------------------------------------
set Firmware=%~dp0firmwares\02.hex
set ExternalLoader=%~dp0firmwares\EL.stldr
set ProgMode=SWD
set ProgSN=55FF6A066675544914192587
rem -----------------------------------------
C:
cd "Program Files\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin"
STM32_Programmer_CLI.exe -c port=%ProgMode% sn=%ProgSN% -q -ob RDP=0xAA -w %Firmware% -ob RDP=0xBB
::STM32_Programmer_CLI.exe -c port=%ProgMode% -w %Firmware% -ob RDP=0xBB
::pause




