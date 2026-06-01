# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2468?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2468
- Title: Renewing Immigration Provisions of the Immigration Act of 1929
- Congress: 119
- Bill type: S
- Bill number: 2468
- Origin chamber: Senate
- Introduced date: 2025-07-28
- Update date: 2025-12-17T12:03:16Z
- Update date including text: 2025-12-17T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-28: Introduced in Senate
- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S4776)
- Latest action: 2025-07-28: Introduced in Senate

## Actions

- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S4776)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-28",
    "latestAction": {
      "actionDate": "2025-07-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2468",
    "number": "2468",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Renewing Immigration Provisions of the Immigration Act of 1929",
    "type": "S",
    "updateDate": "2025-12-17T12:03:16Z",
    "updateDateIncludingText": "2025-12-17T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S4776)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-07-28T19:52:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "IL"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "HI"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "WA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "CT"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-28",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "MA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "MA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "NJ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "NM"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "CA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MN"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2468is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2468\nIN THE SENATE OF THE UNITED STATES\nJuly 28, 2025 Mr. Padilla (for himself, Mr. Durbin , Mr. Schatz , Mrs. Murray , Mr. Murphy , Mr. Sanders , Ms. Warren , Mr. Markey , Ms. Duckworth , Mr. Booker , Mr. Luj\u00e1n , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 249 of the Immigration and Nationality Act to render available to certain long-term residents of the United States the benefit under that section.\n#### 1. Short title\nThis Act may be cited as the Renewing Immigration Provisions of the Immigration Act of 1929 .\n#### 2. Registry\n##### (a) In general\nSection 249 of the Immigration and Nationality Act ( 8 U.S.C. 1259 ) is amended\u2014\n**(1)**\nin the section header, by striking entered the united states prior to july 1, 1924 or january 1, 1972 ; and inserting are long-term residents of the united states ; and\n**(2)**\nby amending subsection (a) to read as follows:\n(a) entered the United States at least 7 years before the application date; .\n##### (b) Effective date\nThe amendments made by this section shall take effect 60 days after the date of the enactment of this Act.",
      "versionDate": "2025-07-28",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-23",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4696",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Renewing Immigration Provisions of the Immigration Act of 1929",
      "type": "HR"
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
        "name": "Immigration",
        "updateDate": "2025-09-12T14:45:35Z"
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
      "date": "2025-07-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2468is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Renewing Immigration Provisions of the Immigration Act of 1929",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Renewing Immigration Provisions of the Immigration Act of 1929",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 249 of the Immigration and Nationality Act to render available to certain long-term residents of the United States the benefit under that section.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:20Z"
    }
  ]
}
```
