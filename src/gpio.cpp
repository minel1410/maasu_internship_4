#include "gpio.h"

Gpio::Gpio()
{
    // Use constructor for enabling clock for GPIOX port
    // Save pointer to GPIO in variable, and save pin value in variable
    // Fill the missing parameters
    // Tip: you can create multiple parameter/s for specific config (ex. input mode, or output mode)
}

void Gpio::set_mode()
{
    // MODER -> mode register
    // Reset mode register for GPIOX port
    // Set mode register to desirable mode
    // Fill the missing parameter/s 
}

void Gpio::set_input_pull()
{
    // PUPDR -> pull up/pull down register
    // Reset PUPDR
    // Set PUPDR to desirable mode (pull up, pull down, or floating)
    // Fill the missing parameter/s 
}

void Gpio::set_output_type()
{
    // OTYPER -> output type register
    // Reset OTYPER
    // Set OTYPER to desirable type (Push-pull, open-drain)
    // Fill missing parameter/s
}

void Gpio::set_output_speed()
{
    // OSPEEDR -> Output speed register
    // Reset OSPEEDR
    // Set OSPEEDR to desirable speed (low, medium, fast, high)
    // Fill missing parameter/s
}

void Gpio::set_alt_func()
{
    // Alternate function register is composed of 2 registers: low and high
    // It is defined as array AFR[0] and AFR[1]
    // Configure appropriate Alternate function for peripheral you need
    // alternate function number can be found in reference manual at page 150
    // Fill missing parameter
}

void Gpio::write()
{
    // Find the differences between ODR and BSRR registers
    // Use one of these registers to write value to pin
    // Fill missing parameter
}

uint32_t Gpio::read()
{
    // Use IDR register to read from pin
}