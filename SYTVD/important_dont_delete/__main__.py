from __future__ import print_function
import sys
import os
import argparse

from . import YouTube
from .utils import print_status, FullPaths
from .exceptions import PytubeError
from pprint import pprint


def main():
    parser = argparse.ArgumentParser(description='YouTube video downloader')
    parser.add_argument("url", help=(
        "The URL of the Video to be downloaded"))
    parser.add_argument("--extension", "-e", dest="ext", help=(
        "The requested format of the video"))
    parser.add_argument("--resolution", "-r", dest="res", help=(
        "The requested resolution"))
    parser.add_argument("--path", "-p", action=FullPaths, default=os.getcwd(),
                        dest="path", help=("The path to save the video to."))
    parser.add_argument("--filename", "-f", dest="filename", help=(
        "The filename, without extension, to save the video in."))
    parser.add_argument("--show_available", "-s", action='store_true',
            dest='show_available', help=("Prints a list of available formats for download."))

    args = parser.parse_args()

    try:
        yt = YouTube(args.url)
        videos = []
        for i, video in enumerate(yt.get_videos()):
            ext = video.extension
            res = video.resolution
            videos.append((ext, res))


    if args.show_available:
        print_available_vids(videos)
        sys.exit(0)

    if args.filename:
        yt.set_filename(args.filename)

    if args.ext or args.res:
        if not all([args.ext, args.res]):
            print("Make sure you give either of the below specified "
                  "format/resolution combination.")
            print_available_vids(videos)
            sys.exit(1)

    if args.ext and args.res:
        vid = yt.get(args.ext, args.res)
        if not vid:
            print("There's no video with the specified format/resolution "
                  "combination.")
            pprint(videos)
            sys.exit(1)

    elif args.ext:
        videos = yt.filter(extension=args.ext)
        if not videos:
            print("There are no videos in the specified format.")
            sys.exit(1)
        vid = max(videos)
    elif args.res:
        videos = yt.filter(resolution=args.res)
        if not videos:
            print("There are no videos in the specified in the specified "
                  "resolution.")
            sys.exit(1)
        vid = max(videos)
    else:
        print_available_vids(videos)
        while True:
            try:
                choice = int(input("Enter choice: "))
                vid = yt.get(*videos[choice])
                break
            except (ValueError, IndexError):
                print("Requires an integer in range 0-{}".format(len(videos) - 1))
            except KeyboardInterrupt:
                sys.exit(2)

    try:
        vid.download(path=args.path, on_progress=print_status)
    except KeyboardInterrupt:
        print("Download interrupted.")
        sys.exit(1)

def print_available_vids(videos):
    formatString = "{:<2} {:<15} {:<15}"
    print(formatString.format("", "Resolution", "Extension"))
    print("-"*28)
    print("\n".join([formatString.format(index, *formatTuple) for index, formatTuple in enumerate(videos)]))

if __name__ == '__main__':
    main()
