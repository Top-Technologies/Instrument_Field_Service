# Instrument Field Service Register (Odoo 19)

This installable addon extends the existing **Field Service** app with two menus:

- **Instrument Register** for delivery, installation, SSO training, calibration, site, staff, and next-action fields, plus block and heated-cover serials, region, zone, and customer contact number.
- **Field Service → Reporting → Instrument Register Reporting** with graph, pivot, and list views for register counts by installation status and site.
- **Training Participants** as a repeatable line table on each register entry, with an **Add a line** control for each trainee.
- **Installation Documents** with a completion checkbox and document upload for both the Installation Checklist and IQ/OQ/IPV documentation.
- **Instrument Model** selected from product variants, plus last and next scheduled calibration dates.
- **Field Service task maintenance details** for optional customer contact number, distance travelled, actual maintenance date, and repeatable spare part name/number lines.
- **Optional task customer**: the standard Customer Name relation is not required when creating a task.

## Install or update

The Odoo 19 **Field Service** app must be installed. This addon depends on `industry_fsm`.

For a new installation, copy the `instrument_field_service` folder into an Odoo 19 addons path, restart the Odoo server, update the Apps list, and install **Instrument Field Service Register**. The Products app must also be installed; the addon uses `product.product` variants for Instrument Model.

To update an existing installation, replace its addon folder with this version, restart Odoo, then upgrade **Instrument Field Service Register** from Apps. The migration links prior free-text instrument model values to matching product variant/template names when a match exists. Unmatched legacy model text remains stored in the hidden legacy field for manual review.

## Import workbook records

Open **Field Service → Instrument Register**, use the list view's **Import records** option, and upload the workbook. Match each workbook column to the corresponding field. The included `import/instrument_register_template.csv` shows the supported headings. The source workbook contains two calibration-status columns; this module stores one `Calibration Status` field, so import that value once. Map Instrument Model to an existing product variant by its product name or external ID.

Dates should be imported as Excel dates. Delivery, installation, and SSO training statuses accept Pending, Delivered where applicable, In Progress, Completed, and Not Required where applicable. The original workbook's participant text field is retained for compatibility; enter new trainees as separate lines in the Training Participants table.

## Field Service task fields

In a Field Service task, open **Maintenance Details** to enter Distance Travelled (km), Actual Maintenance Date, and Customer Contact Number. Customer Name remains optional. Select **Spare Parts Used** to show the repeatable Part Name / Part Number table.

## Workbook field mapping

| Workbook column | Odoo field |
| --- | --- |
| No. | No. |
| Customer Name | Customer Name |
| Instrument Model | Instrument Model (Product Variant) |
| Serial Number | Serial Number |
| Block Serial Number | Block Serial Number |
| Heated Cover Serial Number | Heated Cover Serial Number |
| Region | Region |
| Zone | Zone |
| Customer Name | Customer Name |
| Customer Contact Number | Customer Contact Number |
| Delivery Date | Delivery Date |
| Delivery Status | Delivery Status |
| Installation Status | Installation Status |
| SSO Training Status | SSO Training Status |
| Installation Date | Installation Date |
| Installer Name | Installer Name |
| Installation Checklist Complete | Installation Checklist Complete |
| Installation Checklist Document | Installation Checklist Document attachment |
| IQ/OQ/IPV Documentation Complete | IQ/OQ/IPV Documentation Complete |
| IQ/OQ/IPV Documentation | IQ/OQ/IPV Documentation attachment |
| SSO Training Date | SSO Training Date |
| Trainer Name | Trainer Name |
| Calibration status | Calibration Status |
| Last Calibration Date | Last Calibration Date |
| Next Scheduled Calibration Date | Next Scheduled Calibration Date |
| Installation FSE / FAS | Installation FSE / FAS |
| Training Participants | Training Participants |
| Site / City | Site / City |
| Remarks / Next Action | Remarks / Next Action |
| Last Updated | Last Updated |

This package targets Odoo 19 and adds its menus under the existing Field Service app. No Odoo server or database was reachable from this workspace, so installation into a live database has not been performed.
