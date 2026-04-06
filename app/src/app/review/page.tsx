import { getAllNotes } from "@/lib/notes";
import Link from "next/link";

export default function ReviewPage() {
  const notes = getAllNotes().filter((n) => n.flashcards.length > 0);
  const totalCards = notes.reduce((sum, n) => sum + n.flashcards.length, 0);

  return (
    <>
      <header className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight">複習</h1>
        <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
          共 {totalCards} 張閃卡，來自 {notes.length} 篇筆記
        </p>
      </header>

      <div className="flex flex-col gap-3">
        {notes.map((note) => (
          <Link
            key={note.slug}
            href={`/notes/${note.slug}#flashcards`}
            className="flex items-center justify-between rounded-2xl border border-gray-200 bg-white p-4 shadow-sm dark:border-gray-700 dark:bg-gray-900"
          >
            <div className="flex-1 min-w-0">
              <h2 className="text-sm font-bold truncate">{note.title}</h2>
              <p className="text-xs text-gray-500 mt-1">
                {note.flashcards.length} 張閃卡
              </p>
            </div>
            <div className="ml-3 flex items-center justify-center rounded-full bg-blue-50 px-3 py-1 dark:bg-blue-900/30">
              <span className="text-sm font-bold text-blue-600 dark:text-blue-400">
                {note.flashcards.length}
              </span>
            </div>
          </Link>
        ))}
      </div>

      {notes.length === 0 && (
        <div className="text-center mt-20">
          <p className="text-gray-400">尚無閃卡</p>
          <p className="text-xs text-gray-400 mt-2">
            在筆記的 frontmatter 中加入 flashcards 欄位即可
          </p>
        </div>
      )}
    </>
  );
}
