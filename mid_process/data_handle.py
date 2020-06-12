#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 14:57
# @Author  : Zhangyp
# @File    : data_handle.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""数据的处理模块"""


# 时间推迟一天
def date_add(date):
	import datetime
	after_date = (date.strftime("%Y-%m-%d %H:%M") + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
	return after_date


"""测试考核--延期统计需要使用"""


# 解析html获得工时耗时
def parse_html(html):
	from lxml import etree
	html_string = etree.HTML(html)
	content = html_string.xpath('//span')
	try:
		text_list = [span.text for span in content if span.text is not None]
		key_index = [i for i, text in enumerate(text_list) if 'MD' in text.upper() or 'MH' in text.upper()][0]
		time_consuming = text_list[key_index]
	except Exception:
		time_consuming = None
	return time_consuming


# 将获取耗时统计
def task_report_statistc(_list):
	"""
	:arg 传入的models对象
	"""
	rows = []
	for row in _list:
		# row_list = []
		exp_desc = parse_html(row.task_desc)
		act_desc = parse_html(row.report_desc)
		# 获取延期时间
		exp_list = exp_desc.replace(' ', '').split('M')
		if exp_list[-1] == 'H':
			exp = float(exp_list[0]) / 8
		else:
			exp = float(exp_list[0])
		act_list = act_desc.replace(' ', '').split('M')
		if act_list[-1] == 'H':
			act = float(act_list[0]) / 8
		else:
			act = float(act_list[0])
		ed = act - exp
		# row_list={"task_id":row.task_id, "reporter":row.reporter, "exp_time":exp_desc, "act_time":act_desc,"delay_day":ed}
		row_list = [row.task_id, row.reporter, exp_desc, act_desc, ed]
		rows.append(row_list)
	return rows


"""测试考核--bug分类、有效bug需要使用"""


# bug严重率统计

def bug_severity_rate_statistics(begin, end):
	bug_type_sql = """SELECT
	S.openedBy,
	S.severityNum,
	T.total,
	CONCAT(S.severityNum / T.total * 100,'%') as  severityRate
FROM
	(
	SELECT
		openedBy,
		count( id ) AS severityNum
	FROM
		zt_bug
	WHERE
		openedBy IN ( SELECT account FROM zt_user WHERE dept = 4 AND deleted = '0' )
		AND openedDate BETWEEN "{0}"
		AND "{1}"
		AND deleted = '0'
		AND severity IN ( 1, 2 )
	GROUP BY
		openedBy
	) AS S
	RIGHT JOIN (
	SELECT
		openedBy,
		count( id ) AS total
	FROM
		zt_bug
	WHERE
		openedBy IN ( SELECT account FROM zt_user WHERE dept = 4 AND deleted = '0' )
		AND openedDate BETWEEN "{0}"
		AND "{1}"
		AND deleted = '0'
	GROUP BY
	openedBy
	) AS T ON S.openedBy = T.openedBy""".format(begin, end)
	from mid_process.mysql import query
	return query(bug_type_sql)


# bug无效率统计
def bug_invalid_rate_statistics(begin, end):
	bug_invalid_sql = """SELECT
	E.openedBy,
	E.invalidCount,
	T.total,
	CONCAT(E.invalidCount / T.total *100,'%') AS invalidRate
FROM
	(
	SELECT
		openedBy,
		count( id ) AS total
	FROM
		zt_bug
	WHERE
		openedBy IN ( SELECT account FROM zt_user WHERE dept = 4 AND deleted = '0' )
		AND openedDate BETWEEN '{0}' -- 统计日期
		AND '{1}'
		AND deleted = '0'
	GROUP BY
		openedBy
	) AS T
	INNER JOIN (
	SELECT
		openedBy,
		count( id ) AS invalidCount
	FROM
		zt_bug
	WHERE
		resolution IN ( 'bydesign', 'duplicate', 'notrepro' )
		AND openedBy IN ( SELECT account FROM zt_user WHERE dept = 4 AND deleted = '0' )
		AND openedDate BETWEEN '{0}'
		AND '{1}'
		AND deleted = '0'
	GROUP BY
	openedBy
	) AS E ON T.openedBy = E.openedBy""".format(begin, end)
	from mid_process.mysql import query
	return query(bug_invalid_sql)
