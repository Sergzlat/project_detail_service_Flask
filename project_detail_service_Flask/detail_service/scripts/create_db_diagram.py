from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import create_engine

# Создайте подключение к вашей базе данных
engine = create_engine('postgresql://postgres:password@localhost:5432/postgres')

# Импортируйте ваши модели SQLAlchemy
from detail_service.models import Base

# Получите метаданные вашей базы данных
metadata = Base.metadata

# Создайте граф схемы базы данных
graph = create_schema_graph(metadata=metadata)

# Сохраните граф в файл
graph.write_png('database_schema.png')
