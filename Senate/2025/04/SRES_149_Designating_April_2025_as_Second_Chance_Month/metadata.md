# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/149?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/149
- Title: A resolution designating April 2025 as "Second Chance Month".
- Congress: 119
- Bill type: SRES
- Bill number: 149
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2026-04-21T19:33:27Z
- Update date including text: 2026-04-21T19:33:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-04-28 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-04-28 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2610; text: 3/31/2025 CR S2096)
- 2025-04-28 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-04-28 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-04-28 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-04-28 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2610; text: 3/31/2025 CR S2096)
- 2025-04-28 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-04-28 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/149",
    "number": "149",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A resolution designating April 2025 as \"Second Chance Month\".",
    "type": "SRES",
    "updateDate": "2026-04-21T19:33:27Z",
    "updateDateIncludingText": "2026-04-21T19:33:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2610; text: 3/31/2025 CR S2096)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-04-28",
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
      "actionDate": "2025-04-28",
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
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
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
            "date": "2025-04-28T22:52:01Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-04-01T19:54:14Z",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "ND"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WV"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MD"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres149is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 149\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Ms. Klobuchar (for herself, Mr. Cramer , Mr. Markey , and Mrs. Capito ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating April 2025 as Second Chance Month .\nThat the Senate\u2014\n**(1)**\ndesignates April 2025 as Second Chance Month ;\n**(2)**\nhonors the work of communities, governmental institutions, nonprofit organizations, congregations, employers, and individuals to remove unnecessary legal and societal barriers that prevent individuals with criminal records from becoming productive members of society; and\n**(3)**\ncalls upon the people of the United States to observe Second Chance Month through actions and programs that\u2014\n**(A)**\npromote awareness of those unnecessary legal and social barriers; and\n**(B)**\nprovide closure for individuals with a criminal record who have paid their debt.",
      "versionDate": "2025-04-01",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres149ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 149\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Ms. Klobuchar (for herself, Mr. Cramer , Mr. Markey , Mrs. Capito , Mr. Durbin , Mr. Padilla , Mr. Van Hollen , and Ms. Blunt Rochester ) submitted the following resolution; which was referred to the Committee on the Judiciary\nApril 28, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nDesignating April 2025 as Second Chance Month .\nThat the Senate\u2014\n**(1)**\ndesignates April 2025 as Second Chance Month ;\n**(2)**\nhonors the work of communities, governmental institutions, nonprofit organizations, congregations, employers, and individuals to remove unnecessary legal and societal barriers that prevent individuals with criminal records from becoming productive members of society; and\n**(3)**\ncalls upon the people of the United States to observe Second Chance Month through actions and programs that\u2014\n**(A)**\npromote awareness of those unnecessary legal and social barriers; and\n**(B)**\nprovide closure for individuals with a criminal record who have paid their debt.",
      "versionDate": "2025-04-28",
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-14",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1173",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of April 2026 as \"Second Chance Month\".",
      "type": "HRES"
    },
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
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of April 2025 as \"Second Chance Month\".",
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
            "name": "Criminal justice information and records",
            "updateDate": "2025-04-29T14:24:33Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-04-29T14:24:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-04-04T13:35:40Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres149is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres149ats.xml"
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
      "title": "A resolution designating April 2025 as \"Second Chance Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:40Z"
    },
    {
      "title": "A resolution designating April 2025 as \"Second Chance Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T10:56:25Z"
    }
  ]
}
```
