import subprocess
import time
import webview

# Start the Streamlit server in the background
process = subprocess.Popen(
    ["streamlit", "run", "app.py", "--server.headless=true", "--browser.gatherUsageStats=false"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

# Wait for Streamlit to boot up
print("Starting server... please wait.")
time.sleep(3)

# Create a native desktop window pointing to the local server
window = webview.create_window(
    title="Medicare Assistant (Local RAG)", 
    url="http://localhost:8501",
    width=1200,
    height=800
)

# This blocks until the window is closed
webview.start()

# When the window is closed, kill the Streamlit server
process.terminate()
print("Server stopped. Goodbye!")