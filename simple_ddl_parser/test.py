from ddl_parser import DDLParser

ddl = """
create table if not exists imods.ods_imp_app_tracking_info
(
row_id string ,
event_name      string comment '傻逼',
trigger_type    string ,
channel_user    string ,
key_desc        string ,
etl_load_time  string
)
    """

result = DDLParser(ddl).run()
print(result)
# print('\\u50bb\\u903c'.encode().decode('unicode-escape'))

