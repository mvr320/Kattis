// extract to string
#include <iostream>
#include <string>
#include <regex>

int main ()
{
  std::string empty;
  int instructions;
  std::cin >> instructions;
  std::getline (std::cin, empty); 
  
  for(int i=0; i<instructions; i++){
  	std::string line;
  	std::string simon;
  	
  	std::getline (std::cin, line);
  	simon = "Simon says";
  	
  	std::size_t found = line.find(simon);
	if (found!=std::string::npos){
    	std::string instruction;
    	std::cout << line.substr(found+10) << std::endl;
  	}
  }
}