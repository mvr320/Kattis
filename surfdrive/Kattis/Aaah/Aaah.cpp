// extract to string
#include <iostream>
#include <string>

int main ()
{
  std::string ah1, ah2;

  std::getline (std::cin,ah1);
  std::getline (std::cin,ah2);
  
  if(ah1.length()<ah2.length()){
  	std::cout << "no";
  } else {
  	std::cout << "go";
  }

  return 0;
}