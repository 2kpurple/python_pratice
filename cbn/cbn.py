# coding: utf-8

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import xlsxwriter

db = SqliteExtDatabase('CBN.db')


class BaseModel(Model):
    class Meta:
        database = db


class CBNWeek(BaseModel):

    number = TextField()
    week_id = IntegerField()
    issue_date = TextField()
    name = TextField()
    cover_img = TextField()


class Ariticle(BaseModel):

    week = ForeignKeyField(CBNWeek, related_name='ariticle')
    art_id = IntegerField()
    title = TextField()
    chapt_brief = TextField()
    chapt_time = TextField()
    category_name = TextField()
    url = TextField()


def create_xlsx():
    workbook = xlsxwriter.Workbook('cbn_all.xlsx')
    worksheet = workbook.add_worksheet()
    table_head = [u'刊号', u'刊名', u'发行时间', u'封面', u'文章名', u'文章概要', u'文章栏目', u'文章发布时间', u'文章链接']
    # worksheet.set_column('A:M', 10)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('E:E', 30)
    worksheet.set_column('H:H', 15)
    bold = workbook.add_format({'bold': 1, 'align': 'center'})
    worksheet.write_row('A1', table_head, bold)


def main():
    db.connect()
    create_xlsx()
    print Ariticle.select().join(CBNWeek).where(CBNWeek.week_id == 1).count()
    print CBNWeek.select().where(CBNWeek.week_id == 1).get().name
    # for ariticle in Ariticle.select().join(CBNWeek).where(CBNWeek.week_id > 500):
    #     print ariticle.title


if __name__ == '__main__':
    main()