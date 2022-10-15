export const qpDate = (value: string, tz: string="America/Toronto", has_type="full") => {
    let date_value = new Date(value)
    let options: Intl.DateTimeFormatOptions = {
        timeZone: tz,
        hour12: false,
        year: (["full","date"].includes(has_type) ? "numeric" : undefined),
        month: (["full","date"].includes(has_type) ? "long" : undefined),
        day: (["full","date"].includes(has_type) ? "numeric" : undefined),
        hour: (["full","time"].includes(has_type) ? "2-digit" : undefined),
        minute: (["full","time"].includes(has_type) ? "2-digit" : undefined)
    }
    return date_value.toLocaleString("fr", options)
}

const qpFilters = {
    qpDate
}

export default qpFilters