# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3206?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3206
- Title: Protecting America's Property Rights Act
- Congress: 119
- Bill type: HR
- Bill number: 3206
- Origin chamber: House
- Introduced date: 2025-05-06
- Update date: 2026-05-20T08:08:25Z
- Update date including text: 2026-05-20T08:08:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-06: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-05-06: Introduced in House

## Actions

- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3206",
    "number": "3206",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Protecting America's Property Rights Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:25Z",
    "updateDateIncludingText": "2026-05-20T08:08:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T14:02:10Z",
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
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "TX"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "FL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "DE"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "OH"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "TX"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "MO"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "KY"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "KS"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "R000610",
      "district": "14",
      "firstName": "Guy",
      "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Reschenthaler",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "PA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NY"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "SD"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3206ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3206\nIN THE HOUSE OF REPRESENTATIVES\nMay 6, 2025 Mr. Garbarino (for himself and Mr. Vicente Gonzalez of Texas ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo provide additional requirements for the purchase and sale of conventional mortgages by the enterprises, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting America's Property Rights Act .\n#### 2. Ensuring safe and sound lien and title protection products\n##### (a) Prudential management\nSection 1108(a) of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4513b(a) ) is amended by inserting at the end the following:\n(12) management of risk related to loss or damage suffered by reason of liens, encumbrances upon, or defects in the title to such property, or the invalidity or unenforceability of any liens or encumbrances thereon by utilizing third party products subject to regulation by\u2014 (A) a State insurance authority as defined in 15 section 6809(11) of title 15, United States Code; or (B) a State regulator as defined in section 5481(22) of title 12, United States Code. .\n##### (b) Capital Standards\nIn establishing minimum capital level pursuant to section 4612 of title 12, United States Code, the Director shall require the Enterprises to hold an additional 1.00 percent of the unpaid principal balance of any mortgage purchased by the Enterprises that does not meet the requirements of subsection (a).\n##### (c) Implementation and Compliance\nThe Director shall, not later than 180 days after the date of enactment of this section, issue such regulations and guidance as necessary to ensure compliance with subsection (a), including requiring the Enterprises to verify that any product meeting the definition in subsection (a) is appropriately regulated.\n##### (d) Definitions\nFor purposes of this section\u2014\n**(1)**\nthe term Enterprises shall have the same meaning as in section 4502(10) of title 12, United States Code; and\n**(2)**\nthe term Director shall have the same meaning as in section 4052(9) of title 12, United States Code.",
      "versionDate": "2025-05-06",
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
        "updateDate": "2025-05-21T12:04:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-06",
    "originChamber": "House",
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
          "measure-id": "id119hr3206",
          "measure-number": "3206",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-06",
          "originChamber": "HOUSE",
          "update-date": "2026-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3206v00",
            "update-date": "2026-04-16"
          },
          "action-date": "2025-05-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting America's Property Rights Act</strong></p><p>This bill directs the government-sponsored enterprises\u2014Fannie Mae and Freddie Mac\u2014to establish standards for the use of products such as title insurance. (The enterprises facilitate liquidity in the mortgage market by purchasing mortgages and issuing mortgage-backed securities.)</p><p>Specifically, the enterprises must establish regulations or guidelines for risk management related to loss or damage from liens upon, encumbrances on, or defects in the title to property, or the invalidity or\u00a0unenforceability of any liens or encumbrances on property by using third party products subject to state regulation.</p><p>Further, the enterprises must hold an additional 1% of the unpaid principal of any mortgage that does not meet the above regulations or guidelines as part of each enterprise\u2019s minimum capital levels.</p>"
        },
        "title": "Protecting America's Property Rights Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3206.xml",
    "summary": {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting America's Property Rights Act</strong></p><p>This bill directs the government-sponsored enterprises\u2014Fannie Mae and Freddie Mac\u2014to establish standards for the use of products such as title insurance. (The enterprises facilitate liquidity in the mortgage market by purchasing mortgages and issuing mortgage-backed securities.)</p><p>Specifically, the enterprises must establish regulations or guidelines for risk management related to loss or damage from liens upon, encumbrances on, or defects in the title to property, or the invalidity or\u00a0unenforceability of any liens or encumbrances on property by using third party products subject to state regulation.</p><p>Further, the enterprises must hold an additional 1% of the unpaid principal of any mortgage that does not meet the above regulations or guidelines as part of each enterprise\u2019s minimum capital levels.</p>",
      "updateDate": "2026-04-16",
      "versionCode": "id119hr3206"
    },
    "title": "Protecting America's Property Rights Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting America's Property Rights Act</strong></p><p>This bill directs the government-sponsored enterprises\u2014Fannie Mae and Freddie Mac\u2014to establish standards for the use of products such as title insurance. (The enterprises facilitate liquidity in the mortgage market by purchasing mortgages and issuing mortgage-backed securities.)</p><p>Specifically, the enterprises must establish regulations or guidelines for risk management related to loss or damage from liens upon, encumbrances on, or defects in the title to property, or the invalidity or\u00a0unenforceability of any liens or encumbrances on property by using third party products subject to state regulation.</p><p>Further, the enterprises must hold an additional 1% of the unpaid principal of any mortgage that does not meet the above regulations or guidelines as part of each enterprise\u2019s minimum capital levels.</p>",
      "updateDate": "2026-04-16",
      "versionCode": "id119hr3206"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3206ih.xml"
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
      "title": "Protecting America's Property Rights Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:08Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting America's Property Rights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide additional requirements for the purchase and sale of conventional mortgages by the enterprises, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:48:37Z"
    }
  ]
}
```
