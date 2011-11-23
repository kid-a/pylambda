EXEC=pylambda

run:
	python $(EXEC).py

clean:
	-rm *.pyc *~
	-rm parser.out
	-rm parsetab.py