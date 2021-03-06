# encoding = utf-8


def fetch_every_nth_record(db, table, n, limit, where=None):
    query = create_query_every_nth_record(table, n, where, limit)
    records = db_perform_query(db, query)
    return records


def create_query_every_nth_record(table: str, n: int, where: str, limit: int = 50):
    query = create_query_every_nth_record_mysql(table, n, where, limit)
    return query


def db_perform_query(db, query: str):
    result = db_perform_query_sqlalchemy(db, query)
    return result


def create_query_every_nth_record_mysql(table: str, n: int, where: str, limit: int) -> str:
    if where:
        where = " " + where
    else:
        where = ""
    query = f"""
    SELECT {table}.* FROM {table} INNER JOIN (
        SELECT id FROM (
            SELECT @row:=@row+1 AS rownum, id FROM (
                SELECT id FROM {table}{where} ORDER BY id desc LIMIT {limit * n} 
            ) AS sorted
        ) as ranked WHERE rownum mod {n} = 0
    ) AS subset ON subset.id = {table}.id
    """
    return query


def db_perform_query_sqlalchemy(db, query):
    query = " ".join(query.split())
    db.engine.execute("set @row:=-1;")
    result = db.engine.execute(query)
    return result
