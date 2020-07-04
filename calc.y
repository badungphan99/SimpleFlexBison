%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror (char const *s);
int yylex();
void checkVar(char *s);
void checkDiv(int num);
char var[20];
int value;
%}

%union {
    char varName[20];
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


int main() {
  if (yyparse())
     fprintf(stderr, "Successful parsing.\n");
  else
     fprintf(stderr, "error found.\n");
}