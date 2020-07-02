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
{variable} {sscanf(yytext, "%s", yylval.varName); return(VAR);}
{integer} { yylval.val=atoi(yytext);
 return NUMBER;
}
"=" {return EQUAL;}
"+" {return PLUS;}
"-" {return MINUS;}
"*" {return TIMES;}
"/" {return DIVIDE;}
.   {errorMsg(); return *yytext;}
%%

void errorMsg(){
    printf("Cannot understand character .\n");
}