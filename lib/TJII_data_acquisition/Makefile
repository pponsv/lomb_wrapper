MAIN = ./src/tjii_data_acquisition.f90
MODNAME = TJII_data_acquisition_f
ACTIVATE_VENV = . ../../env/bin/activate

all: $(MAIN)
	$(ACTIVATE_VENV); python3 -m numpy.f2py -c --f90flags='-Wno-tabs -lRpcC' -L./lib/ -m $(MODNAME) $(MAIN) ./lib/libRpcC.a

pyc: $(MAIN)
	$(ACTIVATE_VENV); python3 -m numpy.f2py -h tmp.pyf -m $(MODNAME) $(MAIN)

clean:
	rm -f *.so

test:
	$(ACTIVATE_VENV); python3 test.py