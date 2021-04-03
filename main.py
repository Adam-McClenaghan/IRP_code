def Watch_func():

    import time
    from watchdog.observers import Observer
    from watchdog.events import PatternMatchingEventHandler
    import subprocess
    import ctypes  # An included library with Python install.   


    stim = [5, 6, 7, 8]

    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_modified(event):
        print(f"{event.src_path} has been modified")

        filename = 'C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv'
        f = open(filename)

        excel_val = (f.read(1))
        if excel_val.isdigit():
            reg_val = int(excel_val)
            print(type(reg_val), reg_val)

            if reg_val == stim[0]:
                ctypes.windll.user32.MessageBoxW(0, "Input frequency is 5", "title test", 1)
            elif reg_val == stim[1]:
                ctypes.windll.user32.MessageBoxW(0, "input frequency is 6", "title test", 1)
            elif  reg_val == stim[2]:
                ctypes.windll.user32.MessageBoxW(0, "input frequency is 7", "title test", 1)
            elif reg_val == stim[3]:
                ctypes.windll.user32.MessageBoxW(0, "Input frequency is 8", "title test", 1)
    
    


    my_event_handler.on_modified = on_modified


    path = "/Users/Adam/Documents/MENG_yr3/IRP_papers"

    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()