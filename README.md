## Splitly

## Description

corne  hybrid wireless keyboard based .As it consists of a left part keyboard  connected to pc wired ,and right part keyboard powered by a rechargeable Battery which can operate up to week and connected to left part via bluetooth.And operated by nice Nano and CAT display. And a  numpad with RGB colours, connected wired to pc and powered by pico rp2040 .
## Why it was built
I built this,beacause i always need full split mechanical keyboard,but i need to customize it features by myself.So this keyboard it custosmized to my needings.Also,it has customized features based on usage.Splitly is not just regular keybaord but,desgined to be my companion.
## How to use it / Build it
Firsly,printing all 3d models after that fabricate PCB.After that assemble mx switches,MCU and battery management of pcb.then assemble all this parts together.finally,upload firmware on nice nano and pico,the test all 
## Schematic
I made the schematic and keyboard matrix for the corne keyboard, then the  numpad  .

### Left Part

<img width="1281" height="830" alt="Screenshot 2026-07-29 151332" src="https://github.com/user-attachments/assets/7fc373df-c67f-4e1a-b278-30c3300d975f" />

### Right Part

<img width="855" height="794" alt="Screenshot 2026-07-29 151346" src="https://github.com/user-attachments/assets/444bc069-c6c5-4659-ae42-8b1b5ec42f36" />

### Numpad

<img width="1128" height="774" alt="Screenshot 2026-07-29 165054" src="https://github.com/user-attachments/assets/5753f726-605d-4d95-b758-d277d076299e" />

## PCB
I routed the pcb ,then i outlined the shape of 2 keboard parts and numpad .

### Left Part

<img width="873" height="590" alt="Screenshot 2026-07-29 140454" src="https://github.com/user-attachments/assets/2b0f83ec-4b79-4644-bd26-c08e4eea5d2e" />

### Right Part

<img width="1116" height="634" alt="Screenshot 2026-07-29 151357" src="https://github.com/user-attachments/assets/80f14335-cfa7-4745-9641-f2ef0c3e2be1" />
### Numpad
<img width="903" height="800" alt="Screenshot 2026-07-29 165110" src="https://github.com/user-attachments/assets/cd8a4122-7466-4436-b963-f076522f73a5" />

## CAD
I started   sketching the plate for left & right part keyboard,the i the Enclosure , then the top cover.After that i worked on numpad  plate, then enclosure and top cover,finally i redered them all.

### Left Part

<img width="1216" height="718" alt="Screenshot 2026-07-29 144237" src="https://github.com/user-attachments/assets/05e26893-7be8-475f-948a-f5de75ddb9eb" />
<img width="559" height="417" alt="Screenshot 2026-07-29 144055" src="https://github.com/user-attachments/assets/d8105978-1ad5-4049-881b-d3a4d598f2ba" />
<img width="727" height="558" alt="Screenshot 2026-07-29 175948" src="https://github.com/user-attachments/assets/e6c111f6-6ffe-4eec-8a87-6ac39c609a93" />

### Right Part

<img width="989" height="559" alt="Screenshot 2026-07-29 180152" src="https://github.com/user-attachments/assets/d6f11cf6-6c9c-4a3b-8f54-409cdfda61b6" />
<img width="923" height="493" alt="Screenshot 2026-07-29 180138" src="https://github.com/user-attachments/assets/25f1ae1f-8c9c-4ef1-b90b-799a67c83205" />
<img width="1192" height="696" alt="Screenshot 2026-07-29 180126" src="https://github.com/user-attachments/assets/bed708a5-d5a1-4a52-a5c4-f102fc7b7219" />
<img width="912" height="520" alt="Screenshot 2026-07-29 180047" src="https://github.com/user-attachments/assets/5c645c49-4c7a-4a7d-9140-ae73383b03cd" />

### Numpad

<img width="1053" height="591" alt="Screenshot 2026-07-29 214557" src="https://github.com/user-attachments/assets/06b257c2-8393-4052-9258-a6992f31f725" />
<img width="896" height="697" alt="Screenshot 2026-07-29 214609" src="https://github.com/user-attachments/assets/4dab3999-c26a-4a51-8d1a-5665c0898947" />
<img width="1019" height="652" alt="Screenshot 2026-07-29 214643" src="https://github.com/user-attachments/assets/e0c1257d-e595-4abf-949f-7245a4592786" />
<img width="847" height="557" alt="Screenshot 2026-07-29 214633" src="https://github.com/user-attachments/assets/aca7094f-167a-4b83-a708-093e59ebe3fd" />


 

## Firmware
I used kmk with CircuitPython as firmware,and made code for the left  & right part which is keyboard and the numpad

### Left Part

<img width="727" height="302" alt="Screenshot 2026-07-29 154041" src="https://github.com/user-attachments/assets/a7b9f5d4-9019-4d62-99b8-6796508d379e" />
<img width="788" height="322" alt="Screenshot 2026-07-29 154053" src="https://github.com/user-attachments/assets/2a306568-f3f2-4692-8cae-a73b42affca3" />
<img width="780" height="525" alt="Screenshot 2026-07-29 154101" src="https://github.com/user-attachments/assets/6128b179-6638-4fff-add2-fc7439a407a4" />
<img width="688" height="729" alt="Screenshot 2026-07-29 154108" src="https://github.com/user-attachments/assets/bc0fff06-0bf1-41d3-bf5b-70ec6c2b3639" />

### Right Part

<img width="487" height="236" alt="Screenshot 2026-07-29 154227" src="https://github.com/user-attachments/assets/fd9a284a-bda1-4463-9967-6010fd9ec6c4" />
<img width="753" height="808" alt="Screenshot 2026-07-29 154236" src="https://github.com/user-attachments/assets/fb3f3be1-8035-4c54-a074-109b93fbdec9" />
<img width="827" height="163" alt="Screenshot 2026-07-29 154240" src="https://github.com/user-attachments/assets/5cd6257f-94ec-4f7b-bd26-b0e4c2bb9467" />

### Numpad
<img width="896" height="830" alt="Screenshot 2026-07-29 184534" src="https://github.com/user-attachments/assets/f61eeaa1-5793-41c8-b75c-4645f261b729" />

## BOM 
I made the BOM  and needed materials ,in egypt then convert its price to USD dollar.
<img width="1893" height="526" alt="Screenshot 2026-07-29 185849" src="https://github.com/user-attachments/assets/d81c4fa9-b6bf-4b9c-8c44-378c825d144f" />

