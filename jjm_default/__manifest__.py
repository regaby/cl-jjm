##############################################################################
#
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Jjm',
    'version': '13.0.0.0.0',
    'category': 'Tools',
    'summary': "Jjm v13 CE",
    'website': 'https://github.com/regaby/cl-jjm',
    'license': 'AGPL-3',
    'depends': [
        # basic applications
        'sale_management',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~

    # manifest version, if omitted it is backward compatible but
    # oe will show a deprecation warning
    'env-ver': '2',

    # Configuration data for odoo.conf
    'config': [

        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
                'workers = 0',
                'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
                'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
                'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
                'limit_memory_hard = 2684354560',


        # Prevents the worker from using more than CPU seconds for each request.
        # If the limit is exceeded, the worker is killed. Defaults to 60 sec.
                'limit_time_cpu = 60',

        # Prevents the worker from taking longer than seconds to process a request.
        # If the limit is exceeded, the worker is killed. Defaults to 120. Differs
        # from --limit-time-cpu in that this is a "wall time" limit including e.g.
        # SQL queries.
                'limit_time_real = 120',

        # default CSV separator for import and export
                'csv_internal_sep = ,',

        # disable loading demo data for modules to be installed
                'without_demo = False',

        # Comma-separated list of server-wide modules, there are modules loaded
        # automatically even if you do not create any database.
                'server_wide_modules = "base,web,dbfilter_from_header"',

        # Filter listed database REGEXP
                'dbfilter =',

                'db_maxconn = 64',
                'db_name = False',
                'db_password = odoo',
                'db_port = 5432',
                'db_sslmode = prefer',
                'db_template = template0',
                'db_user = odoo',
                'demo = {}',
                'email_from = False',
                'geoip_database = /usr/share/GeoIP/GeoLite2-City.mmdb',
                'http_enable = True',
                'http_interface =',
                'http_port = 8069',
                'limit_time_real_cron = -1',
                'list_db = True',
                'log_db = False',
                'log_db_level = warning',
                'log_handler = :INFO',
                'log_level = info',
                'logfile = /dev/pts/0',
                'osv_memory_age_limit = 1.0',
                'osv_memory_count_limit = False',
                'pg_path =',

                'proxy_mode = True',
                'reportgz = False',
                'screencasts =',
                'screenshots = /tmp/odoo_tests',
                'smtp_password = False',
                'smtp_port = 25',
                'smtp_server = localhost',
                'smtp_ssl = False',
                'smtp_user = False',
                'syslog = False',
                'test_enable = False',
                'test_file =',
                'test_tags = None',
                "translate_modules = ['all']",
                'unaccent = False',
                'upgrade_path =',
    ],

    # Default to CE, can be ommited
    'odoo-license': 'CE',

    # Port where odoo docker image starts serving pages.
    'port': '8069',

    # repositories to be installed in sources/ dir
    # syntax: the same as git clone
    'git-repos': [
        'https://github.com/regaby/cl-jjm.git',
        'https://github.com/DaniRoBAzan/jjm_custom_addons_v13.git',
        'https://github.com/regaby/odoo-custom.git',
        'https://github.com/jobiols/odoo-addons.git',
        ## localización
        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/odoo-argentina-ce.git',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/account-payment.git',
        'https://github.com/ingadhoc/account-invoicing.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/sale.git',
        'https://github.com/ingadhoc/stock.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/website.git',
        'https://github.com/OCA/account-financial-reporting.git',
        'https://github.com/OCA/reporting-engine.git',
        'https://github.com/OCA/server-ux.git',
        'https://github.com/OCA/mis-builder.git',
        'https://github.com/OCA/sale-workflow.git',
        'https://github.com/OCA/web.git',
        'https://github.com/OCA/partner-contact.git',
        'https://github.com/OCA/server-tools.git',
        ##
        # 'https://github.com/regaby/contract.git',
        'https://github.com/ctmil/contract.git ctmil/contract',
        #'https://github.com/regaby/account_debt_management.git',
        'https://github.com/ctmil/account_debt_management.git ctmil/account_debt_management -b master',
        'https://github.com/CybroOdoo/CybroAddons.git',
        'https://github.com/odoomates/odooapps.git',
    ],

    # Docker images to be used in this deployment
    # syntax: name url
    'docker-images': [
        'odoo regaby/odoo-ce:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
