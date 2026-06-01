# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/108
- Title: A resolution affirming the rule of law and the legitimacy of judicial review.
- Congress: 119
- Bill type: SRES
- Bill number: 108
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2026-03-12T15:03:55Z
- Update date including text: 2026-03-12T15:03:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1583)
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1583)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/108",
    "number": "108",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "A resolution affirming the rule of law and the legitimacy of judicial review.",
    "type": "SRES",
    "updateDate": "2026-03-12T15:03:55Z",
    "updateDateIncludingText": "2026-03-12T15:03:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1583)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": [
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionDate": "2025-03-05",
                  "committees": {
                    "item": {
                      "name": "Judiciary Committee",
                      "systemCode": "ssju00"
                    }
                  },
                  "sourceSystem": {
                    "code": "0",
                    "name": "Senate"
                  },
                  "text": "Referred to the Committee on the Judiciary.",
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2025-03-05",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2025-03-05",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                }
              ]
            },
            "count": "3"
          },
          "amendedBill": {
            "congress": "119",
            "number": "108",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "A resolution affirming the rule of law and the legitimacy of judicial review.",
            "type": "SRES",
            "updateDateIncludingText": "2026-03-12"
          },
          "chamber": "Senate",
          "congress": "119",
          "latestAction": {
            "actionDate": "2025-03-05",
            "text": "Referred to the Committee on the Judiciary."
          },
          "number": "1230",
          "purpose": "To improve the preamble.",
          "sponsors": {
            "item": {
              "bioguideId": "G000386",
              "firstName": "Chuck",
              "fullName": "Sen. Grassley, Chuck [R-IA]",
              "lastName": "Grassley",
              "party": "R",
              "state": "IA"
            }
          },
          "submittedDate": "2025-03-05T05:00:00Z",
          "textVersions": {
            "count": "1"
          },
          "type": "SAMDT",
          "updateDate": "2025-03-05T21:58:58Z"
        },
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionDate": "2025-03-05",
                  "committees": {
                    "item": {
                      "name": "Judiciary Committee",
                      "systemCode": "ssju00"
                    }
                  },
                  "sourceSystem": {
                    "code": "0",
                    "name": "Senate"
                  },
                  "text": "Referred to the Committee on the Judiciary.",
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2025-03-05",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2025-03-05",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                }
              ]
            },
            "count": "3"
          },
          "amendedBill": {
            "congress": "119",
            "number": "108",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "A resolution affirming the rule of law and the legitimacy of judicial review.",
            "type": "SRES",
            "updateDateIncludingText": "2026-03-12"
          },
          "chamber": "Senate",
          "congress": "119",
          "latestAction": {
            "actionDate": "2025-03-05",
            "text": "Referred to the Committee on the Judiciary."
          },
          "number": "1229",
          "purpose": "To improve the resolution.",
          "sponsors": {
            "item": {
              "bioguideId": "G000386",
              "firstName": "Chuck",
              "fullName": "Sen. Grassley, Chuck [R-IA]",
              "lastName": "Grassley",
              "party": "R",
              "state": "IA"
            }
          },
          "submittedDate": "2025-03-05T05:00:00Z",
          "textVersions": {
            "count": "1"
          },
          "type": "SAMDT",
          "updateDate": "2025-03-05T21:58:46Z"
        }
      ]
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
          "date": "2025-03-05T21:01:52Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "DE"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MN"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "RI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NH"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "HI"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NV"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CO"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NM"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "VT"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres108is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 108\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Durbin (for himself, Mr. Coons , Mr. Blumenthal , Mr. Schiff , Mr. Booker , Ms. Klobuchar , Mr. Whitehouse , Mr. Kim , Mrs. Shaheen , Ms. Hirono , Ms. Cortez Masto , Mr. Hickenlooper , Mr. Heinrich , Ms. Duckworth , Mr. Wyden , Mr. Welch , Mr. Kelly , Mr. Padilla , Mr. Schumer , Mr. Ossoff , and Mr. Warnock ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nAffirming the rule of law and the legitimacy of judicial review.\nThat the Senate affirms that\u2014\n**(1)**\nArticle III of the Constitution of the United States vests the judicial Power of the United States . . . in one supreme Court, and in such inferior Courts as the Congress may from time to time ordain and establish ;\n**(2)**\nas Chief Justice Marshall held in the Supreme Court\u2019s landmark 1803 decision Marbury v. Madison, It is emphatically the province and duty of the judicial department to say what the law is ; and\n**(3)**\nthe Constitution of the United States and established precedent require the executive branch to comply with all Federal court rulings.",
      "versionDate": "2025-03-05",
      "versionType": "IS"
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
        "actionDate": "2025-03-25",
        "text": "Referred to the Committee on the Judiciary. (text: CR S1837-1838)"
      },
      "number": "136",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution affirming the rule of law and the legitimacy of judicial review.",
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
        "name": "Law",
        "updateDate": "2025-03-10T17:51:23Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres108is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution affirming the rule of law and the legitimacy of judicial review.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:28Z"
    },
    {
      "title": "A resolution affirming the rule of law and the legitimacy of judicial review.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T11:56:18Z"
    }
  ]
}
```
