from flask import render_template, redirect, url_for, current_app, Blueprint, request
from atoz.utils import select_t, impala_s, result_l, result_3d

area_bp = Blueprint('area', __name__)


@area_bp.route('/')
def index():
    return render_template('area.html')


@area_bp.route('/a0/')
def area0():
    return render_template('charts/五大城市前20职位图.html')


@area_bp.route('/a1/')
def area1():
    return render_template('charts/上海市.html')


@area_bp.route('/a2/')
def area2():
    return render_template('charts/北京市.html')


@area_bp.route('/a3/')
def area3():
    return render_template('charts/天津市.html')


@area_bp.route('/a4/')
def area4():
    return render_template('charts/广东省.html')


@area_bp.route('/a5/')
def area5():
    return render_template('charts/湖北省.html')


@area_bp.route('/a6/')
def map_t():
    return render_template('charts/全国主要城市岗位分布图.html')


# 3d图
@area_bp.route('/a7')
def c_3d_1():
    sql = 'select a.j_t, a.j_e, cast(a.avg_sal as int) from t_sh a;'
    db_n = 'job_db'
    items = select_t(sql, db_n)

    def f_x(j):
        if j == '不限':
            return 0
        if j == '应届毕业生':
            return 1
        if j == '1年以下':
            return 2
        if j == '1-3年':
            return 3
        if j == '3-5年':
            return 4
        if j == '5-10年经验':
            return 5
        if j == '10年以上':
            return 6

        if j == '不限':
            return 0
        if j == '中专及以下':
            return 1
        if j == '大专':
            return 2
        if j == '本科':
            return 3
        if j == '硕士':
            return 4
        if j == '博士':
            return 5

    t = []
    for i in items:
        t.append([f_x(i[0]), f_x(i[1]), i[2]])

    return render_template('charts/bar3d.html', t_data=t)


@area_bp.route('/a8')
def c_3d_2():
    sql = 'select a.j_t, a.j_e, cast(a.avg_sal as int) from t_bj a;'
    db_n = 'job_db'
    items = select_t(sql, db_n)

    def f_x(j):
        if j == '不限':
            return 0
        if j == '应届毕业生':
            return 1
        if j == '1年以下':
            return 2
        if j == '1-3年':
            return 3
        if j == '3-5年':
            return 4
        if j == '5-10年经验':
            return 5
        if j == '10年以上':
            return 6

        if j == '不限':
            return 0
        if j == '中专及以下':
            return 1
        if j == '大专':
            return 2
        if j == '本科':
            return 3
        if j == '硕士':
            return 4
        if j == '博士':
            return 5

    t = []
    for i in items:
        t.append([f_x(i[0]), f_x(i[1]), i[2]])

    return render_template('charts/bar3d.html', t_data=t)


@area_bp.route('/a9')
def c_3d_3():
    sql = 'select a.j_t, a.j_e, cast(a.avg_sal as int) from t_gz a;'
    db_n = 'job_db'
    items = select_t(sql, db_n)

    def f_x(j):
        if j == '不限':
            return 0
        if j == '应届毕业生':
            return 1
        if j == '1年以下':
            return 2
        if j == '1-3年':
            return 3
        if j == '3-5年':
            return 4
        if j == '5-10年经验':
            return 5
        if j == '10年以上':
            return 6

        if j == '不限':
            return 0
        if j == '中专及以下':
            return 1
        if j == '大专':
            return 2
        if j == '本科':
            return 3
        if j == '硕士':
            return 4
        if j == '博士':
            return 5

    t = []
    for i in items:
        t.append([f_x(i[0]), f_x(i[1]), i[2]])

    return render_template('charts/bar3d.html', t_data=t)


@area_bp.route('/a10')
def c_3d_4():
    sql = 'select a.j_t, a.j_e, cast(a.avg_sal as int) from t_sz a;'
    db_n = 'job_db'
    items = select_t(sql, db_n)

    def f_x(j):
        if j == '不限':
            return 0
        if j == '应届毕业生':
            return 1
        if j == '1年以下':
            return 2
        if j == '1-3年':
            return 3
        if j == '3-5年':
            return 4
        if j == '5-10年经验':
            return 5
        if j == '10年以上':
            return 6

        if j == '不限':
            return 0
        if j == '中专及以下':
            return 1
        if j == '大专':
            return 2
        if j == '本科':
            return 3
        if j == '硕士':
            return 4
        if j == '博士':
            return 5

    t = []
    for i in items:
        t.append([f_x(i[0]), f_x(i[1]), i[2]])

    return render_template('charts/bar3d.html', t_data=t)


