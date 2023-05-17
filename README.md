# auto_message_sending
Automated sending messages to telegram and whatsapp through a mobile phone operating system emulator

You can use any mobile phone operating system emulator, such as Andriod Studio or Genymotion You can also deploy Android in a Docker container

You must correctly specify the properties of the operating system, its version, etc. (an example is given in desired_caps), socket - the ip and port on which the emulator is deployed.

Using this script, actions are automatically performed on the phone to send messages in messengers (for a more believable emulation of user actions, you can put time.sleep(...) before some actions)
