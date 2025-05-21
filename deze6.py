import logging
from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d'
)

logging.info(f'Сьогоднішня дата: {current_date}')
