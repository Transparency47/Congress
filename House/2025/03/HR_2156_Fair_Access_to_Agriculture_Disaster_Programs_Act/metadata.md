# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2156?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2156
- Title: Fair Access to Agriculture Disaster Programs Act
- Congress: 119
- Bill type: HR
- Bill number: 2156
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-04-03T08:05:34Z
- Update date including text: 2026-04-03T08:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2156",
    "number": "2156",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Fair Access to Agriculture Disaster Programs Act",
    "type": "HR",
    "updateDate": "2026-04-03T08:05:34Z",
    "updateDateIncludingText": "2026-04-03T08:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:07:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T13:13:50Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "FL"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "GA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "NC"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "NC"
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
      "sponsorshipDate": "2025-03-21",
      "state": "PA"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "FL"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "WA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2156ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2156\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Panetta (for himself, Mrs. Cammack , Ms. Lofgren , and Mr. Austin Scott of Georgia ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to establish an exception to certain payment limitations in the case of person or legal entity that derives income from agriculture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Access to Agriculture Disaster Programs Act .\n#### 2. Exception for income derived from agriculture\nSection 1001D(b) of the Food Security Act of 1985 (7 U.S.C. 1308\u20133a(b)) is amended\u2014\n**(1)**\nin paragraph (1), by striking paragraph (3) and inserting paragraphs (3) and (4) ; and\n**(2)**\nby adding at the end the following:\n(4) Exception (A) In general In the case of an excepted payment or benefit, the limitation established by paragraph (1) shall not apply to a person or legal entity during a crop, fiscal, or program year, as appropriate, if greater than or equal to 75 percent of the average adjusted gross income of the person or legal entity is derived from farming, ranching, or silviculture activities (including agri-tourism, direct-to-consumer marketing of agricultural products, the sale of agricultural equipment owned by such person or entity, and other agricultural related activities, as determined by the Secretary). (B) Excepted payment or benefit For purposes of this paragraph, the term excepted payment or benefit means\u2014 (i) a payment or benefit under subtitle E of title I of the Agricultural Act of 2014 ( 7 U.S.C. 9081 et seq. ); and (ii) a payment or benefit under section 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ). .",
      "versionDate": "2025-03-14",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-05T21:06:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2156",
          "measure-number": "2156",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2156v00",
            "update-date": "2025-05-15"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fair Access to Agriculture Disaster Programs Act</strong></p><p>This bill waives the adjusted gross income limitations for payments or benefits under specific Department of Agriculture (USDA) disaster assistance programs for a person or legal entity that derives a portion of their income from agriculture. Currently, a person or entity is not eligible to receive certain benefits during a crop, fiscal, or program year if their average gross income exceeds $900,000.</p><p>Specifically, in the case of an excepted payment or benefit, the adjusted gross income limitation is waived if 75% or more of the average adjusted gross income for the person or entity is derived from farming, ranching, or silviculture activities. These activities include agritourism, direct-to-consumer marketing of agricultural products, and the sale of agricultural equipment owned by such person or entity.</p><p>The bill applies to the USDA</p><ul><li>Livestock Indemnity Program;</li><li>Livestock Forage Disaster Program;</li><li>Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program;</li><li>Tree Assistance Program; and</li><li>Noninsured Crop Disaster Assistance Program.</li></ul>"
        },
        "title": "Fair Access to Agriculture Disaster Programs Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2156.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Access to Agriculture Disaster Programs Act</strong></p><p>This bill waives the adjusted gross income limitations for payments or benefits under specific Department of Agriculture (USDA) disaster assistance programs for a person or legal entity that derives a portion of their income from agriculture. Currently, a person or entity is not eligible to receive certain benefits during a crop, fiscal, or program year if their average gross income exceeds $900,000.</p><p>Specifically, in the case of an excepted payment or benefit, the adjusted gross income limitation is waived if 75% or more of the average adjusted gross income for the person or entity is derived from farming, ranching, or silviculture activities. These activities include agritourism, direct-to-consumer marketing of agricultural products, and the sale of agricultural equipment owned by such person or entity.</p><p>The bill applies to the USDA</p><ul><li>Livestock Indemnity Program;</li><li>Livestock Forage Disaster Program;</li><li>Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program;</li><li>Tree Assistance Program; and</li><li>Noninsured Crop Disaster Assistance Program.</li></ul>",
      "updateDate": "2025-05-15",
      "versionCode": "id119hr2156"
    },
    "title": "Fair Access to Agriculture Disaster Programs Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Access to Agriculture Disaster Programs Act</strong></p><p>This bill waives the adjusted gross income limitations for payments or benefits under specific Department of Agriculture (USDA) disaster assistance programs for a person or legal entity that derives a portion of their income from agriculture. Currently, a person or entity is not eligible to receive certain benefits during a crop, fiscal, or program year if their average gross income exceeds $900,000.</p><p>Specifically, in the case of an excepted payment or benefit, the adjusted gross income limitation is waived if 75% or more of the average adjusted gross income for the person or entity is derived from farming, ranching, or silviculture activities. These activities include agritourism, direct-to-consumer marketing of agricultural products, and the sale of agricultural equipment owned by such person or entity.</p><p>The bill applies to the USDA</p><ul><li>Livestock Indemnity Program;</li><li>Livestock Forage Disaster Program;</li><li>Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program;</li><li>Tree Assistance Program; and</li><li>Noninsured Crop Disaster Assistance Program.</li></ul>",
      "updateDate": "2025-05-15",
      "versionCode": "id119hr2156"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2156ih.xml"
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
      "title": "Fair Access to Agriculture Disaster Programs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Access to Agriculture Disaster Programs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to establish an exception to certain payment limitations in the case of person or legal entity that derives income from agriculture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:33:41Z"
    }
  ]
}
```
