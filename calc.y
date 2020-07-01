%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex();
int checkVar(char *s);
char var[20];
int value;
%}

%union {
    char iden[20];
    int ival;
}

%token NUMBER
%token VAR
%token EQUAL PLUS MINUS TIMES DIVIDE

%type<ival> NUMBER Declaration Expression
%type<iden> VAR

%start Input
%%

Input:
	| Input Line
;

Line:
	Declaration Expression { printf("%d\n",value); exit(0); }
;

Declaration:
	VAR EQUAL NUMBER {sscanf($1, "%s", var); value = $3;}
;

Expression:
	VAR PLUS NUMBER { checkVar($1); value=value+$3; }
	| VAR MINUS NUMBER { checkVar($1); value=value-$3; }
	| VAR TIMES NUMBER { checkVar($1); value=value*$3; }
	| VAR DIVIDE NUMBER { checkVar($1); value=value/$3; }
;

%%

int checkVar(char *s){
	if (strcmp(s, var)) {
		printf("Variable \"%s\" is not declared", s);
		exit(1);
            };
}

int main() {
  if (yyparse())
     fprintf(stderr, "Successful parsing.\n");
  else
     fprintf(stderr, "error found.\n");
}