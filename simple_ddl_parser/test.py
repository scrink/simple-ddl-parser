import re
from ddl_parser import DDLParser as dcl

s = '''create table if not exists imods.ods_imbs_bp_data_dev ( idsite string comment '应用id', server_time string comment '操作的日期时间') comment "埋点系统es总表数据" partitioned by (dt string) ;'''


reg = re.compile(r'\s+')
ddl = reg.sub(repl=' ',string=s)
ddl = ddl.lower().replace('\"','\'')
print(ddl)
result = dcl(ddl).run()
print(result)
print('\\u5e94\\u7528id'.encode().decode('unicode-escape'))