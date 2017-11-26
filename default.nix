with import <nixpkgs> {};

pkgs.python35.withPackages (ps: with ps; [ alembic sqlalchemy psycopg2 pygments-markdown-lexer pandoc jedi PyGithub github3_py ])


# To use, run this command:
# nix-env -if ~/.nixpkgs/mypy.nix

