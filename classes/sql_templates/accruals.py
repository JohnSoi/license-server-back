MORE_PAID_CLIENTS = """
    SELECT
        SUM(ac."sum") AS "value",
        cl."name" AS "title"
    FROM
        "accruals" ac
    LEFT JOIN
        "clients" cl
        ON ac."client_id" = cl."id"
    GROUP BY
        "ac"."client_id",
        cl."name"
    LIMIT 
        10
"""