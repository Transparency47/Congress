# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/276?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/276
- Title: A resolution designating June 12, 2025, as "Women Veterans Appreciation Day".
- Congress: 119
- Bill type: SRES
- Bill number: 276
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-07-24T15:34:51Z
- Update date including text: 2025-07-24T15:34:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-07-21 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-07-21 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S4511: 4; text: 6/12/2025 CR S3393)
- 2025-07-21 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-07-21 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-07-21 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-07-21 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S4511: 4; text: 6/12/2025 CR S3393)
- 2025-07-21 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-07-21 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/276",
    "number": "276",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "A resolution designating June 12, 2025, as \"Women Veterans Appreciation Day\".",
    "type": "SRES",
    "updateDate": "2025-07-24T15:34:51Z",
    "updateDateIncludingText": "2025-07-24T15:34:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S4511: 4; text: 6/12/2025 CR S3393)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
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
            "date": "2025-07-21T22:37:47Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-06-12T19:31:10Z",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NJ"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "AR"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "ME"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NV"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres276is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 276\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mrs. Blackburn (for herself, Mr. Booker , Mr. Boozman , Ms. Collins , Ms. Rosen , and Mrs. Shaheen ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating June 12, 2025, as \u201cWomen Veterans Appreciation Day\u201d.\nThat the Senate designates June 12, 2025, as Women Veterans Appreciation Day to recognize the service and sacrifices of women veterans who have served valiantly on behalf of the United States.",
      "versionDate": "2025-06-12",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres276ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 276\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mrs. Blackburn (for herself, Mr. Booker , Mr. Boozman , Ms. Collins , Ms. Rosen , and Mrs. Shaheen ) submitted the following resolution; which was referred to the Committee on the Judiciary\nJuly 21, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nDesignating June 12, 2025, as \u201cWomen Veterans Appreciation Day\u201d.\nThat the Senate designates June 12, 2025, as Women Veterans Appreciation Day to recognize the service and sacrifices of women veterans who have served valiantly on behalf of the United States.",
      "versionDate": "2025-07-21",
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
            "updateDate": "2025-07-24T15:34:51Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-07-24T15:34:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-17T20:48:55Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres276is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres276ats.xml"
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
      "title": "A resolution designating June 12, 2025, as \"Women Veterans Appreciation Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T10:56:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution designating June 12, 2025, as \"Women Veterans Appreciation Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T10:56:24Z"
    }
  ]
}
```
