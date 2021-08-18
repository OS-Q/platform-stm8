/**
  \file config.h

  \brief set project configurations

  set project configurations like used device or board etc.
*/

/*-----------------------------------------------------------------------------
    MODULE DEFINITION FOR MULTIPLE INCLUSION
-----------------------------------------------------------------------------*/
#ifndef _CONFIG_H_
#define _CONFIG_H_


/*----------------------------------------------------------
    INCLUDE FILES
----------------------------------------------------------*/
#if defined(STM8S_DISCOVERY)
  #include "STM8S105C6.h"
  #define LED_PORT   sfr_PORTD
  #define LED_PIN    PIN0
  //print this out as an info during compilation
  #warning "[INFO] USING STM8S_DISCOVERY PIN MAP"
#elif defined(STM8S_NUCLEO_207K8)
  #include "STM8S207K8.h"
  #define LED_PORT   sfr_PORTC
  #define LED_PIN    PIN5
  //print this out as an info during compilation
  #warning "[INFO] USING NUCLEO_8S207K8 PIN MAP PORTC PIN5"
#elif defined(STM8S_NUCLEO_208RB)
  #include "STM8S208RB.h"
  #define LED_PORT   sfr_PORTC
  #define LED_PIN    PIN5
  //print this out as an info during compilation
  #warning "[INFO] USING NUCLEO_8S208RB PIN MAP PORTC PIN5"
#elif defined(STM8L_DISCOVERY)
  #include "STM8L152C6.h"
  #define LED_PORT   sfr_PORTC
  #define LED_PIN    PIN7
#elif defined(STM8_SO8_DISCO_STM8S001)
  #include "STM8S001J3.h"
  #define LED_PORT   sfr_PORTA
  #define LED_PIN    PIN3
#elif defined(SDUINO)
  #include "STM8S105K6.h"
  #define LED_PORT   sfr_PORTC
  #define LED_PIN    PIN5
#elif defined(MUBOARD)
  #include "STM8S207MB.h"
  #define LED_PORT   sfr_PORTH
  #define LED_PIN    PIN2
#else
  #include "STM8S103F3.h"
  #define LED_PORT   sfr_PORTB
  #define LED_PIN    PIN5
  #warning "[INFO] USING STM8S103F3 PINMAP PORTB, PIN 5"
#endif


/*-----------------------------------------------------------------------------
    END OF MODULE DEFINITION FOR MULTIPLE INLUSION
-----------------------------------------------------------------------------*/
#endif // _CONFIG_H_
