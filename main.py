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
    # print(sql)

    sql = text(sql)

    result = db_bz.engine.execute(sql)
    names = []
    for row in result:
        names.append(row[0])
    return names


def createInsert(names, table_name, old_table_name, to_schema, from_schema):
    names = ['"%s"' % i for i in names]
    # old_names = ['"%s"' % i for i in old_names]
    names = ',\n'.join(names)
    # old_names = ',\n'.join(old_names)
    old_names = names
    sql = '''
INSERT INTO %s.%s(
    %s)
SELECT %s FROM %s.%s;
        ''' % (to_schema, table_name, names, old_names, from_schema, old_table_name)
    return sql


def main():
    to_schema = 'public'
    from_schema = 'public'
    if len(sys.argv) == 5:
        table_name = sys.argv[1]
        old_table_name = sys.argv[2]
        to_schema = sys.argv[3]
        from_schema = sys.argv[4]
    elif len(sys.argv) == 3:
        table_name = sys.argv[1]
        old_table_name = sys.argv[2]
    else:
        print('you need run like: python %s table_name old_table_name' %
              sys.argv[0])
        exit(1)
    names = getColumns(table_name)
    # old_names = getColumns(old_table_name, from_schema)
    print(createInsert(names, table_name,
                       old_table_name, to_schema, from_schema))


if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
