﻿Задание:
Л.р. 4: Изучение внеполосного режима передачи данных.

Модифицировать программу из л/р № 3: во время передачи данных с использованием протокола TCP, передающая сторона должна генерировать внеполосные данные и выводить на экран общее количество переданных байт данных (не включая срочные), принимающая сторона должна выводить на экран общее количество принятых байт (не включая срочные) при получении срочных данных.
Инструкция по запуску:
	
	1) python main.py client - запуск клиента
	
	2) python main.py server - запуск сервера
	
	3) следовать дальнейшим указаниям (номер порта сервера должен быть введен ранее, чем у клиента)