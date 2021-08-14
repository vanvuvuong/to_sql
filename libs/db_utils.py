"""
	Resolving the SQL connection staff
"""
from libs.get_config import get_config_yaml
from sqlalchemy.orm import Session
import sqlalchemy


def init_engine(config_file):
	"""
		Create a engine to connect to the SQL server
	"""
	config_data = get_config_yaml(config_file)
	engine_url = f"mysql+pymysql://{config_data['username']}:{config_data['password']}"\
					f"@{config_data['host']}/{config_data['database']}"
	try:
		engine = sqlalchemy.create_engine(engine_url, encoding='utf-8', echo=True)
		return engine
	except Exception as errors:
		print(f"Failed to connect to MySQL: {errors}")
		return None


def init_session(engine):
	"""
		Create the session of the engine
	"""
	try:
		session = Session(engine)
		return session
	except Exception as errors:
		print(f"Failed to init session: {errors}")
		return None

