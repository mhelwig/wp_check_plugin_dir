# wp_check_plugin_dir

Script to check the plugins in your Wordpress plugin directory against the vulndb.com api.

You get an output of all known vulnerabilities in vulndb.com for these plugins.

This script currently doesn't check themes or the Wordpress core nor does it check the version of your plugins, so it's pretty basic.

Be warned: The vulnerabilitiy list might scare you.

## Usage

Usage: python check_wp_plugin_dir.py path/to/plugin/directory

## Output

```
[+] duplicate-post
     * [SQLI] Duplicate Post 2.5 - duplicate-post-admin.php User Login Cookie Value SQL Injection
        Fixed in: 2.6
     * [XSS] Duplicate Post 2.5 - options-general.php post Parameter Reflected XSS
        Fixed in: 2.6
        
[+] w3-total-cache
     * [UNKNOWN] W3 Total Cache 0.9.2.4 - Username & Hash Extract
        Fixed in: 0.9.2.5
        + http://seclists.org/fulldisclosure/2012/Dec/242
        + https://github.com/FireFart/W3TotalCacheExploit
     * [RCE] W3 Total Cache - Remote Code Execution
        Fixed in: 0.9.2.9
        + http://www.acunetix.com/blog/web-security-zone/wp-plugins-remote-code-execution/
        + http://wordpress.org/support/topic/pwn3d
        + http://blog.sucuri.net/2013/04/update-wp-super-cache-and-w3tc-immediately-remote-code-execution-vulnerability-disclosed.html
     * [CSRF] W3 Total Cache 0.9.4 - Edge Mode Enabling CSRF
        Fixed in: 0.9.4.1
        + http://seclists.org/fulldisclosure/2014/Sep/29
     * [CSRF] W3 Total Cache <= 0.9.4 - Cross-Site Request Forgery (CSRF)
        Fixed in: 0.9.4.1
        + http://mazinahmed1.blogspot.com/2014/12/w3-total-caches-w3totalfail.html
     * [XSS] W3 Total Cache <= 0.9.4 - Debug Mode XSS
        Fixed in: 0.9.4.1
     * [XSS] W3 Total Cache <= 0.9.4.1 - Authenticated Reflected Cross-Site Scripting (XSS)
        Fixed in: 0.9.5 - Published on: 2016-09-21T00:00:00.000Z
        + https://blog.zerial.org/seguridad/vulnerabilidad-cross-site-scripting-en-wordpress-w3-total-cache/
        + http://seclists.org/fulldisclosure/2016/Sep/52
        + https://sumofpwn.nl/advisory/2016/reflected_cross_site_scripting_vulnerability_in_w3_total_cache_plugin.html
        + http://seclists.org/fulldisclosure/2016/Nov/63
     * [BYPASS] W3 Total Cache <= 0.9.4.1 – Unauthenticated Security Token Bypass
        Fixed in: 0.9.5 - Published on: 2016-09-26T00:00:00.000Z
        + https://secupress.me/4-new-security-flaws-w3-total-cache-0-9-4-1/
```
