from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    is_field_service_task = fields.Boolean(
        string="Is Field Service Task",
        related="project_id.is_fsm",
    )
    customer_contact_number = fields.Char(string="Customer Contact Number")
    spare_parts_used = fields.Boolean(string="Spare Parts Used")
    spare_part_line_ids = fields.One2many(
        "project.task.spare.part",
        "task_id",
        string="Spare Parts Used",
        copy=True,
    )
    distance_travelled = fields.Float(string="Distance Travelled (km)", digits=(16, 2))
    actual_maintenance_date = fields.Date(string="Actual Maintenance Date")


class ProjectTaskSparePart(models.Model):
    _name = "project.task.spare.part"
    _description = "Field Service Spare Part Used"
    _order = "sequence, id"

    sequence = fields.Integer(default=10)
    task_id = fields.Many2one(
        "project.task",
        string="Field Service Task",
        required=True,
        ondelete="cascade",
        index=True,
    )
    part_name = fields.Char(string="Part Name", required=True)
    part_number = fields.Char(string="Part Number", index=True)
