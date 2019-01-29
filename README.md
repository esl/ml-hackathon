# ml-hackathon


Under demo there is a little example I hacked up just to show how to get raw images, prepare them and plot the result.

This is just to be used as reference as models should indeed be stored, deployed, wrapped into daemons/containers and connected to Erlang via port/distribution.

Figure_1 shows the result which is far from accurate.

In order to make it more accurate, there could be more preparation on the images, a higher definition and more data.

In particular some images came up with "photo is no longer available" and therefore should be removed from the training and test set.



## NixPkg (very optional)

If you are running NixPkg the packages mentioned in the machine
learning will be available in the included nix-shell. Just run
`nix-shell` in the root of the repository.

One thing that is not included is guildai (because it was not
available as a nix package). It can be installed by:

```shell
> nix-shell
(wait a bit)
nix-shell> virtualenv guild
nix-shell> source guild/bin/activate
nix-shell> pip install guildai
```

This should give you everything you need to run the examples while you
are in the nix-shell.
