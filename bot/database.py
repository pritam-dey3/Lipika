from pathlib import Path

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

Base = automap_base()


# customise models
class Note(Base):  # type: ignore
    __tablename__ = "notes"

    def __repr__(self) -> str:
        """Represent self."""
        return f"Note:\nid:{self.id}, user:{self.user}\n{self.title}\n{self.body}"


path = Path() / "databases" / "notes.db"
eng = create_engine(
    f"sqlite+pysqlite:///{path.absolute()}",
    future=True,
)

# session and metadata
Session = sessionmaker(bind=eng)
metadata = MetaData()

# reflect with orm models
Base.prepare(eng, reflect=True)
