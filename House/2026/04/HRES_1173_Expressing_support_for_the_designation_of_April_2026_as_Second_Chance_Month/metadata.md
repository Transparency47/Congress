# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1173?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1173
- Title: Expressing support for the designation of April 2026 as "Second Chance Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1173
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-04-28T08:06:41Z
- Update date including text: 2026-04-28T08:06:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-04-14 - IntroReferral: Submitted in House
- Latest action: 2026-04-14: Submitted in House

## Actions

- 2026-04-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-04-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1173",
    "number": "1173",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000821",
        "district": "4",
        "firstName": "Bruce",
        "fullName": "Rep. Westerman, Bruce [R-AR-4]",
        "lastName": "Westerman",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Expressing support for the designation of April 2026 as \"Second Chance Month\".",
    "type": "HRES",
    "updateDate": "2026-04-28T08:06:41Z",
    "updateDateIncludingText": "2026-04-28T08:06:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-14",
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
      "actionCode": "1025",
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
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
          "date": "2026-04-14T16:00:30Z",
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
      "sponsorshipDate": "2026-04-14",
      "state": "IL"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "WV"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "GA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "AL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NJ"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "NE"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "VA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "LA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1173ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1173\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Mr. Westerman (for himself, Mr. Davis of Illinois , Mrs. Miller of West Virginia , Mrs. McBath , Mr. Moore of Alabama , Mrs. McIver , Mr. Bacon , and Mr. Scott of Virginia ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nExpressing support for the designation of April 2026 as Second Chance Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Second Chance Month ;\n**(2)**\nhonors the work of communities, governmental institutions, nonprofit organizations, congregations, employers, and individuals to remove unnecessary legal and societal barriers that prevent individuals with criminal records from becoming productive members of society; and\n**(3)**\ncalls upon the people of the United States to observe Second Chance Month through actions and programs that\u2014\n**(A)**\npromote awareness of those unnecessary legal and social barriers; and\n**(B)**\nprovide closure for individuals with a criminal record who have paid their debt.",
      "versionDate": "2026-04-14",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "289",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of April 2025 as \"Second Chance Month\".",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-28",
        "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2610; text: 3/31/2025 CR S2096)"
      },
      "number": "149",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution designating April 2025 as \"Second Chance Month\".",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-14",
        "text": "Referred to the Committee on the Judiciary. (text: CR S1743-1744)"
      },
      "number": "668",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution designating April 2026 as \"Second Chance Month\".",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-17T19:57:56Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1173ih.xml"
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
      "title": "Expressing support for the designation of April 2026 as \"Second Chance Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-15T08:18:34Z"
    },
    {
      "title": "Expressing support for the designation of April 2026 as \"Second Chance Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T08:06:14Z"
    }
  ]
}
```
