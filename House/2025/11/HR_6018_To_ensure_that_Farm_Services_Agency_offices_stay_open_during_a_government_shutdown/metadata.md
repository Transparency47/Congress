# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6018?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6018
- Title: Bringing Assistance for Rural Needs During Shutdowns Act
- Congress: 119
- Bill type: HR
- Bill number: 6018
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-04-30T08:06:44Z
- Update date including text: 2026-04-30T08:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6018",
    "number": "6018",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "W000829",
        "district": "8",
        "firstName": "Tony",
        "fullName": "Rep. Wied, Tony [R-WI-8]",
        "lastName": "Wied",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Bringing Assistance for Rural Needs During Shutdowns Act",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:44Z",
    "updateDateIncludingText": "2026-04-30T08:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
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
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:03:20Z",
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
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "MI"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "KS"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "PA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "MS"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "NC"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "MD"
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
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6018ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6018\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mr. Wied (for himself, Mr. Bergman , Mr. Schmidt , Mr. Mackenzie , Mr. Guest , Mr. Harrigan , and Mrs. McClain Delaney ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo ensure that Farm Services Agency offices stay open during a government shutdown.\n#### 1. Short title\nThis Act may be cited as the Bringing Assistance for Rural Needs During Shutdowns Act .\n#### 2. Farm Services Agency to be regarded as providing essential services during a government shutdown\nAny services by an officer or employee of the Farm Services Agency shall be deemed, for purposes of section 1342 of title 31, United States Code, services for emergencies involving the safety of human life or the protection of property.",
      "versionDate": "2025-11-10",
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
        "updateDate": "2025-11-25T17:01:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-10",
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
          "measure-id": "id119hr6018",
          "measure-number": "6018",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6018v00",
            "update-date": "2026-04-28"
          },
          "action-date": "2025-11-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bringing Assistance for Rural Needs During Shutdowns Act</strong></p><p>This bill\u00a0requires Farm Service Agency (FSA) officers and employees to continue to work during a government shutdown.</p><p>As background, under an exception in the Antideficiency Act, an employee whose duties involve the safety of human life or the protection of property may be required to work during a government shutdown (i.e., lapse in appropriations).</p><p>Under this bill, any services by an FSA officer or employee are deemed to be for an emergency involving the safety of human life or the protection of property. Thus, if a lapse in FSA appropriations occurs, FSA officers and employees may be required to continue working.\u00a0</p>"
        },
        "title": "Bringing Assistance for Rural Needs During Shutdowns Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6018.xml",
    "summary": {
      "actionDate": "2025-11-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bringing Assistance for Rural Needs During Shutdowns Act</strong></p><p>This bill\u00a0requires Farm Service Agency (FSA) officers and employees to continue to work during a government shutdown.</p><p>As background, under an exception in the Antideficiency Act, an employee whose duties involve the safety of human life or the protection of property may be required to work during a government shutdown (i.e., lapse in appropriations).</p><p>Under this bill, any services by an FSA officer or employee are deemed to be for an emergency involving the safety of human life or the protection of property. Thus, if a lapse in FSA appropriations occurs, FSA officers and employees may be required to continue working.\u00a0</p>",
      "updateDate": "2026-04-28",
      "versionCode": "id119hr6018"
    },
    "title": "Bringing Assistance for Rural Needs During Shutdowns Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bringing Assistance for Rural Needs During Shutdowns Act</strong></p><p>This bill\u00a0requires Farm Service Agency (FSA) officers and employees to continue to work during a government shutdown.</p><p>As background, under an exception in the Antideficiency Act, an employee whose duties involve the safety of human life or the protection of property may be required to work during a government shutdown (i.e., lapse in appropriations).</p><p>Under this bill, any services by an FSA officer or employee are deemed to be for an emergency involving the safety of human life or the protection of property. Thus, if a lapse in FSA appropriations occurs, FSA officers and employees may be required to continue working.\u00a0</p>",
      "updateDate": "2026-04-28",
      "versionCode": "id119hr6018"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6018ih.xml"
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
      "title": "Bringing Assistance for Rural Needs During Shutdowns Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T08:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bringing Assistance for Rural Needs During Shutdowns Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T08:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that Farm Services Agency offices stay open during a government shutdown.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T08:33:23Z"
    }
  ]
}
```
