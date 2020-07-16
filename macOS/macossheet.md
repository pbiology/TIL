# macOS cheat sheet
--

##### Disable mouse acceleration
Disable
`$ defaults write .GlobalPreferences com.apple.mouse.scaling -1`

Enable
`$ defaults write .GlobalPreferences com.apple.mouse.scaling 1`

##### Keep ssh connections alive
To the .ssh/config file, add:

```
Host *
  ServerAliveInterval 120
```