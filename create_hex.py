#!/usr/bin/env python3
"""
Create an academic law-themed hex sticker
"""

from PIL import Image, ImageDraw, ImageFont
import math

# Hex dimensions
width = 800
height = 924  # Approximately width * 1.155 for proper hex ratio

# Create image with transparent background
img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Calculate hexagon points
center_x = width / 2
center_y = height / 2
radius = width / 2 - 20

hex_points = []
for i in range(6):
    angle = math.pi / 3 * i - math.pi / 6
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    hex_points.append((x, y))

# Draw hexagon with academic colors (deep burgundy/maroon)
draw.polygon(hex_points, fill='#8B1538', outline='#FFFFFF', width=8)

# Add decorative elements - scales of justice symbol using basic shapes
scale_color = '#D4AF37'  # Gold color

# Draw balance beam (horizontal line)
beam_y = center_y - 80
beam_width = 200
draw.line([(center_x - beam_width/2, beam_y), (center_x + beam_width/2, beam_y)],
          fill=scale_color, width=10)

# Draw center post
draw.rectangle([center_x - 5, beam_y, center_x + 5, beam_y + 120], fill=scale_color)

# Draw scales (circles and lines)
scale_radius = 50
left_scale_x = center_x - 80
right_scale_x = center_x + 80
scale_y = beam_y + 40

# Left scale pan
draw.ellipse([left_scale_x - scale_radius, scale_y - scale_radius,
              left_scale_x + scale_radius, scale_y + scale_radius],
             outline=scale_color, width=4)
draw.line([(left_scale_x, beam_y), (left_scale_x, scale_y - scale_radius)],
          fill=scale_color, width=4)

# Right scale pan
draw.ellipse([right_scale_x - scale_radius, scale_y - scale_radius,
              right_scale_x + scale_radius, scale_y + scale_radius],
             outline=scale_color, width=4)
draw.line([(right_scale_x, beam_y), (right_scale_x, scale_y - scale_radius)],
          fill=scale_color, width=4)

# Add text
try:
    # Try to use a nice font
    title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 80)
    subtitle_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 40)
except:
    # Fallback to default
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

# Draw title
title = "LEX"
bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = bbox[2] - bbox[0]
title_x = (width - title_width) / 2
draw.text((title_x, center_y + 100), title, fill='#FFFFFF', font=title_font)

# Draw subtitle
subtitle = "ACADEMIA"
bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
subtitle_width = bbox[2] - bbox[0]
subtitle_x = (width - subtitle_width) / 2
draw.text((subtitle_x, center_y + 180), subtitle, fill='#D4AF37', font=subtitle_font)

# Save the image
img.save('images/law_hex.png', 'PNG')
print("Hex sticker created successfully: images/law_hex.png")
