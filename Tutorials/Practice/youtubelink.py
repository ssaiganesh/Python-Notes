#this program takes in only the final code of the video for youtube websites

youtube_link = input("Insert link: ")
length = len(youtube_link)
for i in range(length):
    if youtube_link[i] == "=":
        for x in range(i+1,length):
            print(youtube_link[x],end='')
    