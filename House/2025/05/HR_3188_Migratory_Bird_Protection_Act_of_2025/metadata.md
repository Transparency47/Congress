# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3188?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3188
- Title: Migratory Bird Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3188
- Origin chamber: House
- Introduced date: 2025-05-05
- Update date: 2026-04-17T08:07:10Z
- Update date including text: 2026-04-17T08:07:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-05-05: Introduced in House

## Actions

- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3188",
    "number": "3188",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "H001068",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Huffman, Jared [D-CA-2]",
        "lastName": "Huffman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Migratory Bird Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:10Z",
    "updateDateIncludingText": "2026-04-17T08:07:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T16:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "PA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "ME"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "HI"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "VA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "DC"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3188ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3188\nIN THE HOUSE OF REPRESENTATIVES\nMay 5, 2025 Mr. Huffman (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Migratory Bird Treaty Act to affirm that the prohibition on the unauthorized take or killing of migratory birds of that Act includes incidental take, and to direct the United States Fish and Wildlife Service to authorize such incidental take, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Migratory Bird Protection Act of 2025 .\n#### 2. Amendments to the Migratory Bird Treaty Act\n##### (a) In general\nThe Migratory Bird Treaty Act ( 16 U.S.C. 703 et seq. ) is amended\u2014\n**(1)**\nby striking of Agriculture each place it appears;\n**(2)**\nby striking of the Interior each place it appears;\n**(3)**\nin section 5 ( 16 U.S.C. 706 ), as amended by paragraph (1) of this section, by inserting of the Interior after employee of the Department ;\n**(4)**\nin section 6 ( 16 U.S.C. 707 ), as amended by paragraph (1) of this section, by adding at the end the following:\n(e) Authorizing civil penalties for incidental take (1) In general A person who incidentally takes a migratory bird without an authorization issued pursuant to section 14 or in violation of the terms and conditions of an applicable permit or regulation issued by the Secretary to administer section 14 may be assessed a civil penalty by the Secretary of not more than $10,000 per violation, except that unpermitted incidental take which is caused by conduct that is reckless or grossly negligent shall be subject to the penalties of subsection (a). (2) Civil action The Secretary may commence a civil action for appropriate relief, including a permanent or temporary injunction, for any incidental take of a migratory bird without a permit or any violation of the terms and conditions of a permit issued or regulation promulgated pursuant to section 14. ; and\n**(5)**\nby adding at the end the following:\n14. Incidental take of migratory birds (a) In general It shall be a violation of this Act to incidentally take any migratory bird, and any part, nest, or egg of any such bird, except as authorized by the Secretary. The Secretary shall promulgate regulations to authorize the incidental take of migratory birds pursuant to this section, including issuing general permits. Before the Secretary promulgates regulations for an industry, the Secretary shall continue to enforce the document titled Director\u2019s Order No.: 225 (published October 5, 2021). No penalty shall be assessed unless such entity is given notice and opportunity for a hearing on the record in accordance with sections 554 and 556 of title 5, United States Code. In determining the amount of the penalty, the Secretary shall consider the gravity of the violation and the demonstrated good faith of the entity. For good cause shown, the Secretary, in an extraordinary case, may remit or mitigate any such penalty. (b) Authorization of fees The Secretary may collect fees pursuant to authorizing and administering the incidental take of migratory birds. The fees may be used to cover the administrative costs for the permit program and conserving populations of bird species\u2014 (1) affected by the authorized activities; or (2) identified as birds of conservation concern under authority of section 13 of the Fish and Wildlife Conservation Act of 1980 ( 16 U.S.C. 2912 ). (c) Deposit of fees There is established in the Treasury a separate account, which shall be known as the Migratory Bird Recovery Fund . The fund shall be managed by the Secretary and may consist of\u2014 (1) amounts received from fees pursuant to regulations under subsection (b); (2) amounts received pursuant to section 6(e); (3) amounts made available from appropriations; and (4) amounts received by the Secretary in the form of donations. (d) Authorization of appropriations There is authorized to be appropriated $10,000,000 for each fiscal year beginning after the date of the enactment of this section to carry out this section. (e) Report to Congress Not later than 5 years after the date of enactment of this section, and at the end of each 5 year period thereafter, the Secretary shall submit a report to the Chair and Ranking Member of the House Natural Resources Committee and to the Chair and Ranking Member of the Senate Environment and Public Works Committee on\u2014 (1) the conservation status of migratory birds; (2) the impacts upon migratory birds of activities for which authorizing regulations have been issued under this section; and (3) the Secretary\u2019s progress in carrying out the functions and responsibilities given to the Secretary under this section. (f) Research program The Secretary shall establish and maintain, through direct programming, contracts, or other form of agreement, and in consultation with research institutions, institutions of higher education, wildlife conservation groups, and representatives of authorized activities regulated under this section, a research program to\u2014 (1) better monitor the status of bird populations; (2) understand the stressors to bird populations; (3) identify opportunities to reduce the impact of such stressors; and (4) deploy and validate mitigation measures to conserve bird populations. 15. Definitions For the purposes of this Act: (1) Institution of higher education The term institution of higher education has the meaning given the term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ). (2) Secretary The term Secretary means the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service. .\n##### (b) Conforming amendment\nSection 7(b) of the North American Wetlands Conservation Act ( 16 U.S.C. 4406(b) ) is amended by inserting subsections (a) through (d) of before section 6 of the Migratory Bird Treaty Act .",
      "versionDate": "2025-05-05",
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
        "name": "Environmental Protection",
        "updateDate": "2025-05-21T13:40:16Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3188ih.xml"
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
      "title": "Migratory Bird Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Migratory Bird Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Migratory Bird Treaty Act to affirm that the prohibition on the unauthorized take or killing of migratory birds of that Act includes incidental take, and to direct the United States Fish and Wildlife Service to authorize such incidental take, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T09:03:53Z"
    }
  ]
}
```
