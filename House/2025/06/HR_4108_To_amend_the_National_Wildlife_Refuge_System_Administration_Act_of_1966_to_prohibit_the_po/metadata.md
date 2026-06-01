# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4108
- Title: Refuge From Cruel Trapping Act
- Congress: 119
- Bill type: HR
- Bill number: 4108
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2025-08-30T08:05:25Z
- Update date including text: 2025-08-30T08:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4108",
    "number": "4108",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "N000002",
        "district": "12",
        "firstName": "Jerrold",
        "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
        "lastName": "Nadler",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Refuge From Cruel Trapping Act",
    "type": "HR",
    "updateDate": "2025-08-30T08:05:25Z",
    "updateDateIncludingText": "2025-08-30T08:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:00:45Z",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "TN"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "WA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "DC"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "VA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "GA"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MD"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "IN"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4108ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4108\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mr. Nadler (for himself, Ms. Barrag\u00e1n , Mr. Cohen , Ms. DelBene , Mr. Krishnamoorthi , Ms. Meng , Ms. Norton , Mr. Beyer , Mr. Huffman , and Mr. Casten ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the National Wildlife Refuge System Administration Act of 1966 to prohibit the possession or use of body-gripping traps in the National Wildlife Refuge System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Refuge From Cruel Trapping Act .\n#### 2. Possession or use of body-gripping trap prohibited\n##### (a) In general\nThe National Wildlife Refuge System Administration Act of 1966 ( 16 U.S.C. 668dd et seq. ) is amended\u2014\n**(1)**\nin section 4(f), by striking this Act each place it appears and inserting this section ; and\n**(2)**\nby inserting after section 4 the following:\n4A. Possession or use of body-gripping trap prohibited (a) In general Except as provided in subsection (b), a person may not possess or use a body-gripping trap in the System. (b) Exceptions (1) Federal agency Subsection (a) does not apply to the possession or use of a body-gripping trap by a Federal agency\u2014 (A) to\u2014 (i) control an invasive species to achieve resource management objectives; or (ii) protect a species that\u2014 (I) is listed as threatened or endangered under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ); or (II) the Secretary has designated as a sensitive species; and (B) if\u2014 (i) such use is in accordance with Federal and State law; and (ii) all other viable nonlethal methods for achieving a goal described in subparagraph (A) have been thoroughly explored, described, and attempted and documentation of such activities is maintained at the relevant headquarters of the Federal agency that carried out such exploration, description, and attempt. (2) Dismantling Subsection (a) does not apply to the dismantling of body-gripping traps. (3) Alaska Subsection (a) does not apply to the System in Alaska. (4) Members of Indian Tribes Subsection (a) does not apply to the possession or use of a body-gripping trap by a member of a federally recognized Indian Tribe for subsistence purposes. (c) Penalties (1) In general A person who violates subsection (a) shall be subject to\u2014 (A) a civil fine of not more than $500 for\u2014 (i) each body-gripping trap possessed; and (ii) each use of a body-gripping trap; (B) imprisonment for not more than 180 days; or (C) both a civil fine and imprisonment in accordance with subparagraphs (A) and (B). (2) Adjustment for inflation The Secretary shall annually adjust the fine described in paragraph (1) to reflect the change in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor. (d) Forfeiture Any body-gripping trap that is possessed or used in violation of this section, and any wildlife captured through the use of such body-gripping trap, including a pelt or raw fur of such wildlife, shall be subject to forfeiture to the United States in accordance with the provisions of chapter 46 of title 18, United States Code, relating to civil forfeitures. (e) Payment of associated court costs A person found to be in violation of subsection (a) shall pay all associated court costs. (f) Definitions In this section: (1) Body-Gripping trap The term body-gripping trap \u2014 (A) means any device that is intended to kill or capture wildlife by physically restraining any part of the animal; (B) includes any\u2014 (i) steel-jaw, padded, or other modified leghold trap; (ii) kill-type trap; (iii) snare trap; or (iv) modified version of any trap described in clauses (i) through (iii); and (C) does not include any\u2014 (i) cage or box trap; or (ii) suitcase-type live beaver trap. (2) Invasive species The term invasive species means, with regard to a particular ecosystem, a non-native organism the introduction of which causes or is likely to cause economic or environmental harm, or harm to human, animal, or plant health. .\n##### (b) Regulations\n**(1) In general**\nNot later than 120 days after the date of the enactment of this section, the Secretary of the Interior shall issue any regulations necessary to carry out the amendments made by subsection (a).\n**(2) Enforceability**\nThe enforceability of the amendments made by subsection (a) shall not be affected by a failure of the Secretary of the Interior to issue regulations under paragraph (1).\n##### (c) Effective date\nThe amendments made by subsection (a) shall take effect on the date that is 120 days after the date of the enactment of this section.",
      "versionDate": "2025-06-24",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-24T21:52:23Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4108ih.xml"
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
      "title": "Refuge From Cruel Trapping Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Refuge From Cruel Trapping Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Wildlife Refuge System Administration Act of 1966 to prohibit the possession or use of body-gripping traps in the National Wildlife Refuge System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:22Z"
    }
  ]
}
```
