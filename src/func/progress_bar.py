class MyProgressListener(ProgressListener):
    def __init__(self, interval=1):
        ProgressListener.__init__(self)
        self.interval = interval
        self.last_time = time.time()

    def notify_progress(self, progress_data):
        current_time = time.time()
        if current_time - self.last_time >= self.interval:
            progress = progress_data.current_objective
            print(f"Current Objective: {progress:.6f}", end='\r')
            sys.stdout.flush()
            self.last_time = current_time
