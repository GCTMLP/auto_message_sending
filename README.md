# auto_message_sending
Автоматизированная отправка сообщений в telegram и whatsapp через эмулятор операционной системы мобильного телефона

Можно использовать любой эмулятор операционной системы мобильного телефона, например Andriod Studio или Genymotion
Лично я разворачивал Андройд в Docker-контейнере

Необходимо правильно указать свойства операционной системы ее версию и т.д. (в desired_caps приведен пример), socket - ip и порт, на котором развернут эмулятор.

При помощи данного скрипта в автоматическом режиме производятся действия на телефоне для отправки сообщений в мессенджерах (для более правдоподобной эмуляции действий пользователя можно поставить time.sleep(...) перед некоторыми действиями)
