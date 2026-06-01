# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3052?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3052
- Title: A bill to promote recruiter access to secondary schools.
- Congress: 119
- Bill type: S
- Bill number: 3052
- Origin chamber: Senate
- Introduced date: 2025-10-23
- Update date: 2026-03-09T19:59:36Z
- Update date including text: 2026-03-09T19:59:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-23: Introduced in Senate
- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-10-23: Introduced in Senate

## Actions

- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-23",
    "latestAction": {
      "actionDate": "2025-10-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3052",
    "number": "3052",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "A bill to promote recruiter access to secondary schools.",
    "type": "S",
    "updateDate": "2026-03-09T19:59:36Z",
    "updateDateIncludingText": "2026-03-09T19:59:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-23",
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
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionDate": "2025-12-15",
                "committees": {
                  "item": {
                    "name": "Armed Services Committee",
                    "systemCode": "ssas00"
                  }
                },
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Referred to the Committee on Armed Services.",
                "type": "IntroReferral"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-12-15",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-12-15",
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
          "number": "3052",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "A bill to promote recruiter access to secondary schools.",
          "type": "S",
          "updateDateIncludingText": "2026-03-09"
        },
        "chamber": "Senate",
        "congress": "119",
        "cosponsors": {
          "count": "1",
          "countIncludingWithdrawnCosponsors": "1",
          "item": {
            "bioguideId": "K000377",
            "firstName": "Mark",
            "fullName": "Sen. Kelly, Mark [D-AZ]",
            "isOriginalCosponsor": "True",
            "lastName": "Kelly",
            "party": "D",
            "sponsorshipDate": "2025-12-15",
            "state": "AZ"
          }
        },
        "latestAction": {
          "actionDate": "2025-12-15",
          "text": "Referred to the Committee on Armed Services."
        },
        "number": "3989",
        "sponsors": {
          "item": {
            "bioguideId": "C001056",
            "firstName": "John",
            "fullName": "Sen. Cornyn, John [R-TX]",
            "lastName": "Cornyn",
            "party": "R",
            "state": "TX"
          }
        },
        "submittedDate": "2025-12-15T05:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2025-12-15T23:48:26Z"
      }
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
          "date": "2025-10-23T19:51:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3052is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3052\nIN THE SENATE OF THE UNITED STATES\nOctober 23, 2025 Mr. Cornyn (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo promote recruiter access to secondary schools.\n#### 1. Recruiter access to secondary schools\nSection 503(c)(1)(A) of chapter 31 of title 10, United States Code, is amended\u2014\n**(1)**\nby amending clause (i) to read as follows:\n(i) shall provide military recruiters the same access to the campus of each secondary school served by the local educational agency for the purpose of recruiting students who are at least 17 years of age that is provided to any prospective employer, institution of higher education, or other recruiter; ;\n**(2)**\nin clause (ii), by striking provide to military recruiters access to and inserting facilitate upon request made by military recruiters for military recruiting purposes not fewer than four in-person recruitment events per academic year, across different grading periods, which may include ; and\n**(3)**\nby amending clause (iii) to read as follows:\n(iii) shall provide to military recruiters within 60 days of the commencement of the academic year, and thereafter within 30 days of a recruiter request, access to secondary school student names, academic grade, addresses, electronic mail addresses (which shall be the electronic mail addresses provided by the school, if available), and telephone and mobile phone listings, notwithstanding subsection (a)(5) of section 444 of the General Education Provisions Act ( 20 U.S.C. 1232g ). .",
      "versionDate": "2025-10-23",
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-02T18:24:17Z"
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
      "date": "2025-10-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3052is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote recruiter access to secondary schools.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-29T06:03:19Z"
    },
    {
      "title": "A bill to promote recruiter access to secondary schools.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-24T10:56:15Z"
    }
  ]
}
```
