rule [NAME] {
	meta:
		copyright = "[COPYRIGHT]"
		description = "[DESCRIPTION]"
		author = "[AUTHOR]"
		reference = "[REFERENCE]"
		date = "[DATE]"
	strings:
		$str1 = { [STRING] }
		$str2 = { [STRING] }
		$str3 = { [STRING] }
		$str4 = { [STRING] }
		$str5 = { [STRING] }
		$str6 = { [STRING] }
		$str7 = { [STRING] }
		$str8 = { [STRING] }
		$str9 = { [STRING] }

	condition:
		x of them
		all of them
		any of them
}