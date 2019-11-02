# Stepper-Motor

The Arduino version is the .ino file

The ESP version for micropython is under the ESP folder

esptool.py --port COM5 erase_flash
esptool.py --port COM5 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp`autocomplete`