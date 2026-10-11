#include <dlfcn.h>
#include <cstdlib>
#include <iostream>
#include <string>
#include <codecvt>
#include <locale>
#include <filesystem>
// Adapter for the exported conversion API of the installed digiKam 9.1.0.
// All native allocations are deliberately oversized and process-local.
template<class F> F symbol(void* lib,const char* name) {
 auto p=dlsym(lib,name); if(!p) {std::cerr<<dlerror()<<'\n';std::exit(2);} return reinterpret_cast<F>(p);
}
int main(int argc,char**argv){
 if(argc!=3 || !std::filesystem::is_regular_file(argv[1]) || std::filesystem::exists(argv[2])) return 2;
 const char* base="/Applications/digiKam.org/digikam.app/Contents";
 auto qt=dlopen((std::string(base)+"/libexec/qt6/lib/QtCore.framework/Versions/A/QtCore").c_str(),RTLD_NOW|RTLD_GLOBAL);
 if(!qt){std::cerr<<dlerror()<<'\n';return 2;}
 auto core=dlopen((std::string(base)+"/lib/libdigikamcore.9.1.0.dylib").c_str(),RTLD_NOW|RTLD_GLOBAL);
 if(!core){std::cerr<<dlerror()<<'\n';return 2;}
 auto app=std::calloc(1,4096);
 symbol<void(*)(void*,int*,char**,int)>(qt,"_ZN16QCoreApplicationC1ERiPPci")(app,&argc,argv,0x060b00);
 auto makeString=[&](const char* s){
   auto u=std::wstring_convert<std::codecvt_utf8_utf16<char16_t>,char16_t>{}.from_bytes(s);
   auto q=std::calloc(1,64);
   symbol<void(*)(void*,const void*,long long)>(qt,"_ZN7QStringC1EPK5QCharx")(q,u.data(),u.size());return q;
 };
 symbol<void(*)(const void*)>(qt,"_ZN16QCoreApplication18setApplicationNameERK7QString")(makeString("digikam"));
 symbol<bool(*)()>(core,"_ZN7Digikam10MetaEngine15initializeExiv2Ev")();
 auto writer=std::calloc(1,64);
 symbol<void(*)(void*)>(core,"_ZN7Digikam9DNGWriterC1Ev")(writer);
 symbol<void(*)(void*,const void*)>(core,"_ZN7Digikam9DNGWriter12setInputFileERK7QString")(writer,makeString(argv[1]));
 symbol<void(*)(void*,const void*)>(core,"_ZN7Digikam9DNGWriter13setOutputFileERK7QString")(writer,makeString(argv[2]));
 symbol<void(*)(void*,bool)>(core,"_ZN7Digikam9DNGWriter19setCompressLossLessEb")(writer,true);
 symbol<void(*)(void*,bool)>(core,"_ZN7Digikam9DNGWriter24setBackupOriginalRawFileEb")(writer,false);
 symbol<void(*)(void*,bool)>(core,"_ZN7Digikam9DNGWriter17setUpdateFileDateEb")(writer,true);
 symbol<void(*)(void*,int)>(core,"_ZN7Digikam9DNGWriter14setPreviewModeEi")(writer,1);
 int result=symbol<int(*)(void*)>(core,"_ZN7Digikam9DNGWriter7convertEv")(writer);
 std::cout<<"DNGWriter result="<<result<<std::endl;
 symbol<void(*)(void*)>(core,"_ZN7Digikam9DNGWriterD1Ev")(writer);
 // OS reclaims Qt/core state on exit; no global app or source metadata is changed.
 return result==0?0:1;
}
