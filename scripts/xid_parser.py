if __name__ != '__main__':
    raise ImportError

with open("./DerivedCoreProperties.txt",'r',encoding='utf-8') as f:
    lines = f.read().split("\n")

XID_Start = []
XID_Continue = []

for l in lines:
    if l.startswith("#") or ';' not in l:
        continue
    index = l.index(';')
    rs = l[:index]
    if '..' in rs:
        _ = rs.split('..')
        rc = (_[0].strip(),_[1].strip())
    else:
        rc = rs.strip()
    config = l[index+1:]
    if '#' in config:
        config = config[:config.index('#')]
    if 'XID_Start' in config:
        XID_Start.append(rc)
    elif 'XID_Continue' in config:
        XID_Continue.append(rc)

file_fmt = '''\
#ifndef __UNICODE_XID_HPP
#define __UNICODE_XID_HPP

namespace UnicodeXid {
    typedef struct {
        int xid_start;
        int xid_end;    // 0xFFFFF0: XidStartChar; 0xFFFFF1: XidContinueChar; >0: XidStartRange; <0: XidContinueRange (abs)
    } UnicodeXidType;

    const char UNICODE_XID_VERSION[] = "a.b.c";   // Manually
    const unsigned int UNICODE_XID_LIST_LEN = %d;
    const unsigned int UNICODE_XID_START_CHAR_ENDNUM = 0xFFFFF0;
    const unsigned int UNICODE_XID_CONTINUE_CHAR_ENDNUM = 0xFFFFF1;

    const UnicodeXidType UNICODE_XID_LIST[] = {
%s
    };
}

#endif
'''
xid_start_char_fmt = '        { 0x%s , 0xFFFFF0 },'
xid_continue_char_fmt = '        { 0x%s , 0xFFFFF1 },'
xid_start_range_fmt = '        { 0x%s , 0x%s },'
xid_continue_range_fmt = '        { 0x%s , -0x%s },'

xid_list = []

for i in XID_Start:
    if isinstance(i,tuple):
        r0 = i[0]
        r1 = i[1]
        xid_list.append(xid_start_range_fmt%(r0,r1))
    else:
        xid_list.append(xid_start_char_fmt%i)

for i in XID_Continue:
    if isinstance(i,tuple):
        r0 = i[0]
        r1 = i[1]
        xid_list.append(xid_continue_range_fmt%(r0,r1))
    else:
        xid_list.append(xid_continue_char_fmt%i)

with open('unicode.hpp','w',encoding='utf-8') as f:
    f.write(file_fmt%(len(xid_list),'\n'.join(xid_list)))