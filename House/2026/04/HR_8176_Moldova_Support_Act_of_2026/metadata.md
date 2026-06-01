# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8176?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8176
- Title: Moldova Support Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8176
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-04-24T08:06:48Z
- Update date including text: 2026-04-24T08:06:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-02 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-02 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8176",
    "number": "8176",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000375",
        "district": "9",
        "firstName": "William",
        "fullName": "Rep. Keating, William R. [D-MA-9]",
        "lastName": "Keating",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Moldova Support Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-24T08:06:48Z",
    "updateDateIncludingText": "2026-04-24T08:06:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-02",
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
      "actionDate": "2026-04-02",
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
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
          "date": "2026-04-02T12:33:05Z",
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
          "date": "2026-04-02T12:33:00Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "NC"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "SC"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NV"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8176ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8176\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Mr. Keating (for himself, Mr. Lawler , and Ms. Ross ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of State to facilitate strategic dialogue with Moldova and submit a report on support for Moldova, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Moldova Support Act of 2026 .\n#### 2. Sense of Congress\nIt is the sense of Congress that:\n**(1)**\nFor more than 3 decades, the Republic of Moldova has demonstrated a strong commitment to advancing democracy, strengthening civil society, furthering accession to the European Union, and deepening cooperation with the North Atlantic Treaty Organization through the Partnership for Peace Program.\n**(2)**\nThe Russian Federation\u2019s illegal invasion of Ukraine has threatened the sovereignty and territorial integrity of Moldova by destabilizing the country\u2019s economy as well as its energy security.\n**(3)**\nThe reelection of Moldovan President Maia Sandu further cements Moldova\u2019s pro-European path and Moldova\u2019s expedient accession to the European Union is in the direct interest of the United States.\n**(4)**\nMoldova represents a United States foreign assistance success story with United States foreign assistance to Moldova contributing to Moldova\u2019s energy security, economic development, and democratic values as well as furthering the United States-Moldova bilateral relationship, all which benefit the people and businesses of the United States and strengthen the transatlantic relationship.\n**(5)**\nThe United States-Moldova Strategic Dialogue is an important platform for strengthening the United States-Moldova bilateral relationship.\n**(6)**\nThe Russian Federation has historically targeted Moldova, seeking to undermine its democratic institutions, weaponize energy supplies in Moldova (including through Transnistria), and use Moldova as a lynchpin of a wider campaign to expand its malign influence and promote broader instability across Europe and the world.\n#### 3. United States-Moldova strategic dialogue\n##### (a) In general\nThe Secretary of State shall facilitate a strategic dialogue between the United States and the Republic of Moldova to\u2014\n**(1)**\nadvance bilateral priorities, including defense and security cooperation;\n**(2)**\ndiscuss Moldova\u2019s progress towards European Union integration and ways the United States can facilitate, through foreign assistance, investment, and public-private partnership, Moldova\u2019s process of accession to the European Union;\n**(3)**\nstrengthen economic and energy ties between Moldova and the United States, including expanding United States Government support for the Straseni-Gutinas transmission line project that will provide opportunities for United States businesses, strengthen Moldova\u2019s energy independence, and enhance Moldovan and European energy security;\n**(4)**\nreaffirm support for Moldova\u2019s sovereignty and territorial integrity within its internationally recognized borders;\n**(5)**\nexpand support for the State Partnership Program between Moldova and North Carolina; and\n**(6)**\nexpand and support State Department facilitated American Spaces in Moldova.\n##### (b) Frequency of dialogue\nThe Secretary, in partnership with the Government of Moldova, shall facilitate the strategic dialogue required in subsection (a) not less frequently than annually.\n#### 4. Strategy to promote Moldova\u2019s pro-European future\nNot later than 30 days after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate Congressional Committees a report that includes\u2014\n**(1)**\na 4-year strategy to\u2014\n**(A)**\nbolster United States-Moldovan bilateral relations, including to advance the priorities outlined in the strategic dialogue required in section 3; and\n**(B)**\nsupport Moldova\u2019s process of accession to the European Union and Moldova\u2019s goal of becoming a member of the European Union by the year 2030, including through United States foreign assistance that avoids conflicts with Moldova\u2019s obligations related to European Union accession or agreements with international financial institutions or other official creditors;\n**(2)**\na description of actions taken by the Department of State to counter malign influence by the Russian Federation and the People\u2019s Republic of China in Moldova since January 20, 2025;\n**(3)**\na list of active and cancelled foreign assistance programs in or related to Moldova since January 20, 2025; and\n**(4)**\na description of actions taken by the Department to support the accession of Moldova to the European Union and expand, where appropriate and within the interests of both the United States and Moldova, Moldova\u2019s cooperation with the North Atlantic Treaty Organization.\n#### 5. Maintenance of certain sanctions\n##### (a) In general\nNotwithstanding any other provision of law, any sanction imposed by the United States and in effect on the date of the enactment of this Act with respect to a person described in subsection (c) may not be terminated until the Secretary of State and the Secretary of the Treasury have, in addition to any other measure required by law\u2014\n**(1)**\nsubmitted to the appropriate congressional committees a written certification that the person (or the immediate family member of such person, as appropriate) is no longer engaging in the behavior that caused the person to be subject to the sanction;\n**(2)**\nbriefed the appropriate congressional committees regarding such certification; and\n**(3)**\nconsulted with the appropriate congressional committees regarding such certification.\n##### (b) Ineligibility for entry\nNotwithstanding any other provision of law, including paragraph (3) of section 7031(c) of the Consolidated Appropriations Act, 2022 ( 8 U.S.C. 1182 note), the Secretary may not waive or terminate the application of paragraph (1) of such section with respect to an individual described in subsection (c) unless the Secretary has\u2014\n**(1)**\nsubmitted to the appropriate congressional committees a written certification that the individual (or the immediate family member of the individual, as appropriate) is no longer engaging in significant corruption or a gross violation of human rights described in such section 7031(c)(1);\n**(2)**\nprovided to the appropriate congressional committees a briefing regarding such certification; and\n**(3)**\nconsulted with the appropriate congressional committees regarding such certification.\n##### (c) Persons described\nA person described in this subsection is any of the following:\n**(1)**\nFormer member of the Moldovan Parliament Ilan Shor.\n**(2)**\nThe Shor Party.\n**(3)**\nFormer member of the Moldovan Parliament Vlad Plahotniuc.\n**(4)**\nIgor Yuryevich Chayka.\n**(5)**\nIvan Alesksandrovich Zavorotnyi.\n**(6)**\nYuriy Igorevich Gudilin.\n**(7)**\nOlga Yurievna Grak.\n**(8)**\nLeonid Mikhailovich Gonin.\n**(9)**\nAleksei Valeryevich Troshin.\n**(10)**\nMaksim Yakubets.\n**(11)**\nThe National Engineering Corporation (commonly known as NIK ).\n**(12)**\nAny person with respect to whom sanctions have been imposed by the United States due to the relationship between such person and an individual described in paragraphs (1) through (11).\n#### 6. Congressional committees defined\nIn this Act, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations of the Senate.",
      "versionDate": "2026-04-02",
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
        "updateDate": "2026-04-13T21:12:25Z"
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
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8176ih.xml"
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
      "title": "Moldova Support Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Moldova Support Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of State to facilitate strategic dialogue with Moldova and submit a report on support for Moldova, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:46Z"
    }
  ]
}
```
