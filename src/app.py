import signal

class App:
    
    def __init__(self):
        pass
    
    def run(self, i):
        while True:
            try:
                result = i.executeline()
                if result != 0:
                    break
            except Exception as e:
                print(f"Error: {e}")
                break
            
    def stop(self):
        signal.signal(signal.SIGINT, lambda sig, frame : exit(0))