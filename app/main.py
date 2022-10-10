import sys
import os
import zlib

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")
        print("Initialized git directory")
    elif command == "cat-file":
        print(os.listdir(".git/objects"))
        blob_sha = sys.argv[3]
        with open(f".git/objects/{blob_sha}", 'r') as f:
            content = f.read()
        print(zlib.decompress(content.encode()), end='')
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
