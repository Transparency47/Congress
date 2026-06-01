# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3038?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3038
- Title: SAFE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3038
- Origin chamber: House
- Introduced date: 2025-04-28
- Update date: 2026-04-07T08:05:28Z
- Update date including text: 2026-04-07T08:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-28: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-28 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-28: Introduced in House

## Actions

- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-28 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3038",
    "number": "3038",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "SAFE Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:28Z",
    "updateDateIncludingText": "2026-04-07T08:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-28",
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
          "date": "2025-04-28T16:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-28T16:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3038ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3038\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2025 Mr. Feenstra (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Animal Health Protection Act to improve the prevention of the spread of animal diseases, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe American Food Exports Act of 2025 or the SAFE Act of 2025 .\n#### 2. Engagement with key export markets\n##### (a) In general\nSection 10405 of the Animal Health Protection Act ( 7 U.S.C. 8304 ) is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Engagement with key export markets (1) In general To reduce the impact of animal disease outbreaks on United States exports, the Secretary, acting through the Administrator of the Animal and Plant Health Inspection Service, the Under Secretary of Agriculture for Trade and Foreign Agricultural Affairs, and the Administrator of the Food Safety and Inspection Service, in consultation with the United States Trade Representative, is authorized to negotiate in advance, to the extent practicable, regionalization, zoning, compartmentalization, and other agreements regarding outbreaks of known animal disease threats of trade significance with the governments of countries with export markets for livestock animals or animal products from the United States. (2) Research A negotiation carried out under paragraph (1) should seek to take into account accepted global research advances. .\n##### (b) Rule of construction\nNothing in this section shall be construed\u2014\n**(1)**\nto limit the ability of the United States Trade Representative to negotiate trade agreements; or\n**(2)**\nto require the United States Trade Representative to condition other trade agreements on the inclusion of language relating to reducing the impact of animal disease outbreaks on United States exports, as described in subsection (d)(1) of section 10405 of the Animal Health Protection Act ( 7 U.S.C. 3804 ) (as inserted by subsection (a)(2)).",
      "versionDate": "2025-04-28",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-04-28",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1501",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAFE Act of 2025",
      "type": "S"
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
        "updateDate": "2025-05-29T17:54:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-28",
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
          "measure-id": "id119hr3038",
          "measure-number": "3038",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-28",
          "originChamber": "HOUSE",
          "update-date": "2025-08-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3038v00",
            "update-date": "2025-08-13"
          },
          "action-date": "2025-04-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Safe American Food Exports Act of\u00a02025 or the SAFE Act of 2025</strong></p><p>This bill provides statutory authority for the Department of Agriculture to negotiate in advance for regional export ban agreements\u00a0for known animal disease threats that apply only to areas affected by animal disease outbreaks to enable the continuation of exports from areas not affected by an outbreak.</p><p>The Animal and Plant Health Inspection Service, the Food Safety and Inspection Service, and the Foreign Agricultural Service, in consultation with the Office of the U.S. Trade Representative, may negotiate the regionalization, zoning, compartmentalization, and other agreements regarding outbreaks of known animal disease threats of trade significance with countries with export markets for livestock animals or animal products from the United States.</p><p>The bill also specifies that such a negotiation should seek to take into account accepted global research advances.</p>"
        },
        "title": "SAFE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3038.xml",
    "summary": {
      "actionDate": "2025-04-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safe American Food Exports Act of\u00a02025 or the SAFE Act of 2025</strong></p><p>This bill provides statutory authority for the Department of Agriculture to negotiate in advance for regional export ban agreements\u00a0for known animal disease threats that apply only to areas affected by animal disease outbreaks to enable the continuation of exports from areas not affected by an outbreak.</p><p>The Animal and Plant Health Inspection Service, the Food Safety and Inspection Service, and the Foreign Agricultural Service, in consultation with the Office of the U.S. Trade Representative, may negotiate the regionalization, zoning, compartmentalization, and other agreements regarding outbreaks of known animal disease threats of trade significance with countries with export markets for livestock animals or animal products from the United States.</p><p>The bill also specifies that such a negotiation should seek to take into account accepted global research advances.</p>",
      "updateDate": "2025-08-13",
      "versionCode": "id119hr3038"
    },
    "title": "SAFE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safe American Food Exports Act of\u00a02025 or the SAFE Act of 2025</strong></p><p>This bill provides statutory authority for the Department of Agriculture to negotiate in advance for regional export ban agreements\u00a0for known animal disease threats that apply only to areas affected by animal disease outbreaks to enable the continuation of exports from areas not affected by an outbreak.</p><p>The Animal and Plant Health Inspection Service, the Food Safety and Inspection Service, and the Foreign Agricultural Service, in consultation with the Office of the U.S. Trade Representative, may negotiate the regionalization, zoning, compartmentalization, and other agreements regarding outbreaks of known animal disease threats of trade significance with countries with export markets for livestock animals or animal products from the United States.</p><p>The bill also specifies that such a negotiation should seek to take into account accepted global research advances.</p>",
      "updateDate": "2025-08-13",
      "versionCode": "id119hr3038"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3038ih.xml"
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
      "title": "SAFE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe American Food Exports Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Animal Health Protection Act to improve the prevention of the spread of animal diseases, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:26Z"
    }
  ]
}
```
