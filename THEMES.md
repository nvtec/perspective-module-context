# **Ignition Perspective Design Tokens & CSS Variables**

When generating Perspective resources, always use Ignition's native CSS variables in place of hardcoded color strings (hex, rgb, hsl). Using CSS variables ensures styles automatically adapt to Ignition's built-in light, dark, warm, and cool themes.

## ---

**1\. Surfaces & Backgrounds**

| Variable | Description   |
| :---- | :---- |
| var(--container-background) | Main background color for pages and root views |
| var(--surface) | Default surface color for cards, panels, and containers |
| var(--surface-secondary) | Subtle background for nested panels or headers |
| var(--surface-highlight) | Highlight background on table rows, list items, or hovers |

## ---

**2\. Neutrals & Grayscale**

Grayscale tokens adapt between light and dark themes (low values are light in light themes and dark in dark themes).

| Variable | Light Theme Role | Dark Theme Role   |
| :---- | :---- | :---- |
| var(--neutral-10) | Lightest background / white | Darkest background / black |
| var(--neutral-20) | Subtle card fill | Deep surface fill |
| var(--neutral-30) | Default borders | Dark borders |
| var(--neutral-40) | Active borders & dividers | Muted borders |
| var(--neutral-50) | Disabled borders | Disabled borders |
| var(--neutral-60) | Placeholder & disabled text | Muted text |
| var(--neutral-70) | Secondary text | Secondary text |
| var(--neutral-80) | Standard body text | Standard body text |
| var(--neutral-90) | Strong headings | Strong headings |
| var(--neutral-100) | Darkest text / black | Brightest text / white |

## ---

**3\. Brand & Semantic States**

Use semantic variables for status indication, alarms, inputs, and calls to action.

| Variable | Usage   |
| :---- | :---- |
| var(--call-to-action) | Primary action buttons, active navigation markers |
| var(--call-to-action-hover) | Hover state for primary action elements |
| var(--call-to-action-active) | Pressed state for primary action elements |
| var(--info) | Informational badges, indicators, neutral notifications |
| var(--success) | Normal operation, verified state, running pumps/motors |
| var(--warning) | Low/High non-critical warnings, maintenance flags |
| var(--error) | Critical alarms, failed writes, tripped equipment |

## ---

**4\. Borders, Spacing & Typography**

| Variable | Recommended Usage   |
| :---- | :---- |
| var(--border) | Default 1px solid border definition |
| var(--border-radius) | Standard component border radius (typically 4px) |
| var(--font-primary) | Standard UI font stack (sans-serif / Roboto / Noto) |
| var(--font-mono) | Monospace font stack for code, timestamps, and tag paths |

## ---

**5\. Implementation Examples**

### **In a Perspective Component (props.style)**

{  
  "type": "ia.display.label",  
  "meta": { "name": "StatusLabel" },  
  "props": {  
    "text": "Running",  
    "style": {  
      "backgroundColor": "var(--surface)",  
      "color": "var(--success)",  
      "border": "var(--border)",  
      "borderRadius": "var(--border-radius)",  
      "padding": "4px 8px",  
      "fontFamily": "var(--font-primary)"  
    }  
  }  
}

### **In a Style Class Definition (style.json)**

{  
  "base": {  
    "style": {  
      "backgroundColor": "var(--surface)",  
      "color": "var(--neutral-90)",  
      "border": "1px solid var(--neutral-30)",  
      "borderRadius": "var(--border-radius)"  
    }  
  },  
  "variants": \[  
    {  
      "pseudo": "hover",  
      "style": {  
        "backgroundColor": "var(--surface-highlight)",  
        "borderColor": "var(--call-to-action)"  
      }  
    }  
  \]  
}  
