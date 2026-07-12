import threading
import webbrowser
import time
from truerize.dashboard import app

PORT = 5000
URL = f"http://127.0.0.1:{PORT}"


def start_server():
    app.run(
        host="127.0.0.1",
        port=PORT,
        debug=False,
        use_reloader=False
    )


def run():
    print("Starting Truerize Dashboard...")

    thread = threading.Thread(target=start_server, daemon=True)
    thread.start()

    time.sleep(3)

    print("Opening browser:", URL)
    webbrowser.open(URL)


if __name__ == "__main__":
    run()