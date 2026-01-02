/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import {
    Many2ManyTagsField,
    many2ManyTagsField,
} from "@web/views/fields/many2many_tags/many2many_tags_field";

export class Many2ManyRazsTagsField extends Many2ManyTagsField {

    // 🔑 DECLARAR PROPS ADICIONALES
    static props = {
        ...Many2ManyTagsField.props,
        fieldsToShow: { type: Array, optional: true },
    };

    getTagProps(record) {
        const props = super.getTagProps(record);

        const fields = this.props.fieldsToShow || [];
        if (fields.length) {
            const values = fields
                .map((f) => record.data?.[f])
                .filter(Boolean);

            if (values.length) {
                props.text = values.join(" | ");
            }
        }

        return props;
    }
}

export const many2ManyRazsTagsField = {
    ...many2ManyTagsField,
    component: Many2ManyRazsTagsField,

    relatedFields: ({ options }) => {
        const relatedFields = [{ name: "display_name", type: "char" }];

        if (Array.isArray(options.fields)) {
            for (const fieldName of options.fields) {
                relatedFields.push({ name: fieldName, readonly: true });
            }
        }

        if (options.color_field) {
            relatedFields.push({
                name: options.color_field,
                type: "integer",
                readonly: false,
            });
        }

        return relatedFields;
    },

    extractProps(args, dynamicInfo) {
        const props = many2ManyTagsField.extractProps(args, dynamicInfo);
        props.fieldsToShow = args.options.fields || [];
        return props;
    },
};

registry.category("fields").add("many2many_razs", many2ManyRazsTagsField);
