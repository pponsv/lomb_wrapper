.PHONY : run build configure rebuild_ui clean remove_env deep_clean
ACTIVATE_VENV = . ./env/bin/activate
PYTHON = python3

all: run

run:
	$(PYTHON) main.py

build: 
	$(MAKE) -C ./lib/TJII_data_acquisition

rebuild_ui: 
	mkdir -p src/ui/
	pyside6-uic ./ui/MainWindow.ui -o ./src/ui/ui_mainwindow.py
	pyside6-uic ./ui/ListDialog.ui -o ./src/ui/ui_listdialog.py

configure: 
	$(MAKE) rebuild_ui
	$(MAKE) build

clean:
	rm -rf .vscode/ __pycache__/ src/ui/ figs/
	$(MAKE) -C ./lib/TJII_data_acquisition clean

deep_clean: remove_env clean