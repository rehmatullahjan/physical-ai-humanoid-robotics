---
title: Physical Systems & Actuators
---


# Chapter 3: Physical Systems & Actuators

## Learning Objectives

*   Understand the role of actuators in physical systems.
*   Identify different types of actuators and their applications.
*   Learn how to interface actuators with microcontrollers.
*   Implement basic control strategies for actuators.

## Introduction

This chapter delves into the world of physical systems and the crucial role of actuators. Actuators are the muscles of any robotic or automated system, converting electrical signals into physical motion or force. We will explore various actuator types, their working principles, and practical examples of interfacing them with microcontrollers like the Arduino. Understanding actuators is fundamental to building interactive and responsive physical systems.

## 3.1: DC Motors

DC motors are a common and versatile actuator, widely used for applications ranging from simple toys to complex robotic systems. They convert electrical energy into rotational mechanical energy.

### 3.1.1: Working Principle

DC motors operate based on the principle of electromagnetism. A current-carrying conductor placed in a magnetic field experiences a force. In a DC motor, a coil of wire (the armature) is placed within a magnetic field. When current flows through the coil, it experiences a torque, causing it to rotate.

### 3.1.2: Control

The speed and direction of a DC motor can be controlled by varying the voltage applied to it.  A higher voltage results in a faster speed. Reversing the polarity of the voltage reverses the direction of rotation.  PWM (Pulse Width Modulation) is a common technique for controlling the average voltage applied to the motor, allowing for precise speed control.

### 3.1.3: Code Example (Arduino)

```arduino
// DC Motor Control Example

int motorPin = 9; // PWM pin for speed control
int dirPinA = 8; // Digital pin for direction control (Motor Driver Input A)
int dirPinB = 7; // Digital pin for direction control (Motor Driver Input B)

void setup() {
  pinMode(motorPin, OUTPUT);
  pinMode(dirPinA, OUTPUT);
  pinMode(dirPinB, OUTPUT);
}

void loop() {
  // Forward at half speed
  digitalWrite(dirPinA, HIGH);
  digitalWrite(dirPinB, LOW);
  analogWrite(motorPin, 127); // 127 is approximately half of 255
  delay(2000);

  // Reverse at full speed
  digitalWrite(dirPinA, LOW);
  digitalWrite(dirPinB, HIGH);
  analogWrite(motorPin, 255);
  delay(2000);

  // Stop
  digitalWrite(dirPinA, LOW);
  digitalWrite(dirPinB, LOW);
  analogWrite(motorPin, 0);
  delay(2000);
}
```

## 3.2: Servo Motors

Servo motors are rotary actuators that allow for precise angular position control. They are commonly used in robotics, model airplanes, and other applications where precise positioning is required.

### 3.2.1: Working Principle

A servo motor typically contains a DC motor, a gear train, a potentiometer, and a control circuit. The control circuit compares the desired position (set by a PWM signal) with the actual position (read from the potentiometer) and adjusts the motor until the desired position is reached.

### 3.2.2: Control

Servo motors are controlled by sending a PWM signal with a specific pulse width. The pulse width determines the desired angular position of the servo. Typically, a pulse width of 1ms corresponds to one extreme position, 2ms corresponds to the other extreme position, and 1.5ms corresponds to the center position.

### 3.2.3: Code Example (Arduino)

```arduino
// Servo Motor Control Example
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  // Sweep from 0 to 180 degrees
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    myservo.write(pos);                  // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  // Sweep from 180 to 0 degrees
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);                  // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
```

## 3.3: Stepper Motors

Stepper motors are electric motors that divide a full rotation into a number of equal steps. They can be precisely controlled to move and hold at specific positions.

### 3.3.1: Working Principle

Stepper motors consist of multiple coils arranged around a central rotor. By energizing the coils in a specific sequence, the rotor can be moved in discrete steps.

### 3.3.2: Control

Stepper motors require more complex control than DC or servo motors.  They are typically controlled by a dedicated driver chip that sequences the energizing of the motor's coils.  Different stepping modes (full step, half step, microstepping) offer varying degrees of precision and smoothness.

### 3.3.3: Code Example (Arduino) (using Stepper library)

```arduino
// Stepper Motor Control Example
#include <Stepper.h>

// Define the number of steps per revolution of your motor
const int stepsPerRevolution = 200;

// Initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() {
  // Set the speed at which to rotate the motor
  myStepper.setSpeed(60); // RPM
}

void loop() {
  // Step one revolution  in one direction:
  myStepper.step(stepsPerRevolution);
  delay(500);

  // Step one revolution in the other direction:
  myStepper.step(-stepsPerRevolution);
  delay(500);
}
```

## 3.4: Linear Actuators

Linear actuators convert rotary motion into linear motion. They are used in applications such as robotics, automation, and adjustable furniture.

### 3.4.1: Working Principle

Linear actuators typically consist of a motor (DC or stepper), a gearbox, and a lead screw. The motor rotates the lead screw, which moves a nut along the screw, resulting in linear motion.

### 3.4.2: Control

The control of linear actuators depends on the type of motor used. DC motor based linear actuators can be controlled with similar techniques as DC motors. Stepper motor based actuators offer more precise position control.  Limit switches are often incorporated for safety and to prevent over-extension.

### 3.4.3: (Concept) - Code example would depend heavily on the specific actuator's motor type.  The principle is the same as controlling the underlying motor (DC or Stepper).

## Key Takeaways

*   Actuators are essential for converting electrical signals into physical motion in physical systems.
*   DC motors are versatile for speed control; servo motors offer precise angular positioning; stepper motors provide incremental steps; linear actuators generate linear motion.
*   Microcontrollers like Arduino can be used to control actuators using PWM signals and digital output.
*   Understanding the working principle and control methods of different actuators is crucial for designing and building effective robotic and automated systems.
```

