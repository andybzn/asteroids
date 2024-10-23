{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
   pkgs.python3
   pkgs.python3Packages.pygame
   pkgs.black
  ];
  shellHook = ''
    python3 -m venv venv
    echo "Welcome to your development environment! 🐍"
    echo "Python is available."
  '';
}
