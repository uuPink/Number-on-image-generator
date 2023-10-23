import os
from number_translation import translate_number

def clear_cache(file = "numbers.txt"):
    print("Attempting to delete old cache in file '" + file + "'...")

    if os.path.isfile(file):
        os.remove(file)
        print("—————File has been deleted")
    else:
        print("—————File does not exist and therefore has not been deleted")

def cache_numbers(debug: bool):
    #137 -> 857

    with open("numbers.txt", "a") as f:
        for i in range(137, 858):
            translation = translate_number(i)
            f.write(translation + "\n")
            
            if debug:
                print(translation)

def main(reset: bool, debug: bool, blitter: bool):
    if reset:
        clear_cache()
    
    cache_numbers(debug = debug)

    if blitter:
        import blitter

if __name__ == "__main__":
    main(reset = False, debug = False, blitter = True)