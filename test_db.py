import pyodbc
import logging

logging.basicConfig(level=logging.DEBUG, filename='db_test.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=localhost\\TEST;"
        "DATABASE=gestion_parc_informatique;"
        "UID=hamza;"
        "PWD=hamza;"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    version = cursor.fetchone()[0]
    logger.info(f"SQL Server Version: {version}")
    print(f"Connected: {version}")
    conn.close()
except pyodbc.Error as e:
    logger.error(f"Database connection error: {str(e)}")
    print(f"Error: {str(e)}")