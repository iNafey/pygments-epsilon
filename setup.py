from setuptools import setup, find_packages

setup (
  name='pygments-epsilon',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  etl = lexer:EtlLexer
  eol = lexer:EolLexer
  emfatic = lexer:EmfaticLexer
  """,
)