/*** Definition Section ***/

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void yyerror(char *);
#include "quat.h"
#include "y.tab.h"
%}

%%

(0|[1-9][0-9]*)(\.[0-9]+)?   {
/*
	printf("Token: NUMBER; Lexeme: %s\n", yytext);
*/
	yylval.num = atof(yytext);
	return NUMBER;
	}

Rotation   {
/*
	printf("Token: ROTATION; Lexeme: %s\n", yytext);
*/
	yylval.str = strdup(yytext);
	return ROTATION;
	}

[+\-*(),ijk/]   {
/*
	printf("Token and Lexeme: %s\n", yytext);
*/
	return *yytext;
	}

\n   {
/*
	printf("Token and Lexeme: <newline>\n");
*/
	return *yytext;
	}

[ \t]   {   }

.   {
/*
	printf("Invalid character.\n");
*/
	yyerror("invalid character");
}

%%
/*** C Code section ***/

void yyerror(char *s) {
	fprintf(stderr, "line %d: yytext = %s. Error msg: %s.\n:", yylineno, yytext, s);
}

int yywrap(void) {
	return 1;
}

/* comment out the function main() if using lex with yacc */
/*
int main(void) {
	yylex();
	return 0;
}
*/
