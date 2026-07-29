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
