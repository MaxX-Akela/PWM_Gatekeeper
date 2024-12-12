# PWM_Gatekeeper

<img src="PWM_Gatekeeper/www/SibRoboFest_Led_On.png" align="right" width="400px" >
<img src="PWM_Gatekeeper/www/SibRobaFest_Led_Off.pngf.png" align="down" width="400px" >


Широко Импульсная Модуляция

Наша дружная команда состоит из трех человек: Программист-инженер,Специалист по документации дизайнер.
Мы живем в городе Новосибирске и на хакатоне "СибРобоФест" представляем ЦЦО "ITcube" на базе 22 лицея «Надежда Сибири»

# О нашем проекте
"Gatekeeper" – это система автоматического обнаружения пролета дронов через определенную зону, обозначенную воротами. Система использует компьютерное зрение и лазерный дальномер для распознавания дронов. При обнаружении дрона над воротами, встроенная светодиодная лента на самих воротах начинает мигать интенсивным красным светом, сигнализируя о пролете.

Проблема: Отсутствие быстрого и надежного способа обнаружения и сигнализации о пролете дронов в контролируемой зоне. Существующие методы могут быть неточными, медленными или требовать ручного наблюдения.
Решение: "Gatekeeper" предлагает автоматизированное решение, 

# Описание электронной составляющей проекта
Подробное описание выполнения электронной части проекта
Из чего состоит эл.часть проекта, как запрогана, как работает, есть ли недочеты.
В нашем проекте используется микрокомпьютер Raspberry pi 4 B 2gb, на который стоит, [ROS](https://www.ros.org) операционная система для роботов. Светодиодная лента ws281x которая позволяет управлять отдельными светодиодам, а также всеми вместе, также на нашем образе для RPI предустановлена ROS библиотека для работы с ws281x.
Также мы используем Дальномер VL53L1X и УЗ HC-400. Благодаря им мы можем следить за изменением расстоянии и при  резком изменении расстояния они дают сигнал на ленту и за счёт этого осущетвляется индикация.

