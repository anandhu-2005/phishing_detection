---
name: Sentinel Cyber-Security System
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#c2c6d6'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#8c909f'
  outline-variant: '#424754'
  surface-tint: '#adc6ff'
  primary: '#adc6ff'
  on-primary: '#002e6a'
  primary-container: '#4d8eff'
  on-primary-container: '#00285d'
  inverse-primary: '#005ac2'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#ffb3ad'
  on-tertiary: '#68000a'
  tertiary-container: '#ff5451'
  on-tertiary-container: '#5c0008'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdad7'
  tertiary-fixed-dim: '#ffb3ad'
  on-tertiary-fixed: '#410004'
  on-tertiary-fixed-variant: '#930013'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
  surface-card: '#1E293B'
  border-glow: '#334155'
  data-blue: '#60A5FA'
  warning-amber: '#F59E0B'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md-mobile:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-code:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  stats-number:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1200px
  gutter: 24px
  margin-edge: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered to project **unwavering authority, precision, and proactive protection**. It targets security analysts and high-stakes environments where trust is the primary currency. The aesthetic is a sophisticated blend of **Modern Corporate** and **High-Tech Cyber-Security**, utilizing deep spatial layers and glowing focal points to simulate a digital "command center" environment.

The visual direction follows a **Modern Cyber-Security** style:
- **Minimalist Layouts:** High information density without clutter, using ample negative space to separate critical data from diagnostic features.
- **Subtle Glassmorphism:** Translucent surface layers that create a sense of depth and technical complexity.
- **Tactile Feedback:** Crisp, high-contrast borders and "active" glowing states that indicate real-time processing and machine learning analysis.

## Colors

The system utilizes a **True Dark Mode** default to reduce eye strain during intensive monitoring and to emphasize "glowing" status indicators.

- **Primary (Security Blue):** Used for active states, primary actions, and neutral "scanning" animations.
- **Secondary (Legitimate Green):** Exclusively reserved for high-confidence safety results. It represents a "clear" or "secure" status.
- **Tertiary (Alert Red):** Reserved for "Phishing" detections and critical system errors. It must be used sparingly to maintain high visual impact.
- **Neutral (Deep Navy):** The foundation of the UI. Backgrounds use the deepest shades, while UI containers use slightly lighter navy tones to establish hierarchy.

## Typography

The typography strategy prioritizes **legibility and technical rigor**. 

- **Inter** is the workhorse for the interface, providing a clean, neutral foundation for headlines and body copy.
- **JetBrains Mono** is utilized for all "technical" data points—including URLs, feature extraction scores, and ML weights. This font choice signals to the user that they are looking at raw, calculated intelligence.
- Use **Label-Caps** for metadata and section headers to create an institutional, categorized feel.
- **Stats-Number** should be used for the final prediction confidence score to ensure immediate readability.

## Layout & Spacing

This design system uses a **Fixed Grid** approach for desktop (12 columns) to maintain a controlled, professional layout, transitioning to a **Fluid** 1-column layout for mobile.

- **The Analysis Hub:** The main interface should be centered, utilizing a 8-column wide central column for the URL input to focus user attention.
- **Result Grid:** When displaying feature extraction (the 12 URL features), use a 3-column grid on desktop and 1-column on mobile.
- **Spacing Rhythm:** A strict 8px base grid is used. Elements are separated by `stack-md` (16px) for related items and `stack-lg` (32px) for distinct functional sections.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Luminescent Accents** rather than traditional shadows.

- **Level 0 (Background):** Base navy (`#0F172A`).
- **Level 1 (Cards):** Surface Navy (`#1E293B`) with a 1px border of `border-glow`. This layer holds the main content and forms.
- **Level 2 (Active/Glass):** For the result overlay, use a backdrop-blur (12px) with a semi-transparent version of the primary color.
- **Glow Effects:** Critical indicators (Safe/Phishing) should use a `box-shadow` with a high blur radius (20px) and low opacity (0.3) matching the status color (Green or Red) to create a "warning light" effect.

## Shapes

The shape language is **Soft (0.25rem base)**. While the aesthetic is "cyber," overly sharp corners feel aggressive and unrefined. 

- **Small elements (Checkboxes, small buttons):** Use `0.25rem` radius.
- **Standard Cards:** Use `0.5rem` (`rounded-lg`) to provide a containerized, modern feel.
- **Input Fields:** Maintain a `0.25rem` radius to keep the "technical tool" appearance.
- **Pill Tags:** Status indicators (e.g., "HTTPS Detected") may use fully rounded pill shapes to distinguish them from interactive buttons.

## Components

### Input Fields
The URL input is the most critical component. It should feature a large, mono-spaced font for the URL text, a subtle interior glow when focused (`primary-blue`), and a clear "Analyze" button anchored to the right side of the field.

### Status Cards
The "Result" card must change its border and accent color based on the ML output.
- **Legitimate:** Emerald green border, soft green glow, "SAFE" icon.
- **Phishing:** Alert red border, soft red glow, "THREAT" icon.

### Feature Matrix
Use a list-based component to show the 12 extracted features. Each row should display the feature name in `label-caps` and the extracted value in `data-code`. Use subtle horizontal dividers (`#334155`).

### Buttons
- **Primary:** Solid `primary-blue` with white text. On hover, increase the brightness and add a subtle outer glow.
- **Secondary:** Outlined with `border-glow`, using `data-blue` text. Used for "Clear" or "View Detailed Logs."

### Glass Containers
For the ML logic explanation, use a surface with `background: rgba(30, 41, 59, 0.7)` and `backdrop-filter: blur(10px)`. This separates the technical breakdown from the primary results visually.