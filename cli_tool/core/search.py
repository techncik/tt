def search(
        options: str,
        input: tuple[str]
):

    # Need to have some sort of handling for clashing options.
    # Eg, if options are 'spa', this means shuffle a playlist and album.
    # In this case, I think we just take the first input
    INDIVIDUAL_SEARCHES = ['a', 'r', 'p', 'm', '.']

    searched = ' '.join(input)
    searched_type = ""

    ignore = []

    # Once again I think the logic is sound here, aside from maybe tightening
    # the order of operations in terms of shuffling and queueing.
    # Would be good to just put S and Q at the back of the options regardless.'

    # Just need to implement the Spotify calls now, and then this might
    # be operational in a MVP

    for opt in options:

        if opt in ignore:
            continue

        match opt:

            # Search for an album
            case 'a':
                #some api call

                ignore.extend(INDIVIDUAL_SEARCHES)
                searched_type = "album"
                print(f"Searching for the album {searched}")
            
            # Search for a playlist
            case 'p':
                ignore.extend(INDIVIDUAL_SEARCHES)
                searched_type = "playlist"
                print(f"Searching for the playlist {searched}")
            
            # Search for a radio
            case 'r':
                ignore.extend(INDIVIDUAL_SEARCHES)
                searched_type = "radio"
                print(f"Searching for the radio {searched}")
            
            # Add searched thing to the queue
            case 'q':
                ignore.append('q')
                print(f"Adding {searched} to the queue")
            
            # Shuffle searched thing. Needs either an album, playist, or radio
            case 's':
                ignore.append('s')
                if not searched:
                    print(f"Nothing to be shuffled")

                    # TODO; Remove continues
                    continue
                if searched_type == "song":
                        print(f"Can't shuffle a single song")
                        continue
                print(f"Shuffling {searched_type}")
            
            # Search and play an artist
            case 'm':
                ignore.extend(INDIVIDUAL_SEARCHES)
                searched_type = "artist"
                print(f"Searching for the artist {searched}")
            
            # Search for a single song
            case '.':
                ignore.extend(INDIVIDUAL_SEARCHES)
                searched_type = "song"
                print(f"Searching for the song {searched}")
        
