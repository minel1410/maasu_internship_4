==================
STM32F411 Overview
==================

The STM32F411 microcontrollers are part of the STM32 Dynamic Efficiency™ lines. These devices represent the entry level to the High Performance F4 Series, offering a balanced combination of dynamic power consumption (in run mode) and processing performance. They integrate a rich set of features in compact 3 x 3 mm packages.

The STM32F411 MCUs are powered by a Cortex®-M4 core with floating point unit, operating at 100 MHz, and achieve exceptionally low power consumption in both run and stop modes. A key feature, Batch Acquisition Mode (BAM), optimizes power usage during data batching. This mode enables efficient data exchange through communication peripherals while keeping the CPU and other parts of the device in power-saving modes.

Features
--------

- Includes ST state-of-the-art patented technology
- Dynamic efficiency line with BAM (Batch acquisition mode)
- Operating voltage: 1.7 V to 3.6 V
- Temperature range: -40°C to 85/105/125 °C

**Core**

- Arm® 32-bit Cortex®-M4 CPU with FPU
- Adaptive real-time accelerator (ART Accelerator) for 0-wait state execution from flash memory
- Operating frequency up to 100 MHz
- Memory protection unit
- 125 DMIPS/1.25 DMIPS/MHz (Dhrystone 2.1)
- DSP instructions

**Memories**

- Up to 512 Kbytes of flash memory
- 128 Kbytes of SRAM

**Clock, Reset, and Supply Management**

- Wide range application supply and I/O voltage: 1.7 V to 3.6 V
- Power-on reset (POR), power-down reset (PDR), power voltage detector (PVD), and brown-out reset (BOR)
- 4-to-26 MHz crystal oscillator
- Internal 16 MHz factory-trimmed RC oscillator
- 32 kHz oscillator for RTC with calibration
- Internal 32 kHz RC oscillator with calibration

**Power Consumption**

- Run mode: 100 μA/MHz (peripheral off)
- Stop mode (Flash in Stop mode, fast wakeup time): 42 μA typical at 25 °C; 65 μA max at 25 °C
- Stop mode (Flash in Deep power down mode, slow wakeup time): down to 9 μA at 25 °C; 28 μA max at 25 °C
- Standby: 1.8 μA at 25 °C / 1.7 V without RTC; 11 μA at 85 °C at 1.7 V
- VBAT supply for RTC: 1 μA at 25 °C

**Analog Features**

- 1x12-bit, 2.4 MSPS A/D converter: up to 16 channels

**DMA**

- General-purpose DMA: 16-stream DMA controllers with FIFOs and burst support

**Timers**

- Up to 11 timers: up to six 16-bit, two 32-bit timers up to 100 MHz
- Each timer with up to four IC/OC/PWM or pulse counter and quadrature (incremental) encoder input
- Two watchdog timers (independent and window)
- SysTick timer

**Debugging**

- Serial wire debug (SWD) & JTAG interfaces
- Cortex®-M4 Embedded Trace Macrocell™ (ETM)

**I/O Ports**

- Up to 81 I/O ports with interrupt capability
- Up to 78 fast I/Os up to 100 MHz
- Up to 77 5 V-tolerant I/Os

**Communication Interfaces**

- Up to 13 communication interfaces:
  - Up to 3 x I2C interfaces (SMBus/PMBus)
  - Up to 3 USARTs (2 x 12.5 Mbit/s, 1 x 6.25 Mbit/s)
  - ISO 7816 interface, LIN, IrDA, modem control
  - Up to 5 SPI/I2Ss (up to 50 Mbit/s)
  - SPI2 and SPI3 with muxed full-duplex I2S for audio class accuracy via internal audio PLL or external clock
  - SDIO interface (SD/MMC/eMMC)
  - USB 2.0 full-speed device/host/OTG controller with on-chip PHY

**Other Features**

- CRC calculation unit
- 96-bit unique ID
- RTC: subsecond accuracy, hardware calendar

**Compliance**

- All packages are ECOPACK2 compliant


Block Diagram
-------------

.. image:: ../images/stm32f411diagram2.svg
    :width: 1000 em