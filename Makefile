.PHONY : run build configure rebuild_ui clean remove_env deep_clean env
ENV_PATH = ./env/
ACTIVATE_VENV = . $(ENV_PATH)/bin/activate

run:
	$(ACTIVATE_VENV); lomb_wrapper

install: clean env
	$(ACTIVATE_VENV); pip install .

rebuild_ui: 
	$(ACTIVATE_VENV); pyside6-uic ./lomb_wrapper/ui/MainWindow.ui -o ./lomb_wrapper/ui_mainwindow.py

env: 
	test -d $(ENV_PATH) || python3 -m venv $(ENV_PATH)

clean:
	rm -rf .vscode/ __pycache__/ figs/ build/ *.egg-info/

remove_env:
	rm -rf env/

deep_clean: remove_env clean
