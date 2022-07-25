# Development environment

1. copied the **odoo.conf** file form the all-in-one odoo and add it to my odoo clone
2. in VSCode, Run>Add Configuration>Python replaced it with

    ```json
    {
      // Use IntelliSense to learn about possible attributes.
      // Hover to view descriptions of existing attributes.
      // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
      "version": "0.2.0",
      "configurations": [
        {
          "name": "Python: odoo15",
          "type": "python",
          "request": "launch",
          "stopOnEntry": false,
          "python": "C:\\python\\python.exe",
          "console": "integratedTerminal",
          "program": "${workspaceRoot}\\odoo-bin",
          "args": [
            "--config=${workspaceRoot}\\odoo.conf",
          ],
          "cwd": "${workspaceRoot}",
          "env": {},
          "envFile": "${workspaceRoot}/.env",
          "redirectOutput": true,
        }
      ]
    }
    ```

3. edited some filed in odoo.conf to fit my odoo clone

    ```py
    [options]
    addons_path = C:\Users\bashr\odoo\odoo\addons
    admin_passwd = $pbkdf2-sha512$25000$CmEspdTam5NSKoWw1roXYg$PxAJYYHTuda0wdLSYjJtpafnpZKwbX.SIhd1xGGr2XfgvzufFjv7Jpz1fZ2WpKCI0y43c962dBeA8Yyb/x5D5A
    # bin_path = C:\Users\bashr\odoo\thirdparty
    csv_internal_sep = ,
    # data_dir = C:\Users\bashr\AppData\Local\OpenERP S.A\Odoo
    db_host = localhost
    db_maxconn = 64
    db_name = False
    db_password = odoo
    db_port = 5432
    db_sslmode = prefer
    db_template = template0
    db_user = odoo
    dbfilter =
    demo = {}
    email_from = False
    from_filter = False
    # geoip_database = C:\usr\share\GeoIP\GeoLite2-City.mmdb
    http_enable = True
    http_interface =
    http_port = 8069
    import_partial =
    limit_memory_hard = None
    limit_memory_soft = None
    limit_request = None
    limit_time_cpu = None
    limit_time_real = None
    limit_time_real_cron = None
    list_db = True
    log_db = False
    log_db_level = warning
    log_handler = :INFO
    log_level = info
    # logfile = C:\Users\bashr\odoo15\server\odoo.log
    longpolling_port = 8072
    max_cron_threads = 2
    osv_memory_age_limit = False
    osv_memory_count_limit = False
    pg_path =
    pidfile =
    proxy_mode = False
    reportgz = False
    screencasts =
    screenshots = C:\Users\bashr\AppData\Local\Temp\odoo_tests
    server_wide_modules = base,web
    smtp_password = False
    smtp_port = 25
    smtp_server = localhost
    smtp_ssl = False
    smtp_ssl_certificate_filename = False
    smtp_ssl_private_key_filename = False
    smtp_user = False
    syslog = False
    test_enable = False
    test_file =
    test_tags = None
    transient_age_limit = 1.0
    translate_modules = ['all']
    unaccent = False
    upgrade_path =
    without_demo = False
    workers = None
    ```

4. now run it form any place with F5.  
  **Important**: any place that is not .vscode\launch.json file
