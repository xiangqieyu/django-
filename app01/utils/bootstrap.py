from django import forms

class Bootstrap:
    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {"class": "form-control", "placeholder": field.label}
            # field.widget.attrs = {"class": "form-control", "placeholder": field.label}




class BootStrapModelForm(Bootstrap, forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         if field.widget.attrs:
    #             field.widget.attrs['class'] = "form-control"
    #             field.widget.attrs['placeholder'] = field.label
    #         else:
    #             field.widget.attrs = {"class": "form-control", "placeholder": field.label}
    #         # field.widget.attrs = {"class": "form-control", "placeholder": field.label}
    pass


class BootStrapForm(Bootstrap, forms.Form):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         if field.widget.attrs:
    #             field.widget.attrs['class'] = "form-control"
    #             field.widget.attrs['placeholder'] = field.label
    #         else:
    #             field.widget.attrs = {"class": "form-control", "placeholder": field.label}
    #         # field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    pass