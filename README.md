# qt_precommit

[pre-commit](https://pre-commit.com/) hooks for Qt tools.

Currently supported hooks:

- **qmlformat**: Formats QML files according to the QML Coding Conventions;
- **qmllint**: QML syntax verifier and analyzer;

## Installing hooks

Add the following to your `.pre-commit-config.yaml`:

```yaml
  - repo: https://github.com/KDABLabs/qt_precommit
    rev: v0.0.1
    hooks:
      - id: qmlformat
      - id: qmllint
```

## Configuration

qt_precommit will check for a `.qt-precommit` file in the current working directory, for example:

```ini
[Qt]
path = /path/to/Qt/6.8.2/macos/bin
```

If the file does not exist, or the Qt `path` is not configured, `qt_precommit` will use the `PATH`
environment variable when searching for the specified tool.

If used, the `.qt-precommit` file should be added to the `.gitignore` file, as this is a
machine-specific configuration.

## Licensing

qt_precommit is © Klarälvdalens Datakonsult AB (KDAB) and is made available under the terms of the
[MIT](LICENSE) license.

Contact KDAB at info@kdab.com if you need different licensing options.
