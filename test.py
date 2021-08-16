# coding=utf-8

import ipsrvdb

if __name__ == "__main__":
    a = ipsrvdb.IPSrvDB("/path/to/ipsrv.dat", mode="MEMORY")
    print(a.find('8.8.8.255'))
    print(a.find('2001:250::ffff'))
    print(a.findx('220.181.0.0'))
    print(a.get_header())
    print(a.get_date())
    print(a.get_description())
