# create dictionary
playlist = {
    "The sound of silence": {"artist": "Disturbed", "genre": "Rock"},
    "Demons": {"artist": "Imagine Dragons", "genre": "Pop-rock"},
    "A sky full of stars": {"artist": "Coldplay", "genre": "Pop"},
    "A bar song": {"artist": "Shaboozey", "genre": "Country"},
    "Hold me": {"artist": "Eminem/Teddy Swims", "genre": "Alternative"},
    "Don't give up on me": {"artist": "Andy Grammer", "genre": "R&B soul"}
}

# add a song
def add_song():
    try:
        song_title = input("Please enter your song title: ")
        song_artist = input("Please insert the artist: ")
        song_genre = input("Please insert genre: ")
        # used strip to remove whitespace
        if not song_title.strip() or not song_artist.strip() or not song_genre.strip():
            raise ValueError("You must add the song name, artist, and genre.")
        playlist[song_title] = {"artist": song_artist, "genre": song_genre}
    # exception
    except ValueError as e:
        print(e)
    else:
        print(f"Song '{song_title}' was added successfully.")

# view playlist
def view_playlist():
    if not playlist:
        print("Your playlist is empty!")
        return
    print("\nHere is your playlist:")
    for song in playlist:
        print(f"{song} by {playlist[song]['artist']} (Genre: {playlist[song]['genre']})")

# update song's details
def update_song():
    song_title = input("Enter the song title to update: ").strip()
    if song_title in playlist:
        new_artist = input("Enter the new artist: ").strip()
        new_genre = input("Enter the new genre: ").strip()

        if not new_artist or not new_genre:
            print("Artist and genre fields cannot be empty.")
            return
        playlist[song_title] = {"artist": new_artist, "genre": new_genre}
        print(f"Updated: '{song_title}' to {new_artist}, Genre: {new_genre}")
    else:
        print("The song you are trying to update is not in the playlist.")

# delete a song
def delete_song():
    song_title = input("Enter the song title to delete: ").strip()
    if song_title in playlist:
        del playlist[song_title]
        print(f"Deleted '{song_title}' from the playlist.")
    else:
        print("The song you are trying to delete is not in the playlist.")

# user choice 
while True:
    print("\nWhat would you like to do?")
    print("1. Add a Song")
    print("2. View Playlist")
    print("3. Update a Song")
    print("4. Delete a Song")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ").strip()

    if choice == "1":
        add_song()
    elif choice == "2":
        view_playlist()
    elif choice == "3":
        update_song()
    elif choice == "4":
        delete_song()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
