#include <iostream>

int main(void)
{
    char name[100];
    char lang[200];

    std::cout<<"what's your name";
    std::cin>>name;

    std::cout<<"what's favorite programming language ";
    std::cin>>lang;

    std::cout<<"My name is"<<name;
    std::cout<<"My favorite programming language is"<<lang<<std::endl;

    return 0;

}
