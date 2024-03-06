MAIN = ./src/tjii_data_acquisition.f90
MODNAME = TJII_data_acquisition_f

all: $(MAIN)
	python3 -m numpy.f2py -c --f90flags='-Wno-tabs -lRpcC' -L./lib/ -m $(MODNAME) $(MAIN) ./lib/libRpcC.a

pyc: $(MAIN)
	python3 -m numpy.f2py -h tmp.pyf -m $(MODNAME) $(MAIN)

clean:
	rm -f *.so

test:
	python3 test.py