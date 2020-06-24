

RED='\033[0;31m'

GREEN='\033[0;32m'

NC='\033[0m' # No Color



echo -e "\n${RED}##### Starting OS X bootstrap #####${NC} \n"

echo -e "${GREEN} ---> Check and install Homebrew${NC} \n"

command -v brew >/dev/null 2>&1 || { echo >&2 "Installing Homebrew Now"; \

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"; }



install_python37 () {

brew install python3

brew link --overwrite python3

export PATH=/usr/local/share/python:$PATH

}



echo -e "\n${GREEN} ---> installing/updating Python 3.7 ${NC} \n"



if command -v python3 &>/dev/null; then

if [[ $(python3 --version | grep "Python 3.7") =~ 3.7 ]]; then

echo -e "\n${GREEN} ---> Skipping Python 3.7 install. Already installed. ${NC}\n"--version | grep "Python 3.7"

elif command -v python3.7 &>/dev/null; then

echo -e "\n${GREEN} ---> Verified for specific python3.7. Skipped install. Already installed. ${NC}\n"--version | grep "Python 3.7"

else

echo -e "\n${GREEN} ---> Installing Python 3.7 #####${NC}\n"

install_python37

fi

else

echo -e "\n${GREEN} ---> Installing Python 3.7 #####${NC}\n"

install_python37

fi