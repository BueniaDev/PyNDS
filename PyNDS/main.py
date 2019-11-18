import sys
from mmu import MMU

def main():
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " BIOS9")
        sys.exit(1)

    mem = MMU()
    mem.loadarm9bios(sys.argv[1])
    print(hex(mem.readLongarm9(0xFFFF0000)))

if __name__ == "__main__":
    main()
    
