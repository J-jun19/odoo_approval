# -*- coding: utf-8 -*-
{
    'name': "流程审批",
    'summary': """自定义审批流程，实现会签和或签，转签，抄送转阅等基本功能,可配置消息发送至企业微信""",
    'author': "<jj190214@163.com>",
    'category': 'Tools',
    'version': '16.0',
    'license': 'OPL-1',
    'category': 'Tools',
    'version': '16.0',
    'depends': ['base', 'web', 'hr'],
    'data': [
        'data/res_users_employee.xml',
        'data/rabbitmq.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/approval_flow.xml',
        'views/approval_flow_node.xml',
        'views/rabbitmq.xml',
        'views/res_users.xml',
        'views/workwx_users.xml',
        'views/res_config_setting.xml',
        'views/approval_model_record.xml',
        'views/approval_transfer_reading.xml',
        'views/approval_copy.xml',
        'views/menuitem.xml',
        'wizard/release_flow_action.xml',
        'wizard/action_approval_wizard.xml',
        'wizard/approval_turn_wizard.xml',
        'wizard/action_transfer_reading.xml',
        'wizard/workwx_users_wizard.xml',
    ],
    'assets': {
        'web.assets_frontend': [
        ],
        'web.assets_qweb': [
        ],

        'web.assets_backend': [
            'jwm_web_approval/static/src/js/graph.js',
            'jwm_web_approval/static/src/js/vec2.js',
            'jwm_web_approval/static/src/js/flow_action_diagram.js',
            'jwm_web_approval/static/src/js/form_renderer.js',
            'jwm_web_approval/static/src/js/flow_node_instance_diagram.js',
            'jwm_web_approval/static/src/js/workwx_user.js',
            'jwm_web_approval/static/src/js/kanban_renderer.js',
            'jwm_web_approval/static/src/scss/diagram_view.scss',
            'jwm_web_approval/static/src/scss/flow_view.scss',
            'jwm_web_approval/static/src/xml/flow_action_diagram.xml',
            'jwm_web_approval/static/src/xml/flow_node_instance_template.xml',
            'jwm_web_approval/static/src/xml/workwx_user_template.xml',
            'jwm_web_approval/static/src/xml/kanban_renderer.xml',
        ],

        'web.assets_common': [
        ],
    },
    'images': [
        'static/description/icon1.png',
    ],
    'demo': [],
    'installable': True,

    'active': True,
    'auto_install': False,
}
