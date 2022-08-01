# Development environment

edited my launch.json to be

```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: odoo15",
      "type": "python",
      "request": "launch",
      "stopOnEntry": false,
      "python": "C:\\python\\python.exe",
      "console": "integratedTerminal",
      "program": "${workspaceRoot}\\odoo-bin",
      "args": [
        "--config=${workspaceRoot}\\odoo.conf","-u","hospital","-d","odoo15"
      ],
      "cwd": "${workspaceRoot}",
      "env": {},
      "envFile": "${workspaceRoot}/.env",
      "redirectOutput": true,
    }
  ]
}
```
