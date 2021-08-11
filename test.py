# coding=utf-8

import ipsrvdb

if __name__ == "__main__":
    a = ipsrvdb.IPSrvDB("/home/ipsrv/dat/20210809.dat", mode="MEMORY")
    print(a.find('8.8.8.255'))
    print(a.findx('8.8.8.255'))
    print(a.findx('2001:250::ffff'))
    print(a.get_header())
    print(a.get_date())
    print(a.get_description())