@area_bp.route('/a11')
def c_3d_5():
    sql = 'select a.j_t, a.j_e, cast(a.avg_sal as int) from t_hz a;'
    db_n = 'job_db'
    items = select_t(sql, db_n)

    def f_x(j):
        if j == '不限':
            return 0
        if j == '应届毕业生':
            return 1
        if j == '1年以下':
            return 2
        if j == '1-3年':
            return 3
        if j == '3-5年':
            return 4
        if j == '5-10年经验':
            return 5
        if j == '10年以上':
            return 6

        if j == '不限':
            return 0
        if j == '中专及以下':
            return 1
        if j == '大专':
            return 2
        if j == '本科':
            return 3
        if j == '硕士':
            return 4
        if j == '博士':
            return 5

    t = []
    for i in items:
        t.append([f_x(i[0]), f_x(i[1]), i[2]])

    return render_template('charts/bar3d.html', t_data=t)


@area_bp.route('/a12')
def c_3d_6():
    sql = 'select a.j_t, a.j_e, cast(a.avg_sal as int) from t_wh a;'
    db_n = 'job_db'
    items = select_t(sql, db_n)

    def f_x(j):
        if j == '不限':
            return 0
        if j == '应届毕业生':
            return 1
        if j == '1年以下':
            return 2
        if j == '1-3年':
            return 3
        if j == '3-5年':
            return 4
        if j == '5-10年经验':
            return 5
        if j == '10年以上':
            return 6

        if j == '不限':
            return 0
        if j == '中专及以下':
            return 1
        if j == '大专':
            return 2
        if j == '本科':
            return 3
        if j == '硕士':
            return 4
        if j == '博士':
            return 5

    t = []
    for i in items:
        t.append([f_x(i[0]), f_x(i[1]), i[2]])

    return render_template('charts/bar3d.html', t_data=t)


@area_bp.route('/a13')
def c_sal_1():
    d = {
        '经验要求': (['不限', '应届毕业生', '1年以下', '1-3年', '3-5年', '5-10年经验', '10年以上', ], 'j_t'),
        '学历要求': (['不限', '中专及以下', '大专', '本科', '硕士', '博士', ],'j_e'),
        '公司规模': (['0-20', '20-50', '50-150', '150-500', '500-1000', '1000-5000', '5000-10000', '10000-max', ], 'c_size',),
        '行业大类': (['后端开发', '通信', '人工智能', '前端开发', '软件销售支持', '数据', '测试', '移动开发', '运维/技术支持', '软件销售', '硬件开发', '项目管理', '硬件', '高端技术职位', '电子/半导体', ], 'j_cate_l'),
        '地区': (['港澳台', '华南', '华中', '东北', '西南', '西北', '华东', '华北', ], 'area'),
    }

    d1 = {'岗位数量': 'count(*)', '平均薪资': 'avg(salary_range)',}

    flag = request.args.get('flag')
    value = request.args.get('value')
    chart = request.args.get('chart')

    field1 = d[flag.split(',')[0]][1]
    field2 = d[flag.split(',')[1]][1]
    value = d1[value]

    sql = "select " + field1 + "," + field2 + "," + value + " from job_t group by " + field1 + "," + field2 + ";"

    results_all = impala_s(sql)
    results, time = results_all[0], results_all[1]
    x = d[flag.split(',')[0]][0]
    y = d[flag.split(',')[1]][0]
    if chart == '3D图':
        return render_template('charts/bar3d.html', datas=result_3d(results, x, y), x=x, y=y)
    else:
        return render_template('charts/学历与公司规模 岗位占比(1).html', datas=result_l(results, x, y))


@area_bp.route('/a14')
def c_sal_2():
    return render_template('charts/经验与公司规模 岗位占比(1).html')


@area_bp.route('/a15')
def c_sal_3():
    return render_template('charts/薪资范围与规模 岗位占比(1).html')


# 大数据
@area_bp.route('/a16')
def c_big_1():
    return render_template('charts/大数据学历经验.html')


@area_bp.route('/a17')
def c_big_2():
    return render_template('charts/大数据工作经验薪资范围.html')


@area_bp.route('/a18')
def c_big_3():
    return render_template('charts/大数据热门城市平均薪资.html')


@area_bp.route('/a19')
def c_big_4():
    return render_template('charts/六大城市大数据职位分布图.html')


@area_bp.route('/a20')
def c_big_5():
    return render_template('charts/大数据相关职位分布.html')

