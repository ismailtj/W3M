.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================
Account Fiscal Year
===================

This module extends `date.range.type` to add `fiscal_year` flag.

Override official `res_company.compute_fiscal_year_dates` to get the
fiscal year date start / date end for any given date.
That methods first looks for a date range of type fiscal year that
encloses the give date.
If it does not find it, it falls back on the standard Odoo
technique based on the day/month of end of fiscal year.

Installation
============

Just install it

Configuration
=============

Nothing

Usage
=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/92/9.0


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/{project_repo}/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======


Contributors
------------

* Damien Crier <damien.crier@camptocamp.com>
* Laurent Mignon <laurent.mignon@acsone.eu>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>

Maintainer
----------

   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
