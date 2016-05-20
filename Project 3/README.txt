-Script should be run with filename/path of image to be classified specified in the command line as the lone argument.

-Script expects access to 'Data' provided (all of the sets of images organized in the way that they are on google) for dictionary creation.

	- Script expects image sets to be in Data folder (and same sub folders) in same directory as script. If accessed from another directory, script will need to
		be modified to include full paths for each imageFilePath variable in the 'createExamples' function