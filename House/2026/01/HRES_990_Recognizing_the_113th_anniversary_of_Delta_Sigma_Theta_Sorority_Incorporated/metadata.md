# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/990?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/990
- Title: Recognizing the 113th anniversary of Delta Sigma Theta Sorority, Incorporated.
- Congress: 119
- Bill type: HRES
- Bill number: 990
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-04-06T18:43:32Z
- Update date including text: 2026-04-06T18:43:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-13 - IntroReferral: Submitted in House
- 2026-01-13 - IntroReferral: Submitted in House
- Latest action: 2026-01-13: Submitted in House

## Actions

- 2026-01-13 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-13 - IntroReferral: Submitted in House
- 2026-01-13 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/990",
    "number": "990",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "L000602",
        "district": "12",
        "firstName": "Summer",
        "fullName": "Rep. Lee, Summer L. [D-PA-12]",
        "lastName": "Lee",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Recognizing the 113th anniversary of Delta Sigma Theta Sorority, Incorporated.",
    "type": "HRES",
    "updateDate": "2026-04-06T18:43:32Z",
    "updateDateIncludingText": "2026-04-06T18:43:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-01-13T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "OH"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "OH"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "IL"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "AL"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NC"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "IL"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "GA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "VA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MD"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "VI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres990ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 990\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Ms. Lee of Pennsylvania (for herself, Mrs. Beatty , Ms. Brown , Ms. Clarke of New York , Ms. Crockett , Mr. Davis of Illinois , Mr. Figures , Mrs. Foushee , Mr. Jackson of Illinois , Mr. Kennedy of New York , Mrs. McBath , Ms. McClellan , Mr. Mfume , and Ms. Plaskett ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nRecognizing the 113th anniversary of Delta Sigma Theta Sorority, Incorporated.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the 113th anniversary of the founding of Delta Sigma Theta Sorority, Incorporated; and\n**(2)**\napplauds and honors Delta Sigma Theta Sorority, Incorporated, and all its members for more than a century of fortitude and distinguished service to the people of the United States and the global community.",
      "versionDate": "2026-01-13",
      "versionType": "IH"
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
        "actionDate": "2025-01-13",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "35",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing the 112th Anniversary of Delta Sigma Theta Sorority, Incorporated.",
      "type": "HRES"
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
        "name": "Education",
        "updateDate": "2026-01-16T13:02:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-13",
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
          "measure-id": "id119hres990",
          "measure-number": "990",
          "measure-type": "hres",
          "orig-publish-date": "2026-01-13",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres990v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2026-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes the 113th anniversary of the founding of Delta Sigma Theta Sorority, Incorporated.</p>"
        },
        "title": "Recognizing the 113th anniversary of Delta Sigma Theta Sorority, Incorporated."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres990.xml",
    "summary": {
      "actionDate": "2026-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the 113th anniversary of the founding of Delta Sigma Theta Sorority, Incorporated.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres990"
    },
    "title": "Recognizing the 113th anniversary of Delta Sigma Theta Sorority, Incorporated."
  },
  "summaries": [
    {
      "actionDate": "2026-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the 113th anniversary of the founding of Delta Sigma Theta Sorority, Incorporated.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres990"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres990ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recognizing the 113th anniversary of Delta Sigma Theta Sorority, Incorporated.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-15T04:03:17Z"
    },
    {
      "title": "Recognizing the 113th anniversary of Delta Sigma Theta Sorority, Incorporated.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T09:06:38Z"
    }
  ]
}
```
