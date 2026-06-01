# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1071?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1071
- Title: Recognizing the desegregation efforts at Girard College in Philadelphia, and the leaders involved in African-American integration and civil rights expansion.
- Congress: 119
- Bill type: HRES
- Bill number: 1071
- Origin chamber: House
- Introduced date: 2026-02-23
- Update date: 2026-02-27T17:49:43Z
- Update date including text: 2026-02-27T17:49:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-23: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-02-23 - IntroReferral: Submitted in House
- 2026-02-23 - IntroReferral: Submitted in House
- Latest action: 2026-02-23: Submitted in House

## Actions

- 2026-02-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-02-23 - IntroReferral: Submitted in House
- 2026-02-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-23",
    "latestAction": {
      "actionDate": "2026-02-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1071",
    "number": "1071",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "E000296",
        "district": "3",
        "firstName": "Dwight",
        "fullName": "Rep. Evans, Dwight [D-PA-3]",
        "lastName": "Evans",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Recognizing the desegregation efforts at Girard College in Philadelphia, and the leaders involved in African-American integration and civil rights expansion.",
    "type": "HRES",
    "updateDate": "2026-02-27T17:49:43Z",
    "updateDateIncludingText": "2026-02-27T17:49:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-23",
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
          "date": "2026-02-23T17:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "IL"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "PA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "MO"
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
      "sponsorshipDate": "2026-02-23",
      "state": "DC"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "MD"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "GA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "OH"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1071ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1071\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 23, 2026 Mr. Evans of Pennsylvania (for himself, Mr. Davis of Illinois , Mr. Boyle of Pennsylvania , Mr. Cleaver , Ms. Norton , Mr. Ivey , Mr. Johnson of Georgia , Mrs. Beatty , and Mr. Thompson of Mississippi ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing the desegregation efforts at Girard College in Philadelphia, and the leaders involved in African-American integration and civil rights expansion.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the importance of the desegregation efforts at Girard College and the Philadelphian leaders that supported the local and national civil rights movements;\n**(2)**\nrecognizes and uplifts ongoing efforts that highlight African-American stories and history; and\n**(3)**\nrecognizes the need to continue protecting diversity at colleges and universities throughout the Nation, and the civil rights of students.",
      "versionDate": "2026-02-23",
      "versionType": "IH"
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-02-27T17:49:43Z"
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
      "date": "2026-02-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1071ih.xml"
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
      "title": "Recognizing the desegregation efforts at Girard College in Philadelphia, and the leaders involved in African-American integration and civil rights expansion.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T09:18:26Z"
    },
    {
      "title": "Recognizing the desegregation efforts at Girard College in Philadelphia, and the leaders involved in African-American integration and civil rights expansion.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T09:05:44Z"
    }
  ]
}
```
