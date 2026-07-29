author: Youssef Ayman Mohamed

description: Closed feedback greenhouse system for lettuce and pepper plants in Egypt. Controlled by ESP.
 
created_at: "2026-07-15"

## Entry 1 
created at:2026-7-15

### Content 
During this session, I  mainly worked on searching for and sketching out the workflow and materials.Firstly,i searched about split keyboard types and found corne keyboard layout achieve my requirments ,from size and distrubution of keys,after that,i watched videos and searched about corne keyboard keycomponets.and most 
of them use Nice Nano as Mcu and it does not require power chargers as it has it own.
<img width="786" height="521" alt="Screenshot 2026-07-29 131906" src="https://github.com/user-attachments/assets/8cd1ce35-3afc-464e-9b8c-be4041add7cf" />
After that, i use draw.io to sketch keyboard worflow.i starting adding MCU ,after watching  video about wireless keyboard connection and MCu.then i started adding switches,which wil be cherry mx and dsa keycaps,and searched on reddit about corne layout.then i added display chossing oled 128*32.

I decided left part,will be wired connection because display,and right part will connect to wireless.then i starting seacrhing for sutiable battery for rigth part.
Finally,i searched for numpad and mcu i will use (pico rp 2040) ,then i added it to workflow and will be connected to pc wired ,beacuse of oled 128*64 and rgb light in numpad.
<img width="1041" height="446" alt="Screenshot 2026-07-29 131850" src="https://github.com/user-attachments/assets/8e46c557-a0c7-41cc-9cb2-b40eb07acc2c" />
<img width="1230" height="601" alt="Screenshot 2026-07-29 123833" src="https://github.com/user-attachments/assets/00bf0838-ca77-4b2c-bedf-cb42f53429fd" />

### Recording (44 min) :
https://lapse.hackclub.com/timelapse/c5cdFFcw_wo8


## Entry 2
created at:2026-7-15

### Content 
During this session ,i worked mainly of left part schematic & PCB.firstly,First, I added and organized a switch from Scottkeebs' library based on my keyboard layout. Then I started connecting the switches in rows and columns , forming a keyboard matrix.
After that,i add nice nano ,i started connecting columns & rows of matrix to it.and added rectangles to each part such as matrix and nicnano,adding some organizing in schematic.then i added oled screen ,and connect it to nice nano.then assigned footprint for each componets.
<img width="1337" height="803" alt="Screenshot 2026-07-29 140726" src="https://github.com/user-attachments/assets/077cc1d9-4bd6-4cc9-8746-5deab8ac0abb" />

After that,i worked on pcb,i uploaded left part json file,and upload it to keyboard library on kicad to organize layout.but it lack ,as switched names were missing.then i cotinued adding 3d model for oled and nice nano.
After that,while i routing i found sw order was wrong switches coming another in same row.then i started edit on their name to be accurate order.And started routing sws and align diodes with their switches.then i started routing matrix and oled to nice nano.
<img width="873" height="590" alt="Screenshot 2026-07-29 140454" src="https://github.com/user-attachments/assets/5cddd3eb-205e-44a8-9eef-79895fb6da66" />
After , that i added mounting holes for m3 screws,to set pcb on enclosure.after that,i reroute pcb edge cuts lines.
Finally,i added filled zones on top for Vcc and lower for GND.
<img width="1148" height="776" alt="Screenshot 2026-07-29 140504" src="https://github.com/user-attachments/assets/43bddc5e-bfc3-4fbd-8032-6eaf35d77446" />

### Recording (2 hour & 2 min) :

https://lapse.hackclub.com/timelapse/jyOiTPzKX9hP

## Entry 3
created at:2026-7-16

### Content 
During this session ,i worked mainly of left part 3d models and assembly.firstly,i uploaded pcb 3d model to fusion,then started project pcb outline , switches ,MCU and oled.after that, i uploaded projected dxf and worked on plate.Firslty,i routed plate outline leaving space between pcb and plate sketch.after that, i offest it and adding filleset on edges.after that,i checked plate aligment with pcb using section analaysis.
Then,i started adding switches opening based on sketch.then check switches aligment with openig and hanged on its edges.after that,i extruded plate by 3mm,and added moutning holes at edges to,where m3 screws will attached to enclosure.finally,cutting rectangle area in plate for nice nano and display oled.
<img width="561" height="388" alt="Screenshot 2026-07-29 143937" src="https://github.com/user-attachments/assets/9eb2ee26-80bc-4bd1-ae61-8c8d33dad87a" />
<img width="559" height="417" alt="Screenshot 2026-07-29 144055" src="https://github.com/user-attachments/assets/324f07d2-feb9-45a3-acee-42f3a1cc2f1d" />

