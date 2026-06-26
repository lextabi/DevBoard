# Frontend - DevBoard

React TypeScript frontend application for DevBoard.

## Quick Start

```bash
npm install
npm run dev
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run test` - Run tests
- `npm run preview` - Preview production build

## Folder Structure

See [FOLDER_STRUCTURE.md](../FOLDER_STRUCTURE.md#frontend-structure) in root directory.

## Environment Variables

Copy `.env.example` to `.env.local` and update values:

```
VITE_API_URL=http://localhost:8000/api/v1
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_key
```

## Dependencies

- React 18
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Axios
- @dnd-kit (drag-and-drop)
- Recharts (charts)

See `package.json` for full dependencies.
