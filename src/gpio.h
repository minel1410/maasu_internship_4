#ifndef _GPIO_H_
#define _GPIO_H_

#include <stdint.h>
#include "stm32f4xx.h"

// Feel free to improvise and modify to your will and needs
// If you need some structs or const values you can define them here
// If you need some enums you can also use them here

// For steps to do when configuring modes (ex. alternate function)
// you can find them in reference manual.

// For input and output registers when you are configuring
// you don't need to config input_pull, output_type, output_speed it is enough for enabling clock
// and setting mode because every register has it's own default value so you can use also that.
// For alternate function it is needed to configure as it is described in reference manual.

// The file where registers are defined is stm32f411xe.h in include folder (vendor/CMSIS/Device/ST/STM32F4)

// Make sure to include gpio in Makefile!

class Gpio
{
    private:

    public:
        Gpio();
        void set_mode();
        void set_input_pull();
        void set_output_type();
        void set_output_speed();
        void set_alt_func();

        void write();
        uint32_t read();
};

#endif