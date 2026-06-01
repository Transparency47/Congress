# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/249?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/249
- Title: Recognizing the 204th anniversary of the War of Greek Independence.
- Congress: 119
- Bill type: HRES
- Bill number: 249
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2026-03-30T22:43:22Z
- Update date including text: 2026-03-30T22:43:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-03-25 - IntroReferral: Submitted in House
- Latest action: 2025-03-25: Submitted in House

## Actions

- 2025-03-25 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-03-25 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/249",
    "number": "249",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001257",
        "district": "12",
        "firstName": "Gus",
        "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
        "lastName": "Bilirakis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Recognizing the 204th anniversary of the War of Greek Independence.",
    "type": "HRES",
    "updateDate": "2026-03-30T22:43:22Z",
    "updateDateIncludingText": "2026-03-30T22:43:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NH"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "NJ"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NJ"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "RI"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "RI"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres249ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 249\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Bilirakis (for himself, Mr. Pappas , Ms. Malliotakis , Ms. Titus , Mr. Smith of New Jersey , Mr. Pallone , Mr. Amo , Mr. Magaziner , and Ms. Meng ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRecognizing the 204th anniversary of the War of Greek Independence.\nThat the House of Representatives\u2014\n**(1)**\nextends warm congratulations and best wishes to the people of Greece as they celebrate the 204th anniversary of the War of Greek Independence;\n**(2)**\nexpresses support for the principles of democracy, human rights, and the rule of law to which the people of the United States and Greece are committed;\n**(3)**\nnotes the important role that Greece has played in the wider European region and in the community of nations since gaining its independence;\n**(4)**\ncommends the Greek-American community for its contributions to the United States and its role as a bridge between the two countries;\n**(5)**\ncommends the geostrategic importance of Greece at the junction of three continents and in particular the critical role Greece plays in promoting stability in the Eastern Mediterranean and Western Balkans and in continuously upholding international law and respect for national sovereignty and territorial integrity; and\n**(6)**\nappreciates the deepening cooperation between the United States and Greece, based on shared values and interests, including the important bilateral energy and security partnership and the important role that Greece plays in bolstering European energy security.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2026-03-27",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "1143",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing the 205th anniversary of the War of Greek Independence.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-05-20T12:20:27Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-05-20T12:20:27Z"
          },
          {
            "name": "Greece",
            "updateDate": "2025-05-20T12:20:27Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2025-05-20T12:20:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-15T00:19:38Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres249ih.xml"
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
      "title": "Recognizing the 204th anniversary of the War of Greek Independence.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recognizing the 204th anniversary of the War of Greek Independence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T08:18:26Z"
    }
  ]
}
```
