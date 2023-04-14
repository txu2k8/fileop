#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:TXU
@file:main
@time:2023/4/14
@email:tao.xu2008@outlook.com
@description: 
"""
import typer
from typing import Optional

VERSION = 'v1.1.0'


def version_callback(value: bool):
    if value:
        print(f"LTS Version: {VERSION}")
        raise typer.Exit()


def public(
        version: Optional[bool] = typer.Option(
            None, "--version", callback=version_callback, help='Show the tool version'
        ),
):
    """公共参数"""
    pass


app = typer.Typer(name="FileOP", callback=public, add_completion=False, help="文件操作测试工具集 CLI.")


if __name__ == '__main__':
    app()

