

all: elso.so

%.so: %.o
	gcc --shared -o $@ $<

%.o: %.asm
	nasm -f elf64 -o $@ $<

clean:
	-rm ./*.o
	-rm ./*.so