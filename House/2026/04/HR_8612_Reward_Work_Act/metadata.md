# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8612?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8612
- Title: Reward Work Act
- Congress: 119
- Bill type: HR
- Bill number: 8612
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-20T08:08:13Z
- Update date including text: 2026-05-20T08:08:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8612",
    "number": "8612",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000586",
        "district": "4",
        "firstName": "Jes\u00fas",
        "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
        "lastName": "Garc\u00eda",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Reward Work Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:13Z",
    "updateDateIncludingText": "2026-05-20T08:08:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:08:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "OR"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "WI"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "TX"
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
      "sponsorshipDate": "2026-05-11",
      "state": "DC"
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
      "sponsorshipDate": "2026-05-11",
      "state": "GA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "MN"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "AZ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8612ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8612\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Garc\u00eda of Illinois (for himself, Mr. Khanna , and Ms. Hoyle of Oregon ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo prohibit public companies from repurchasing their shares on the open market, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reward Work Act .\n#### 2. Prohibition on stock buybacks on the open market\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe terms equity security , exchange , and issuer have the meanings given the terms in section 3 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c ); and\n**(2)**\nthe term national securities exchange means an exchange registered under section 6 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78f ).\n##### (b) Prohibitions\nNotwithstanding any other provision of law, no issuer may purchase an equity security of the issuer on a national securities exchange.\n##### (c) No force or effect\nSection 240.10b\u201318 of title 17, Code of Federal Regulations, shall have no force or effect.\n##### (d) Rule of construction\nNothing in this section may be construed to affect tender offers subject to section 240.13e\u20134 and sections 240.14e\u20131 through 240.14f\u20131 of title 17, Code of Federal Regulations.\n#### 3. Worker representation on corporate board of directors\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term director has the meaning given the term in section 3 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c ); and\n**(2)**\nthe term employee \u2014\n**(A)**\nhas the meaning given the term in section 2 of the National Labor Relations Act ( 29 U.S.C. 152 ); and\n**(B)**\nincludes any individual employed by an employer subject to the Railway Labor Act ( 45 U.S.C. 151 et seq. ).\n##### (b) Registration requirements for securities\nSection 12 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78l ) is amended by adding at the end the following:\n(m) No issuer may register securities on a national exchange unless at least 1/3 of the issuer\u2019s directors are chosen by the issuing company\u2019s employees in a one-employee-one-vote election process. .\n##### (c) Policy\nThe Securities and Exchange Commission, in consultation with the National Labor Relations Board, shall promulgate regulations\u2014\n**(1)**\nto ensure that director elections at issuing firms are fair and democratic; and\n**(2)**\nto ensure that 1/3 of an issuer\u2019s board of directors will be composed of employee representatives within 2 years of the date of enactment of this Act.\n#### 4. Regulations\nThe Securities and Exchange Commission shall promulgate regulations to direct national securities exchanges and issuers, as defined in section 2(a), to comply with this Act and the amendments made by this Act.",
      "versionDate": "2026-04-30",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-05-19T20:18:48Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8612ih.xml"
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
      "title": "Reward Work Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reward Work Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit public companies from repurchasing their shares on the open market, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:40Z"
    }
  ]
}
```
