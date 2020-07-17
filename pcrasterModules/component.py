from pcraster import *
from pcraster.framework import *

class Component:
  def __init__(self):
    pass

  ### reporting of maps

  def reportMaps(self,sample,timestep):
    if timestep in self.timeStepsToReport:
      for variable in self.variablesToReport:
        report(self.variablesToReport[variable],generateNameST(variable, sample, timestep))

  ### reporting as numpy, each time step and realization a seperate file

  def reportAsNumpy(self,locations,sample,timestep):
    import generalfunctions
    for variable in self.variablesAsNumpyToReport:
      tmp=self.variablesAsNumpyToReport[variable]
      generalfunctions.reportLocationsAsNumpyArray(locations,self.variablesAsNumpyToReport[variable], \
                       variable,sample,timestep)

  def reportAsNumpyPostmcloop(self,samples,timeSteps):
    import generalfunctions
    for variable in self.variablesAsNumpyToReport:
      aVariable = generalfunctions.openSamplesAndTimestepsAsNumpyArraysAsNumpyArray(variable,samples,timeSteps)
      numpy.save(variable,aVariable)

  ## reporting as numpy, each realization a seperate file

  def reportAsNumpyOneFilePerRealization(self,locations,sample,timestep,endTimeStep):
    import generalfunctions
    for variable in self.variablesAsNumpyToReport:
      generalfunctions.reportLocationsAsNumpyArrayOneFilePerRealization(locations,self.variablesAsNumpyToReport[variable], \
                       variable,sample,timestep, endTimeStep)

  def reportAsNumpyOneFilePerRealizationPostmcloop(self,samples,timeSteps):
    print(self.variablesAsNumpyToReport)
    import generalfunctions
    for variable in self.variablesAsNumpyToReport:
      aVariable = generalfunctions.openSamplesAsNumpyArrays(variable,samples,timeSteps)
      numpy.save(variable + '_of',aVariable)