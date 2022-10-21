
def get_slugific_names(self):
    if self:
        result = "%s" % (self.first_name)
        if self.middle_name:
            result += "%s" % (self.middle_name)
        return result
    return ""
