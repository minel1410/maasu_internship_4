GPIO in STM32 Microcontrollers
===============================

Introduction
------------

In this lesson, we collectively explored the concepts and practical implementation of GPIO (General Purpose Input/Output) in STM32 microcontrollers. Our journey covered theoretical knowledge, practical coding, and challenges faced along the way. This document summarizes the key lessons learned and includes useful resources for further reading.

Learning Process
----------------

Our learning process involved various resources and hands-on coding exercises. We primarily relied on recorded Lark video sessions, YouTube tutorials, and documentation. Here are some key resources that helped us:

- `Understanding STM32 GPIO <https://youtu.be/hyZS2p1tW-g?si=pNPXJLKsf5A7oHNc>`_
- `GPIO Configuration in STM32 <https://youtu.be/7xnUsPo_fG8?si=0p9v-UJoJ4iEK2n6>`_
- `Debugging Common Errors <https://youtu.be/jcy5TpbXfAY?si=21mCAGxIbkA9EvIP>`_
- `ODR vs. BSRR Registers <https://youtu.be/E0VESHUOb1c?si=w-nblw-3112YsOFH>`_
- `Detailed GPIO Configuration <https://youtu.be/Wbs0TOwv3aI?si=xD94Du2QwZh9QHgE>`_

Key Terms and Concepts
----------------------

1. **GPIO (General Purpose Input/Output)**:
   - GPIO pins can be configured as input or output and can perform various functions like digital input, digital output, analog input, and PWM output.
   
2. **RCC (Reset and Clock Control)**:
   - RCC manages system clocks and resets. To enable the clock for a GPIO port, use the RCC AHB1ENR register.
   
3. **MODER (Mode Register)**:
   - Configures the mode of GPIO pins as input, output, analog, or alternative functions.
   
4. **PUPDR (Pull-Up/Pull-Down Register)**:
   - Configures pull-up and pull-down resistors for GPIO pins to define their default state when configured as input.
   
5. **OTYPER (Output Type Register)**:
   - Configures the output type for GPIO pins as push-pull or open-drain outputs.
   
6. **OSPEEDR (Output Speed Register)**:
   - Configures the output speed for GPIO pins to low, medium, fast, or very fast.
   
7. **AFR (Alternate Function Register)**:
   - Configures alternate functions of GPIO pins for various peripherals like UART, I2C, SPI, and PWM.

8. **ODR (Output Data Register)**:
   - Directly writes the output state of GPIO pins.
   
9. **BSRR (Bit Set/Reset Register)**:
   - Allows atomic operations on GPIO pins for setting or resetting individual pins.

Difference between ODR and BSRR
-------------------------------

Using the ODR register for quick changes to the entire port requires caution to avoid unintended changes to pin states. The BSRR register provides precise control over individual pins, beneficial for scenarios requiring fine control.

Challenges Faced
----------------

- Limited experience with embedded systems and register programming.
- Navigating extensive documentation to find relevant information.
- Testing the correctness of written functions.
- Understanding bitwise operations for register manipulation.

Review of GPIO Implementation
-----------------------------

Enumerations for Function Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enum classes for various function parameters were created to enhance code readability and maintainability.

Constructor Logic
^^^^^^^^^^^^^^^^^

The constructor logic matches forwarded ports and enables specified ports. Handling of invalid ports remains an area for further learning.

Mode and Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Set Mode Function**:
  Resets the MODER register and assigns the given mode using an enum.

- **Set Pull Function**:
  Applies similar logic for configuring pull-up and pull-down resistors.

Optimizing the Read Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Returns a boolean value to reduce memory usage and minimize errors.
- Uses the BSRR register for efficient state checking.

Research and Resources
----------------------

- `STM32 Manual <https://www.st.com/resource/en/reference_manual/rm0008-stm32f101xx-stm32f102xx-stm32f103xx-stm32f105xx-and-stm32f107xx-advanced-armbased-32bit-mcus-stmicroelectronics.pdf>`_
- `GitHub Repository for GPIO <https://github.com/LonelyWolf/stm32/blob/master/max44009/periph/gpio.h>`_

Conclusion
----------

Our journey into STM32 GPIO programming has been enlightening and challenging. We have learned to configure and control GPIO pins, manage register settings, and implement practical code solutions. While there is still much to learn, we are motivated by the progress we have made and look forward to further exploring embedded programming.

**Written by Lamija Veladžić, Nejra Adilović and Minel Salihagić**
