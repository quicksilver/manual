# Command Line Tool

Allows data to be piped into Quicksilver from the command line.

 Summary                    | &nbsp; 
---------------------------:|:--------------------
 Available on macOS version | 10.11, 10.12, 10.13
      for Quicksilver build | 4024


The `qs` command allows you to select files or text in Quicksilver (or send
them to the Shelf) from the command line.

Select a file:

    
    
    qs MyFile.jpg
    qs ~/Documents
    

Select multiple files:

    
    
    qs file1.txt file2.txt
    qs *.pdf
    

Select text:

    
    
    echo example | qs
    echo "example with multiple words" | qs
    whoami | qs
    pbpaste | qs
    

Note that when you pipe text to `qs`, the same smarts apply that you would get
when typing text by hand. URLs, file paths, etc. are automatically recognized
and the appropriate action will be displayed in Quicksilver's interface.

To send an item to the Shelf instead of selecting it, use the `-s` option.

    
    
    qs -s ~/Documents/MyMainProject