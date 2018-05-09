#Installation
##Bash Integration
add to .bash_profile:

function openha() {
   python path/to/openha.py $1 $2 $3
}

##Arguments
1. first argument: index of homework
2. second argument: prename
3. third argument: lastname


##Settings
adjust  self.mainpath  and self.zippath

1. in zippath are the folders SoSe18 Prog2 WINF-HA01, SoSe18 Prog2 WINF-HA02,... that contain the zips. Please remove the token  (whatsorever) behind SoSe18 Prog2 WINF-HA01
2. In mainpath we extract the zips and open


##Note also
You have to make sure you can run idea from the command line (Tools > Create Command-line launcher)



