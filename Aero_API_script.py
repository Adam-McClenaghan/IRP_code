#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
import threading, random, json, os, math
import io
app = None
ui = adsk.core.UserInterface.cast(None)
handlers = []
stopFlag = None
myCustomEvent = 'AeroGen'
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
            Gen_aerofoil()
            
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
        Last_mod = os.path.getmtime('C:/Users/Adam/Desktop/IRP_CODE/Aero_coords.csv')
        while not self.stopped.wait(0.1):
            if os.path.getmtime('C:/Users/Adam/Desktop/IRP_CODE/Aero_coords.csv') > Last_mod:
                get_freq()
                args = {'Value': get_freq.reg_val}
                app.fireCustomEvent(myCustomEvent, json.dumps(args)) 
            
            Last_mod = os.path.getmtime('C:/Users/Adam/Desktop/IRP_CODE/Aero_coords.csv')

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

# Create Aerofoil and extrude
def Gen_aerofoil():
    app = adsk.core.Application.get()
    ui  = app.userInterface
    # Get all components in the active design.
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)
    rootComp = product.rootComponent  
    extrudes = rootComp.features.extrudeFeatures

    Existing_sketch = rootComp.sketches.itemByName('BCI_sketch')
    if Existing_sketch:
        Existing_sketch.deleteMe()

    Existing_extrusion = extrudes.itemByName('BCI Extrusion')
    if Existing_extrusion:
        Existing_extrusion.deleteMe()
    
    title = 'Import Spline csv'
    if not design:
        ui.messageBox('No active Fusion design', title)
        return
    
    filename = 'C:/Users/Adam/Desktop/IRP_CODE/Aero_coords.csv'
    with io.open(filename, 'r', encoding='utf-8-sig') as f:
        points = adsk.core.ObjectCollection.create()
        line = f.readline()
        data = []
        while line:
            pntStrArr = line.split(',')
            for pntStr in pntStrArr:
                try:
                    data.append(float(pntStr))
                except:
                    break
        
            if len(data) >= 3 :
                point = adsk.core.Point3D.create(data[0], data[1], data[2])
                points.add(point)
            line = f.readline()
            data.clear()       

    if points.count:
        root = design.rootComponent
        sketch = root.sketches.add(root.xYConstructionPlane)
        sketch.sketchCurves.sketchFittedSplines.add(points)
        sketch.name = ('BCI_sketch')
    else:
        ui.messageBox('No valid points', title)     



    sketch = rootComp.sketches.itemByName('BCI_sketch')
    if not sketch:
        ui.messageBox("unable to locate sketch")
        return
    #Extrude Sketch
    ext_file = 'C:/Users/Adam/Desktop/IRP_CODE/Extrude_distance.csv'
    with io.open(ext_file, 'r', encoding='utf-8-sig') as f:
        ext_val = int(f.read()) 

    ex_dist = adsk.core.ValueInput.createByReal(ext_val)
    

    #Extrude first profile in sketch
    extrudeInput = extrudes.createInput(sketch.profiles[0], adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

    extrudeInput.setSymmetricExtent(ex_dist, True)

    extrudeInput.isSolid = True

    extrusion = extrudes.add(extrudeInput)
    extrusion.name = 'BCI Extrusion'
  

def Event_14():
    ui.messageBox('Will return to previous function')

def Event_15():
    ui.messageBox('Back')



def run(context):
    global ui
    global app
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
       
        # cmdDefs = ui.commandDefinitions

        # Create a button command definition and add to toolbar
        # # buttonSample = cmdDefs.addButtonDefinition('MyButtonDefIdPython', 
        #                                            'BCI monitor running', 
        #                                            'Background operation currently monitoring EEG inputs',
        #                                            'C:/Users/Adam/AppData/Roaming/Autodesk/Autodesk Fusion 360/API/AddIns/Button Test/SketchShapes')

        # Get the ADD-INS panel in the model workspace. 
        # addInsPanel = ui.allToolbarPanels.itemById('SolidScriptsAddinsPanel')
        
        # Add the button to the bottom of the panel.
        #buttonControl = addInsPanel.controls.addCommand(buttonSample)
        # cmdControl :adsk.core.CommandControl = addInsPanel.controls.addCommand(buttonSample)
        # cmdControl.isPromotedByDefault = True

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