from datapaths import projectPath, imagePath
from resistics.time.reader_lemib423 import folderB423Headers

# first need to create headers
sitePath = projectPath / "timeData" / "site1_mt"
folderB423Headers(
    sitePath, 500, hxSensor=712, hySensor=710, hzSensor=714, hGain=16, dx=60, dy=60.7
)

# load project
from resistics.project.io import loadProject

proj = loadProject(projectPath)
proj.printInfo()
fig = proj.view()
fig.savefig(imagePath / "timeline.png")

# view time
from resistics.project.time import viewTime

fig = viewTime(
    proj,
    startDate="2019-05-27 14:15:00",
    endDate="2019-05-27 15:00:00",
    filter={"lpfilt": 4},
    save=False,
    show=False,
)
fig.savefig(imagePath / "viewTime.png")

from resistics.project.spectra import calculateSpectra
from resistics.project.statistics import calculateStatistics
from resistics.project.transfunc import processProject, viewImpedance
from resistics.common.plot import plotOptionsTransferFunction, getPaperFonts

calculateSpectra(proj)
proj.refresh()
calculateStatistics(proj)
processProject(proj)
plotOptions = plotOptionsTransferFunction(figsize=(24, 12), plotfonts=getPaperFonts())
plotOptions["res_ylim"] = [1, 1000000]
figs = viewImpedance(
    proj, oneplot=False, plotoptions=plotOptions, show=False, save=False
)
figs[0].savefig(imagePath / "impedance_default.png")