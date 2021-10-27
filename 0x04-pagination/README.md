## Offset Pagination
``` GET /items?limit=20&offset=100 ```

Easiest to implement, stateless on the server, works regardless of sort_by parameters.

## Keyset Pagination
Uses filter values of last page to fetch next set of items. Those columns are indexed. 

Works with existing filters without additional backend logic. Only need additional limit URL parameter.

Consistent ordering even when newer items are added to the table. Works well when sorting by most recent first.

Consistent performance even with large offsets.

## Seek Pagination
And extension of Keyset Pagination. By adding after_id or start_id parameters we can remove the tight coupling of paging to filters and sorting. Seek Pagination is difficult to implement when a custom sort order is needed.


