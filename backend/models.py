from typing import List

from sqlalchemy import Column, create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy import Table
from sqlalchemy.orm import Mapped, sessionmaker, declarative_base
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///./resources/sqlite/sales_db.db', connect_args={"check_same_thread": False}, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

tab_api_purchase_items = Table(
    "tab_api_purchase_items",
    Base.metadata,
    Column("purchase_id", ForeignKey("tab_api_purchase.id")),
    Column("item_id", ForeignKey("tab_api_item.id"))
)

tab_api_sale_items = Table(
    "tab_api_sale_items",
    Base.metadata,
    Column("sale_id", ForeignKey("tab_api_sale.id")),
    Column("item_id", ForeignKey("tab_api_item.id"))
)

class Item(Base):
    __tablename__ = "tab_api_item"
    id = mapped_column("id", Integer, nullable=False, primary_key=True)
    name = mapped_column("item_name", String)
    gold = mapped_column("gold", Integer)
    silver = mapped_column("silver", Integer)
    copper = mapped_column("copper", Integer)
    item_sales = relationship("Sale", secondary="tab_api_sale_items", back_populates="items")


class Purchase(Base):
    __tablename__ = "tab_api_purchase"
    id = Column("id", Integer, nullable=False, primary_key=True)
    items: Mapped[List[Item]] = relationship(secondary=tab_api_purchase_items)


class Sale(Base):
    __tablename__ = "tab_api_sale"
    id = Column("id", Integer, nullable=False, primary_key=True)
    items= relationship("Item", secondary="tab_api_sale_items", back_populates="item_sales")

Base.metadata.create_all(engine)