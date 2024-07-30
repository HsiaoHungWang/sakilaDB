from DB_DEMO import Category

# 新增
# print(Category.category_create('abc'))
# 修改
# print(Category.category_update(19,'xyz'))

#刪除
print(Category.category_delete(19))
# 讀取
print(Category.category_all())
print(Category.category_single(1))