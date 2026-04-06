import { getNoteBySlug, getAllNotes } from "@/lib/notes";
import { notFound } from "next/navigation";
import Link from "next/link";
import FlashcardDeck from "@/components/FlashcardDeck";
import TagPill from "@/components/TagPill";

export async function generateStaticParams() {
  return getAllNotes().map((note) => ({ slug: note.slug }));
}

export default async function NotePage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const note = await getNoteBySlug(slug);

  if (!note) notFound();

  const allNotes = getAllNotes();
  const relatedNotes = allNotes.filter(
    (n) =>
      n.slug !== note.slug &&
      n.tags.some((t) => note.tags.includes(t))
  );

  return (
    <>
      {/* Back */}
      <Link
        href="/"
        className="mb-4 inline-flex items-center gap-1 text-sm text-blue-600 dark:text-blue-400"
      >
        <svg className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth={2} viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
        </svg>
        返回
      </Link>

      {/* Title */}
      <h1 className="text-xl font-bold leading-snug mb-2">{note.title}</h1>
      <time className="text-xs text-gray-400 block mb-3">{note.date}</time>

      {/* Tags */}
      <div className="flex flex-wrap gap-2 mb-6">
        {note.tags.map((tag) => (
          <TagPill key={tag} tag={tag} />
        ))}
      </div>

      {/* Content */}
      <article
        className="prose text-sm text-gray-800 dark:text-gray-200"
        dangerouslySetInnerHTML={{ __html: note.contentHtml }}
      />

      {/* Flashcards */}
      {note.flashcards.length > 0 && (
        <section className="mt-8 rounded-2xl border border-gray-200 bg-gray-50 p-5 dark:border-gray-700 dark:bg-gray-900">
          <FlashcardDeck cards={note.flashcards} />
        </section>
      )}

      {/* Related notes */}
      {relatedNotes.length > 0 && (
        <section className="mt-8">
          <h3 className="text-base font-bold mb-3">相關筆記</h3>
          <div className="flex flex-col gap-2">
            {relatedNotes.map((rn) => (
              <Link
                key={rn.slug}
                href={`/notes/${rn.slug}`}
                className="rounded-xl border border-gray-200 p-3 text-sm hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-800"
              >
                <span className="font-medium">{rn.title}</span>
                <span className="block mt-1 text-xs text-gray-500">
                  {rn.tags.map((t) => `#${t}`).join(" ")}
                </span>
              </Link>
            ))}
          </div>
        </section>
      )}
    </>
  );
}
