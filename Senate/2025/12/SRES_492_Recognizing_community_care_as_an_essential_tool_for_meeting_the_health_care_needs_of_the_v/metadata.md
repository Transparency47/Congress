# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/492?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/492
- Title: A resolution recognizing community care as an essential tool for meeting the health care needs of the veterans of the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 492
- Origin chamber: Senate
- Introduced date: 2025-11-10
- Update date: 2025-12-19T17:00:42Z
- Update date including text: 2025-12-19T17:00:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in Senate
- 2025-11-10 - IntroReferral: Introduced in Senate
- 2025-11-10 - IntroReferral: Referred to the Committee on Veterans' Affairs. (text: CR S8133)
- 2025-12-17 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-12-17 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S8874; text: CR S8874)
- 2025-12-17 - Discharge: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- 2025-12-17 - Committee: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- Latest action: 2025-11-10: Introduced in Senate

## Actions

- 2025-11-10 - IntroReferral: Introduced in Senate
- 2025-11-10 - IntroReferral: Referred to the Committee on Veterans' Affairs. (text: CR S8133)
- 2025-12-17 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-12-17 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S8874; text: CR S8874)
- 2025-12-17 - Discharge: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- 2025-12-17 - Committee: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/492",
    "number": "492",
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
    "title": "A resolution recognizing community care as an essential tool for meeting the health care needs of the veterans of the United States.",
    "type": "SRES",
    "updateDate": "2025-12-19T17:00:42Z",
    "updateDateIncludingText": "2025-12-19T17:00:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S8874; text: CR S8874)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Veterans' Affairs discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Veterans' Affairs discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Veterans' Affairs. (text: CR S8133)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-10",
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
            "date": "2025-12-18T01:02:08Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-11-10T18:33:53Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sponsorshipDate": "2025-11-10",
      "state": "ND"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "NC"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "MS"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres492is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 492\nIN THE SENATE OF THE UNITED STATES\nNovember 10, 2025 Mrs. Blackburn (for herself, Mr. Cramer , Mr. Tillis , Mr. Wicker , and Mr. Moran ) submitted the following resolution; which was referred to the Committee on Veterans' Affairs\nRESOLUTION\nRecognizing community care as an essential tool for meeting the health care needs of the veterans of the United States.\nThat the Senate\u2014\n**(1)**\nrecognizes community care as an essential tool for meeting the health care needs of the veterans of the United States;\n**(2)**\naffirms that community care complements, rather than threatens, the mission of the Department of Veterans Affairs (referred to in this resolution as the VA );\n**(3)**\nurges the VA to implement the VA MISSION Act of 2018 ( Public Law 115\u2013182 ; 132 Stat. 1393) in both letter and spirit, ensuring veterans have timely access to community providers when the VA cannot meet their needs; and\n**(4)**\nreaffirms the commitment of the Senate to ensuring that every veteran has timely access to high-quality, affordable, and veteran-centered care, whether provided in VA facilities or in the community.",
      "versionDate": "2025-11-10",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres492ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 492\nIN THE SENATE OF THE UNITED STATES\nNovember 10, 2025 Mrs. Blackburn (for herself, Mr. Cramer , Mr. Tillis , Mr. Wicker , and Mr. Moran ) submitted the following resolution; which was referred to the Committee on Veterans' Affairs\nDecember 17, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nRecognizing community care as an essential tool for meeting the health care needs of the veterans of the United States.\nThat the Senate\u2014\n**(1)**\nrecognizes community care as an essential tool for meeting the health care needs of the veterans of the United States;\n**(2)**\naffirms that community care complements, rather than threatens, the mission of the Department of Veterans Affairs (referred to in this resolution as the VA );\n**(3)**\nurges the VA to implement the VA MISSION Act of 2018 ( Public Law 115\u2013182 ; 132 Stat. 1393) in both letter and spirit, ensuring veterans have timely access to community providers when the VA cannot meet their needs; and\n**(4)**\nreaffirms the commitment of the Senate to ensuring that every veteran has timely access to high-quality, affordable, and veteran-centered care, whether provided in VA facilities or in the community.",
      "versionDate": "2025-12-17",
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
            "name": "Community life and organization",
            "updateDate": "2025-12-18T18:09:28Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-12-18T18:11:08Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-12-18T18:11:35Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-12-18T18:09:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-05T16:55:36Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres492is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres492ats.xml"
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
      "title": "A resolution recognizing community care as an essential tool for meeting the health care needs of the veterans of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-12T15:03:16Z"
    },
    {
      "title": "A resolution recognizing community care as an essential tool for meeting the health care needs of the veterans of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T11:56:15Z"
    }
  ]
}
```
