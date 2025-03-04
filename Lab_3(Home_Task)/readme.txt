Q: Blow on the sensor and observe whether it detects minor changes in temperature and humidity.
Ans: As the sensor detects minor changes in the atmosphere, it displays them. I have experienced this by blowing near the sensor the values will increase and decrease depending on the speed of the blow. 


What are Interrupts in MicroPython?
Interrupts are signals that pause the normal execution of your code to immediately execute a special function called an Interrupt Service Routine (ISR). Once the ISR finishes, the main code resumes from where it was interrupted. This is useful for handling asynchronous events like button presses or sensor data updates without continuously polling them in your main loop.



 Why Do We Use Interrupts?
Interrupts allow a microcontroller to immediately respond to important events without constantly checking for them in the main program loop.
They are used to:

Improve Responsiveness: Execute tasks instantly when an event occurs (e.g., button press or sensor update).
Handle Multiple Tasks: Allow the microcontroller to manage various tasks efficiently.
Reduce Polling: Eliminate the need for continuous checking of input devices, saving processing time.


How Do Interrupts Lower the Processing Cost of the Microcontroller?
Efficient CPU Utilization:
The microcontroller can perform other tasks instead of constantly checking for specific conditions (polling).
Reduced Power Consumption:
By spending more time in low-power modes waiting for interrupts, power usage is minimized.
Faster Response Time:
The CPU can immediately handle high-priority tasks without delay.
Simpler Code Logic:
Reduces complexity by separating event-driven tasks from the main loop.


 What is a Debounce Issue?
Debounce is a phenomenon where a mechanical switch (like a button) bounces rapidly between on and off states before settling when pressed or released. This occurs due to the mechanical contacts vibrating momentarily. As a result, a single button press can be registered as multiple presses by a microcontroller.



Why We Get Rid of It:

Prevent False Triggers: Ensures that a single press is detected as a single event.
Maintain System Reliability: Reducing erroneous inputs leads to a stable system.
Improve User Experience: Prevents unexpected behavior in user interfaces.




In Which Applications or Domains Can Debounce Issues Be Threatening If Not Resolved?
Embedded Systems:
Critical in automotive controls (e.g., brake or accelerator pedals).
Medical Devices:
Ensures reliable inputs in life-supporting systems.
Industrial Automation:
Accurate switch detection for emergency stops and control panels.
Consumer Electronics:
Prevents multiple triggers in remote controls, keyboards, and gaming devices.
Safety Systems:
False triggers in fire alarms or security systems could cause dangerous delays.



Why Does Debounce Occur? Is It a Compiler Error, Logical Error, or Due to Cheap Microcontrollers?
Debounce occurs due to the mechanical nature of switches, not due to compiler errors, logical errors, or cheap microcontrollers.
It’s caused by vibrations and mechanical contact bouncing when a switch is pressed or released.
Even high-quality microcontrollers experience debounce unless specifically handled in the code.



How to Fix Debounce Issues:
Software Debouncing:

Use a delay after detecting a button press to ignore subsequent false triggers.
Example: Wait 10–50 milliseconds before registering a button press.
Hardware Debouncing:

Use capacitors or Schmitt triggers to smooth out the signals.
Efficient Coding:

Implement state machines or interrupts to handle button presses cleanly.