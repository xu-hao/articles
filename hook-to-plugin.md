# That Claude Code Hook You Love? Turn It Into a Plugin Anyone Can Install.

## How to convert a private hook into an installable plugin, using a notification sound as the running example.

You have a hook you love. Maybe it plays a sound when Claude finishes a task, formats files after every edit, or logs your bash commands. It lives in `~/.claude/settings.json`, it works great, and it is completely stuck there. New laptop? Copy the JSON by hand. A colleague sees your terminal ding and asks how you did it? You paste a JSON fragment into Slack and wish them luck with the merge.

Claude Code plugins fix this, and converting a hook is much less work than the word "plugin" suggests. **A plugin is a git repo with two small JSON files and your script; the whole conversion takes about ten minutes.** This tutorial walks through a real one: [chime](https://github.com/xu-hao/claude-chime), which plays a sound and shows a desktop notification when Claude needs you.

## Step 1: Look at what you have

The starting point is a hook block in `~/.claude/settings.json`. Here is the one we're converting, which fires on two `Notification` events:

```json
"hooks": {
  "Notification": [
    {
      "matcher": "permission_prompt",
      "hooks": [{
        "type": "command",
        "command": "notify-send 'Claude Code' 'Permission needed' && pw-play /usr/share/sounds/freedesktop/stereo/bell.oga",
        "timeout": 5
      }]
    },
    {
      "matcher": "idle_prompt",
      "hooks": [{
        "type": "command",
        "command": "notify-send 'Claude Code' \"What's next?\" && pw-play /usr/share/sounds/freedesktop/stereo/complete.oga",
        "timeout": 5
      }]
    }
  ]
}
```

`permission_prompt` fires when Claude wants approval. `idle_prompt` fires when Claude finishes and waits for input. That second one is the "task done" sound.

## Step 2: Create the skeleton

A hooks plugin needs exactly this layout:

```
claude-chime/
├── .claude-plugin/
│   ├── plugin.json        # the manifest
│   └── marketplace.json   # makes the repo installable (step 6)
├── hooks/
│   └── hooks.json         # your hook config, almost verbatim
└── scripts/
    └── notify.sh          # your command, promoted to a file
```

Note the split: `plugin.json` and `marketplace.json` live inside `.claude-plugin/`, while `hooks/` and `scripts/` sit at the repo root. Getting this backwards is the most common mistake.

## Step 3: Write the manifest

`.claude-plugin/plugin.json` describes the plugin. Only `name` is required, and it must be kebab-case:

```json
{
  "name": "chime",
  "displayName": "Chime",
  "description": "Desktop notification and sound when Claude Code finishes a task or needs permission",
  "version": "0.1.0",
  "author": { "name": "Hao Xu" },
  "license": "MIT"
}
```

## Step 4: Promote the command to a script

You could paste the shell one-liners straight into the plugin's hook config. Resist that. A script file gives you room to handle other people's machines, and other people's machines is the entire reason you're making a plugin. Here is `scripts/notify.sh`:

```bash
#!/usr/bin/env bash
# chime — desktop notification + sound for Claude Code events.
# Usage: notify.sh <kind>    kind: permission | done
kind="${1:-done}"
case "$kind" in
  permission) msg="Permission needed"; sound=bell.oga ;;
  *)          msg="What's next?";      sound=complete.oga ;;
esac

command -v notify-send >/dev/null 2>&1 && notify-send "Claude Code" "$msg"

player=$(command -v pw-play || command -v paplay || true)
[ -n "$player" ] && "$player" "/usr/share/sounds/freedesktop/stereo/$sound" 2>/dev/null

exit 0
```

Two portability moves worth copying: every external tool is checked with `command -v` before use, and the script exits 0 no matter what. A notification hook that fails should stay silent; it should never break someone's session. Don't forget `chmod +x scripts/notify.sh`.

## Step 5: Write the hook config

`hooks/hooks.json` is your settings.json block with one change: commands point at the bundled script through `${CLAUDE_PLUGIN_ROOT}`, a variable Claude Code resolves to wherever the plugin ends up installed:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "permission_prompt",
        "hooks": [{
          "type": "command",
          "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/notify.sh permission",
          "timeout": 5
        }]
      },
      {
        "matcher": "idle_prompt",
        "hooks": [{
          "type": "command",
          "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/notify.sh done",
          "timeout": 5
        }]
      }
    ]
  }
}
```

Keep the quotes around `${CLAUDE_PLUGIN_ROOT}`. Install paths can contain spaces.

Now validate:

```
$ claude plugin validate ./claude-chime
Validating plugin manifest: ./claude-chime/.claude-plugin/plugin.json
✔ Validation passed
```

## Step 6: The marketplace gotcha

Here is where the ten minutes usually becomes twenty. You'd expect to install straight from the directory, and you'd be wrong:

```
$ claude plugin install ./claude-chime
✘ Failed to install plugin "./claude-chime": Plugin "./claude-chime"
  not found in any configured marketplace
```

Plugins install from marketplaces. The fix is to make the repo its own marketplace by adding `.claude-plugin/marketplace.json`:

```json
{
  "name": "xu-hao",
  "owner": { "name": "Hao Xu" },
  "plugins": [
    {
      "name": "chime",
      "source": "./",
      "description": "Desktop notification and sound when Claude Code finishes a task or needs permission"
    }
  ]
}
```

The marketplace `name` is your namespace (your GitHub username is a good choice), and `source: "./"` says the plugin lives in this same repo. Now both commands work:

```
$ claude plugin marketplace add ./claude-chime
✔ Successfully added marketplace: xu-hao (declared in user settings)
$ claude plugin install chime@xu-hao --scope user
✔ Successfully installed plugin: chime@xu-hao (scope: user)
```

## Step 7: Delete the original hook

If the hook stays in settings.json while the plugin is enabled, both fire. You get two notifications and a double chime on every event. Open `~/.claude/settings.json`, delete the block from step 1, and check the file still parses:

```
$ jq -e 'has("hooks") | not' ~/.claude/settings.json
true
```

A malformed settings.json silently disables everything in it, so the `jq` check is worth the five seconds. Plugin hooks load at session start; open a fresh session and trigger a permission prompt to hear it work.

## Step 8: Push it

```
$ gh repo create you/claude-chime --public --source=. --push
```

That's the whole distribution story. Anyone can now run:

```sh
claude plugin marketplace add you/claude-chime
claude plugin install chime@you
```

And your own next laptop is those same two commands.

## The checklist

1. **Skeleton**: `.claude-plugin/` for the two JSON files, `hooks/` and `scripts/` at root.
2. **Manifest**: `plugin.json` with a kebab-case `name`.
3. **Script**: promote inline commands to `scripts/`, guard every dependency, exit 0.
4. **Hooks**: copy your settings block, swap paths to `"${CLAUDE_PLUGIN_ROOT}"/...`.
5. **Marketplace**: `marketplace.json` with `source: "./"` makes the repo installable.
6. **Install**: `marketplace add` the repo, then `install name@marketplace`.
7. **Dedup**: delete the old settings.json block or everything fires twice.
8. **Publish**: push to GitHub; installation is two commands for anyone.

The next time someone watches your terminal ding and asks how, the answer fits in one Slack message, and it isn't JSON.
