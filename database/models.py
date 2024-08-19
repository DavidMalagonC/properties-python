"""
Defines the models and data access logic for the application.
"""
import mysql.connector

class PropertyModel:
    """
    Provides methods to retrieve property data from the database based on filters.
    Ensures that only properties with the latest status are retrieved.
    Limits the results to 100 records.
    """
    @staticmethod
    def get_properties(db, filters: dict) -> list:
        """
        Retrieves properties from the database based on the provided filters.
        Ensures that only properties with the latest status are retrieved.
        Limits the results to 100 records.
        """
        query = """
        SELECT p.address, p.city, p.price, p.description, p.year, s.name AS status 
        FROM property p
        JOIN status_history sh ON p.id = sh.property_id
        JOIN status s ON sh.status_id = s.id
        WHERE sh.update_date = (
            SELECT MAX(sh2.update_date)
            FROM status_history sh2
            WHERE sh2.property_id = p.id
        )
        AND s.name IN ('pre_venta', 'en_venta', 'vendido')
        """
        params = []

        if 'year' in filters and filters['year']:
            query += " AND p.year = %s"
            params.append(filters['year'])

        if 'city' in filters and filters['city']:
            query += " AND p.city = %s"
            params.append(filters['city'])

        if 'status' in filters and filters['status']:
            query += " AND s.name = %s"
            params.append(filters['status'])

        query += " LIMIT 100"

        try:
            result = db.execute_query(query, params)
            return [dict(row) for row in result]
        except mysql.connector.Error as e:
            print(f"Database error occurred: {e}")
            return []
        except TypeError as e:
            print(f"Type error occurred: {e}")
            return []
        except ValueError as e:
            print(f"Value error occurred: {e}")
            return []
