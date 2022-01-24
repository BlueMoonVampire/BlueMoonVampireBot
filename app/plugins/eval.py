"""
MIT License
Copyright (C) 2021-2022, NkSama
Copyright (C) 2021-2022 Moezilla
Copyright (c) 2021, Sylviorus, <https://github.com/Sylviorus/BlueMoonVampireBot>
This file is part of @BlueMoonVampireBot (Antispam Telegram Bot)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from app import bot as app
from pyrogram import filters
import sys, traceback, io
from subprocess import getoutput as run

# overwriting devs values


@app.on_message(filters.command("eval", prefixes=["/", ".", "?", "-"]))
async def eval(client, message):
    DEVS = [
        825664681, 1091139479, 2107137268, 2079472115, 2076788242, 5086015489
    ]

    if message.from_user.id in DEVS:

        status_message = await message.reply_text("Processing ...")
        cmd = message.text.split(" ", maxsplit=1)[1]

        reply_to_ = message
        if message.reply_to_message:
            reply_to_ = message.reply_to_message

        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None

        try:
            await aexec(cmd, client, message)
        except Exception:
            exc = traceback.format_exc()

        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr

        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"

        final_output = "<b>EVAL</b>: "
        final_output += f"<code>{cmd}</code>\n\n"
        final_output += "<b>OUTPUT</b>:\n"
        final_output += f"<code>{evaluation.strip()}</code> \n"

        if len(final_output) > 4096:
            with io.BytesIO(str.encode(final_output)) as out_file:
                out_file.name = "eval.text"
                await reply_to_.reply_document(document=out_file,
                                               caption=cmd,
                                               disable_notification=True)
        else:
            await reply_to_.reply_text(final_output)
        await status_message.delete()

    else:
        await message.reply("You can't use eval")


async def aexec(code, client, message):
    exec("async def __aexec(client, message): " +
         "".join(f"\n {l_}" for l_ in code.split("\n")))
    return await locals()["__aexec"](client, message)


@app.on_message(filters.command("bash", prefixes=['/', '.', '?', '-']))
def bash(_, m):
    DEVS = [825664681, 1091139479, 2079472115, 2076788242]
    if m.from_user.id in DEVS:
        code = m.text.replace(m.text.split(" ")[0], "")
        x = run(code)
        m.reply(
            f"<b>BASH</b>: <code>{code}</code>\n\n<b>OUTPUT</b>:\n<code>{x}</code>",
            parse_mode="html")
    else:
        m.reply("You can't use bash")
