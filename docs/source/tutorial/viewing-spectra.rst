.. role:: python(code)
   :language: python

.. |Ex| replace:: E\ :sub:`x`
.. |Ey| replace:: E\ :sub:`y`
.. |Hx| replace:: H\ :sub:`x`
.. |Hy| replace:: H\ :sub:`y`
.. |Hz| replace:: H\ :sub:`z`
.. |Zxy| replace:: Z\ :sub:`xy`
.. |Zxx| replace:: Z\ :sub:`xx`
.. |Zyx| replace:: Z\ :sub:`yx`
.. |Zyy| replace:: Z\ :sub:`yy`
.. |fs| replace:: f\ :sub:`s`

Viewing spectra
---------------

Spectra data is stored in the following locations. 

.. code-block:: text

    exampleProject
    ├── calData 
    ├── timeData   
    │   └── site1
    |       |── dataFolder1
    │       |── dataFolder2
    |       |──     .     
    |       |──     .
    |       |──     .
    |       └── dataFolderN     
    ├── specData
    │   └── site1
    |       |── dataFolder1
    |       |   └── spectra
    │       |── dataFolder2
    |       |   └── spectra    
    |       |──     .     
    |       |──     .
    |       |──     .
    |       └── dataFolderN
    |           └── spectra        
    ├── statData
    ├── maskData   
    ├── transFuncData 
    ├── images
    └── mtProj.prj

Each spectra file that is calculated is written out with a set of comments. The comment file is a text file that can be opened in any text editor and records the various parameters used when calculating out spectra. An example is given below.

.. literalinclude:: ../_static/examples/tutorial/viewSpec_comments.txt
    :linenos:
    :language: text

There are a few methods in the project :mod:`~resistics.project.spectra` module that can be used to visualise spectra. These are:

- View raw spectra data for time windows
- View spectra sections - an image of spectras calculated over the period of recording
- View spectra periodograms

To begin looking at spectra, load the project in the standard way.

.. literalinclude:: ../../../examples/tutorial/viewSpectra.py
    :linenos:
    :language: python
    :lines: 1-5
    :lineno-start: 1

The fourier spectra can be viewed using the :meth:`~resistics.project.spectra.viewSpectra` method, which takes a site and measurement as arguments. 

.. literalinclude:: ../../../examples/tutorial/viewSpectra.py
    :linenos:
    :language: python
    :lines: 7-11
    :lineno-start: 7

This gives the following output: 

.. figure:: ../_static/examples/tutorial/viewSpec_projspec_128_view.png
    :align: center
    :alt: alternate text
    :figclass: align-center

    Plot of the first time window spectrum

Plotting options can be defined using the :python:`plotoptions` keyword for :meth:`~resistics.project.spectra.viewSpectra`. This needs to be a dictionary defining layout options (limits etc). There are some built-in plot options for different types of plots. In the below example, :meth:`~resistics.common.plot.plotOptionsSpec` returns a dictionary of standard plot options for spectra. Further, :meth:`~resistics.common.plot.getPaperFonts` returns a dictionary of font sizes to use for the plot targetted at papers. 

.. literalinclude:: ../../../examples/tutorial/viewSpectra.py
    :linenos:
    :language: python
    :lines: 13-17
    :lineno-start: 13

The plot options dictionary looks like this:

.. code-block:: text

    {'figsize': (20, 12), 'plotfonts': {'suptitle': 18, 'title': 17, 'axisLabel': 16, 'axisTicks': 15, 'legend': 15}, 'block': True, 'amplim': []}

Now plotting the spectra again with the new plot options gives the same plot but with bigger font sizes which might be useful for an academic paper. 

.. literalinclude:: ../../../examples/tutorial/viewSpectra.py
    :linenos:
    :language: python
    :lines: 19-28
    :lineno-start: 19

.. figure:: ../_static/examples/tutorial/viewSpec_projspec_128_view_plotoptions.png
    :align: center
    :alt: alternate text
    :figclass: align-center

    Plot of the first time window spectrum using a different set of plot options

