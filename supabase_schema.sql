create extension if not exists "pgcrypto";

create table if not exists public.consultas_clima (
  id uuid primary key default gen_random_uuid(),
  ciudad text not null,
  pais text not null,
  temperatura numeric not null,
  sensacion_termica numeric not null,
  humedad integer not null,
  descripcion text not null,
  notas text,
  created_at timestamptz not null default now()
);

alter table public.consultas_clima enable row level security;

create policy "Permitir lectura publica de consultas"
on public.consultas_clima
for select
using (true);

create policy "Permitir insertar consultas"
on public.consultas_clima
for insert
with check (true);

create policy "Permitir actualizar consultas"
on public.consultas_clima
for update
using (true)
with check (true);

create policy "Permitir eliminar consultas"
on public.consultas_clima
for delete
using (true);
