calc: calc.y calc.l
		bison -d calc.y
		flex -o calc.lex.c calc.l
		gcc -o calc calc.lex.c calc.tab.c -lm

clean:
		rm calc calc.lex.c calc.tab.c calc.tab.h
