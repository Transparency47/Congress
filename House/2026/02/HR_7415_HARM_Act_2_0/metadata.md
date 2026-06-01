# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7415?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7415
- Title: HARM Act 2.0
- Congress: 119
- Bill type: HR
- Bill number: 7415
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-03-27T08:06:17Z
- Update date including text: 2026-03-27T08:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7415",
    "number": "7415",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000795",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Wilson, Joe [R-SC-2]",
        "lastName": "Wilson",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "HARM Act 2.0",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:17Z",
    "updateDateIncludingText": "2026-03-27T08:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-02-09T17:05:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-09T17:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "TN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "IN"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NV"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7415ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7415\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Wilson of South Carolina (for himself, Mr. Cohen , Mr. Lawler , Ms. Salazar , Mr. Panetta , Mr. Fallon , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo designate Russian-based paramilitary organizations and their successor entities as foreign terrorist organizations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Holding Accountable Russian Mercenaries Act or the HARM Act 2.0 .\n#### 2. Findings and statement of policy\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nFollowing the death of Wagner Group leader Yevgeniy Prigozhin in August 2023, the organization\u2019s personnel, operational infrastructure, and activities have been absorbed into the Russian Ministry of Defense and reorganized under various successor entities, including the Africa Corps, Redut PMC, and Patriot PMC.\n**(2)**\nThese successor entities continue to conduct operations consistent with the Wagner Group\u2019s historical activities, including mercenary operations, human rights abuses, resource extraction facilitation, and support for authoritarian regimes in Africa, the Middle East, Eastern Europe, and Latin America.\n**(3)**\nThe integration of Wagner-derived forces into Ministry of Defense structures does not diminish their threat to international peace and security, human rights, or United States national security interests.\n**(4)**\nThe Wagner Group and its successor entities constitute a terrorist group that engages in terrorism (as defined in section 140(d) of the Foreign Relations Authorization Act, Fiscal Year 1988 and 1989 ( 22 U.S.C. 2656f(d) )).\n**(5)**\nThe Wagner Group and its successor entities have committed, or are credibly accused of committing, terrorist activity (as defined in section 212(a)(3)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(3)(B) )) and ongoing atrocities and human rights violations conducted by successor entities operating under the Africa Corps, Redut PMC, Patriot PMC, and other Ministry of Defense-affiliated formations in Africa, the Middle East, and other regions in 2024 and 2025.\n##### (b) Statement of policy\nIt shall be the policy of the United States to designate as a Foreign Terrorist Organization and Specially Designated Global Terrorists the successor and associated entities to the Wagner Group.\n#### 3. Reports required and determination\n##### (a) Secretary of State report\nThe Secretary of State shall submit to the appropriate congressional committees a report on the following:\n**(1)**\nA list of all successor and affiliated entities of the organization formerly known as the Wagner Group, including Africa Corps, Redut PMC, Patriot PMC, and any Ministry of Defense-affiliated paramilitary formations that inherit Wagner personnel, operations, or assets.\n**(2)**\nA list of all individuals that order, control, or otherwise direct the organizations described in paragraph (1).\n**(3)**\nAny entity that\u2014\n**(A)**\noperates under the direction, control, or coordination of the Russian Ministry of Defense;\n**(B)**\nemploys personnel previously associated with the Wagner Group or its successor entities; and\n**(C)**\nconducts operations consistent with Wagner Group activities.\n**(4)**\nA description of any conduct of the organizations or individuals described in paragraphs (1) through (3) that\u2014\n**(A)**\nmay be grounds for designation pursuant to Executive Order 13224 ( 50 U.S.C. 1701 note; relating to blocking property and prohibiting transactions with persons who commit, threaten to commit, or support terrorism); and\n**(B)**\nmay constitute terrorist activity (as defined in section 212(a)(3)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(3)(B) )).\n##### (b) Comptroller General report\nNot later than 60 days after the submission of the report required by subsection (a), the Comptroller General of the United States shall submit to the appropriate congressional committees a report evaluating the accuracy and completeness of the report required by subsection (a), including an assessment of the methodologies and data sources used in preparing such report.\n##### (c) Form\nThe reports required by subsections (a) and (b) shall be transmitted in an unclassified form, and may contain a classified annex.\n##### (d) Determination\n**(1) In general**\nNot later than 30 days after the date on which the Comptroller General submits the report required by subsection (b), the Secretary of State, in coordination with the Secretary of the Treasury, the Attorney General, and the Office of the Director of National Intelligence, shall determine whether any person identified in the report under paragraph (1), (2), or (3) of subsection (a) meets the criteria for designation under paragraph (4) of subsection (a).\n**(2) Effect of positive determination**\nThe Secretary of State, the Secretary of Treasury, and the Attorney General (as appropriate) shall apply the measures described in subsection (a)(4) to each person with respect to which a positive determination under paragraph (1) has been made.\n**(3) Periodic review and updates**\nThe Secretary of State shall periodically review and update the designations under this section to include any newly identified successor entities, affiliates, or rebranded organizations that meet the criteria specified in subsection (a)(4).\n##### (e) Annual report\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, and annually thereafter for five years, the Secretary of State, in consultation with the Secretary of Defense, the Director of National Intelligence, and the Secretary of the Treasury, shall submit to the appropriate congressional committees a report on the international activities of the Russian-based mercenary Wagner Group and its successor entities that includes\u2014\n**(A)**\na comprehensive assessment of the operations, activities, and force disposition of the Wagner Group and successor entities in Africa, Latin America, Eastern Europe, the Middle East, and any other region;\n**(B)**\nan analysis of the relationship between the Wagner Group, its successor entities, and the Russian Ministry of Defense, including command and control structures, funding mechanisms, and operational coordination;\n**(C)**\na detailed account of human rights abuses, war crimes, and violations of international humanitarian law committed by the Wagner Group and successor entities;\n**(D)**\nan assessment of the financial networks, revenue sources, and economic activities supporting the Wagner Group and successor entities, including resource extraction operations;\n**(E)**\nan evaluation of the effectiveness of sanctions imposed against the Wagner Group and successor entities;\n**(F)**\nrecommendations for additional legislative or executive actions to counter the activities of the Wagner Group and successor entities;\n**(G)**\nan assessment of cooperation with international partners in addressing threats posed by the Wagner Group and successor entities; and\n**(H)**\nspecific information regarding the deployment, activities, and objectives of Russian paramilitary forces in Venezuela and throughout the Western Hemisphere, including any threats to regional security or United States interests.\n**(2) Form**\nThe report required by this subsection shall be submitted in unclassified form, but may include a classified annex.\n##### (f) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Relations of the Senate;\n**(2)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate;\n**(3)**\nthe Committee on Financial Services of the House of Representatives;\n**(4)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(5)**\nthe Committee on the Judiciary of the House of Representatives.",
      "versionDate": "2026-02-09",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-02-13T17:55:48Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7415ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "HARM Act 2.0",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HARM Act 2.0",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Holding Accountable Russian Mercenaries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate Russian-based paramilitary organizations and their successor entities as foreign terrorist organizations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:03:42Z"
    }
  ]
}
```
