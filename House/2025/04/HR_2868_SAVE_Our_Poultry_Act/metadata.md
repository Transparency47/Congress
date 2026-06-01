# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2868?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2868
- Title: SAVE Our Poultry Act
- Congress: 119
- Bill type: HR
- Bill number: 2868
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-01-17T04:41:13Z
- Update date including text: 2026-01-17T04:41:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2868",
    "number": "2868",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001238",
        "district": "",
        "firstName": "Sarah",
        "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
        "lastName": "McBride",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "SAVE Our Poultry Act",
    "type": "HR",
    "updateDate": "2026-01-17T04:41:13Z",
    "updateDateIncludingText": "2026-01-17T04:41:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:00:20Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-29",
      "state": "PA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2868ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2868\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Ms. McBride (for herself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 to add highly pathogenic avian influenza as a high priority research and extension area.\n#### 1. Short title\nThis Act may be cited as the Supporting Avian Virus Eradication Act or the SAVE Our Poultry Act .\n#### 2. Addition of highly pathogenic avian influenza as a high priority research and extension area\nSection 1672(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925(d) ) is amended by adding at the end the following:\n(21) Highly pathogenic avian influenza Research and extension grants may be made under this section to land-grant colleges and universities (as defined in section 1404 of National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 )) to study highly pathogenic avian influenza for the purposes of\u2014 (A) developing and improving the efficacy of vaccines for poultry, including with respect to\u2014 (i) researching the effectiveness of such vaccines across poultry species; (ii) improving formulations of such vaccines; (iii) improving the delivery mechanisms for such vaccines; and (iv) assessing the potential implications of vaccination on domestic and international poultry markets, including trade and market access considerations; and (B) enhancing biosecurity procedures for poultry producers, including with respect to\u2014 (i) evaluating training and biosecurity practices; (ii) improving farm-level interventions; and (iii) developing new disinfection methods. .",
      "versionDate": "2025-04-10",
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
        "updateDate": "2025-05-07T13:27:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2868",
          "measure-number": "2868",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2025-08-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2868v00",
            "update-date": "2025-08-26"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supporting Avian Virus Eradication Act or the SAVE Our Poultry Act</strong></p><p>This bill includes research on highly pathogenic avian influenza (HPAI) as a Department of Agriculture (USDA) high-priority research and extension area.</p><p>Under the bill, USDA may award grants to land-grant colleges and universities to study HPAI for the purposes of (1) developing and improving the efficacy of vaccines for poultry, and (2) enhancing biosecurity procedures for poultry producers.</p>"
        },
        "title": "SAVE Our Poultry Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2868.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Avian Virus Eradication Act or the SAVE Our Poultry Act</strong></p><p>This bill includes research on highly pathogenic avian influenza (HPAI) as a Department of Agriculture (USDA) high-priority research and extension area.</p><p>Under the bill, USDA may award grants to land-grant colleges and universities to study HPAI for the purposes of (1) developing and improving the efficacy of vaccines for poultry, and (2) enhancing biosecurity procedures for poultry producers.</p>",
      "updateDate": "2025-08-26",
      "versionCode": "id119hr2868"
    },
    "title": "SAVE Our Poultry Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Avian Virus Eradication Act or the SAVE Our Poultry Act</strong></p><p>This bill includes research on highly pathogenic avian influenza (HPAI) as a Department of Agriculture (USDA) high-priority research and extension area.</p><p>Under the bill, USDA may award grants to land-grant colleges and universities to study HPAI for the purposes of (1) developing and improving the efficacy of vaccines for poultry, and (2) enhancing biosecurity procedures for poultry producers.</p>",
      "updateDate": "2025-08-26",
      "versionCode": "id119hr2868"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2868ih.xml"
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
      "title": "SAVE Our Poultry Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAVE Our Poultry Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Avian Virus Eradication Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Agriculture, Conservation, and Trade Act of 1990 to add highly pathogenic avian influenza as a high priority research and extension area.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T04:18:26Z"
    }
  ]
}
```
