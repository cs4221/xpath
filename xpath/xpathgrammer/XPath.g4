grammar XPath;



// Parser Rules
xpath: expr EOF;
expr: '/' nodetest pred? expr?;
pred: '['']';
nodetest: ( qualifiedPath | unqualifiedPath );
qualifiedPath: ;
unqualifiedPath: ;


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
KW_DESCENDANT: 'descendant';
KW_DESCENDANT_OR_SELF: 'descendant-or-self';
KW_FOLLOWING: 'following';
KW_FOLLOWING_SIBLING: 'following-sibling';
KW_NODE: 'node';
KW_PARENT: 'parent';
KW_PRECEDING: 'preceding';
KW_PRECEDING_SIBLING: 'preceding-sibling';
KW_SELF: 'self';
KW_TEXT: 'text';

      WS: [ \t\n\r\f\s] -> skip;
