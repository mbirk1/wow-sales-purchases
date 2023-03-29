from sqlalchemy import Column, create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy import Table
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///./resources/sqlite/sales_db.db', connect_args={"check_same_thread": False}, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

ItemPurchases = Table("tab_api_purchase_items",
                      Base.metadata,
                      Column("id", Integer, primary_key=True),
                      Column("purchase_id", Integer, ForeignKey('tab_api_purchase.id')),
                      Column("item_id", Integer, ForeignKey('tab_api_item.id')))

ItemSales = Table("tab_api_sale_items",
                  Base.metadata,
                  Column("id", Integer, primary_key=True),
                  Column("sale_id", Integer, ForeignKey('tab_api_sale.id')),
                  Column("item_id", Integer, ForeignKey('tab_api_item.id')))


class Item(Base):
    __tablename__ = "tab_api_item"
    id = mapped_column("id", Integer, nullable=False, primary_key=True)
    name = mapped_column("name", String)
    gold = mapped_column("gold", Integer)
    silver = mapped_column("silver", Integer)
    copper = mapped_column("copper", Integer)
    item_sales = relationship('Sale', secondary=ItemSales, backref='Item')
    item_purchase = relationship('Purchase', secondary=ItemPurchases, backref='Item')


class Purchase(Base):
    __tablename__ = "tab_api_purchase"
    id = Column("id", Integer, nullable=False, primary_key=True)


class Sale(Base):
    __tablename__ = "tab_api_sale"
    id = mapped_column("id", Integer, nullable=False, primary_key=True)


Base.metadata.create_all(engine)
