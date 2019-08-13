<template>
  <q-page padding>
  <div class="q-pa-md">
    <q-table
      title="Treats"
      dense
      :data="data"
      :columns="columns"
      row-key="name"
    />
  </div>
  </q-page>
</template>

<script>
export default {
  // name: 'Personas',
}
</script>

<style>
</style>
