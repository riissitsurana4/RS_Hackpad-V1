  # RS_Hackpad-V1

Hello everyone!
This is my first hardware project, built as part of **Blueprint (Hack Club)**.

It is a custom macropad made using switches, a rotatory encoder, oled display, etc.

---

## Case Design

The case consists of **two 3D-printed parts**

* **Top plate**
* **Base case**

<img width="523" height="417" alt="Bottom case design" src="https://github.com/user-attachments/assets/218deb73-4f02-4c51-a9ce-5b4de04cbfc2" />

<img width="542" height="451" alt="Top plate design" src="https://github.com/user-attachments/assets/a43d4c59-62ba-40d7-bcbc-98b8a24e86cf" />

---

## PCB Design

The PCB was designed in **KiCad** and includes the following features:

* **8 mechanical switches** arranged in a matrix (4 columns × 2 rows)
* **8 SK6812 RGB LEDs** for underglow
* **1 rotary encoder**
* **0.91 inch OLED display**
* **Seeed XIAO RP2040** as the MCU

The LEDs are placed near the edges of the PCB to create an underglow effect through the case.

<img width="678" height="529" alt="PCB layout" src="https://github.com/user-attachments/assets/dc8ed503-94d7-407f-a9fd-e0e63232056d" />

---
## Final Design
Arranged 3D version of all the parts including the pcb.

<img width="761" height="483" alt="Final PCB render" src="https://github.com/user-attachments/assets/06365c3d-064f-4835-b97d-f71bbf996ca7" />

---

## Firmware

I have made the firmware using **KMK**. 

I have only made basic firmware as it is very confusing and i do not have anything to test on.

---

## BOM

Seeed XIAO RP2040 

Through-hole 1N4148 Diodes (x9)

MX-Style switches (x8)

EC11 Rotary encoders (x1)

0.91 inch OLED displays

SK6812 MINI-E LEDs (x8)

M3x16mm screws & M3x5mx4mm heatset inserts

---
