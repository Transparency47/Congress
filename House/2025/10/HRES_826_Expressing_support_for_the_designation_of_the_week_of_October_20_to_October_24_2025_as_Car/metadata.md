# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/826?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/826
- Title: Expressing support for the designation of the week of October 20 to October 24, 2025, as "Careers in Energy Week".
- Congress: 119
- Bill type: HRES
- Bill number: 826
- Origin chamber: House
- Introduced date: 2025-10-21
- Update date: 2025-12-05T16:14:18Z
- Update date including text: 2025-12-05T16:14:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-21: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-10-21 - IntroReferral: Submitted in House
- 2025-10-21 - IntroReferral: Submitted in House
- Latest action: 2025-10-21: Submitted in House

## Actions

- 2025-10-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-10-21 - IntroReferral: Submitted in House
- 2025-10-21 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/826",
    "number": "826",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Expressing support for the designation of the week of October 20 to October 24, 2025, as \"Careers in Energy Week\".",
    "type": "HRES",
    "updateDate": "2025-12-05T16:14:18Z",
    "updateDateIncludingText": "2025-12-05T16:14:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-21",
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
      "actionDate": "2025-10-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T18:00:45Z",
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
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NJ"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "PA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "TX"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "NJ"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "LA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "OH"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres826ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 826\nIN THE HOUSE OF REPRESENTATIVES\nOctober 21, 2025 Mr. Thompson of Pennsylvania (for himself, Mr. Norcross , Mr. Meuser , Mr. Veasey , Mr. Kean , and Mr. Carter of Louisiana ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for the designation of the week of October 20 to October 24, 2025, as Careers in Energy Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Careers in Energy Week ;\n**(2)**\nrecognizes and honors the dedication and professionalism of the millions of individuals working in the energy sector who ensure the safe and reliable delivery of energy to the Nation;\n**(3)**\nhighlights the rewarding career opportunities available in the energy industry, from skilled trades and technical professions to engineering, science, and management roles;\n**(4)**\npromotes energy education and awareness among students and the general public, emphasizing the importance of career and technical education, vocational training, and science, technology, engineering, and mathematics skills on the future of energy innovation;\n**(5)**\nencourages collaboration between industry, educational institutions, industry workforce, community-based organizations, and government agencies to support workforce development and address the evolving needs of the energy sector; and\n**(6)**\nencourages all Americans to observe Careers in Energy Week with relevant programs, activities, and ceremonies showcasing the full range of energy careers, promoting career and technical education opportunities, and strengthening workforce development.",
      "versionDate": "2025-10-21",
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
        "actionDate": "2025-10-21",
        "text": "Referred to the Committee on Energy and Natural Resources. (text: CR S7188)"
      },
      "number": "461",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of the week of October 20 to October 24, 2025, as \"Careers in Energy Week\".",
      "type": "SRES"
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
        "name": "Energy",
        "updateDate": "2025-12-05T16:14:18Z"
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
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres826ih.xml"
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
      "title": "Expressing support for the designation of the week of October 20 to October 24, 2025, as \"Careers in Energy Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T08:18:18Z"
    },
    {
      "title": "Expressing support for the designation of the week of October 20 to October 24, 2025, as \"Careers in Energy Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-22T08:05:51Z"
    }
  ]
}
```
