select p.flavor
    from (
    (select f.flavor, sum(f.total_order) as total_order 
        from first_half as f
    group by f.flavor) 
    union
    (select j.flavor, sum(j.total_order) as total_order 
        from july as j
    group by j.flavor)) as p
group by flavor
order by sum(p.total_order) desc
limit 3