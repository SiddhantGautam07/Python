import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            try:
                videos = json.load(file)
                return videos
            except json.decoder.JSONDecodeError:
                # If file is empty or has invalid JSON, return empty list
                return []
    except FileNotFoundError:
        # Create a new file with empty list
        with open('youtube.txt', 'w') as file:
            json.dump([], file)
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print()
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration : {video['time']}")
    print()
    print("*" * 70)



def add_video(videos):
    name = input("Enter Video name : ").strip()
    if not name:
        print("Video name cannot be empty")
        return
    time = input("Enter Video Time : ").strip()
    if not time:
        print("Video time cannot be empty")
        return
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter your video number to update : "))
        if 1 <= index <= len(videos):
            name = input("Enter your video name : ")
            time = input("Enter your video time : ")
            videos[index -1] = {'name':name, 'time': time}
            save_data_helper(videos)
        else:
            print("Invalid Index Selected")
    except ValueError:
        print("Please enter a valid number")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted : "))
    if 1<= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid Index selected")


def main():
    videos = load_data()
    while True:
        print("\n Welcome to the YouTube Manager | Choose your Option")
        print("1. List all Youtube Videos : "  )
        print("2. Add a youtube video : ")
        print("3. Update a youtube video details : ")
        print("4. Delete the youtube Video : ")
        print("5. Exit the app.")

        choice = input("Enter your choice : ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos) 
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
    