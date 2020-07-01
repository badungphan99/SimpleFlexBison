%{
#include "calc.tab.h"
#include <stdlib.h>
#include <stdio.h>
#define YY_DECL int yylex()
%}

whitespace [ \t]+
variable [_a-zA-Z][_a-zA-Z0-9]{0,30}
integer [0-9]+

%%

{whitespace}
{variable} {sscanf(yytext, "%s", yylval.iden); return(VAR);}
{integer} { yylval.ival=atoi(yytext);
 return NUMBER;
}
.   {errorMsg(); return *yytext;}
"=" {return EQUAL;}
"+" {return PLUS;}
"-" {return MINUS;}
"*" {return TIMES;}
"/" {return DIVIDE;}
%%

void errorMsg(){
    printf("Cannot understand character .\n");
}