#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:TXU
@file:file_cp
@time:2023/4/14
@email:tao.xu2008@outlook.com
@description: 
"""
import typer

from pkgs.log_config import init_logger
from main import app


@app.command(help='文件/文件夹复制', hidden=False)
def fcp1(
        src: str = typer.Option(..., help="源文件地址：例 Z:/src/"),
        dst: str = typer.Option(..., help="目标地址：例 Y:/dst/"),
        loop: int = typer.Option(1, min=1, help="循环测试次数"),
        trace: bool = typer.Option(False, help="print TRACE level log"),
):
    init_logger(prefix='file_cp1', trace=trace)
    from ops.file_cp1 import run_cp
    run_cp(src, dst, loop)


@app.command(help='文件/文件夹复制', hidden=False)
def fcp2(
        src: str = typer.Option(..., help="源文件地址：例 Z:/src/"),
        dst: str = typer.Option(..., help="目标地址：例 Y:/dst/"),
        loop: int = typer.Option(1, min=1, help="循环测试次数"),
        trace: bool = typer.Option(False, help="print TRACE level log"),
):
    init_logger(prefix='file_cp2', trace=trace)
    from ops.file_cp2 import run_cp
    run_cp(src, dst, loop)


if __name__ == '__main__':
    pass
