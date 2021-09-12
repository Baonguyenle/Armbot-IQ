# This is a program to control the Armbot with the VEX IQ Controller
# - Base Rotator: L Down to turn left; R Down to turn right
# - Shoulder: joystick A
# - Elbow: Joystick D 
# - Claw: L up release, R up grab 


# IMPORT OBJECTS FROM LIBRARY
# ===========================

from vex import (
    Brain,
    Controller,
    Motor,
    Ports,
    BrakeType, FORWARD, REVERSE, PERCENT
)


# INITIALIZE ROBOT COMPONENTS
# ===========================

# init the Brain
brain = Brain()

# init the Controller
controller = Controller()
controller.set_deadband(20)   # if movement is less than 20%, then consider 0%

# init the Motors
base_rotator_motor = Motor(Ports.PORT10, True)   # reverse direction
shoulder_motor = Motor(Ports.PORT6, True)   # reverse direction
elbow_motor = Motor(Ports.PORT1)
claw_motor = Motor(Ports.PORT4)


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
    # - if up, then raise the shoulder
    # - if down, then lower the shoulder
    joystick_a_position = controller.axisA.position()

    if joystick_a_position != 0:
        shoulder_motor.spin(FORWARD, joystick_a_position, PERCENT)

    # otherwise stop
    else:
        shoulder_motor.stop(BrakeType.HOLD)


def control_elbow():
    # Joystick D 
    joystick_d_position = controller.axisD.position()

    if joystick_d_position != 0:
        elbow_motor.spin(FORWARD, joystick_d_position, PERCENT)

    # otherwise stop
    else:
        elbow_motor.stop(BrakeType.HOLD)



def control_claw():
    # L up: release
    if controller.buttonLUp.pressing():
        claw_motor.spin(REVERSE, 100, PERCENT)
    
    # R up: grab
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
