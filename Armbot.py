# This is a program to control the Armbot with the VEX IQ Controller:
# - Base Rotator: L Down to turn left; R Down to turn right
# - Shoulder: Joystick A
# - Elbow: Joystick D
# - Claw: L Up to release, R Up to grab


# IMPORT OBJECTS FROM LIBRARY
# ===========================

from vex import (
    Brain,
    Controller,
    Motor,
    Bumper,
    Ports,
    BrakeType, FORWARD, REVERSE, PERCENT
)


# INITIALIZE ROBOT COMPONENTS
# ===========================

# init the Brain
brain = Brain()

# init the Controller
controller = Controller()
controller.set_deadband(10)   # if joystick position < 10%, then consider it 0%

# init the Motors
base_rotator_motor = Motor(Ports.PORT10, True)   # reverse direction
shoulder_motor = Motor(Ports.PORT6, True)   # reverse direction
elbow_motor = Motor(Ports.PORT1)
claw_motor = Motor(Ports.PORT4)

# init the Base Bumper + Elbow Bumper
base_bumper = Bumper(Ports.PORT2)
elbow_bumper = Bumper(Ports.PORT9)

# FUNCTIONS
# =========

def control_base_rotator():
    # L Down to turn left
    if controller.buttonLDown.pressing():
        base_rotator_motor.spin(REVERSE, 100, PERCENT)

    # R Down to turn right
    elif controller.buttonRDown.pressing():
        base_rotator_motor.spin(FORWARD, 100, PERCENT)

    # otherwise stop
    else:
        base_rotator_motor.stop(BrakeType.HOLD)


def control_shoulder():
    # Joystick A:
    # - if up, then raise the shoulder, unless the base bumper is pressed
    # - if down, then lower the shoulder
    joystick_a_position = controller.axisA.position()

    if ((joystick_a_position > 0) and (not base_bumper.pressing())) or \
            (joystick_a_position < 0):
        shoulder_motor.spin(FORWARD, joystick_a_position, PERCENT)

    # otherwise stop
    else:
        shoulder_motor.stop(BrakeType.HOLD)


def control_elbow():
    # Joystick D:
    # - if up, then raise the elbow
    # - if down, then lower the elbow
    joystick_d_position = controller.axisD.position()

    if ((joystick_d_position > 0) and (not elbow_bumper.pressing())) or \
            (joystick_d_position < 0):
        elbow_motor.spin(FORWARD, joystick_d_position, PERCENT)

    # otherwise stop
    else:
        elbow_motor.stop(BrakeType.HOLD)


def control_claw():
    # L Up to release
    if controller.buttonLUp.pressing():
        claw_motor.spin(REVERSE, 100, PERCENT)

    # R Up to grab
    elif controller.buttonRUp.pressing():
        claw_motor.spin(FORWARD, 100, PERCENT)

    # otherwise stop
    else:
        claw_motor.stop(BrakeType.HOLD)


# MAIN PROGRAM LOOP
# =================

while True:
    control_base_rotator()
    control_shoulder()
    control_claw()
    control_elbow()
