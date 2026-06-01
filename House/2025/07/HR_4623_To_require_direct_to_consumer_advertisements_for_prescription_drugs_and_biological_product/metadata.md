# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4623?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4623
- Title: Plain Prescription Prices Act
- Congress: 119
- Bill type: HR
- Bill number: 4623
- Origin chamber: House
- Introduced date: 2025-07-22
- Update date: 2025-12-02T16:39:20Z
- Update date including text: 2025-12-02T16:39:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-22: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-22: Introduced in House

## Actions

- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4623",
    "number": "4623",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Plain Prescription Prices Act",
    "type": "HR",
    "updateDate": "2025-12-02T16:39:20Z",
    "updateDateIncludingText": "2025-12-02T16:39:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-22",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T14:05:45Z",
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
          "date": "2025-07-22T14:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "NE"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "MN"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "WI"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4623ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4623\nIN THE HOUSE OF REPRESENTATIVES\nJuly 22, 2025 Ms. Williams of Georgia (for herself, Mr. Bacon , Ms. Craig , and Mr. Steil ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require direct-to-consumer advertisements for prescription drugs and biological products to include truthful and not misleading pricing information.\n#### 1. Short title\nThis Act may be cited as the Plain Prescription Prices Act .\n#### 2. Regulating advertisements for prescription drug and biological product prices\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Health and Human Services, acting through the Administrator of the Centers for Medicare & Medicaid Services (referred to in this section as the Administrator ), shall promulgate regulations requiring each direct-to-consumer advertisement on television (including broadcast, cable, streaming, and satellite television) for a prescription drug or biological product for which payment is available under title XVIII or XIX of the Social Security Act to include a textual statement, which shall be truthful and not misleading, indicating the list price, as determined on the first day of the quarter during which the advertisement is being aired or otherwise broadcast, for a typical 30-day regimen or typical course of treatment (whichever is most appropriate).\n##### (b) Determinations\nIn promulgating regulations under subsection (a), the Administrator shall determine\u2014\n**(1)**\nwhether such regulations should apply with respect to additional forms of advertising;\n**(2)**\nthe manner and format of textual statements described in such subsection;\n**(3)**\nappropriate enforcement mechanisms; and\n**(4)**\nwhether such textual statements should include any other price information, as appropriate.",
      "versionDate": "2025-07-22",
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
        "name": "Health",
        "updateDate": "2025-09-11T17:10:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-22",
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
          "measure-id": "id119hr4623",
          "measure-number": "4623",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-22",
          "originChamber": "HOUSE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4623v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-07-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Plain Prescription Prices Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to issue a rule requiring direct-to-consumer television advertisements for prescription drugs that are covered by Medicare or Medicaid to include a textual statement of the drug's list price.</p>"
        },
        "title": "Plain Prescription Prices Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4623.xml",
    "summary": {
      "actionDate": "2025-07-22",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Plain Prescription Prices Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to issue a rule requiring direct-to-consumer television advertisements for prescription drugs that are covered by Medicare or Medicaid to include a textual statement of the drug's list price.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4623"
    },
    "title": "Plain Prescription Prices Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-22",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Plain Prescription Prices Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to issue a rule requiring direct-to-consumer television advertisements for prescription drugs that are covered by Medicare or Medicaid to include a textual statement of the drug's list price.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4623"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4623ih.xml"
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
      "title": "Plain Prescription Prices Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Plain Prescription Prices Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require direct-to-consumer advertisements for prescription drugs and biological products to include truthful and not misleading pricing information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:28Z"
    }
  ]
}
```
