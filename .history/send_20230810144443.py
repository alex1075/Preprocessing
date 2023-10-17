import io
import os
import sys
import tqdm
import socket
import base64

def send_file(path, file, server, port):
    """
    Send a file to a server.
    """
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"
    # get the file size
    filesize = os.path.getsize(path + file)
    # create the client socket
    s = socket.socket()
    print(f"[+] Connecting to {server}:{port}")
    filename = file
    # connect to the server
    s.connect((server, int(port)))
    print("[+] Connected.")
    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(path +file, "rb") as f:
        data = base64.b64encode(f.read())
        data = io.BytesIO(data)
        while True:
            # read the bytes from the file
            bytes_read = data.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    # close the socket
    s.close()
    print(f"[+] File {file} sent to {server}:{port}")

if __name__ == "__main__":
    send_file(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])