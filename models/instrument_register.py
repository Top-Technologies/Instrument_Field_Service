from odoo import fields, models


class InstrumentFieldServiceRegister(models.Model):
    _name = "instrument.field.service.register"
    _description = "Instrument Field Service Register"
    _rec_name = "customer_name"
    _order = "delivery_date desc, register_no, id desc"

    register_no = fields.Integer(string="No.", index=True)
    customer_name = fields.Char(string="Customer / Ship-to Name", required=True, index=True)
    instrument_model = fields.Char(string="Instrument Model", index=True)
    serial_number = fields.Char(string="Serial Number", index=True)
    delivery_date = fields.Date(string="Delivery Date")
    delivery_status = fields.Selection(
        [("pending", "Pending"), ("delivered", "Delivered")],
        string="Delivery Status",
        default="pending",
        index=True,
    )
    installation_status = fields.Selection(
        [
            ("pending", "Pending"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
            ("not_required", "Not Required"),
        ],
        string="Installation Status",
        default="pending",
        index=True,
    )
    sso_training_status = fields.Selection(
        [
            ("pending", "Pending"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
            ("not_required", "Not Required"),
        ],
        string="SSO Training Status",
        default="pending",
        index=True,
    )
    installation_date = fields.Date(string="Installation Date")
    installer_name = fields.Char(string="Installer Name")
    sso_training_date = fields.Date(string="SSO Training Date")
    trainer_name = fields.Char(string="Trainer Name")
    calibration_status = fields.Char(string="Calibration Status", index=True)
    installation_fse_fas = fields.Char(string="Installation FSE / FAS")
    training_participants = fields.Text(string="Training Participants")
    training_participant_ids = fields.One2many(
        "instrument.field.service.participant",
        "register_id",
        string="Training Participants",
        copy=True,
    )
    site_city = fields.Char(string="Site / City", index=True)
    remarks_next_action = fields.Text(string="Remarks / Next Action")
    last_updated = fields.Date(string="Last Updated")

    # Stored measure for the graph and pivot views: each register row counts once.
    record_count = fields.Integer(string="Records", default=1, readonly=True, copy=False)


class InstrumentFieldServiceParticipant(models.Model):
    _name = "instrument.field.service.participant"
    _description = "Instrument SSO Training Participant"
    _order = "sequence, id"

    sequence = fields.Integer(default=10)
    register_id = fields.Many2one(
        "instrument.field.service.register",
        string="Instrument Register Entry",
        required=True,
        ondelete="cascade",
        index=True,
    )
    participant_name = fields.Char(string="Participant Name", required=True)
    role_or_organization = fields.Char(string="Role / Organization")
