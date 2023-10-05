# -*- coding: utf-8 -*-
"""
    Epsilon language lexers
    ~~~~~~~~~

    Pygments lexer for Epsilon languages.

"""

import re
from pygments.lexer import RegexLexer, bygroups, default
from pygments.token import Number, Comment, String, Keyword, Name, Operator, Whitespace, Punctuation, Text

__all__ = ['EtlLexer', 'EolLexer', 'EmfaticLexer']

class EtlLexer(RegexLexer):
     
    name = 'ETL'
    aliases = ['etl']
    filenames = ['*.etl']
    
    flags = re.MULTILINE | re.DOTALL
    
    tokens = {
        'root': [
            default('base'),
        ],
        'base': [
            (r'((?<![\\])[\'"])((?:.(?!(?<![\\])\1))*.?)\1', String),
            (r'[^\S\n]+', Whitespace),
            (r'(//.*?)(\n)', bygroups(Comment.Single, Whitespace)),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'\@(abstract|lazy|primary|greedy)', Keyword.Type),
            (r'^rule', Name.Class),
            (r'(?<=    |    )+(transform|to)', Name.Function),
            (r'((?<=rule )\w+)|((?<=extends )\w+)', Name.Attribute),
            (r'null', Operator.Word),
            (r'var', Keyword.Declaration),
            (r'extends|guard(?=:)', Name.Entity),
            (r'([0-9][0-9_]*\.([0-9][0-9_]*)?|'
             r'\.[0-9][0-9_]*)'
             r'([eE][+\-]?[0-9][0-9_]*)?[fFdD]?|'
             r'[0-9][eE][+\-]?[0-9][0-9_]*[fFdD]?|'
             r'[0-9]([eE][+\-]?[0-9][0-9_]*)?[fFdD]|'
             r'0[xX]([0-9a-fA-F][0-9a-fA-F_]*\.?|'
             r'([0-9a-fA-F][0-9a-fA-F_]*)?\.[0-9a-fA-F][0-9a-fA-F_]*)'
             r'[pP][+\-]?[0-9][0-9_]*[fFdD]?', Number.Float),
            (r'0[xX][0-9a-fA-F][0-9a-fA-F_]*[lL]?', Number.Hex),
            (r'0[bB][01][01_]*[lL]?', Number.Bin),
            (r'0[0-7_]+[lL]?', Number.Oct),
            (r'0|[1-9][0-9_]*[lL]?', Number.Integer),
            (r'[~^*!%&\[\]<>|+=/?-]', Operator),
            (r'[{}();:.,]', Punctuation),
            (r'[\w]+', Text),
            (r'\n', Whitespace),
        ]
    }
    
