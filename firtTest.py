
#include "std_testcase.h"

#include <wchar.h>

namespace test
{


void testo()
{
    wchar_t * data;
    wchar_t * &dataRef = data;
    data = (wchar_t *)malloc(100*sizeof(wchar_t));
    if (data == NULL) {exit(-1);}
  
    wmemset(data, L'A', 100-1);
    data[100-1] = L'\0';
    {
        wchar_t * data = dataRef;
        {
            wchar_t dest[50] = L"";
          
            wcscpy(dest, data);
            printWLine(data);
            free(data);
        }
    }
}

