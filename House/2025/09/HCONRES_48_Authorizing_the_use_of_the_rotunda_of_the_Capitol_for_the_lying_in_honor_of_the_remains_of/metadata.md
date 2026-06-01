# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/48?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/48
- Title: Authorizing the use of the rotunda of the Capitol for the lying in honor of the remains of the late Charles James Kirk, a lifelong advocate for freedom of speech, civil political discourse, and the political engagement of youth.
- Congress: 119
- Bill type: HCONRES
- Bill number: 48
- Origin chamber: House
- Introduced date: 2025-09-15
- Update date: 2025-09-27T08:05:35Z
- Update date including text: 2025-09-27T08:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-09-15 - IntroReferral: Submitted in House
- 2025-09-15 - IntroReferral: Submitted in House
- Latest action: 2025-09-15: Submitted in House

## Actions

- 2025-09-15 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-09-15 - IntroReferral: Submitted in House
- 2025-09-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/48",
    "number": "48",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Authorizing the use of the rotunda of the Capitol for the lying in honor of the remains of the late Charles James Kirk, a lifelong advocate for freedom of speech, civil political discourse, and the political engagement of youth.",
    "type": "HCONRES",
    "updateDate": "2025-09-27T08:05:35Z",
    "updateDateIncludingText": "2025-09-27T08:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T16:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "AZ"
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
      "sponsorshipDate": "2025-09-15",
      "state": "NJ"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "OH"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "KY"
    },
    {
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "FL"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "SC"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "FL"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "CO"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "AZ"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres48ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 48\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 15, 2025 Ms. Mace (for herself, Mr. Biggs of Arizona , Mr. Smith of New Jersey , Mr. Rulli , Mr. Massie , Mr. Diaz-Balart , Mr. Wilson of South Carolina , Mr. Patronis , Mr. Babin , Mr. McGuire , Ms. Boebert , Mr. Gill of Texas , and Mr. Jackson of Texas ) submitted the following concurrent resolution; which was referred to the Committee on House Administration\nCONCURRENT RESOLUTION\nAuthorizing the use of the rotunda of the Capitol for the lying in honor of the remains of the late Charles James Kirk, a lifelong advocate for freedom of speech, civil political discourse, and the political engagement of youth.\nThat the remains of the late Charles James Kirk, a lifelong advocate for freedom of speech, civil political discourse, and the political engagement of youth, shall be permitted to lie in honor in the rotunda of the Capitol on a date and for a period of time to be determined by the Speaker of the House of Representatives and the President pro tempore of the Senate, and the Architect of the Capitol, under the direction of the Speaker of the House of Representatives and the President pro tempore of the Senate, shall take all necessary steps for the accomplishment of that purpose.",
      "versionDate": "2025-09-15",
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
        "name": "Congress",
        "updateDate": "2025-09-24T16:26:55Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres48ih.xml"
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
      "title": "Authorizing the use of the rotunda of the Capitol for the lying in honor of the remains of the late Charles James Kirk, a lifelong advocate for freedom of speech, civil political discourse, and the political engagement of youth.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T02:48:18Z"
    },
    {
      "title": "Authorizing the use of the rotunda of the Capitol for the lying in honor of the remains of the late Charles James Kirk, a lifelong advocate for freedom of speech, civil political discourse, and the political engagement of youth.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T08:05:23Z"
    }
  ]
}
```
