def get_attributes(arr, args):
    order = {}
    for element in ['start_date', 'end_date', 'description', 'title', 'location']:
        if element in arr:
            order[element] = arr.index(element)

    if args.title:
        order['title'] = arr.index(args.title)
    if args.description:
        order['description'] = arr.index(args.description)
    if args.location:
        order['location'] = arr.index(args.location)
    if args.start_date:
        order['start_date'] = arr.index(args.start_date)
    if args.end_date:
        order['end_date'] = arr.index(args.end_date)
    return order


def generate_dict(order, arr):
    ret = {}
    for key in order:
        ret[key] = arr[order[key]]
    return ret


def generation(order, row):
    import jinja2
    template = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./")).get_template("template.ics")
    file = open("event.ics", "w")
    file.write(template.render(event=generate_dict(order, row)))
    file.close()


def csv_manipulations(args):
    with open(args.file) as csvfile:
        import csv
        csv = csv.reader(csvfile)
        order = get_attributes(next(csv), args)
        for row in csv:
            generation(order, row)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="CSV File with title, description, start date, end date and location column")
    parser.add_argument("--title", help="Custom name for title column")
    parser.add_argument("--description", help="Custom name for description column")
    parser.add_argument("--location", help="Custom name for location column")
    parser.add_argument("--start-date", help="Custom name for start date column")
    parser.add_argument("--end-date", help="Custom name for end date column")
    args = parser.parse_args()
    csv_manipulations(args)


if __name__ == '__main__':
    main()
