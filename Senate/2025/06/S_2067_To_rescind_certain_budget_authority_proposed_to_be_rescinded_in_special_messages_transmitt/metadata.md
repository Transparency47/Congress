# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2067?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2067
- Title: Rescissions Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2067
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-09-03T11:03:20Z
- Update date including text: 2025-09-03T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred jointly to the Committees on Appropriations; the Budget pursuant to the order of 1/30/1975 as amended by the order of 4/11/1986.
- 2025-09-02 - Floor: Star Print ordered on the bill.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred jointly to the Committees on Appropriations; the Budget pursuant to the order of 1/30/1975 as amended by the order of 4/11/1986.
- 2025-09-02 - Floor: Star Print ordered on the bill.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2067",
    "number": "2067",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Rescissions Act of 2025",
    "type": "S",
    "updateDate": "2025-09-03T11:03:20Z",
    "updateDateIncludingText": "2025-09-03T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the bill.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": [
          {
            "name": "Appropriations Committee",
            "systemCode": "ssap00"
          },
          {
            "name": "Budget Committee",
            "systemCode": "ssbu00"
          }
        ]
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred jointly to the Committees on Appropriations; the Budget pursuant to the order of 1/30/1975 as amended by the order of 4/11/1986.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-06-12T18:45:31Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Budget Committee",
      "systemCode": "ssbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-12T18:45:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
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
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "KY"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TN"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "WY"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "AL"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "IA"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2067is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2067\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Schmitt introduced the following bill; which was read twice and referred jointly pursuant to the order of January 30, 1975, as amended by the order of April 11, 1986 to the Committee on Appropriations and the Budget\nA BILL\nTo rescind certain budget authority proposed to be rescinded in special messages transmitted to the Congress by the President on June 3, 2025, in accordance with section 1012(a) of the Congressional Budget and Impoundment Control Act of 1974.\n#### 1. Short Title\nThis Act may be cited as the Rescissions Act of 2025 .\n#### 2. Rescissions of budget authority\n##### (a) In general\nPursuant to the special message transmitted by the President on June 3, 2025, to the House of Representatives and the Senate proposing the rescission of budget authority under section 1012 of part B of title X of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 682 et seq. ), the rescissions described under subsection (b) shall take effect immediately upon the date of enactment of this Act.\n##### (b) Rescissions\nThe rescissions described in this subsection are as follows:\n**(1)**\nOf the unobligated balances under the heading International Organizations\u2014Contributions to International Organizations made available by the Department of State, Foreign Operations, and Related Programs Appropriations Act, 2024 (division F of Public Law 118\u201347 ), $33,008,764 are rescinded.\n**(2)**\nOf the unobligated balances under the heading International Organizations\u2014Contributions to International Organizations made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $168,837,230 are rescinded.\n**(3)**\nOf the unobligated balances under the heading International Organizations\u2014Contributions for International Peacekeeping Activities made available by the Department of State, Foreign Operations, and Related Programs Appropriations Act, 2024 (division F of Public Law 118\u201347 ), $203,328,007 are rescinded.\n**(4)**\nOf the unobligated balances under the heading International Organizations\u2014Contributions for International Peacekeeping Activities made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $157,906,000 are rescinded.\n**(5)**\nOf the unobligated balances in the first paragraph under the heading Bilateral Economic Assistance\u2014Funds Appropriated to the President\u2014Global Health Programs made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $500,000,000 are rescinded.\n**(6)**\nOf the unobligated balances in the second paragraph under the heading Bilateral Economic Assistance\u2014Funds Appropriated to the President\u2014Global Health Programs made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $400,000,000 are rescinded.\n**(7)**\nOf the unobligated balances under the heading Department of State\u2014Migration and Refugee Assistance made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $800,000,000 are permanently rescinded.\n**(8)**\nOf the unobligated balances under the heading Bilateral Economic Assistance\u2014Funds Appropriated to the President\u2014Complex Crises Fund made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $43,000,000 are rescinded.\n**(9)**\nOf the unobligated balances under the heading Bilateral Economic Assistance\u2014Funds Appropriated to the President\u2014Democracy Fund made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $83,000,000 are rescinded.\n**(10)**\nOf the unobligated balances under the heading Bilateral Economic Assistance\u2014Funds Appropriated to the President\u2014Economic Support Fund made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $1,650,000,000 are rescinded.\n**(11)**\nOf the unobligated balances under the heading Multilateral Assistance\u2014International Financial Institutions\u2014Contribution to the Clean Technology Fund made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $125,000,000 are rescinded.\n**(12)**\nOf the unobligated balances under the heading Multilateral Assistance\u2014Funds Appropriated to the President\u2014International Organizations and Programs made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $436,920,000 are rescinded.\n**(13)**\nOf the unobligated balances under the heading Bilateral Economic Assistance\u2014Funds Appropriated to the President\u2014Development Assistance made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $2,500,000,000 are rescinded.\n**(14)**\nOf the unobligated balances under the heading Bilateral Economic Assistance\u2014Funds Appropriated to the President\u2014Assistance for Europe, Eurasia and Central Asia made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $460,000,000 are rescinded.\n**(15)**\nOf the unobligated balances under the heading Bilateral Economic Assistance\u2014Funds Appropriated to the President\u2014International Disaster Assistance made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $496,000,000 are rescinded.\n**(16)**\nOf the unobligated balances under the heading United States Agency for International Development\u2014Funds Appropriated to the President\u2014Operating Expenses made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $125,000,000 are rescinded.\n**(17)**\nOf the unobligated balances under the heading Bilateral Economic Assistance\u2014Funds Appropriated to the President\u2014Transition Initiatives made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $57,000,000 are rescinded.\n**(18)**\nOf the unobligated balances under the heading Bilateral Economic Assistance\u2014Independent Agencies\u2014Inter-American Foundation made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $27,000,000 are rescinded.\n**(19)**\nOf the unobligated balances under the heading Bilateral Economic Assistance\u2014Independent Agencies\u2014United States African Development Foundation made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $22,000,000 are rescinded.\n**(20)**\nOf the unobligated balances under the heading Related Programs\u2014United States Institute of Peace made available by the Full-Year Continuing Appropriations Act, 2025 (division A of Public Law 119\u20134 ), $15,000,000 are rescinded.\n**(21)**\n**(A)**\nAmounts made available for Corporation for Public Broadcasting for fiscal year 2026 by Public Law 118\u201347 are rescinded.\n**(B)**\nAmounts made available for Corporation for Public Broadcasting for fiscal year 2027 by Public Law 119\u20134 are rescinded.",
      "versionDate": "2025-06-12",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-24",
        "text": "Became Public Law No: 119-28."
      },
      "number": "4",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rescissions Act of 2025",
      "type": "HR"
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-07-17T20:38:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s2067",
          "measure-number": "2067",
          "measure-type": "s",
          "orig-publish-date": "2025-06-12",
          "originChamber": "SENATE",
          "update-date": "2025-07-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2067v00",
            "update-date": "2025-07-28"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Rescissions Act of 2025</strong></p><p>This bill rescinds specified unobligated funds that were provided to the Department of State, the U.S. Agency for International Development (USAID), various independent and related agencies, and the Corporation for Public Broadcasting.\u00a0</p><p>The rescissions were proposed by the President under procedures included in the Congressional Budget and Impoundment Control Act of 1974. Under current law, the President may propose rescissions to Congress using specified procedures, and the rescissions must be enacted into law to take effect.\u00a0</p><p>Specifically, the bill rescinds funds that were provided to the State Department or the President for</p><ul><li>Contributions to International Organizations;</li><li>Contributions for International Peacekeeping Activities;</li><li>Global Health Programs;</li><li>Migration and Refugee Assistance;</li><li>the Complex Crises Fund;</li><li>the Democracy Fund;</li><li>the Economic Support Fund;</li><li>Contributions to the Clean Technology Fund;</li><li>International Organization and Programs;</li><li>Development Assistance;</li><li>Assistance for Europe, Eurasia, and Central Asia;</li><li>International Disaster Assistance; and</li><li>Transition Initiatives.</li></ul><p>The bill also rescinds funds that were provided for\u00a0</p><ul><li>USAID Operating Expenses,</li><li>the Inter-American Foundation,</li><li>the\u00a0U.S. African Development Foundation,</li><li>the U.S. Institute of Peace, and</li><li>the Corporation for Public Broadcasting.</li></ul>"
        },
        "title": "Rescissions Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2067.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rescissions Act of 2025</strong></p><p>This bill rescinds specified unobligated funds that were provided to the Department of State, the U.S. Agency for International Development (USAID), various independent and related agencies, and the Corporation for Public Broadcasting.\u00a0</p><p>The rescissions were proposed by the President under procedures included in the Congressional Budget and Impoundment Control Act of 1974. Under current law, the President may propose rescissions to Congress using specified procedures, and the rescissions must be enacted into law to take effect.\u00a0</p><p>Specifically, the bill rescinds funds that were provided to the State Department or the President for</p><ul><li>Contributions to International Organizations;</li><li>Contributions for International Peacekeeping Activities;</li><li>Global Health Programs;</li><li>Migration and Refugee Assistance;</li><li>the Complex Crises Fund;</li><li>the Democracy Fund;</li><li>the Economic Support Fund;</li><li>Contributions to the Clean Technology Fund;</li><li>International Organization and Programs;</li><li>Development Assistance;</li><li>Assistance for Europe, Eurasia, and Central Asia;</li><li>International Disaster Assistance; and</li><li>Transition Initiatives.</li></ul><p>The bill also rescinds funds that were provided for\u00a0</p><ul><li>USAID Operating Expenses,</li><li>the Inter-American Foundation,</li><li>the\u00a0U.S. African Development Foundation,</li><li>the U.S. Institute of Peace, and</li><li>the Corporation for Public Broadcasting.</li></ul>",
      "updateDate": "2025-07-28",
      "versionCode": "id119s2067"
    },
    "title": "Rescissions Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rescissions Act of 2025</strong></p><p>This bill rescinds specified unobligated funds that were provided to the Department of State, the U.S. Agency for International Development (USAID), various independent and related agencies, and the Corporation for Public Broadcasting.\u00a0</p><p>The rescissions were proposed by the President under procedures included in the Congressional Budget and Impoundment Control Act of 1974. Under current law, the President may propose rescissions to Congress using specified procedures, and the rescissions must be enacted into law to take effect.\u00a0</p><p>Specifically, the bill rescinds funds that were provided to the State Department or the President for</p><ul><li>Contributions to International Organizations;</li><li>Contributions for International Peacekeeping Activities;</li><li>Global Health Programs;</li><li>Migration and Refugee Assistance;</li><li>the Complex Crises Fund;</li><li>the Democracy Fund;</li><li>the Economic Support Fund;</li><li>Contributions to the Clean Technology Fund;</li><li>International Organization and Programs;</li><li>Development Assistance;</li><li>Assistance for Europe, Eurasia, and Central Asia;</li><li>International Disaster Assistance; and</li><li>Transition Initiatives.</li></ul><p>The bill also rescinds funds that were provided for\u00a0</p><ul><li>USAID Operating Expenses,</li><li>the Inter-American Foundation,</li><li>the\u00a0U.S. African Development Foundation,</li><li>the U.S. Institute of Peace, and</li><li>the Corporation for Public Broadcasting.</li></ul>",
      "updateDate": "2025-07-28",
      "versionCode": "id119s2067"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2067is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Rescissions Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rescissions Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T06:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to rescind certain budget authority proposed to be rescinded in special messages transmitted to the Congress by the President on June 3, 2025, in accordance with section 1012(a) of the Congressional Budget and Impoundment Control Act of 1974.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:28Z"
    }
  ]
}
```
