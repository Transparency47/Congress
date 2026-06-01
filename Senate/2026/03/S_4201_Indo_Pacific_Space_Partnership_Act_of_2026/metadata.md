# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4201?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4201
- Title: Indo-Pacific Space Partnership Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4201
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-05-13T21:42:37Z
- Update date including text: 2026-05-13T21:42:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4201",
    "number": "4201",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Indo-Pacific Space Partnership Act of 2026",
    "type": "S",
    "updateDate": "2026-05-13T21:42:37Z",
    "updateDateIncludingText": "2026-05-13T21:42:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-25",
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
      "amendment": [
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionDate": "2026-04-15",
                  "committees": {
                    "item": {
                      "name": "Foreign Relations Committee",
                      "systemCode": "ssfr00"
                    }
                  },
                  "sourceSystem": {
                    "code": "0",
                    "name": "Senate"
                  },
                  "text": "Referred to the Committee on Foreign Relations.",
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2026-04-15",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2026-04-15",
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
            "number": "4201",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "Indo-Pacific Space Partnership Act of 2026",
            "type": "S",
            "updateDateIncludingText": "2026-05-13"
          },
          "chamber": "Senate",
          "congress": "119",
          "latestAction": {
            "actionDate": "2026-04-15",
            "text": "Referred to the Committee on Foreign Relations."
          },
          "number": "4792",
          "purpose": "To amend the title.",
          "sponsors": {
            "item": {
              "bioguideId": "B001267",
              "firstName": "Michael",
              "fullName": "Sen. Bennet, Michael F. [D-CO]",
              "lastName": "Bennet",
              "party": "D",
              "state": "CO"
            }
          },
          "submittedDate": "2026-04-15T04:00:00Z",
          "textVersions": {
            "count": "1"
          },
          "type": "SAMDT",
          "updateDate": "2026-04-16T11:08:30Z"
        },
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionDate": "2026-04-15",
                  "committees": {
                    "item": {
                      "name": "Foreign Relations Committee",
                      "systemCode": "ssfr00"
                    }
                  },
                  "sourceSystem": {
                    "code": "0",
                    "name": "Senate"
                  },
                  "text": "Referred to the Committee on Foreign Relations.",
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2026-04-15",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2026-04-15",
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
            "number": "4201",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "Indo-Pacific Space Partnership Act of 2026",
            "type": "S",
            "updateDateIncludingText": "2026-05-13"
          },
          "chamber": "Senate",
          "congress": "119",
          "cosponsors": {
            "count": "1",
            "countIncludingWithdrawnCosponsors": "1",
            "item": {
              "bioguideId": "C001096",
              "firstName": "Kevin",
              "fullName": "Sen. Cramer, Kevin [R-ND]",
              "isOriginalCosponsor": "True",
              "lastName": "Cramer",
              "party": "R",
              "sponsorshipDate": "2026-04-15",
              "state": "ND"
            }
          },
          "latestAction": {
            "actionDate": "2026-04-15",
            "text": "Referred to the Committee on Foreign Relations."
          },
          "number": "4791",
          "purpose": "In the nature of a substitute.",
          "sponsors": {
            "item": {
              "bioguideId": "B001267",
              "firstName": "Michael",
              "fullName": "Sen. Bennet, Michael F. [D-CO]",
              "lastName": "Bennet",
              "party": "D",
              "state": "CO"
            }
          },
          "submittedDate": "2026-04-15T04:00:00Z",
          "textVersions": {
            "count": "1"
          },
          "type": "SAMDT",
          "updateDate": "2026-04-16T11:08:30Z"
        }
      ]
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
          "date": "2026-03-25T20:18:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sponsorshipDate": "2026-03-25",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4201is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4201\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mr. Bennet (for himself and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require the Chief of Space Operations to submit a feasibility report on expanding the Multinational Force Operation Olympic Defender.\n#### 1. Short title\nThis Act may be cited as the Indo-Pacific Space Partnership Act of 2026 .\n#### 2. Feasibility report on expanding Multinational Force Operation Olympic Defender\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Chief of Space Operations shall submit to the appropriate committees of Congress a report on the feasibility and advisability of expanding the Multinational Force Operation Olympic Defender to include additional allies in the Indo-Pacific region, including Japan and the Republic of Korea.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nA description of current activities and initiatives to facilitate the expansion of the Multinational Force Operation Olympic Defender to allied countries in the Indo-Pacific region, including Japan and the Republic of Korea.\n**(2)**\nAn identification of any policy change the Government of Japan, the Government of the Republic of Korea, and the government of any other allied country in the Indo-Pacific region identified by the Chief of Space Operations would need to make in order for the United States to extend a formal invitation for such countries to join the Multinational Force Operation Olympic Defender.\n**(3)**\nAn identification of any funding or policy change necessary to facilitate the accession to the Multinational Force Operation Olympic Defender of Japan, the Republic of Korea, and any other allied country in the Indo-Pacific region identified by the Chief of Space Operations.\n**(4)**\nAn assessment of each of the following:\n**(A)**\nThe manner in which the accession to the Multinational Force Operation Olympic Defender of Japan, the Republic of Korea, and any other allied country in the Indo-Pacific region identified by the Chief of Space Operations would affect United States national security interests.\n**(B)**\nWhether the accession to the Multinational Force Operation Olympic Defender of Japan and the Republic of Korea\u2014\n**(i)**\nis feasible; and\n**(ii)**\nwould be in the national interest of the United States.\n**(C)**\nThe additional resources or authorities needed from the executive and legislative branches to carry out the accession to the Multinational Force Operation Olympic Defender of Japan and the Republic of Korea.\n##### (c) Appropriate committees of Congress defined\nIn this section, the term appropriate committees of Congress means\u2014\n**(1)**\nthe Committee on Armed Services and the Committee on Foreign Relations of the Senate; and\n**(2)**\nthe Committee on Armed Services and the Committee on Foreign Affairs of the House of Representatives.",
      "versionDate": "2026-03-25",
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
        "actionDate": "2026-04-29",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "8584",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Indo-Pacific Space Partnership Act of 2026",
      "type": "HR"
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
        "name": "International Affairs",
        "updateDate": "2026-04-13T21:11:41Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4201is.xml"
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
      "title": "Indo-Pacific Space Partnership Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Indo-Pacific Space Partnership Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Chief of Space Operations to submit a feasibility report on expanding the Multinational Force Operation Olympic Defender.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:34Z"
    }
  ]
}
```
