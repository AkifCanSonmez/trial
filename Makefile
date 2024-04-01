create_tag:
	@latest_tag=$$(git tag | sort -V | tail -n1); \
	if [ -z "$$latest_tag" ]; then \
		latest_tag="v0"; \
	fi; \
	tag_number=$$(echo $$latest_tag | grep -o -E '[0-9]+$$'); \
	new_tag_number=$$((tag_number + 1)); \
	new_tag="v$$new_tag_number"; \
	echo $$new_tag > new_tag.txt; \
	echo "New tag created: $$new_tag"

repro:
	dvc repro

push: create_tag
	new_tag=$$(cat new_tag.txt); \
	git add new_tag.txt; \
	git commit -m "Updated with $$new_tag version"; \
	git tag $$new_tag; \
	git push origin main --tags
