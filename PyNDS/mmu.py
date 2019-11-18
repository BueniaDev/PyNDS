import sys

class MMU:
    def __init__(self):
        self.bios9 = bytearray(4096)
        # Initialization code

    def loadarm9bios(self, filename):
        bios9file = open(filename, "rb").read()

        if len(bios9file) != 4096:
            print("MMU::Error - Incorrect ARM9 BIOS size")
            sys.exit(1)
        
        for i in range(0, len(bios9file)):
            self.bios9[i] = bios9file[i]

        print("MMU::ARM9 BIOS succesfully loaded.")

    def readLongarm9(self, addr):
        if addr < 0xFFFF0000:
            return 0xFFFFFFFF
        else:
            tempaddr = (addr - 0xFFFF0000)
            tempval = 0

            for i in range(0, 4):
                tempval |= (self.bios9[tempaddr + i] << (i * 8))

            return tempval
