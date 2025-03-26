import sqlite3

conn = sqlite3.connect('youtube_video.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               Id INTEGER PRIMARY KEY,
               Name TEXT NOT NULL,
               Time TEXT NOT NULL
               )
''')

def list_video():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()


def main():
    while True:
        print("Welcome to Youtub Manager | Choose your Option")
        print("1. List_Video : ")
        print("2. Add Video : ")
        print("3. Update Video : ")
        print("4. Delete Video : ")
        print("5. Exit App")
        choice = input("Enter your choice : ")

        if choice == '1':
            print()
            print("*" * 70)
            list_video()
            print()
            print("*" * 70)
        elif choice == '2':
            name = input("Enter your video Name : ")
            time = input("Enter your Video Time : ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter Video Id to update : ")
            name = input("Enter your video name : ")
            time = input("Enter your video Time : ")
            update_video(video_id,name, time)
        elif choice == '4':
            video_id = input("Enter a video number to delete : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()
