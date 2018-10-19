cli: clean
	pyinstaller cli.py --name pywc --onefile

gui: clean
	pyinstaller gui.py --name pywcg --windowed --onefile --additional-hooks-dir=hooks

exes: cli gui

clean:
	rm -fr dist/ build/
