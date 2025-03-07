# DirJet

**DirJet** is a fast and efficient directory navigator inspired by Zoxide, with enhanced features for better user experience. It supports multiple shells including Bash, Zsh, and Fish.

## Features
- **Current Directory-Based Jumps**: Prioritizes jumps based on the current working directory.
- **Learning Mode**: Learns and predicts frequently used directories based on user habits.
- **Directory Bookmarking**: Bookmark directories with custom aliases.
- **Shell Compatibility**: Support for bash, zsh, and fish shells.
- **Auto-Cleanup**: Periodically clean up the least used directory entries.
- **Path Ranking System**: Smarter path ranking based on frequency, recency, and context.
- **Fast Caching Mechanism**: Optimized caching for instant directory lookup.
- **Shortcut Commands**: User-defined shortcut commands for custom jumps

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sushrut1101/dirJet.git
   cd dirjet
   ```

2. Make the script executable:
   ```bash
   chmod +x dirjet.py
   ```

## Usage

### Adding a Bookmark

To bookmark the current directory:
```bash
djet -b
```

### Listing Bookmarked Directories

To list all bookmarked directories:
```bash
djet -l
```

### Jumping to a Directory

To jump to a directory:
```bash
djet <query>
```

### Integration with Shells

Add the following to your shell configuration file for seamless integration.

#### Bash
Add to your `.bashrc`:
```bash
function djet() {
    python3 /path/to/dirjet.py "$@"
    cd "$(cat /tmp/djet_target_path)"
}
```

#### Zsh
Add to your `.zshrc`:
```zsh
function djet() {
    python3 /path/to/dirjet.py "$@"
    cd "$(cat /tmp/djet_target_path)"
}
```

#### Fish
Add to your `config.fish`:
```fish
function djet
    python3 /path/to/dirjet.py $argv
    cd (cat /tmp/djet_target_path)
end
```

## Contributing
Feel free to submit issues and feature requests. Contributions are welcome!
