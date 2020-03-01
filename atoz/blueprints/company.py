from flask import render_template, redirect, url_for, current_app, Blueprint, request, g
from atoz.utils import select_t

from atoz.utils import impala_s

company_bp = Blueprint('company', __name__)


@company_bp.route('/b/')
def index():
    col_n = ('岗位名称', '薪资', '城市', '公司', '福利', '描述', '小类', '大类', '主营', '规模', '经验', '学历')
    key = request.args.get('key_0')
    if key != '' and key is not None:
        keys = key.split()
        sql = "select j_name, salary_range, city, c_name, c_welfare, j_responsibilities,j_cate_s, j_cate_l, main_business, c_size, j_t, j_e from job_t where "
        for word in keys:
            sql += "concat(j_name, city, c_name, c_welfare, j_responsibilities, j_cate_s, j_cate_l, main_business, c_size, j_t, j_e) like '%{}%' and ".format(
                word)
        sql = sql[:-5] + ' limit 100;'

        res0 = impala_s(sql)

        res, time0 = res0[0], res0[1]

        infos = []
        for row in res[:100]:
            row_l = []
            for col in row:
                row_l.append(col)
            infos.append(row_l)
    else:
        infos = []
        time0 = 0
    return render_template('search.html', items=infos, col_n=col_n, time=(time0 * 1000))




