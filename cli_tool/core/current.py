def current(
        options: str,
        *args: tuple[str]
):

    # Checks if there is any argument input
    if args[0]:

        # If there is an argument, try to convert it to an int
        try:
            input = int(args[0][0])
            
        # Handle this fail case nicer I think?    
        except ValueError:
            return False
        
    ignore = []

    for opt in options:

        # Add options to ignore if they are no longer valid. Eg repeats or multiple inputs       
        if opt in ignore:
            continue

        match opt:

# Pretty happy with this now. Just need to figure out how to replace the print
# statements with the actual Spotify API calls 

# Control commands. Can all be called whenever
            # Play/pause
            case 'p':
                
                # Remove any other instances of p
                ignore.append('p')

                print(f"Pausing/Playing")
            
            # Skip
            case 's':

                ignore.append('s')
            
                print(f"Skipping current song")
            
            # Replay
            case 'r':

                ignore.append('r')
                print(f"Replaying last song")
            
            
# Input controls. Only 1 can be called each command, and require an input
            # Scrub forward. Use input for this
            case 'f':
                if not args[0]:
                    return "ERROR. NO INPUT"
                else:
                    ignore.extend(['f', 'b', 'u'])

                    print(f"Scrubbing forward by {input} seconds")
                
            # Scrub back. Use input for this
            case 'b':
                if not args[0]:
                    return "ERROR. NO INPUT"
                else:
                    ignore.extend(['f', 'b', 'u'])

                    print(f"Scrubbing back by {input} seconds")
            
            # Volume change. Use input for this
            case 'u':
                if not args[0]:
                    return "ERROR. NO INPUT"
                else:
                    ignore.extend(['f', 'b', 'u'])

                    print(f"Changing volume to %{input}")

# Info commands. Can all be called whenever
            # Return queued songs. Use input for this
            case 'q':

                ignore.append('q')
                print(f"Next 5 queued songs")
            
            # Return current song info
            case 'n':
                ignore.append('n')
                print(f"Current song is")
            
            # Return current volume
            case 'v':
                ignore.append('v')
                print(f"Current volume is")
