from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    Register = env["instrument.field.service.register"]
    Product = env["product.product"]

    records = Register.search(
        [("product_id", "=", False), ("instrument_model", "!=", False)]
    )
    for record in records:
        model_name = record.instrument_model.strip()
        if not model_name:
            continue
        product = Product.search(
            ["|", ("default_code", "=", model_name), ("product_tmpl_id.name", "=", model_name)],
            limit=1,
        )
        if product:
            record.product_id = product
