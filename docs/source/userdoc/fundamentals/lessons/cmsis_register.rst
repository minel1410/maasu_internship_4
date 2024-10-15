==============================
CMSIS and Register Definitions
==============================

When we wanted to access the GPIO registers, we had to manually look up the memory addresses in the reference manual and make a `#define` for each register. If we had to do that for every single register for all peripherals, we would probably go insane. Luckily, someone has already done the legwork for us.

`CMSIS <https://github.com/ARM-software/CMSIS_5>`_ is a collection of components for Arm Cortex-based microcontrollers, including an API to the core registers, a DSP library, an RTOS abstraction layer and more. The peripherals of the STM32F4 are covered in the `STM32F4 CMSIS Device component <https://github.com/STMicroelectronics/cmsis_device_f4>`_ made available by STMicroelectronics.
