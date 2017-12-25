#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
home = str(Path.home())
import sys
sys.path.append(home + "/lib_py")
import db_bz

from sqlalchemy import text


def getColumns(table_name, schema='public'):

    sql = '''
    SELECT column_name
    FROM information_schema.columns
    WHERE    upper(table_name)   =  upper('%s')
    and table_schema = '%s'
    order by column_name
    ''' % (table_name, schema)
    #print(sql)

    sql = text(sql)

    result = db_bz.engine.execute(sql)
    names = []
    for row in result:
        names.append(row[0])
    return names


def createInsert(names, old_names, table_name, old_table_name):
    names = ','.join(names)
    old_names = ','.join(old_names)
    sql = '''
INSERT INTO public.%s(
    %s)
SELECT %s FROM public_old.%s;
        ''' % (table_name, names, old_names, old_table_name)
    return sql


def main():
    if len(sys.argv) == 3:
        table_name = sys.argv[1]
        old_table_name = sys.argv[2]
    else:
        print('you need run like: python %s table_name old_table_name' % sys.argv[0])
    names = getColumns(table_name)
    old_names = getColumns(old_table_name, 'public_old')
    print(createInsert(names, old_names, table_name, old_table_name))


if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