Secondly,i worked on main enclosure.firtly, i extruded it based on plate sketch dxf file,then extrude the bottom layer by 2 mmm, then i checked it height with pcb using section analysis,and adjust its height.after that, i cut 5.5 circle from the bottom mounting holes,where m3 head will be in ,with heigth 3mm.
After that,i checked heatinsert dimesnions ,and aligment of enlcosure and pcb heigth in it.then extrude circle with diamter of heatinsert.in which srews will be in it and hold pcb at specific heigth, preventing PCB pins attach bottom layer.
<img width="559" height="412" alt="Screenshot 2026-07-29 143924" src="https://github.com/user-attachments/assets/f3db7c99-acf3-4c4d-bd68-b04e62405028" />
<img width="1216" height="718" alt="Screenshot 2026-07-29 144237" src="https://github.com/user-attachments/assets/5fa9a4af-d38d-41e8-8de1-a0d5b89ebb61" />
After that,i assembled all togehter and check aligment.then i started adding keycapd for switches,after that i started adding srews and heat insert and checking aligment by section analsis form top and rigth,then added battery.then,i sketched nice nano usb opening ,then cut it from plate and enclosure.
After that,i worked on top cover,extrude it with same plate dxf file.and adding covering rectangle for nicnano.then i started cut form the back mounting holes for heatinsert that connected srews of enclosure.then,i assembled all together ,and adding enclosure srews and heatinsert.
then,sign my name on top cover and exlode text,also signed arcana name on plate.
<img width="752" height="408" alt="Screenshot 2026-07-29 144200" src="https://github.com/user-attachments/assets/19724778-6e2c-4df4-8fe5-7f48612aea74" />

Finally,i worked on render it,trying different colours,and choosed black ,white and gold.

<img width="408" height="305" alt="Screenshot 2026-07-29 143900" src="https://github.com/user-attachments/assets/6458e4b4-0e57-4a7a-85e0-7ba67968e4d6" />

### Recording (3 hour & 55 min) :

https://lapse.hackclub.com/timelapse/jyOiTPzKX9hP

## Entry 4
created at:2026-7-17

### Content 

During this session ,i worked mainly of right part schematic & PCB.firstly,i sketched process diamgram of keyboard connection,and the type of connection to each part.
<img width="1281" height="830" alt="Screenshot 2026-07-29 151332" src="https://github.com/user-attachments/assets/19716877-5b8d-4f7d-9a7b-de7a7f3647f2" />

then, I added and organized a switch from Scottkeebs' library based on my keyboard layout. Then I started connecting the switches in rows and columns , forming a keyboard matrix.After that,i add nice nano ,i started connecting columns & rows of matrix to it.and added rectangles to each part such as matrix and nicnano,adding some organizing in schematic.then i searched of slide sw name on kicad,then starting adding power managemnet,adding switches,and jst pin header that connected to battery,then route jst with switch and nicenano.then assigned footprint for each component.
<img width="855" height="794" alt="Screenshot 2026-07-29 151346" src="https://github.com/user-attachments/assets/38187dd4-99aa-4e4b-ba44-7ef61f93aaea" />
<img width="322" height="305" alt="Screenshot 2026-07-29 151413" src="https://github.com/user-attachments/assets/9c786b36-e994-424c-8d22-6c2601127e29" />

After that,i worked on pcb,i uploaded rigth part json file,and upload it to keyboard library on kicad to organize layout.then i cotinued adding 3d model for nice nano.After that,while i routing i found sw order was wrong switches coming another in same row.then i started edit on their name to be accurate order.After , tt i added mounting holes for m3 screws,to set the PCB on enclosure then, i route pcb edge cuts lines. and adding fillset ant corners,And started routing sws and align diodes with their switches.then i started routing matrix  to nice nano.then,i adjust jst pin header location,to be engouh space for battery. After , tt iha added mounting holes for m3 screws,to set the PCB on enclosure.After that, i route pcb edge cuts lines.
Finally,i added filled zones on top for Vcc and lower for GND.
<img width="1116" height="634" alt="Screenshot 2026-07-29 151357" src="https://github.com/user-attachments/assets/59047130-e254-449d-b481-5df54d6ec16b" />
<img width="998" height="648" alt="Screenshot 2026-07-29 151404" src="https://github.com/user-attachments/assets/074e5730-db0d-45c1-a5c2-37306b28ac2a" />

### Recording (2 hour & 16 min) :

https://lapse.hackclub.com/timelapse/1gOH3Y6zuYtc
https://lapse.hackclub.com/timelapse/MOm_24O0OcwB

