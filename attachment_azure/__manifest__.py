# Copyright 2016-2019 Camptocamp SA
# Copyright 2021 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
{
    "name": "Attachments on Azure storage",
    "summary": "Store assets and attachments on a Azure compatible object storage",
    "version": "15.0.1.0.0",
    "author": "Camptocamp, "
    "Open Source Integrators, "
    "Serpent Consulting Services, "
    "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Knowledge Management",
    "depends": ["base_attachment_object_storage"],
    "external_dependencies": {
        "python": ["azure-storage-blob", "azure-identity", "pyopenssl==22.0.0", "redis==2.10.5", "python-json-logger==0.1.5", "statsd==3.2.1", "boto==2.42.0"],
    },
    "website": "https://github.com/camptocamp/odoo-cloud-platform",
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["max3903"],
}
