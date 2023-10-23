# Number-on-image-generator
Image generator made with Pygame that prints all Swedish numbers from 137 -> 857 on the screen.

Run main.py with preferred arguments to get your result.
  
  args:
    
    reset: If True creates a new numbers.txt containing your numbers. If False uses your already created numbers.txt
    
    debug: If True sends debug messages from number caching. If you create your own translate_number function this will not work unless you implement it in your function.
    
    blitter: If True opens pygame and does the blitting after optional caching is done

You can create your own translate_number function to add your own language. The method used for Swedish numbers is kind of brute-force but it works.

You can (and should) change font and gaps between letters to get the range you want to fit in the screen size you want. A lot of tweaking is necessary in most cases.

Example result with Swedish numbers 137 -> 857:
![numbers](https://github.com/uuPink/Number-on-image-generator/assets/94691152/e33ae7f6-d3b3-41bf-a362-1b71d12d7a5d)