## Entry 5
created at:2026-7-18

### Content 
During this session,  I worked manily on main keyboard firmware,i used kmk python version,and i will add more update on code during buidling and test project.
Firstly, I created the main file for the left part. then starting intializing and importing libraries, and import library for displa, HID, and kmk keyboard libraries.
<img width="727" height="302" alt="Screenshot 2026-07-29 154041" src="https://github.com/user-attachments/assets/61b44321-da27-4399-8ce4-0b687085df6d" />

Then, I started defining the keyboard  matrix GPIO pins in the MCU.then making layers and modtap to customize more functions in the same switch.
Then, I defined my keymap, by 4 layers, the first one for alphabetical and the other  layers for other full keyboard switches such as Fn switches.
<img width="788" height="322" alt="Screenshot 2026-07-29 154053" src="https://github.com/user-attachments/assets/cae04295-95b7-4322-808b-f6d682e63496" />

<img width="688" height="729" alt="Screenshot 2026-07-29 154108" src="https://github.com/user-attachments/assets/1d3d8878-561e-4a22-b80c-4d4c256a348a" />

Secondly,i iniatize display screen ,then define it pins,after that , i make it show my name on the top and cat image,then i set it properties from heigth ,brigthness and increase brigtness by 0.2 for 500 ms.
After that, I initialize ae wireless HID connection,where the right part will be connected to it.
<img width="780" height="525" alt="Screenshot 2026-07-29 154101" src="https://github.com/user-attachments/assets/1d631294-dcba-4a4f-beba-4e37c29b1735" />

In the second file(right.py) for the right part, then starting intializing and importing libraries, and import library for HID and kmk keyboard libraries.

<img width="487" height="236" alt="Screenshot 2026-07-29 154227" src="https://github.com/user-attachments/assets/155c81a3-5049-47e7-8cbd-aa837a114a71" />

Then, I started define keyboard  matrix GPIO pins inthe  MCU.then making layers and modtap to customize more functions in same switch.
Then, I defined my keymap, with 4 layers, first one for alphabetical and the  other  layers for other full keyboard switches such as Fn switches.
<img width="753" height="808" alt="Screenshot 2026-07-29 154236" src="https://github.com/user-attachments/assets/4fdc71b9-7037-48cd-a0d6-bf6e937f79eb" />

Finally, i initalize in it with a wireless connection and define it displaying name.
<img width="827" height="163" alt="Screenshot 2026-07-29 154240" src="https://github.com/user-attachments/assets/755b2355-fb14-4af2-ae07-87ea6e48933b" />

### Time (1 hour & 36 min) :

## Entry 6
created at:2026-7-29

### Content 
During this session,i worked mainly on numpad schematic & PCB, firstly,i started adding switches and order them into matrix based on numpad layout.then,i added diodes and route columns and rows together.then i added pico symbol from scotto library, then i added 2 ec11 switch rotary encoder,and connect their switch pins  to matrix on  row 1
after that,i added row and columns flags.
<img width="479" height="446" alt="Screenshot 2026-07-29 165135" src="https://github.com/user-attachments/assets/cd03cdd2-d604-480a-ad41-561442eae540" />
Then, i added oled 128*64 and added it pins flags,then i added 2 rgb ws8b128 leds and define their pins flags.finally,i routed all flags in pico.And add organizing rectangles to each part such as pico pinout.then,i assign footprint to components, and adding mouting holes for m3 screws.
<img width="1128" height="774" alt="Screenshot 2026-07-29 165054" src="https://github.com/user-attachments/assets/1498c56c-3796-4a9b-be68-da5148d16547" />
Secondly,i update pcb , and upload json file to keyboard library to organize switches.but it found issues in organize encoders in matrix,so i did it manually.Then, i found some switches order were wrong, so i redit their names.then,i started routing keyboard matrix.then, i added encoders ,oled and pico 3d models.
After that, i continued routing another parts,and flibbed rgb leds to back layer.,then adding filling zone on top layer for vcc and on on lower for GND.finally,i worked on solvind appeared DRC errors ,then sign my name on PCB,then export pcb step file and gerbers.
<img width="903" height="800" alt="Screenshot 2026-07-29 165110" src="https://github.com/user-attachments/assets/11d63524-538d-473b-a5eb-6593346e4ae2" />
<img width="907" height="884" alt="Screenshot 2026-07-29 165123" src="https://github.com/user-attachments/assets/5abae53e-5a2f-40de-a025-49a203a41238" />

### Recording (1 hour & 25 min) :

https://lapse.hackclub.com/timelapse/xZpGC4tF1jRX