Currently, this is only plotting the spectrum of the first time window. To explore variation, more than a single time window can be plotted. This is achieved using the :python:`plotwindow` keyword. The plotwindow keyword can be:

- An integer which is the local index of the time window (local index means referenced to the start time of the time series)
- "all", which will plot 20 windows across the duration of the whole measurement
- A dictionary with a start and stop, i.e. {start: 30, stop:40}, which will then define the range 30, 31, 32, 33, 34, 35, 36, 37, 38, 39 and 40

In the below example, :python:`plotwindow = "all"` which means that 20 windows across the time series measurement will be plotted. 

.. literalinclude:: ../../../examples/tutorial/viewSpectra.py
    :linenos:
    :language: python
    :lines: 30-41
    :lineno-start: 30

.. figure:: ../_static/examples/tutorial/viewSpec_projspec_128_view_plotall_chans.png
    :align: center
    :alt: alternate text
    :figclass: align-center

    Plot of multiple window spectra

Another useful way to inspect the variation of spectra across the time series measurement is to plot a spectra section using the :meth:`~resistics.project.spectra.viewSpectraSection` method of the project :mod:`~resistics.project.spectra` module. This is a 2-D image of the spectra with time across the x-axis and frequency across the y-axis with colour representing the amplitude. An example of plotting a spectra section and the image is shown below.

.. literalinclude:: ../../../examples/tutorial/viewSpectra.py
    :linenos:
    :language: python
    :lines: 43-54
    :lineno-start: 41

.. figure:: ../_static/examples/tutorial/viewSpec_projspec_128_section.png
    :align: center
    :alt: alternate text
    :figclass: align-center

    Plot of a spectra section for 128Hz sampling frequency data

Spectra sections plot 250 window spectra across the duration of the time series measurement.

To understand the dominant frequencies in a time series measurement, it can be useful to perform spectral stacking. This can be achieved using the :meth:`~resistics.project.spectra.viewSpectraStack` method of the project :mod:`~resistics.project.spectra` module. Spectra stacking will averages the spectra amplitudes across multiple windows.

.. literalinclude:: ../../../examples/tutorial/viewSpectra.py
    :linenos:
    :language: python
    :lines: 56-68
    :lineno-start: 56

.. figure:: ../_static/examples/tutorial/viewSpec_projspec_128_stack.png
    :align: center
    :alt: alternate text
    :figclass: align-center

    Plot of a spectra stacking for 128Hz sampling frequency data

Adding the **coherences** keyword also stacks the coherences. The number of stacks to perform across the duration of the time series measurement can be controlled using the **numstacks** keyword. For more information, see the documentation for :meth:`~resistics.project.spectra.viewSpectraStack`.

The above were demonstrated on data sampled at 128Hz sampling rate but can be easily repeated for the 4096Hz data of the tutorial project. 

.. literalinclude:: ../../../examples/tutorial/viewSpectra.py
    :linenos:
    :language: python
    :lines: 70-101
    :lineno-start: 70

The resultant plots are:

.. figure:: ../_static/examples/tutorial/viewSpec_projspec_4096_view_plotall.png
    :align: center
    :alt: alternate text
    :figclass: align-center

    Plot of a spectra for 20 windows across the 4096Hz measurement

.. figure:: ../_static/examples/tutorial/viewSpec_projspec_4096_view_section.png
    :align: center
    :alt: alternate text
    :figclass: align-center

    Plot of spectra section for the 4096Hz measurement

.. figure:: ../_static/examples/tutorial/viewSpec_projspec_4096_view_stack_coherences.png
    :align: center
    :alt: alternate text
    :figclass: align-center

    Plot of spectra stack for the 4096Hz measurement      

All the above are a means to understand the dominant frequencies in the time series data. Ideally, the Schumann resonances should be visible, as they are in the 128Hz data. Other common features are powerline noise - the exact frequency of this is dependent on geographic location, but often 50Hz - and trainline noise around 16.6Hz.   

Complete example script
~~~~~~~~~~~~~~~~~~~~~~~
For the purposes of clarity, the complete example script is provided below.

.. literalinclude:: ../../../examples/tutorial/viewSpectra.py
    :linenos:
    :language: python
