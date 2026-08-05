config = {}
with open('config.txt', 'r') as file:
    for line in file:
        parameter, value = line.strip().split('=')
        if ',' in value:
            config[parameter] = tuple(int(c.strip()) for c in value.split(','))
        elif '.' in value:
            config[parameter] = float(value)
        else:
            config[parameter] = int(value)
config['vanishing_point'] = (config['width'] * 0.5, config['height'] * 0.25)

def calculate_x_positions(surface, vertical_lines, space):
    x_positions = []
    width        = surface.get_width()
    spacing      = space * width
    central_line = width / 2
    offset       = -int(vertical_lines / 2)

    for _ in range(vertical_lines):
        x_positions.append(central_line + offset * spacing)
        offset += 1

    return x_positions