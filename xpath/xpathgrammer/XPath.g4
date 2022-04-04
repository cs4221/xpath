grammar XPath;

/*
Adapted from XPath2.0 @https://github.com/antlr/grammars-v4/blob/master/xpath/xpath20/XPath20.g4
Original author: Ken Domino, 2 Jan 2022

This is a subset of the XPath2.0 grammar based on NUS CS4221 lecture content.

Issues:
1. Unable to match node(), text() and processing-instructions() {problem caused by greedy matching}
2. Unable to match more than one predicate conditions (predepxrsingle) i.e. a="gt" or a="few"
3. Unable to match path disjunction i.e. (/album1 | /album2)/name
*/

// Parser Rules
xpath: expr EOF;

// Location step
expr: document ( locationstepexpr )*;
document: 'doc' OP StringLiteral CP;
locationstepexpr: SLASH relativepath
                | SLASH relativepath pred
                ;

// Paths
absolutepath: SLASH path;
relativepath: path;
path:  unqualifiedpath | qualifiedpath ;
unqualifiedpath: nodetest;
qualifiedpath: AXES COLONCOLON nodetest;

// Nodetest
// ! Unable to match the selectors as ANTLR4 tries to match the largest possible, which is nodeselector
nodetest: allnodeselector
        | alltextselector
        | allcommentselector
        | allprocessinginstructionselector
        | allselector
        | nodeselector
        ;

allselector: STAR;
allnodeselector: KW_NODE OP CP;
alltextselector: KW_TEXT OP CP;
allcommentselector: KW_COMMENT OP CP;
allprocessinginstructionselector: KW_PROCESSING_INSTRUCTION OP CP;
nodeselector: NODE_NAME;

// Predicates
pred: OB predexpr CB;
predexpr: predexprsingle ( PREDICATE_CONNECTIVES predexprsingle )*;
predexprsingle: predpath PREDICATE_OPERATOR literal;
predpath: absolutepath ( SLASH relativepath )*
        | relativepath ( SLASH relativepath )*
        ;

literal: StringLiteral | IntegerLiteral;

// Lexer Rules
AXES: KW_ANCESTOR
    | KW_ANCESTOR_OR_SELF
    | KW_ATTRIBUTE
    | KW_CHILD
    | KW_DESCENDANT
    | KW_DESCENDANT_OR_SELF
    | KW_FOLLOWING
    | KW_FOLLOWING_SIBLING
    | KW_PARENT
    | KW_PRECEDING
    | KW_PRECEDING_SIBLING
    | KW_SELF
    ;

// NODE_NAME is alias for xml tag names:
//    - Element names are case-sensitive
//    - Element names must start with a letter or underscore
//    - Element names cannot start with the letters xml(or XML, or Xml, etc)
//    - Element names can contain letters, digits, hyphens, underscores, and periods
//    - Element names cannot contain spaces
NODE_NAME: [a-zA-Z_][a-zA-Z0-9._-]*;
DOCUMENT_NAME: [a-zA-Z0-9._-]+;

PREDICATE_OPERATOR: EQ
                  | LT
                  | GT
                  | LE
                  | GE
                  | NE
                  ;

PREDICATE_CONNECTIVES: KW_OR
                     | KW_AND
                     | KW_NOT
                     | P
                     ;

AT : '@' ;
BANG : '!' ;
CB : ']' ;
CC : '}' ;
CEQ : ':=' ;
COLON : ':' ;
COLONCOLON : '::' ;
COMMA : ',' ;
CP : ')' ;
CS : ':*' ;
D : '.' ;
DD : '..' ;
DOLLAR : '$' ;
EG : '=>' ;
EQ : '=' ;
GE : '>=' ;
GG : '>>' ;
GT : '>' ;
LE : '<=' ;
LL : '<<' ;
LT : '<' ;
MINUS : '-' ;
NE : '!=' ;
OB : '[' ;
OC : '{' ;
OP : '(' ;
P : '|' ;
PLUS : '+' ;
POUND : '#' ;
PP : '||' ;
QM : '?' ;
SC : '*:' ;
SLASH : '/' ;
SS : '//' ;
STAR : '*' ;

// Keywords for XPath
KW_ANCESTOR: 'ancestor';
KW_ANCESTOR_OR_SELF: 'ancestor-or-self';
KW_AND: 'and';
KW_ATTRIBUTE: 'attribute';
KW_CHILD: 'child';
KW_COMMENT: 'comment';
KW_DESCENDANT: 'descendant';
KW_DESCENDANT_OR_SELF: 'descendant-or-self';
KW_FOLLOWING: 'following';
KW_FOLLOWING_SIBLING: 'following-sibling';
KW_NODE: 'node';
KW_NOT: 'not';
KW_OR: 'or';
KW_PARENT: 'parent';
KW_PRECEDING: 'preceding';
KW_PRECEDING_SIBLING: 'preceding-sibling';
KW_PROCESSING_INSTRUCTION: 'processing-instruction';
KW_SELF: 'self';
KW_TEXT: 'text';

IntegerLiteral : FragDigits;
StringLiteral : ('"' (FragEscapeQuot | ~[^"])*? '"') | ('\'' (FragEscapeApos | ~['])*? '\'');
fragment FragEscapeQuot : '""';
fragment FragEscapeApos : '\'';
fragment FragDigits : [0-9]+ ;

WS: [ \t\n\r\f]+ -> skip;
