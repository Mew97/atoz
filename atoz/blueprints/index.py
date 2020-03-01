from flask import render_template, redirect, url_for, current_app, Blueprint, g
from atoz.utils import select_t
import pymysql

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    return render_template('index.html')


@index_bp.route('/t1')
def city_area():
    col_n = ('城市', '省份', '地区', '平均薪资', '工作岗位', '公司数量')
    sql = 'select a.city, a.pcv_name, a.area_name, cast(a.avg as int), a.count, a.count_c from city_info a where pcv_name not in ("不明");'
    db_n = 'job_db'
    items = select_t(sql, db_n)
    return render_template('_table.html', items=items, col_n=col_n)


@index_bp.route('/t2')
def welfare():
    col_n = ('福利名称', '公司数目', '岗位大类', '岗位数目')
    sql = 'select a.welfare, cast(a.c_conunt as int), a.j_cate_l, cast(a.count as int) from welfare_info a order by cast(a.c_conunt as int) desc limit 1000;'
    db_n = 'job_db'
    items = select_t(sql, db_n)
    return render_template('_table.html', items=items, col_n=col_n)


@index_bp.route('/t3')
def salary():
    col_n = ('岗位类别', '所属大类', '最高薪资', '最低薪资', '城市岗位数', '平均薪资', '学历', '经验要求')
    sql = 'select a.j_cate_s, a.j_cate_l, a.sal_max, a.sal_min, a.j_c_count, cast(a.sal_avg as int ), a.j_e, a.j_t from sal_infore a where cast(a.sal_min as int) > 2000;'
    db_n = 'job_db'
    items = select_t(sql, db_n)
    return render_template('_table.html', items=items, col_n=col_n)
