import os, math

OUT = "assets/badges"
os.makedirs(OUT, exist_ok=True)

def pill(text, color, fg="#ffffff", height=28):
    fs = 13
    w = max(len(text) * (fs * 0.62) + 24, 46)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{height}">
  <rect width="100%" height="100%" rx="{height/2}" fill="{color}"/>
  <text x="{w/2:.0f}" y="{height/2 + fs*0.36:.0f}" text-anchor="middle" font-family="'Segoe UI', Verdana, sans-serif" font-size="{fs}" font-weight="600" fill="{fg}">{text}</text>
</svg>
'''

badges = {
    # social
    "linkedin": ("LinkedIn", "#0A66C2"),
    "email": ("Email", "#EA4335"),
    "portfolio": ("Portfolio", "#6E40C9"),
    "ieee": ("IEEE Xplore", "#00629B"),
    "scholar": ("Google Scholar", "#4285F4"),
    "researchgate": ("ResearchGate", "#00B09A"),
    # linux / sysadmin
    "rhel9": ("RHEL 9", "#D00000"),
    "shell": ("Shell Scripting", "#5F9E2E"),
    "lvm_raid": ("LVM / RAID", "#B5651D"),
    "selinux": ("SELinux", "#335A87"),
    "firewalld": ("firewalld", "#E4572E"),
    # automation / containers
    "ansible": ("Ansible", "#BA3A2E"),
    "docker": ("Docker", "#1D63ED"),
    "openshift": ("OpenShift", "#8C1F2B"),
    # ai / ml / python
    "python": ("Python", "#3776AB"),
    "cnn_yolo": ("CNN / YOLOv8", "#00B4D8"),
    "edgeai": ("Edge AI / IoT", "#7F5AF0"),
    # web tools
    "react": ("React", "#13A4CC"),
    "flask": ("Flask", "#5A5A5A"),
    "streamlit": ("Streamlit", "#FF4B4B"),
    "git": ("Git", "#F05032"),
}

for name, (label, color) in badges.items():
    with open(os.path.join(OUT, f"{name}.svg"), "w") as f:
        f.write(pill(label, color))

print("generated", len(badges), "badges")
