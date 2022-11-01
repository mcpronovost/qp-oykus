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

export const qpSlugify = (value: string|number) => {
    return value.toString()
    .normalize("NFD")
    .toLowerCase()
    .trim()
    .replace(/\s+/g, "-")
    .replace(/ð/g, "d")
    .replace(/ß/g, "ss")
    .replace(/§/g, "ss")
    .replace(/ł/g, "l")
    .replace(/ø/g, "o")
    .replace(/æ/g, "ae")
    .replace(/œ/g, "oe")
    .replace(/ĸ/g, "k")
    .replace(/µ/g, "u")
    .replace(/[^\w\-]+/g, "")
    .replace(/\_/g, "-")
    .replace(/\-\-+/g, "-")
    .replace(/\-$/g, "");
}

const qpFilters = {
    qpDate,
    qpSlugify
}

export default qpFilters