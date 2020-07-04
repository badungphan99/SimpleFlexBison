%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern FILE *yyin;

void yyerror (char const *s);
int yylex();
void checkVar(char *s);
void checkDiv(int num);
char var[1000];
int value;
%}

%union {
    char varName[1000];
    int val;
}

%token NUMBER
%token VAR
%token EQUAL PLUS MINUS TIMES DIVIDE
%token NEWLINE

%type<val> NUMBER Declaration Expression
%type<varName> VAR

%start Input
%%

Input:
	| Input Line
;

Line:
	Declaration Expression { printf("%d\n",value); exit(0); }
;

Declaration:
	VAR EQUAL NUMBER NEWLINE {sscanf($1, "%s", var); value = $3;}
;

Expression:
	VAR PLUS NUMBER { checkVar($1); value=value+$3; }
	| VAR MINUS NUMBER { checkVar($1); value=value-$3; }
	| VAR TIMES NUMBER { checkVar($1); value=value*$3; }
	| VAR DIVIDE NUMBER { checkVar($1);checkDiv($3); value=value/$3; }
;

%%
void checkDiv(int num){
	if (!num){
		printf("Can not divide by zero\n");
		exit(1);
	}
}

void checkVar(char *s){
	if (strcmp(s, var)) {
		printf("Variable \"%s\" is not declared\n", s);
		exit(1);
            };
}

void yyerror (char const *s) {
	fprintf (stderr, "%s\n", s);
}


int main(int argc, char* argv[]) {
	if (argc == 2){
		FILE *file = fopen(argv[1], "r");
		if(!file){
			fprintf(stderr, "Can not read file %s\n", argv[1]);
			exit(1);
		}else{
			yyin = file;
		}
	}
  if (yyparse())
     fprintf(stderr, "Successful parsing.\n");
  else
     fprintf(stderr, "error found.\n");
}