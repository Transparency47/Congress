# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/340?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/340
- Title: A resolution designating July 30, 2025, as "National Whistleblower Appreciation Day".
- Congress: 119
- Bill type: SRES
- Bill number: 340
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2025-09-24T17:18:19Z
- Update date including text: 2025-09-24T17:18:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-08-01 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-08-01 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S5475; text: CR S4828)
- 2025-08-01 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-08-01 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-08-01 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-08-01 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S5475; text: CR S4828)
- 2025-08-01 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-08-01 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/340",
    "number": "340",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "A resolution designating July 30, 2025, as \"National Whistleblower Appreciation Day\".",
    "type": "SRES",
    "updateDate": "2025-09-24T17:18:19Z",
    "updateDateIncludingText": "2025-09-24T17:18:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S5475; text: CR S4828)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
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
            "date": "2025-08-02T01:54:53Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-07-29T16:23:44Z",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "OR"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TN"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WI"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "ME"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NE"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NM"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "MS"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "GA"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "AR"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "RI"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "OK"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MA"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "IA"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres340is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 340\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Grassley (for himself, Mr. Wyden , Mrs. Blackburn , Ms. Baldwin , Ms. Collins , Ms. Cantwell , Mrs. Fischer , Mr. Luj\u00e1n , Mr. Wicker , Mr. Warnock , Mr. Boozman , Mr. Whitehouse , Mr. Lankford , Mr. Markey , Ms. Ernst , and Mr. Johnson ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating July 30, 2025, as National Whistleblower Appreciation Day .\nThat the Senate\u2014\n**(1)**\ndesignates July 30, 2025, as National Whistleblower Appreciation Day ; and\n**(2)**\nensures that the Federal Government implements the intent of the Founding Fathers, as reflected in the legislation passed on July 30, 1778 (relating to whistleblowers), by encouraging each executive agency to recognize National Whistleblower Appreciation Day by\u2014\n**(A)**\ninforming employees, contractors working on behalf of the taxpayers of the United States, and members of the public about the legal right of a United States citizen to blow the whistle to the appropriate authority by honest and good faith reporting of misconduct, fraud, misdemeanors, or other crimes; and\n**(B)**\nacknowledging the contributions of whistleblowers to combating waste, fraud, abuse, and violations of laws and regulations of the United States.",
      "versionDate": "2025-07-29",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres340ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 340\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Grassley (for himself, Mr. Wyden , Mrs. Blackburn , Ms. Baldwin , Ms. Collins , Ms. Cantwell , Mrs. Fischer , Mr. Luj\u00e1n , Mr. Wicker , Mr. Warnock , Mr. Boozman , Mr. Whitehouse , Mr. Lankford , Mr. Markey , Ms. Ernst , and Mr. Johnson ) submitted the following resolution; which was referred to the Committee on the Judiciary\nAugust 1, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nDesignating July 30, 2025, as National Whistleblower Appreciation Day .\nThat the Senate\u2014\n**(1)**\ndesignates July 30, 2025, as National Whistleblower Appreciation Day ; and\n**(2)**\nensures that the Federal Government implements the intent of the Founding Fathers, as reflected in the legislation passed on July 30, 1778 (relating to whistleblowers), by encouraging each executive agency to recognize National Whistleblower Appreciation Day by\u2014\n**(A)**\ninforming employees, contractors working on behalf of the taxpayers of the United States, and members of the public about the legal right of a United States citizen to blow the whistle to the appropriate authority by honest and good faith reporting of misconduct, fraud, misdemeanors, or other crimes; and\n**(B)**\nacknowledging the contributions of whistleblowers to combating waste, fraud, abuse, and violations of laws and regulations of the United States.",
      "versionDate": "2025-08-01",
      "versionType": "ATS"
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
            "updateDate": "2025-09-03T15:06:09Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-09-03T15:06:09Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-09-03T15:06:09Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-09-03T15:06:09Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-09-03T15:06:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-02T14:55:16Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres340is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres340ats.xml"
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
      "title": "A resolution designating July 30, 2025, as \"National Whistleblower Appreciation Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:48:19Z"
    },
    {
      "title": "A resolution designating July 30, 2025, as \"National Whistleblower Appreciation Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:45:32Z"
    }
  ]
}
```
