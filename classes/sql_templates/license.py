TYPE_PAID_LICENSES = """
    WITH free_licenses AS (
        SELECT 
            COUNT(*) AS "value",
            'Бесплатные лицензии' AS "title"
        FROM
            "licenses"
        WHERE
            "cost" = 0
            AND "license_id" IS NOT NULL
    ), paid_licenses AS (
        SELECT 
            COUNT(*) AS "value",
            'Платные лицензии' AS "title"
        FROM
            "licenses"
        WHERE
            "cost" > 0
            AND "license_id" IS NOT NULL
    ), process AS (
        SELECT * FROM "free_licenses"
        UNION
        SELECT * FROM "paid_licenses"
    )
    
    SELECT
        *
    FROM
        "process"
"""

COUNT_LICENSES = """
	SELECT 
		COUNT(*) AS "value",
		lc."name" AS "title"
	FROM 
		"clients" cl
	LEFT JOIN
		"licenses" as lc
		ON cl."license_id" = lc."id"
	WHERE
		cl."license_id" IS NOT NULL
	GROUP BY
		cl."license_id",
		lc."name"
"""
