
#include <iostream>
#include <stdlib.h>
#include <Windows.h>
void HideConsole();
int main()
{
	HideConsole();
	system("C:/Users/piton/Desktop/e-triyaj/e-triyaj-desktop/e-triyaj-ui/main.py");
	return 0;
}
void HideConsole()
{
	::ShowWindow(::GetConsoleWindow(), SW_HIDE);
}
