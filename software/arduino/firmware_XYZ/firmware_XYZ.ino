
#include <CommandHandler.h>
#include <CommandManager.h>
CommandManager cmdMng;

#include <AccelStepper.h>
#include <LinearAccelStepperActuator.h>
#include <CommandLinearAccelStepperActuator.h>

AccelStepper stp_X(AccelStepper::DRIVER, 54, 55);
CommandLinearAccelStepperActuator X(stp_X, 3, 38);

AccelStepper stp_Y(AccelStepper::DRIVER, 60, 61);
CommandLinearAccelStepperActuator Y(stp_Y, 14, 56);

AccelStepper stp_Z(AccelStepper::DRIVER, 26, 28);
CommandLinearAccelStepperActuator Z(stp_Z, 18, 24);

void setup()
{
  Serial.begin(115200);

  X.registerToCommandManager(cmdMng, "X");
  Y.registerToCommandManager(cmdMng, "Y");
  Z.registerToCommandManager(cmdMng, "Z");


  cmdMng.init();
}

void loop()
{
  cmdMng.update();
}
