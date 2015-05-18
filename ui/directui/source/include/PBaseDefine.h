#ifndef P_BASE_DEFINE_H
#define P_BASE_DEFINE_H 

#ifdef PLIB_EXPORTS
#define PLIBLIB_API __declspec(dllexport)
#else
#define PLIBLIB_API /*__declspec(dllimport)*/

#endif