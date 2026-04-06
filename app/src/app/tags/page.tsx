import { getAllTags } from "@/lib/notes";
import TagPill from "@/components/TagPill";

export default function TagsPage() {
  const tags = getAllTags();

  return (
    <>
      <header className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight">標籤</h1>
        <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
          依主題瀏覽學習筆記
        </p>
      </header>

      <div className="flex flex-wrap gap-3">
        {tags.map(({ tag, count }) => (
          <TagPill key={tag} tag={tag} count={count} />
        ))}
      </div>

      {tags.length === 0 && (
        <p className="text-center text-gray-400 mt-20">尚無標籤</p>
      )}
    </>
  );
}
