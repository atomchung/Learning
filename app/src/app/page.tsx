import { getAllNotes, getAllTags } from "@/lib/notes";
import NoteCard from "@/components/NoteCard";
import TagPill from "@/components/TagPill";

export default function Home() {
  const notes = getAllNotes();
  const tags = getAllTags();

  return (
    <>
      <header className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight">學習筆記</h1>
        <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
          串聯知識，持續成長
        </p>
      </header>

      {/* Tag filter strip */}
      <div className="mb-5 flex gap-2 overflow-x-auto pb-2 scrollbar-none">
        {tags.map(({ tag, count }) => (
          <TagPill key={tag} tag={tag} count={count} />
        ))}
      </div>

      {/* Notes list */}
      <div className="flex flex-col gap-3">
        {notes.map((note) => (
          <NoteCard key={note.slug} note={note} />
        ))}
      </div>

      {notes.length === 0 && (
        <p className="text-center text-gray-400 mt-20">尚無筆記</p>
      )}
    </>
  );
}
