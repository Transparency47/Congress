# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/668?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/668
- Title: A resolution designating April 2026 as "Second Chance Month".
- Congress: 119
- Bill type: SRES
- Bill number: 668
- Origin chamber: Senate
- Introduced date: 2026-04-14
- Update date: 2026-05-05T12:06:06Z
- Update date including text: 2026-05-05T12:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in Senate
- 2026-04-14 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1743-1744)
- 2026-04-14 - IntroReferral: Submitted in Senate
- 2026-04-28 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-04-28 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2075)
- 2026-04-28 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-04-28 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2026-04-14: Submitted in Senate

## Actions

- 2026-04-14 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1743-1744)
- 2026-04-14 - IntroReferral: Submitted in Senate
- 2026-04-28 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-04-28 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2075)
- 2026-04-28 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-04-28 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

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
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/668",
    "number": "668",
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
    "title": "A resolution designating April 2026 as \"Second Chance Month\".",
    "type": "SRES",
    "updateDate": "2026-05-05T12:06:06Z",
    "updateDateIncludingText": "2026-05-05T12:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2075)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-28",
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
      "actionDate": "2026-04-28",
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
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1743-1744)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-14",
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
            "date": "2026-04-28T22:54:38Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-04-14T19:30:13Z",
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
      "sponsorshipDate": "2026-04-14",
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
      "sponsorshipDate": "2026-04-14",
      "state": "MA"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "OK"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres668is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 668\nIN THE SENATE OF THE UNITED STATES\nApril 14, 2026 Ms. Klobuchar (for herself, Mr. Cramer , Mr. Markey , Mr. Lankford , Mr. Padilla , and Mrs. Capito ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating April 2026 as Second Chance Month .\nThat the Senate\u2014\n**(1)**\ndesignates April 2026 as Second Chance Month ;\n**(2)**\nhonors the work of communities, governmental institutions, nonprofit organizations, congregations, employers, and individuals to remove unnecessary legal and societal barriers that prevent individuals with criminal records from becoming productive members of society; and\n**(3)**\ncalls upon the people of the United States to observe Second Chance Month through actions and programs that\u2014\n**(A)**\npromote awareness of those unnecessary legal and social barriers; and\n**(B)**\nprovide closure for individuals with a criminal record who have paid their debt.",
      "versionDate": "2026-04-14",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres668ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 668\nIN THE SENATE OF THE UNITED STATES\nApril 14, 2026 Ms. Klobuchar (for herself, Mr. Cramer , Mr. Markey , Mr. Lankford , Mr. Padilla , and Mrs. Capito ) submitted the following resolution; which was referred to the Committee on the Judiciary\nApril 28, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nDesignating April 2026 as Second Chance Month .\nThat the Senate\u2014\n**(1)**\ndesignates April 2026 as Second Chance Month ;\n**(2)**\nhonors the work of communities, governmental institutions, nonprofit organizations, congregations, employers, and individuals to remove unnecessary legal and societal barriers that prevent individuals with criminal records from becoming productive members of society; and\n**(3)**\ncalls upon the people of the United States to observe Second Chance Month through actions and programs that\u2014\n**(A)**\npromote awareness of those unnecessary legal and social barriers; and\n**(B)**\nprovide closure for individuals with a criminal record who have paid their debt.",
      "versionDate": "2026-04-28",
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
            "updateDate": "2026-04-29T14:37:30Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2026-04-29T14:37:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-05T12:06:06Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres668is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres668ats.xml"
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
      "title": "A resolution designating April 2026 as \"Second Chance Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T03:33:21Z"
    },
    {
      "title": "A resolution designating April 2026 as \"Second Chance Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T10:56:20Z"
    }
  ]
}
```
