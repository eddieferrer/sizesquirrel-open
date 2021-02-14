<script>
export default {
  middleware: [
    function ({ route, redirect }) {
      redirect(`/shoes/${route.params.brand}`);
    },
  ],
};
</script>
