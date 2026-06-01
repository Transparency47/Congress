# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/629?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/629
- Title: A resolution honoring the life and legacy of Reverend Jesse Louis Jackson, Sr., and commending him for his significant leadership during the Civil Rights Movement and his decades of advocacy in pursuit of justice, equality, and human rights.
- Congress: 119
- Bill type: SRES
- Bill number: 629
- Origin chamber: Senate
- Introduced date: 2026-03-09
- Update date: 2026-03-20T14:09:04Z
- Update date including text: 2026-03-20T14:09:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in Senate
- 2026-03-09 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S917)
- 2026-03-09 - IntroReferral: Submitted in Senate
- 2026-03-16 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1058)
- 2026-03-16 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1058)
- 2026-03-16 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-03-16 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2026-03-09: Submitted in Senate

## Actions

- 2026-03-09 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S917)
- 2026-03-09 - IntroReferral: Submitted in Senate
- 2026-03-16 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1058)
- 2026-03-16 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1058)
- 2026-03-16 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-03-16 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/629",
    "number": "629",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
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
    "title": "A resolution honoring the life and legacy of Reverend Jesse Louis Jackson, Sr., and commending him for his significant leadership during the Civil Rights Movement and his decades of advocacy in pursuit of justice, equality, and human rights.",
    "type": "SRES",
    "updateDate": "2026-03-20T14:09:04Z",
    "updateDateIncludingText": "2026-03-20T14:09:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1058)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1058)",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-16",
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
      "actionDate": "2026-03-16",
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
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S917)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-09",
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
      "text": "Submitted in Senate",
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
            "date": "2026-03-16T20:52:25Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-03-09T22:32:00Z",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "IL"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "GA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "NJ"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "DE"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "DE"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "OR"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "MD"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NM"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-03-12",
      "state": "VT"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CO"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CO"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres629is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 629\nIN THE SENATE OF THE UNITED STATES\nMarch 9, 2026 Mr. Durbin (for himself, Ms. Duckworth , Mr. Warnock , Mr. Booker , and Ms. Blunt Rochester ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the life and legacy of Reverend Jesse Louis Jackson, Sr., and commending him for his significant leadership during the Civil Rights Movement and his decades of advocacy in pursuit of justice, equality, and human rights.\nThat the Senate\u2014\n**(1)**\nhonors the life and legacy of Jesse Louis Jackson, Sr., (referred to in this resolution as Reverend Jackson ), a distinguished American and pivotal civil rights leader who\u2014\n**(A)**\ndedicated his life to giving voice to the voiceless; and\n**(B)**\npioneered countless campaigns for the liberation of people across the globe;\n**(2)**\ncommends Reverend Jackson for his contributions to the United States of America and its pledge to ensure liberty and justice for all ;\n**(3)**\nextends its deepest condolences and sympathies to the family of Reverend Jackson; and\n**(4)**\nrequests that the Secretary of the Senate transmit an enrolled copy of this resolution to the family of Reverend Jackson.",
      "versionDate": "2026-03-09",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres629ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 629\nIN THE SENATE OF THE UNITED STATES\nMarch 9, 2026 Mr. Durbin (for himself, Ms. Duckworth , Mr. Warnock , Mr. Booker , Ms. Blunt Rochester , Mr. Coons , Mr. Wyden , Mr. Schumer , Mr. Van Hollen , Mr. Schiff , Mr. Heinrich , Mr. Sanders , Mr. Bennet , and Mr. Hickenlooper ) submitted the following resolution; which was referred to the Committee on the Judiciary March 16, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nHonoring the life and legacy of Reverend Jesse Louis Jackson, Sr., and commending him for his significant leadership during the Civil Rights Movement and his decades of advocacy in pursuit of justice, equality, and human rights.\nThat the Senate\u2014\n**(1)**\nhonors the life and legacy of Jesse Louis Jackson, Sr. (referred to in this resolution as Reverend Jackson ), a distinguished American and pivotal civil rights leader who\u2014\n**(A)**\ndedicated his life to giving voice to the voiceless; and\n**(B)**\npioneered countless campaigns for the liberation of people across the globe;\n**(2)**\ncommends Reverend Jackson for his contributions to the United States of America and its pledge to ensure liberty and justice for all ;\n**(3)**\nextends its deepest condolences and sympathies to the family of Reverend Jackson; and\n**(4)**\nrequests that the Secretary of the Senate transmit an enrolled copy of this resolution to the family of Reverend Jackson.",
      "versionDate": "2026-03-16",
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
            "name": "Congressional tributes",
            "updateDate": "2026-03-17T16:21:23Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2026-03-17T16:21:28Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2026-03-17T16:21:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-03-20T14:09:04Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres629is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres629ats.xml"
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
      "title": "A resolution honoring the life and legacy of Reverend Jesse Louis Jackson, Sr., and commending him for his significant leadership during the Civil Rights Movement and his decades of advocacy in pursuit of justice, equality, and human rights.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-11T03:18:21Z"
    },
    {
      "title": "A resolution honoring the life and legacy of Reverend Jesse Louis Jackson, Sr., and commending him for his significant leadership during the Civil Rights Movement and his decades of advocacy in pursuit of justice, equality, and human rights.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T10:56:19Z"
    }
  ]
}
```
