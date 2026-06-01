# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/43?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hconres/43
- Title: Expressing the sense of Congress that any public rendition of "The Star-Spangled Banner" must be performed as written by Francis Scott Key, in English.
- Congress: 119
- Bill type: HCONRES
- Bill number: 43
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2025-07-25T12:16:39Z
- Update date including text: 2025-07-25T12:16:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-07-10 - IntroReferral: Submitted in House
- 2025-07-10 - IntroReferral: Submitted in House
- Latest action: 2025-07-10: Submitted in House

## Actions

- 2025-07-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-07-10 - IntroReferral: Submitted in House
- 2025-07-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hconres/43",
    "number": "43",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Expressing the sense of Congress that any public rendition of \"The Star-Spangled Banner\" must be performed as written by Francis Scott Key, in English.",
    "type": "HCONRES",
    "updateDate": "2025-07-25T12:16:39Z",
    "updateDateIncludingText": "2025-07-25T12:16:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
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
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:08:05Z",
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
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "AL"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "AL"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "IA"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "IA"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "MT"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "IN"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "GA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "NC"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "SC"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres43ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 43\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mrs. Bice (for herself, Mr. Rogers of Alabama , Mr. Moore of Alabama , Mr. Feenstra , Mr. Murphy , Mrs. Miller-Meeks , Mr. Downing , Mrs. Houchin , and Mr. Carter of Georgia ) submitted the following concurrent resolution; which was referred to the Committee on the Judiciary\nCONCURRENT RESOLUTION\nExpressing the sense of Congress that any public rendition of The Star-Spangled Banner must be performed as written by Francis Scott Key, in English.\nThat\u2014\n**(1)**\nany public rendition of The Star-Spangled Banner should be performed as written by Francis Scott Key, in the English language, to preserve its historical and cultural integrity;\n**(2)**\npublic performances of the national anthem should reflect the original lyrics to maintain its unifying significance for the people of the United States; and\n**(3)**\nperformers and organizers of public events are encouraged to honor the tradition of presenting The Star-Spangled Banner in its original English form, as a tribute to its historical and patriotic importance.",
      "versionDate": "2025-07-10",
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
        "actionDate": "2025-07-14",
        "text": "Referred to the Committee on the Judiciary. (text: CR S4338: 2)"
      },
      "number": "17",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A concurrent resolution expressing the sense of the Senate that any public rendition of \"The Star-Spangled Banner\" should be performed as written by Francis Scott Key, in English.",
      "type": "SCONRES"
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-07-24T14:00:20Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres43ih.xml"
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
      "title": "Expressing the sense of Congress that any public rendition of \"The Star-Spangled Banner\" must be performed as written by Francis Scott Key, in English.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:11Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing the sense of Congress that any public rendition of \"The Star-Spangled Banner\" must be performed as written by Francis Scott Key, in English.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-11T08:18:20Z"
    }
  ]
}
```
