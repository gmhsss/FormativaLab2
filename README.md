# FormativaLab2
Este projeto consiste em um sistema de alarmes para monitoramento de ambientes industriais utilizando placas ESP32 e sensores. O sistema foi desenvolvido para detectar condições críticas de temperatura e umidade, acionando sistemas de ventilação e alertas conforme necessário.



## Funcionalidades
Monitoramento de Temperatura e Umidade:

A ESP32 monitora dois ambientes diferentes.
Utiliza sensores para medir temperatura e umidade.
Controle de Sistemas de Ventilação:

Ambiente 1: Se a temperatura atingir 60°C, o servo motor 1 abre a comporta do sistema de ventilação para 50°.
Ambiente 2: Se a temperatura atingir 60°C, o servo motor 2 abre a comporta do sistema de ventilação para 180°.
Controle de Alertas de Umidade:

Se a umidade em qualquer ambiente for inferior a 20%, uma mensagem é enviada para a ESP2.
A ESP2 então emite um alerta sonoro com um buzzer e pisca um LED a cada 1 segundo.
Quando a umidade normaliza, a ESP1 envia uma mensagem para a ESP2 para desativar os alertas.
Prioridade de Desativação:

ESP2: Um slide switch permite desativar os alarmes, independentemente da umidade.
ESP1: Um slide switch permite desativar o envio de mensagens para a ESP2 e retornar os servos para 0 graus.
Uso de Threads:

O sistema utiliza threads para gerenciar as operações de monitoramento e controle simultaneamente.



## Conclusão
Este sistema é uma solução para o monitoramento e controle de ambientes industriais, utilizando placas ESP32 e diversos sensores. A implementação de threads garante uma operação eficiente e simultânea das funcionalidades.

---

**Autores**: Anthony Sutil, Pedro Martins, Rafaella Somoza
**Data**: 20/08/2024
