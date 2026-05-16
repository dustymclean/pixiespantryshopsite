#!/usr/bin/env python3
"""
Watch for changes to Dyspensr_Master_Catalog_Priced.csv and regenerate cluster pages.
"""
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

class CatalogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("Dyspensr_Master_Catalog_Priced.csv"):
            print(f"🔄 Catalog updated: {event.src_path}")
            subprocess.run(["python3", "generate_cluster_pages.py"])

if __name__ == "__main__":
    event_handler = CatalogHandler()
    observer = Observer()
    observer.schedule(event_handler, path="~/Desktop", recursive=False)
    observer.start()
    print("👀 Watching for catalog changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()