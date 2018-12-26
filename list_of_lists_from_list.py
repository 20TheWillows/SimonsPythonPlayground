from myPackages.nima_emulation import nima_row
import uuid
import random



def main():
    # Create a list of rows
    rows = [ nima_row(uuid.uuid4(), 
                      random.randint(50,100)/2,
                      str(random.randint(100,200)),
                      random.randint(1,10)) for i in range(1,21) ]
    print(*rows, sep='\n')






    

if __name__ == "__main__":
    main()