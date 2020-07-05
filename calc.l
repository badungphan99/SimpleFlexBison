%option noyywrap
%{
#include "calc.tab.h"
#include <stdlib.h>
#include <stdio.h>
%}
newline [\n]
whitespace [ \t]+
variable [_a-zA-Z][_a-zA-Z0-9]*
integer 0|[1-9][0-9]*

%%
{newline} {return NEWLINE;}
{whitespace}
{variable} {sscanf(yytext, "%s", yylval.varName); return VAR;}
{integer} { yylval.val=atoi(yytext); return NUMBER;}
"=" {return EQUAL;}
"+" {return PLUS;}
"-" {return MINUS;}
"*" {return TIMES;}
"/" {return DIVIDE;}
. {printf("Cannot understand character \n"); exit(1);}
%%
