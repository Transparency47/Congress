# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/178?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/178
- Title: A resolution honoring the life and legacy of the late George Foreman.
- Congress: 119
- Bill type: SRES
- Bill number: 178
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-03-12T15:05:56Z
- Update date including text: 2026-03-12T15:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-04-10 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-05-14 - Floor: The preamble was amended after adoption by Unanimous Consent.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-04-10 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-05-14 - Floor: The preamble was amended after adoption by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/178",
    "number": "178",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Sports and Recreation"
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
    "title": "A resolution honoring the life and legacy of the late George Foreman.",
    "type": "SRES",
    "updateDate": "2026-03-12T15:05:56Z",
    "updateDateIncludingText": "2026-03-12T15:05:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "The preamble was amended after adoption by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
                "actionDate": "2025-05-14",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 2227 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2025-05-14",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 2227 proposed by Senator Thune for Senator Cornyn. (consideration: CR S2932) To amend the preamble.",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-05-14",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2025-05-14",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 2227 proposed by Senator Thune for Senator Cornyn.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-05-14",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2025-05-14",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 2227 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "178",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "A resolution honoring the life and legacy of the late George Foreman.",
          "type": "SRES",
          "updateDateIncludingText": "2026-03-12"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2025-05-14",
          "links": {
            "link": {
              "name": "SA 2227",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/2227"
            }
          },
          "text": "Amendment SA 2227 agreed to in Senate by Unanimous Consent."
        },
        "number": "2227",
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
        "proposedDate": "2025-05-14T04:00:00Z",
        "purpose": "To amend the preamble.",
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
        "submittedDate": "2025-05-14T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-03-12T15:05:55Z"
      }
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres178as.xml",
      "text": "IIIA\n119th CONGRESS\n1st Session\nS. RES. 178\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Cornyn (for himself and Mr. Cruz ) submitted the following resolution; which was considered and agreed to\nMay 14, 2025 Preamble amended by unanimous consent\nRESOLUTION\nHonoring the life and legacy of the late George Foreman.\nThat the Senate\u2014\n**(1)**\nhonors the life and legacy of George Foreman for\u2014\n**(A)**\nhis accomplishments as a boxing legend;\n**(B)**\nthe example he provides to future generations of community leaders; and\n**(C)**\nhis dedication to Houston and his support of vulnerable youth in the community; and\n**(2)**\nrespectfully requests the Secretary of the Senate\u2014\n**(A)**\ncommunicate this resolution to the House of Representatives; and\n**(B)**\ntransmit an enrolled copy of this resolution to the family of George Foreman.",
      "versionDate": "2025-05-14",
      "versionType": "AS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres178ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 178\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Cornyn (for himself and Mr. Cruz ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nHonoring the life and legacy of the late George Foreman.\nThat the Senate\u2014\n**(1)**\nhonors the life and legacy of George Foreman for\u2014\n**(A)**\nhis accomplishments as a boxing legend;\n**(B)**\nthe example he provides to future generations of community leaders; and\n**(C)**\nhis dedication to Houston and his support of vulnerable youth in the community; and\n**(2)**\nrespectfully requests the Secretary of the Senate\u2014\n**(A)**\ncommunicate this resolution to the House of Representatives; and\n**(B)**\ntransmit an enrolled copy of this resolution to the family of George Foreman.",
      "versionDate": "2025-04-10",
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
            "name": "Athletes",
            "updateDate": "2025-06-02T15:39:33Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-06-02T15:39:29Z"
          },
          {
            "name": "Professional sports",
            "updateDate": "2025-06-02T15:39:38Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-06-02T15:39:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Sports and Recreation",
        "updateDate": "2025-05-28T13:53:20Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres178as.xml"
        }
      ],
      "type": "AS"
    },
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres178ats.xml"
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
      "title": "A resolution honoring the life and legacy of the late George Foreman.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T10:56:18Z"
    },
    {
      "title": "A resolution honoring the life and legacy of the late George Foreman.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T10:56:18Z"
    }
  ]
}
```
