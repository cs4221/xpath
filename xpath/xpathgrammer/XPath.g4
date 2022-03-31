grammar XPath;



// Parser Rules
xpath: expr EOF;
expr: '/' nodetest;
pred: '['']';
nodetest: ( unqualifiedpath );


qualifiedpath: AXES '::' NODE_NAME
             |
             ;
unqualifiedpath: NODE_NAME;

allnodeselector: KW_NODE FUNCTION_CALL;
alltextselector: KW_TEXT FUNCTION_CALL;
allcommentselector: KW_COMMENT FUNCTION_CALL;
allprocessinginstructionselector: KW_PROCESSING_INSTRUCTION FUNCTION_CALL;


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

FUNCTION_CALL: '()';

OPERATOR:  '+'
        |  '-'
        |  '|'
        |  '*'
        |  'div'
        |  '='
        |  '!='
        |  '<'
        |  '<='
        |  '>'
        |  '>='
        |  'or'
        |  'and'
        |  'mod'
        ;

NODE_NAME: [a-zA-Z]+;

// Keywords for XPath
KW_ANCESTOR: 'ancestor';
KW_ANCESTOR_OR_SELF: 'ancestor-or-self';
KW_ATTRIBUTE: 'attribute';
KW_CHILD: 'child';
KW_COMMENT: 'comment';
KW_DESCENDANT: 'descendant';
KW_DESCENDANT_OR_SELF: 'descendant-or-self';
KW_FOLLOWING: 'following';
KW_FOLLOWING_SIBLING: 'following-sibling';
KW_NODE: 'node';
KW_PARENT: 'parent';
KW_PRECEDING: 'preceding';
KW_PRECEDING_SIBLING: 'preceding-sibling';
KW_PROCESSING_INSTRUCTION: 'processing-instruction';
KW_SELF: 'self';
KW_TEXT: 'text';

WS: [ \t\n\r\f]+ -> skip;
