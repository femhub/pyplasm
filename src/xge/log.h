#ifndef _LOG_H__
#define _LOG_H__

#include <xge/xge.h>

class XGE_API Log
{
public:

	//ask for redirect output to a file
	static bool redirect(uint64 handle);

	//write a log message
	static void printf(const char * format, ...);

	// silence a log 
	static void silence (bool silent);
	
private:
	#ifdef _WINDOWS
	static HANDLE __redirect;
	#endif

	static bool silent;
};

#endif //_LOG_H__
