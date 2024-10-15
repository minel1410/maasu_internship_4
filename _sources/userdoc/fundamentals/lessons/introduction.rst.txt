============
Introduction
============

The MCU (Microcontroller Unit) is a type of embedded system that integrates a processor core, memory, and peripherals on a single chip. MCU in our project is stm32f411 which is based on Cortex-M4 architecture.

The Cortex-M4 is a specific microcontroller architecture developed by ARM Holdings. 

The Cortex-M4 architecture is a 32-bit microcontroller architecture developed by ARM Holdings. Here are some key features of the Cortex-M4 architecture:

1. **Performance**: The Cortex-M4 processor core is based on the ARMv7-M architecture and offers high performance with a 3-stage (Fetch, Decode, Execute) pipeline. This allows for efficient execution of instructions and faster processing of data.
2.	**Digital Signal Processing (DSP) capabilities**: The Cortex-M4 architecture includes a single-cycle multiply-accumulate (MAC) instruction (multiplication and an addition operation is done in a single clock cycle), which is essential for DSP applications. This feature enables efficient processing of digital signals, making the Cortex-M4 suitable for applications that require signal processing capabilities.
3.	**Floating Point Unit (FPU)**: Some Cortex-M4 processors come with an optional Floating Point Unit (FPU) that provides hardware support for floating-point operations. This is beneficial for applications that involve complex mathematical calculations.
4.	**Memory Protection Unit (MPU)**: The Cortex-M4 architecture includes a Memory Protection Unit (MPU) that allows for memory protection and access control. This feature enhances the security and reliability of embedded systems by preventing unauthorized access to memory regions.
5.	**Nested Vector Interrupt Controller (NVIC)**: The Cortex-M4 architecture includes a Nested Vector Interrupt Controller (NVIC) that efficiently handles interrupts. The NVIC supports up to 240 interrupts with configurable priority levels, enabling precise control over interrupt handling.
6.	**Debugging and Trace Support**: The Cortex-M4 architecture includes features for hardware debugging and trace capabilities, allowing developers to efficiently debug and optimize their code.
7.	**Low Power Consumption**: Cortex-M4 processors are designed to be power-efficient, making them suitable for battery-powered and energy-efficient applications.

