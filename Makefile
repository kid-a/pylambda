EXEC=pylambda
TEST=tests

run:
	python3 $(EXEC).py

unit-test:
	python3 $(TEST).py

clean:
	-rm *.pyc *~
	-rm parser.out
	-rm parsetab.py
