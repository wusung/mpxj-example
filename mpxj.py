import jpype
import mpxj
import jpype.imports

if not jpype.isJVMStarted():
    jvmPath = jpype.getDefaultJVMPath()
    jpype.startJVM(classpath = ['libs/*'])

from net.sf.mpxj.reader import UniversalProjectReader
project = UniversalProjectReader().read('example.mpp')

print("Tasks")
for task in project.getTasks():
    if not task.getID():
        print(task.getID().toString() + "\t" + task.getName())


from net.sf.mpxj.sample import MpxjConvert
MpxjConvert().process('example.mpp', 'example.mpx')
