import sys
import os
import zlib

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")
        print("Initialized git directory")
    elif command == "cat-file":
        blob_sha = sys.argv[3]
        blob_folder = blob_sha[:2]
        blob_sha = blob_sha[2:]
        with open(f".git/objects/{blob_folder}/{blob_sha}", 'rb') as f:
            content = f.read()
            decompressed_content = zlib.decompress(content)
            _, object_content = decompressed_content.split(b"\x00")
        print(object_content.decode("utf-8"), end="")
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
