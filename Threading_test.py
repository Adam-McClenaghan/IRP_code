#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
import threading, random, json, os, math

app = None
ui = adsk.core.UserInterface.cast(None)
handlers = []
stopFlag = None
myCustomEvent = 'MyCustomEventId'
customEvent = None
Last_mod = os.path.getmtime('C:/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv')
User_angle = 45

# The event handler that responds to the custom event being fired.
class ThreadEventHandler(adsk.core.CustomEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # Make sure a command isn't running before changes are made.
            if ui.activeCommand != 'SelectCommand':
                ui.commandDefinitions.itemById('SelectCommand').execute()
            STIM = [8, 9, 10, 11, 12, 13, 14, 15]           
            # Get the value from the JSON data passed through the event.
            eventArgs = json.loads(args.additionalInfo)
            newValue = int(eventArgs['Value'])
            
            # Compare value passed to event to known stimulus frequencies
            if newValue == STIM[0]:
                y_up(app, app.activeViewport)
            elif newValue == STIM[1]:
                y_down(app, app.activeViewport)
            elif newValue == STIM[2]:
                # Event_10()
                x_up(app, app.activeViewport)
            elif newValue == STIM[3]:
                # Event_11()
                x_down(app, app.activeViewport)
            elif newValue == STIM[4]:
                Event_12()
            elif newValue == STIM[5]:
                Event_13()
            elif newValue == STIM[6]:
                Event_14()
            elif newValue == STIM[7]:
                Event_15()
            else:
                ui.messageBox('Unrecognised input')
            
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


# The class for the new thread.
class MyThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        # Every 0.1 seconds, check last modified time of target file
        Last_mod = os.path.getmtime('C:/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv')
        while not self.stopped.wait(0.1):
            if os.path.getmtime('C:/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv') > Last_mod:
                get_freq()
                args = {'Value': get_freq.reg_val}
                app.fireCustomEvent(myCustomEvent, json.dumps(args)) 
            
            Last_mod = os.path.getmtime('C:/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv')

# Read value from input file and convert to integer
def get_freq():
    global ui
    filename = 'C:/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv'
    f = open(filename)

    val = (f.read(2))
    stripped_val = val.strip()
    excel_val = str(stripped_val)
    if excel_val.isdigit():
        ui.messageBox(excel_val)
        get_freq.reg_val = int(excel_val)

# Defining events associated with each frequency
def Event_8():
    # ui.messageBox('Event 5')

    global app
    app = adsk.core.Application.get()
    camera = app.activeViewport.camera

    camera.viewOrientation = adsk.core.ViewOrientations.LeftViewOrientation

    camera.isFitView = True

    app.activeViewport.camera = camera

def Event_9():
    # ui.messageBox('Event 6')

    global app
    app = adsk.core.Application.get()
    camera = app.activeViewport.camera

    camera.viewOrientation = adsk.core.ViewOrientations.RightViewOrientation

    camera.isFitView = True

    app.activeViewport.camera = camera

def Event_10():

    global app
    app = adsk.core.Application.get()
    camera = app.activeViewport.camera

    camera.viewOrientation = adsk.core.ViewOrientations.FrontViewOrientation

    camera.isFitView = True

    app.activeViewport.camera = camera

def Event_11():

    global app
    app = adsk.core.Application.get()
    camera = app.activeViewport.camera

    camera.viewOrientation = adsk.core.ViewOrientations.BackViewOrientation

    camera.isFitView = True

    app.activeViewport.camera = camera

def Event_12():

    global app
    app = adsk.core.Application.get()
    camera = app.activeViewport.camera

    camera.viewOrientation = adsk.core.ViewOrientations.LeftViewOrientation

    camera.isFitView = True

    app.activeViewport.camera = camera    

def Event_13():

    global app
    app = adsk.core.Application.get()
    camera = app.activeViewport.camera
   
    camera.viewOrientation = adsk.core.ViewOrientations.RightViewOrientation

    camera.isFitView = True

    app.activeViewport.camera = camera    

def Event_14():
    ui.messageBox('Will return to previous function')

def Event_15():
    ui.messageBox('Back')


def y_up(app, view):
        global User_angle
        camera = view.camera
        ui = app.userInterface
        start_coords = [camera.eye.x , camera.eye.y, camera.eye.z]

        radius = math.sqrt(start_coords[0] ** 2 + start_coords[2] ** 2)
        angle = User_angle * (math.pi / 180)

        rotation_mat = [math.cos(angle), -math.sin(angle), math.sin(angle), math.cos(angle)] 

        target = adsk.core.Point3D.create(0,0,0) #Point about rotation
        up = adsk.core.Vector3D.create(0,1,0) #Axis of rotation
        #rotation about y axis
        new_coords = [start_coords[0] * rotation_mat[0] + start_coords[2] * rotation_mat[1], start_coords[1], start_coords[0] * rotation_mat[2] + start_coords[2] * rotation_mat[3]]
       
        eye = adsk.core.Point3D.create(new_coords[0], new_coords[1], new_coords[2])
        
        camera.eye = eye
        camera.target = target
        camera.upVector = up

        camera.isSmoothTransition = False
        view.camera = camera
        adsk.doEvents()
        view.refresh()


def y_down(app, view):
        global User_angle
        camera = view.camera
        ui = app.userInterface
        start_coords = [camera.eye.x , camera.eye.y, camera.eye.z]

        radius = math.sqrt(start_coords[0] ** 2 + start_coords[2] ** 2)
        angle = -User_angle * (math.pi / 180)

        rotation_mat = [math.cos(angle), -math.sin(angle), math.sin(angle), math.cos(angle)] 

        target = adsk.core.Point3D.create(0,0,0) #Point about rotation
        up = adsk.core.Vector3D.create(0,1,0) #Axis of rotation
        #rotation about y axis
        new_coords = [start_coords[0] * rotation_mat[0] + start_coords[2] * rotation_mat[1], start_coords[1], start_coords[0] * rotation_mat[2] + start_coords[2] * rotation_mat[3]]
       
        eye = adsk.core.Point3D.create(new_coords[0], new_coords[1], new_coords[2])
        
        camera.eye = eye
        camera.target = target
        camera.upVector = up

        camera.isSmoothTransition = False
        view.camera = camera
        adsk.doEvents()
        view.refresh()


# def x_up(app, view):
#         global User_angle
#         camera = view.camera
#         ui = app.userInterface
#         start_coords = [camera.eye.x , camera.eye.y, camera.eye.z]

#         radius = math.sqrt(start_coords[0] ** 2 + start_coords[2] ** 2)
#         angle = User_angle * (math.pi / 180)

#         rotation_mat = [math.cos(angle), -math.sin(angle), math.sin(angle), math.cos(angle)] 

#         target = adsk.core.Point3D.create(0,0,0) #Point about rotation
#         up = adsk.core.Vector3D.create(0,1,0) #Axis of rotation
#         #rotation about x axis
#         new_coords = [start_coords[0], start_coords[1] * rotation_mat[0] + start_coords[2] * rotation_mat[1], start_coords[1] * rotation_mat[2] + start_coords[2] * rotation_mat[3]]
#         eye = adsk.core.Point3D.create(new_coords[0], new_coords[1], new_coords[2])
        
#         camera.eye = eye
#         camera.target = target
#         camera.upVector = up

#         camera.isSmoothTransition = False
#         view.camera = camera
#         adsk.doEvents()
#         view.refresh()

# def x_down(app, view):
#         global User_angle
#         camera = view.camera
#         ui = app.userInterface
#         start_coords = [camera.eye.x , camera.eye.y, camera.eye.z]

#         radius = math.sqrt(start_coords[0] ** 2 + start_coords[2] ** 2)
#         angle = User_angle * (math.pi / 180)

#         rotation_mat = [math.cos(angle), -math.sin(angle), math.sin(angle), math.cos(angle)] 

#         target = adsk.core.Point3D.create(0,0,0) #Point about rotation
#         up = adsk.core.Vector3D.create(0,1,0) #Axis of rotation
#         #rotation about x axis
#         new_coords = [start_coords[0], start_coords[1] * rotation_mat[0] + start_coords[2] * rotation_mat[1], start_coords[1] * rotation_mat[2] + start_coords[2] * rotation_mat[3]]
#         eye = adsk.core.Point3D.create(new_coords[0], new_coords[1], new_coords[2])
        
#         camera.eye = eye
#         camera.target = target
#         camera.upVector = up

#         camera.isSmoothTransition = False
#         view.camera = camera
#         adsk.doEvents()
#         view.refresh()


def run(context):
    global ui
    global app
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
       
        cmdDefs = ui.commandDefinitions

        # Create a button command definition and add to toolbar
        buttonSample = cmdDefs.addButtonDefinition('MyButtonDefIdPython', 
                                                   'BCI monitor running', 
                                                   'Background operation currently monitoring EEG inputs',
                                                   'C:/Users/Adam/AppData/Roaming/Autodesk/Autodesk Fusion 360/API/AddIns/Button Test/SketchShapes')

        # Get the ADD-INS panel in the model workspace. 
        addInsPanel = ui.allToolbarPanels.itemById('SolidScriptsAddinsPanel')
        
        # Add the button to the bottom of the panel.
        #buttonControl = addInsPanel.controls.addCommand(buttonSample)
        cmdControl :adsk.core.CommandControl = addInsPanel.controls.addCommand(buttonSample)
        cmdControl.isPromotedByDefault = True

        # Register the custom event and connect the handler.
        global customEvent
        customEvent = app.registerCustomEvent(myCustomEvent)
        onThreadEvent = ThreadEventHandler()
        customEvent.add(onThreadEvent)
        handlers.append(onThreadEvent)

        # Create a new thread for the other processing.        
        global stopFlag        
        stopFlag = threading.Event()
        myThread = MyThread(stopFlag)
        myThread.start()
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def stop(context):
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        if handlers.count:
            customEvent.remove(handlers[0])
        stopFlag.set() 
        app.unregisterCustomEvent(myCustomEvent)
        ui.messageBox('BCI monitoring stopped')

        # Clean up the UI.
        cmdDef = ui.commandDefinitions.itemById('MyButtonDefIdPython')
        if cmdDef:
            cmdDef.deleteMe()
            
        addinsPanel = ui.allToolbarPanels.itemById('SolidScriptsAddinsPanel')
        cntrl = addinsPanel.controls.itemById('MyButtonDefIdPython')
        if cntrl:
            cntrl.deleteMe()
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))