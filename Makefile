EXEC=pylambda
TEST=tests

run:
	python $(EXEC).py

unit-test:
	python $(TEST).py

clean:
	-rm *.pyc *~
	-rm parser.out
	-rm parsetab.py