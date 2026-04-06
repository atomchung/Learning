import Link from "next/link";
import type { NoteMeta } from "@/lib/notes";

export default function NoteCard({ note }: { note: NoteMeta }) {
  return (
    <Link
      href={`/notes/${note.slug}`}
      className="block rounded-2xl border border-gray-200 bg-white p-5 shadow-sm transition-shadow hover:shadow-md active:shadow-inner dark:border-gray-700 dark:bg-gray-900"
    >
      <h2 className="text-lg font-bold leading-snug text-gray-900 dark:text-gray-100">
        {note.title}
      </h2>
      <p className="mt-2 text-sm text-gray-500 dark:text-gray-400 line-clamp-2">
        {note.summary}
      </p>
      <div className="mt-3 flex flex-wrap gap-2">
        {note.tags.map((tag) => (
          <span
            key={tag}
            className="rounded-full bg-blue-50 px-2.5 py-0.5 text-xs font-medium text-blue-700 dark:bg-blue-900/30 dark:text-blue-300"
          >
            #{tag}
          </span>
        ))}
      </div>
      <time className="mt-3 block text-xs text-gray-400">{note.date}</time>
    </Link>
  );
}
