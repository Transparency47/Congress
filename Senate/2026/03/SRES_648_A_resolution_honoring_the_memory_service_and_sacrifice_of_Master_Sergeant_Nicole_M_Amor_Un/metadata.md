# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/648?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/648
- Title: A resolution honoring the memory, service, and sacrifice of Master Sergeant Nicole M. Amor, United States Army Reserve.
- Congress: 119
- Bill type: SRES
- Bill number: 648
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-03-30T16:17:14Z
- Update date including text: 2026-03-30T16:17:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S1095)
- 2026-03-17 - IntroReferral: Submitted in Senate
- 2026-03-25 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S1609-1610)
- 2026-03-25 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S1610)
- 2026-03-25 - Floor: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S1610)
- 2026-03-25 - Discharge: Senate Committee on Armed Services discharged by Unanimous Consent.
- 2026-03-25 - Committee: Senate Committee on Armed Services discharged by Unanimous Consent.
- Latest action: 2026-03-17: Submitted in Senate

## Actions

- 2026-03-17 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S1095)
- 2026-03-17 - IntroReferral: Submitted in Senate
- 2026-03-25 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S1609-1610)
- 2026-03-25 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S1610)
- 2026-03-25 - Floor: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S1610)
- 2026-03-25 - Discharge: Senate Committee on Armed Services discharged by Unanimous Consent.
- 2026-03-25 - Committee: Senate Committee on Armed Services discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/648",
    "number": "648",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "A resolution honoring the memory, service, and sacrifice of Master Sergeant Nicole M. Amor, United States Army Reserve.",
    "type": "SRES",
    "updateDate": "2026-03-30T16:17:14Z",
    "updateDateIncludingText": "2026-03-30T16:17:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S1610)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S1610)",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Measure laid before Senate by unanimous consent. (consideration: CR S1609-1610)",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Armed Services discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Armed Services discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Armed Services. (text: CR S1095)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
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
                "actionDate": "2026-03-25",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 4785 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2026-03-25",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 4785 proposed by Senator Thune for Senator Klobuchar. (consideration: CR S1610)",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2026-03-25",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2026-03-25",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 4785 proposed by Senator Thune for Senator Klobuchar.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2026-03-25",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2026-03-25",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 4785 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "648",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "A resolution honoring the memory, service, and sacrifice of Master Sergeant Nicole M. Amor, United States Army Reserve.",
          "type": "SRES",
          "updateDateIncludingText": "2026-03-30"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2026-03-25",
          "links": {
            "link": {
              "name": "SA 4785",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/4785"
            }
          },
          "text": "Amendment SA 4785 agreed to in Senate by Unanimous Consent."
        },
        "number": "4785",
        "onBehalfOfSponsor": {
          "item": [
            {
              "bioguideId": "T000250",
              "firstName": "John",
              "fullName": "Sen. Thune, John [R-SD]",
              "lastName": "Thune",
              "party": "R",
              "state": "SD",
              "type": "Submitted on behalf of"
            },
            {
              "bioguideId": "T000250",
              "firstName": "John",
              "fullName": "Sen. Thune, John [R-SD]",
              "lastName": "Thune",
              "party": "R",
              "state": "SD",
              "type": "Proposed on behalf of"
            }
          ]
        },
        "proposedDate": "2026-03-26T00:00:15Z",
        "purpose": "To amend the preamble.",
        "sponsors": {
          "item": {
            "bioguideId": "K000367",
            "firstName": "Amy",
            "fullName": "Sen. Klobuchar, Amy [D-MN]",
            "lastName": "Klobuchar",
            "party": "D",
            "state": "MN"
          }
        },
        "submittedDate": "2026-03-25T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-03-27T11:08:26Z"
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
        "item": [
          {
            "date": "2026-03-25T23:59:25Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-03-17T21:43:21Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres648is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 648\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Ms. Klobuchar (for herself and Ms. Smith ) submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nHonoring the memory, service, and sacrifice of Master Sergeant Nicole M. Amor, United States Army Reserve.\nThat the Senate\u2014\n**(1)**\nhonors the memory, service, and sacrifice of Master Sergeant Nicole M. Amor, United States Army Reserve;\n**(2)**\nextends its sympathies, gratitude, and support to the family of Master Sergeant Amor, and to all others affected by the attack at Port Shuaiba, Kuwait, on March 1, 2026; and\n**(3)**\nrespectfully requests that the Secretary of the Senate transmit an enrolled copy of this resolution to the family of Master Sergeant Amor.",
      "versionDate": "2026-03-17",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres648ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 648\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Ms. Klobuchar (for herself and Ms. Smith ) submitted the following resolution; which was referred to the Committee on Armed Services\nMarch 25, 2026 Committee discharged; considered and agreed to with an amended preamble\nRESOLUTION\nHonoring the memory, service, and sacrifice of Master Sergeant Nicole M. Amor, United States Army Reserve.\nThat the Senate\u2014\n**(1)**\nhonors the memory, service, and sacrifice of Master Sergeant Nicole M. Amor, United States Army Reserve;\n**(2)**\nextends its sympathies, gratitude, and support to the family of Master Sergeant Amor, and to all others affected by the attack at Port Shuaiba, Kuwait, on March 1, 2026; and\n**(3)**\nrespectfully requests that the Secretary of the Senate transmit an enrolled copy of this resolution to the family of Master Sergeant Amor.",
      "versionDate": "2026-03-25",
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
            "updateDate": "2026-03-26T20:38:10Z"
          },
          {
            "name": "Kuwait",
            "updateDate": "2026-03-26T20:38:25Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2026-03-26T20:38:29Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2026-03-26T20:38:15Z"
          },
          {
            "name": "National Guard and reserves",
            "updateDate": "2026-03-26T20:38:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-30T16:17:14Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres648is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres648ats.xml"
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
      "title": "A resolution honoring the memory, service, and sacrifice of Master Sergeant Nicole M. Amor, United States Army Reserve.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:48:40Z"
    },
    {
      "title": "A resolution honoring the memory, service, and sacrifice of Master Sergeant Nicole M. Amor, United States Army Reserve.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T10:56:24Z"
    }
  ]
}
```
