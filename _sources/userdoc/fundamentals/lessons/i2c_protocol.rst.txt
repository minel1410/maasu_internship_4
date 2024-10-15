============
I2C Protocol
============

The I2C (Inter-Integrated Circuit) protocol is a widely used serial communication protocol that enables communication between integrated circuits, microcontrollers, sensors, and other peripheral devices. Here's an explanation of how the I2C protocol works:

1.  Two-Wire Communication: I2C uses two bidirectional lines for communication:

    - Serial Data (SDA): The SDA line carries the actual data being transmitted between devices.
    - Serial Clock (SCL): The SCL line provides the clock signal that synchronizes the data transfer between devices.

2.  Master-Slave Communication: In the I2C protocol, devices are categorized as either masters or slaves:

    - Master: The master device initiates communication on the bus and controls the data transfer.
    - Slave: The slave devices respond to commands from the master and can transmit or receive data.

3.  Addressing: Each slave device on the I2C bus is assigned a unique 7-bit or 10-bit address, allowing the master device to communicate with specific slave devices on the bus.

4.  Start and Stop Conditions:

    - Start Condition: The master initiates communication by sending a start condition, signaling the beginning of a data transfer.
    - Stop Condition: The master sends a stop condition to indicate the end of a data transfer.

5.  Data Transfer:

    - Data Frame: A typical data frame in I2C communication consists of 8 bits of data followed by an acknowledgment bit.
    - Data Transfer: The master device initiates data transfer by sending a start condition, followed by the 7-bit address of the slave device (including the read/write bit), and the data to be transmitted.
    - Acknowledgment: After receiving each byte of data, the receiving device (slave or master) sends an acknowledgment bit to confirm successful reception.

6.  Multi-Master Support: I2C supports multi-master communication, allowing multiple master devices to communicate with slave devices on the same bus. Arbitration mechanisms are used to resolve conflicts if multiple masters attempt to access the bus simultaneously.

7.  Speed and Compatibility: I2C supports different speed modes (standard mode, fast mode, fast mode plus, and high-speed mode) to accommodate various data transfer rates. It is a widely supported protocol in the industry, making it compatible with a wide range of devices.

