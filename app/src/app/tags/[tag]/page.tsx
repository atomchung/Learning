import { getNotesByTag, getAllTags } from "@/lib/notes";
import NoteCard from "@/components/NoteCard";
import Link from "next/link";

export async function generateStaticParams() {
  return getAllTags().map(({ tag }) => ({ tag }));
}

export default async function TagPage({
  params,
}: {
  params: Promise<{ tag: string }>;
}) {
  const { tag } = await params;
  const decoded = decodeURIComponent(tag);
  const notes = getNotesByTag(decoded);

  return (
    <>
      <Link
        href="/tags"
        className="mb-4 inline-flex items-center gap-1 text-sm text-blue-600 dark:text-blue-400"
      >
        <svg className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth={2} viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
        </svg>
        所有標籤
      </Link>

      <header className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight">#{decoded}</h1>
        <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
          {notes.length} 篇筆記
        </p>
      </header>

      <div className="flex flex-col gap-3">
        {notes.map((note) => (
          <NoteCard key={note.slug} note={note} />
        ))}
      </div>
    </>
  );
}
