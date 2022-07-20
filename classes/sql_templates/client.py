ACTIVITY_CLIENTS = """
WITH all_clients AS (
	SELECT 
		COUNT(*) AS "value",
		'Все клиенты' AS "title"
	FROM 
		"clients"
), active_clients AS (
	SELECT 
		COUNT(*) AS "value",
		'Активные клиенты' AS "title"
	FROM 
		"clients"
	WHERE
		"is_active" IS TRUE
), unactive_clients AS (
	SELECT 
		COUNT(*) AS "value",
		'Неактивные клиенты' AS "title"
	FROM 
		"clients"
	WHERE
		"is_active" IS FALSE
), process AS (
	SELECT * FROM "all_clients" 
	UNION
	SELECT * FROM "active_clients"
	UNION
	SELECT * FROM "unactive_clients"
)


SELECT 
	* 
FROM 
	"process"
"""

TYPE_LICENSE_CLIENT = """
WITH all_clients AS (
	SELECT 
		COUNT(*) AS "value",
		'Все клиенты' AS "title"
	FROM 
		"clients"
), paid_clients AS (
	SELECT 
		COUNT(*) AS "value",
		'Платные клиенты' AS "title"
	FROM 
		"clients"
	WHERE
		"license_uuid" IN (SELECT uuid FROM "licenses" WHERE "cost" > 0)
), free_clients AS (
	SELECT 
		COUNT(*) AS "value",
		'Бесплатные клиенты' AS "title"
	FROM 
		"clients"
	WHERE
		"license_uuid" IN (SELECT uuid FROM "licenses" WHERE "cost" > 0)
), not_licenses_clients AS (
	SELECT 
		COUNT(*) AS "value",
		'Клиенты без лицензий' AS "title"
	FROM 
		"clients"
	WHERE
		"license_uuid" IS NULL
), process AS (
	SELECT * FROM "all_clients" 
	UNION
	SELECT * FROM "paid_clients"
	UNION
	SELECT * FROM "free_clients"
	UNION
	SELECT * FROM "not_licenses_clients"
)


SELECT 
	* 
FROM 
	"process"
"""
