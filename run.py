from app import app
import logging
from logging import Formatter, FileHandler

PORT = 5000

if __name__ == '__main__':
    file_handler = FileHandler('app.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s %(username)s: %(message)s')
    )
    app.logger.addHandler(file_handler)
    app.run(port=PORT, debug=True)
