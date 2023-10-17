import pytube
import tqdm

# Function to download a YouTube video


def download_video(video_url):
    # Create a YouTube object
    youtube = pytube.YouTube(video_url)

    # Get the stream with the highest resolution
    stream = youtube.streams.get_highest_resolution()

    # Download the video and get the filename
    video_filename = stream.download()

    # Create a progress bar using tqdm
    pbar = tqdm.tqdm(total=stream.filesize)

    # Read and update the progress bar as the video is downloaded
    with open(video_filename, "rb") as fd:
        for chunk in fd:
            pbar.update(len(chunk))

    # Print a success message when the download is complete
    print("Video downloaded successfully!")


if __name__ == "__main__":
    # Prompt the user for the YouTube video URL
    video_url = input("Enter the URL of the YouTube video to download: ")

    # Call the download_video function to start the download
    download_video(video_url)