class EolLexer(RegexLexer):
     
    name = 'EOL'
    aliases = ['eol']
    filenames = ['*.eol']
    
    flags = re.MULTILINE | re.DOTALL
    
    tokens = {
        'root': [
            default('base'),
        ],
        'base': [
            #Strings, Comments, and Whitespace
            (r'((?<![\\])[\'"])((?:.(?!(?<![\\])\1))*.?)\1', String),
            (r'[^\S\n]+', Whitespace),
            (r'(//.*?)(\n)', bygroups(Comment.Single, Whitespace)),
            (r'/\*.*?\*/', Comment.Multiline),
            #Language Keywords
            (r'not|delete|import|for|while|in|and|or|operation|return|var|throw|if|new|else|transaction|abort|break|continue|assert|assertError|not|function|default|switch|case|as|ext|driver|alias|model|breakAll|async|group|nor|xor|implies', Keyword.Reserved),
            (r'true|false|self', Comment.Preproc),
            (r'Any|String|Integer|Real|Boolean|Native|Bag|Set|List|Sequence|Map|OrderedSet|Collection|Tuple|ConcurrentBag|ConcurrentMap|ConcurrentSet', Keyword.Type),
            #Language Operators, Punctuation, and Numbers
            (r'([0-9][0-9_]*\.([0-9][0-9_]*)?|'
             r'\.[0-9][0-9_]*)'
             r'([eE][+\-]?[0-9][0-9_]*)?[fFdD]?|'
             r'[0-9][eE][+\-]?[0-9][0-9_]*[fFdD]?|'
             r'[0-9]([eE][+\-]?[0-9][0-9_]*)?[fFdD]|'
             r'0[xX]([0-9a-fA-F][0-9a-fA-F_]*\.?|'
             r'([0-9a-fA-F][0-9a-fA-F_]*)?\.[0-9a-fA-F][0-9a-fA-F_]*)'
             r'[pP][+\-]?[0-9][0-9_]*[fFdD]?', Number.Float),
            (r'0[xX][0-9a-fA-F][0-9a-fA-F_]*[lL]?', Number.Hex),
            (r'0[bB][01][01_]*[lL]?', Number.Bin),
            (r'0[0-7_]+[lL]?', Number.Oct),
            (r'0|[1-9][0-9_]*[lL]?', Number.Integer),
            (r'[~^*!%&\[\]<>|+=/?-]', Operator),
            (r'[{}();:.,]', Punctuation),
            #Text and Line Ending Whitespace
            (r'[\w]+', Text),
            (r'\n', Whitespace),
        ]
    }
    
class EmfaticLexer(RegexLexer):

    name = 'Emfatic'
    aliases = ['emfatic']
    filenames = ['*.emf']
    
    flags = re.MULTILINE | re.DOTALL
    
    tokens = {
        'root': [
            default('base'),
        ],
        'base': [
            #Strings, Comments, and Whitespace
            (r'((?<![\\])[\'"])((?:.(?!(?<![\\])\1))*.?)\1', String),
            (r'[^\S\n]+', Whitespace),
            (r'(//.*?)(\n)', bygroups(Comment.Single, Whitespace)),
            (r'(@.*?)(\n)', bygroups(Comment.Single, Whitespace)),
            (r'/\*.*?\*/', Comment.Multiline),
            #Language Keywords
            (r'abstract|attr|class|enum|extends|import|package|ref|val|op|readonly|volatile|transient|unsettable|derived|unique|ordered|resolve|id|datatype', Keyword.Reserved),
            (r'true|false|self', Comment.Preproc),
            (r'boolean|Boolean|byte|Byte|char|Character|double|Double|float|Float|int|Integer|long|Long|short|Short|Date|String|Object|Class|EObject|EClass', Keyword.Type),
            #Language Operators, Punctuation, and Numbers
            (r'([0-9][0-9_]*\.([0-9][0-9_]*)?|'
             r'\.[0-9][0-9_]*)'
             r'([eE][+\-]?[0-9][0-9_]*)?[fFdD]?|'
             r'[0-9][eE][+\-]?[0-9][0-9_]*[fFdD]?|'
             r'[0-9]([eE][+\-]?[0-9][0-9_]*)?[fFdD]|'
             r'0[xX]([0-9a-fA-F][0-9a-fA-F_]*\.?|'
             r'([0-9a-fA-F][0-9a-fA-F_]*)?\.[0-9a-fA-F][0-9a-fA-F_]*)'
             r'[pP][+\-]?[0-9][0-9_]*[fFdD]?', Number.Float),
            (r'0[xX][0-9a-fA-F][0-9a-fA-F_]*[lL]?', Number.Hex),
            (r'0[bB][01][01_]*[lL]?', Number.Bin),
            (r'0[0-7_]+[lL]?', Number.Oct),
            (r'0|[1-9][0-9_]*[lL]?', Number.Integer),
            (r'[~^*!%&\[\]<>|+=/?-]', Operator),
            (r'[{}();:.,]', Punctuation),
            #Text and Line Ending Whitespace
            (r'[\w]+', Text),
            (r'\n', Whitespace),
        ]
    }
