import textwrap

def floattov16(x):
    return int(x * (1<<12))

def floattot16(x):
    return int(x * (1<<12))

obj = open('scene.obj')
v = []
f = []
uv = []
ft = []

def toArray(x):
    return '{\n' + '\n'.join(textwrap.wrap(str(x)[1:-1], width=80, initial_indent='    ', subsequent_indent='    ')) + '\n};'

for line in obj.readlines():
    line = line.split()
    if line[0] == 'v':
        v += [floattov16(float(i)) for i in line[1:]]
    elif line[0] == 'f':
        for i in line[1:]:
            a=i.split('/')
            f.append(int(a[0])-1)
            ft.append(int(a[1])-1)
    elif line[0] == 'vt':
        uv += [floattot16(float(line[1])), floattot16(1.0-float(line[2]))]
        
obj.close()
scene = open('build/scene.h', 'w')
scene.write(
"""//Generated by objtoh.py

#ifndef SCENE_H
#define SCENE_H

#include <nds.h>

const v16 scenePoints[] = """ + toArray(v) + """

const u16 scenePointIndices[] = """ + toArray(f) + """

const t16 sceneUV[] = """ + toArray(uv) + """

const u16 sceneUVIndices[] = """ + toArray(ft) + """

const u16 sceneNumPoints = """ + str(len(v)) + """;
const u16 sceneNumPointIndices = """ + str(len(f)) + """;
const u16 sceneNumUV = """ + str(len(uv)) + """;
const u16 sceneNumUVIndices = """ + str(len(ft)) + """;

#endif"""
)
scene.close()