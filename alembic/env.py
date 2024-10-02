from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from warehouse import models  # Импортируйте ваши модели

# Это место, где вы загружаете конфигурацию Alembic
config = context.config

# Настройка логирования
fileConfig(config.config_file_name)

# Здесь указываем метаданные для модели
target_metadata = models.Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # Другие параметры, если нужно
        )

        with context.begin_transaction():
            context.run_migrations()

if __name__ == '__main__':
    run_migrations_online()
