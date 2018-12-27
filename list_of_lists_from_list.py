from myPackages.nima_emulation import nima_row
import uuid, random

NIMA_ROWS = []


def main():
    # Create a list of rows
    NIMA_ROWS = [ nima_row(uuid.uuid4(), 
                      random.randint(50,100)/2,
                      str(random.randint(100,200)),
                      random.randint(1,10)) for i in range(1,21) ]
    print(*NIMA_ROWS, sep='\n')

    # Get a list of list of arrtibutes
    the_list_of_lists = list(zip(*((row.identifier, row.float_val, row.string_val, row.int_val) for row in NIMA_ROWS)))

    ids = the_list_of_lists[0]
    floats = the_list_of_lists[1]
    strings = the_list_of_lists[2]
    ints = the_list_of_lists[3]

    print(floats)
    print(type(floats))





    

if __name__ == "__main__":
    main()