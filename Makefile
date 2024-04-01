.PHONY : run build configure rebuild_ui clean remove_env deep_clean
ACTIVATE_VENV = . ./env/bin/activate
PYTHON = python3

all: run

run:
	$(ACTIVATE_VENV); $(PYTHON) main.py

build: 
	$(ACTIVATE_VENV); $(MAKE) -C ./lib/TJII_data_acquisition
	$(ACTIVATE_VENV); $(MAKE) -C ./lib/lomb_periodogram
	$(ACTIVATE_VENV); $(MAKE) -C ./lib/vmec_utils

env: 
	test -d env || python3 -m venv ./env
	echo "../../../../lib/" > ./env/lib/python3.10/site-packages/libpath.pth

rebuild_ui: 
	mkdir -p src/ui/
	$(ACTIVATE_VENV); pyside6-uic ./ui/MainWindow.ui -o ./src/ui/ui_mainwindow.py
	$(ACTIVATE_VENV); pyside6-uic ./ui/ListDialog.ui -o ./src/ui/ui_listdialog.py

configure: 
	$(MAKE) env
	$(ACTIVATE_VENV); pip install -r requirements.txt
	$(MAKE) rebuild_ui
	$(MAKE) update_libs
	$(MAKE) build

update_libs:
	git submodule update --remote --merge

clean:
	rm -rf .vscode/ __pycache__/ src/ui/ figs/
	$(MAKE) -C ./lib/TJII_data_acquisition clean
	$(MAKE) -C ./lib/lomb_periodogram clean

remove_env:
	rm -rf env/

deep_clean: remove_env clean
