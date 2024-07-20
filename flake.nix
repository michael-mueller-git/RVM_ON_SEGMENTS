{
  description = "flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        system = "${system}";
        config.allowUnfree = true;
      };
      dependencies = [
        (pkgs.python311.withPackages (p: with p; [
          opencv4
          av
          tqdm
          pims
          torchvision
          pytorch
        ]))
      ];
      libPath = pkgs.lib.makeLibraryPath dependencies;
      binPath = pkgs.lib.makeBinPath dependencies;
    in
    {
      formatter.${system} = pkgs.nixpkgs-fmt;
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = dependencies;
      };
    };
}
