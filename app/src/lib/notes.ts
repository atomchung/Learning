import fs from "fs";
import path from "path";
import matter from "gray-matter";
import { remark } from "remark";
import html from "remark-html";

const contentDir = path.join(process.cwd(), "content");

export interface Flashcard {
  q: string;
  a: string;
}

export interface NoteMeta {
  slug: string;
  title: string;
  date: string;
  tags: string[];
  related: string[];
  summary: string;
  flashcards: Flashcard[];
}

export interface Note extends NoteMeta {
  contentHtml: string;
}

export function getAllNotes(): NoteMeta[] {
  const files = fs.readdirSync(contentDir).filter((f) => f.endsWith(".md"));
  const notes = files.map((file) => {
    const slug = file.replace(/\.md$/, "");
    const raw = fs.readFileSync(path.join(contentDir, file), "utf-8");
    const { data } = matter(raw);
    return {
      slug,
      title: data.title || slug,
      date: data.date || "",
      tags: data.tags || [],
      related: data.related || [],
      summary: data.summary || "",
      flashcards: data.flashcards || [],
    };
  });
  return notes.sort(
    (a, b) => new Date(b.date).getTime() - new Date(a.date).getTime()
  );
}

export async function getNoteBySlug(slug: string): Promise<Note | null> {
  const filePath = path.join(contentDir, `${slug}.md`);
  if (!fs.existsSync(filePath)) return null;

  const raw = fs.readFileSync(filePath, "utf-8");
  const { data, content } = matter(raw);

  const result = await remark().use(html).process(content);

  return {
    slug,
    title: data.title || slug,
    date: data.date || "",
    tags: data.tags || [],
    related: data.related || [],
    summary: data.summary || "",
    flashcards: data.flashcards || [],
    contentHtml: result.toString(),
  };
}

export function getAllTags(): { tag: string; count: number }[] {
  const notes = getAllNotes();
  const tagMap = new Map<string, number>();
  for (const note of notes) {
    for (const tag of note.tags) {
      tagMap.set(tag, (tagMap.get(tag) || 0) + 1);
    }
  }
  return Array.from(tagMap.entries())
    .map(([tag, count]) => ({ tag, count }))
    .sort((a, b) => b.count - a.count);
}

export function getNotesByTag(tag: string): NoteMeta[] {
  return getAllNotes().filter((n) => n.tags.includes(tag));
}
