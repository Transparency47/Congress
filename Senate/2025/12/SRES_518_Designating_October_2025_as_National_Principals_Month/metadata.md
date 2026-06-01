# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/518?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/518
- Title: A resolution designating October 2025 as "National Principals Month".
- Congress: 119
- Bill type: SRES
- Bill number: 518
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-04T15:22:15Z
- Update date including text: 2025-12-04T15:22:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-12-03 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-12-03 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S8487)
- 2025-12-03 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-03 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-12-03 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-12-03 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S8487)
- 2025-12-03 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-03 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/518",
    "number": "518",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001203",
        "district": "",
        "firstName": "Tina",
        "fullName": "Sen. Smith, Tina [D-MN]",
        "lastName": "Smith",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A resolution designating October 2025 as \"National Principals Month\".",
    "type": "SRES",
    "updateDate": "2025-12-04T15:22:15Z",
    "updateDateIncludingText": "2025-12-04T15:22:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S8487)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
            "date": "2025-12-03T22:56:21Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-11-20T21:29:56Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "ME"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-11-20",
      "state": "ME"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MD"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "HI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres518is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 518\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Ms. Smith (for herself, Ms. Collins , Mr. King , Mr. Van Hollen , Ms. Hirono , and Mr. Durbin ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating October 2025 as National Principals Month .\nThat the Senate\u2014\n**(1)**\ndesignates October 2025 as National Principals Month ;\n**(2)**\nhonors the contributions of principals in elementary schools, middle schools, and high schools in the United States; and\n**(3)**\nsupports the goals and ideals of National Principals Month.",
      "versionDate": "2025-11-20",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres518ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 518\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Ms. Smith (for herself, Ms. Collins , Mr. King , Mr. Van Hollen , Ms. Hirono , and Mr. Durbin ) submitted the following resolution; which was referred to the Committee on the Judiciary\nDecember 3, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nDesignating October 2025 as National Principals Month .\nThat the Senate\u2014\n**(1)**\ndesignates October 2025 as National Principals Month ;\n**(2)**\nhonors the contributions of principals in elementary schools, middle schools, and high schools in the United States; and\n**(3)**\nsupports the goals and ideals of National Principals Month.",
      "versionDate": "2025-12-03",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-11-25T19:57:21Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres518is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres518ats.xml"
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
      "title": "A resolution designating October 2025 as \"National Principals Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-22T10:03:30Z"
    },
    {
      "title": "A resolution designating October 2025 as \"National Principals Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T11:56:26Z"
    }
  ]
}
```
