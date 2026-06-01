# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/406?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/406
- Title: A resolution designating September 30, 2025, as "Impact Aid Recognition Day" to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.
- Congress: 119
- Bill type: SRES
- Bill number: 406
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2025-12-12T15:56:08Z
- Update date including text: 2025-12-12T15:56:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6737)
- 2025-10-06 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-10-06 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S6959; text: CR 9/18/2025 S6737)
- 2025-10-06 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-10-06 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6737)
- 2025-10-06 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-10-06 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S6959; text: CR 9/18/2025 S6737)
- 2025-10-06 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-10-06 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/406",
    "number": "406",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "A resolution designating September 30, 2025, as \"Impact Aid Recognition Day\" to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.",
    "type": "SRES",
    "updateDate": "2025-12-12T15:56:08Z",
    "updateDateIncludingText": "2025-12-12T15:56:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S6959; text: CR 9/18/2025 S6737)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-06",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-10-06",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S6737)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
        "item": [
          {
            "date": "2025-10-06T23:28:00Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-09-18T19:10:20Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "ID"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "WI"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WY"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CT"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NJ"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "OK"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WY"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "OK"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "AZ"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "ID"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NY"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "SD"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NM"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "RI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MN"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres406is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 406\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Ms. Hirono (for herself, Mr. Crapo , Ms. Baldwin , Mr. Barrasso , Mr. Blumenthal , Mr. Daines , Mr. Booker , Mr. Lankford , Ms. Duckworth , Ms. Lummis , Mr. Durbin , Mr. Mullin , Mr. Gallego , Mr. Risch , Mrs. Gillibrand , Mr. Thune , Mr. Kaine , Mr. Kelly , Mr. Kim , Ms. Klobuchar , Mr. Luj\u00e1n , Mrs. Murray , Mr. Padilla , Mr. Reed , Mr. Schiff , Ms. Smith , and Mr. Whitehouse ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating September 30, 2025, as Impact Aid Recognition Day to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.\nThat the Senate\u2014\n**(1)**\ndesignates September 30, 2025, as Impact Aid Recognition Day to recognize the 75th anniversary of the establishment of the Impact Aid program; and\n**(2)**\nrecognizes the importance of\u2014\n**(A)**\nthe Impact Aid program under title VII of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7701 et seq. ); and\n**(B)**\nthe objective of that program to ensure that all children educated in federally impacted school districts receive a high-quality education and have access to the opportunities needed to reach their full potential.",
      "versionDate": "2025-09-18",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres406ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 406\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Ms. Hirono (for herself, Mr. Crapo , Ms. Baldwin , Mr. Barrasso , Mr. Blumenthal , Mr. Daines , Mr. Booker , Mr. Lankford , Ms. Duckworth , Ms. Lummis , Mr. Durbin , Mr. Mullin , Mr. Gallego , Mr. Risch , Mrs. Gillibrand , Mr. Thune , Mr. Kaine , Mr. Kelly , Mr. Kim , Ms. Klobuchar , Mr. Luj\u00e1n , Mrs. Murray , Mr. Padilla , Mr. Reed , Mr. Schiff , Ms. Smith , and Mr. Whitehouse ) submitted the following resolution; which was referred to the Committee on the Judiciary\nOctober 6, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nDesignating September 30, 2025, as Impact Aid Recognition Day to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.\nThat the Senate\u2014\n**(1)**\ndesignates September 30, 2025, as Impact Aid Recognition Day to recognize the 75th anniversary of the establishment of the Impact Aid program; and\n**(2)**\nrecognizes the importance of\u2014\n**(A)**\nthe Impact Aid program under title VII of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7701 et seq. ); and\n**(B)**\nthe objective of that program to ensure that all children educated in federally impacted school districts receive a high-quality education and have access to the opportunities needed to reach their full potential.",
      "versionDate": "2025-10-06",
      "versionType": "ATS"
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
        "actionDate": "2025-10-03",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "786",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Supporting the designation of September 30, 2025, as \"Impact Aid Recognition Day\" to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.",
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
            "updateDate": "2025-11-13T20:08:57Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-11-13T20:08:57Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-11-13T20:08:57Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-11-13T20:08:57Z"
          },
          {
            "name": "Property tax",
            "updateDate": "2025-11-13T20:08:57Z"
          },
          {
            "name": "State and local taxation",
            "updateDate": "2025-11-13T20:08:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-12-12T15:55:43Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres406is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres406ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution designating September 30, 2025, as \"Impact Aid Recognition Day\" to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T06:03:28Z"
    },
    {
      "title": "A resolution designating September 30, 2025, as \"Impact Aid Recognition Day\" to recognize and celebrate the 75th anniversary of the establishment of the Impact Aid program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T10:56:27Z"
    }
  ]
}
```
