# coding: utf-8

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import io
import requests
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


def insert_maga(workbook, worksheet, maga, start_row):
    cover = maga.cover_img
    image_data = io.BytesIO(requests.get(cover).content)
    worksheet.insert_image(start_row, 3, cover, {'image_data': image_data, 'x_scale': 0.3, 'y_scale': 0.3})
    content_format = workbook.add_format({'text_wrap': 1, 'valign': 'top'})
    merge_format = workbook.add_format({'align': 'center', 'valign': 'top'})

    art_array = Ariticle.select().join(CBNWeek).where(CBNWeek.week_id == maga.week_id)
    row = start_row
    for art in art_array:
        content = [art.title, art.chapt_brief, art.category_name, art.chapt_time, art.url]
        worksheet.write_row(row, 4, content, content_format)
        row += 1
    print 'start_row = %d, row = %d' % (start_row, row)
    worksheet.merge_range(start_row, 0, row - 1, 0, maga.number, merge_format)
    worksheet.merge_range(start_row, 1, row - 1, 1, maga.name, merge_format)
    worksheet.merge_range(start_row, 2, row - 1, 2, maga.issue_date, merge_format)
    worksheet.merge_range(start_row, 3, row - 1, 3, '', merge_format)
    return row


def create_xlsx():
    workbook = xlsxwriter.Workbook('cbn_all.xlsx')
    worksheet = workbook.add_worksheet()
    table_head = [u'刊号', u'刊名', u'发行时间', u'封面', u'文章名', u'文章概要', u'文章栏目', u'文章发布时间', u'文章链接']
    worksheet.set_column('C:C', 15)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:F', 30)
    worksheet.set_column('H:H', 15)
    worksheet.set_column('G:G', 15)
    worksheet.set_column('I:I', 30)
    head_format = workbook.add_format({'bold': 1, 'align': 'center'})
    worksheet.write_row('A1', table_head, head_format)

    maga_array = CBNWeek.select()

    row = 1

    for maga in maga_array:
        print maga.number + ' ' + maga.name
        row = insert_maga(workbook, worksheet, maga, row)


def main():
    db.connect()
    create_xlsx()
    # for ariticle in Ariticle.select().join(CBNWeek).where(CBNWeek.week_id > 500):
    #     print ariticle.title


if __name__ == '__main__':
    main()