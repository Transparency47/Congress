# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/321?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/321
- Title: A resolution commemorating 30 years of diplomatic relations between the United States and Vietnam on July 11, 2025.
- Congress: 119
- Bill type: SRES
- Bill number: 321
- Origin chamber: Senate
- Introduced date: 2025-07-15
- Update date: 2026-03-12T15:10:20Z
- Update date including text: 2026-03-12T15:10:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in Senate
- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S4371-4372)
- 2025-12-18 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S8891-8893)
- 2025-12-18 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate with an amendment and an amended preamble by Unanimous Consent.
- 2025-12-18 - Floor: Resolution agreed to in Senate with an amendment and an amended preamble by Unanimous Consent. (text: CR S8892-8893)
- 2025-12-18 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-12-18 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- Latest action: 2025-07-15: Introduced in Senate

## Actions

- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S4371-4372)
- 2025-12-18 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S8891-8893)
- 2025-12-18 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate with an amendment and an amended preamble by Unanimous Consent.
- 2025-12-18 - Floor: Resolution agreed to in Senate with an amendment and an amended preamble by Unanimous Consent. (text: CR S8892-8893)
- 2025-12-18 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-12-18 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/321",
    "number": "321",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "A resolution commemorating 30 years of diplomatic relations between the United States and Vietnam on July 11, 2025.",
    "type": "SRES",
    "updateDate": "2026-03-12T15:10:20Z",
    "updateDateIncludingText": "2026-03-12T15:10:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate with an amendment and an amended preamble by Unanimous Consent. (text: CR S8892-8893)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate with an amendment and an amended preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Measure laid before Senate by unanimous consent. (consideration: CR S8891-8893)",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S4371-4372)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-15",
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
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "0",
                    "name": "Senate"
                  },
                  "text": "Amendment SA 4141 agreed to in Senate by Unanimous Consent.",
                  "type": "Floor"
                },
                {
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "0",
                    "name": "Senate"
                  },
                  "text": "Amendment SA 4141 proposed by Senator Thune for Senator Merkley. (consideration: CR S8892-8893) To amend the preamble.",
                  "type": "Floor"
                },
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "93000",
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment proposed (on the floor): Amendment SA 4141 proposed by Senator Thune for Senator Merkley.",
                  "type": "Floor"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                },
                {
                  "actionCode": "94000",
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment agreed to: Amendment SA 4141 agreed to in Senate by Unanimous Consent.",
                  "type": "Floor"
                }
              ]
            },
            "count": "6"
          },
          "amendedBill": {
            "congress": "119",
            "number": "321",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "A resolution commemorating 30 years of diplomatic relations between the United States and Vietnam on July 11, 2025.",
            "type": "SRES",
            "updateDateIncludingText": "2026-03-12"
          },
          "chamber": "Senate",
          "congress": "119",
          "cosponsors": {
            "count": "1",
            "countIncludingWithdrawnCosponsors": "1",
            "item": {
              "bioguideId": "D000618",
              "firstName": "Steve",
              "fullName": "Sen. Daines, Steve [R-MT]",
              "isOriginalCosponsor": "True",
              "lastName": "Daines",
              "party": "R",
              "sponsorshipDate": "2025-12-18",
              "state": "MT"
            }
          },
          "latestAction": {
            "actionDate": "2025-12-18",
            "links": {
              "link": {
                "name": "SA 4141",
                "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/4141"
              }
            },
            "text": "Amendment SA 4141 agreed to in Senate by Unanimous Consent."
          },
          "number": "4141",
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
          "proposedDate": "2025-12-18T05:00:00Z",
          "purpose": "To amend the preamble.",
          "sponsors": {
            "item": {
              "bioguideId": "M001176",
              "firstName": "Jeff",
              "fullName": "Sen. Merkley, Jeff [D-OR]",
              "lastName": "Merkley",
              "party": "D",
              "state": "OR"
            }
          },
          "submittedDate": "2025-12-18T05:00:00Z",
          "textVersions": {
            "count": "1"
          },
          "type": "SAMDT",
          "updateDate": "2025-12-19T01:11:47Z"
        },
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "0",
                    "name": "Senate"
                  },
                  "text": "Amendment SA 4140 agreed to in Senate by Unanimous Consent.",
                  "type": "Floor"
                },
                {
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "0",
                    "name": "Senate"
                  },
                  "text": "Amendment SA 4140 proposed by Senator Thune for Senator Merkley. (consideration: CR S8891-8892) In the nature of a substitute.",
                  "type": "Floor"
                },
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "93000",
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment proposed (on the floor): Amendment SA 4140 proposed by Senator Thune for Senator Merkley.",
                  "type": "Floor"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                },
                {
                  "actionCode": "94000",
                  "actionDate": "2025-12-18",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment agreed to: Amendment SA 4140 agreed to in Senate by Unanimous Consent.",
                  "type": "Floor"
                }
              ]
            },
            "count": "6"
          },
          "amendedBill": {
            "congress": "119",
            "number": "321",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "A resolution commemorating 30 years of diplomatic relations between the United States and Vietnam on July 11, 2025.",
            "type": "SRES",
            "updateDateIncludingText": "2026-03-12"
          },
          "chamber": "Senate",
          "congress": "119",
          "cosponsors": {
            "count": "1",
            "countIncludingWithdrawnCosponsors": "1",
            "item": {
              "bioguideId": "D000618",
              "firstName": "Steve",
              "fullName": "Sen. Daines, Steve [R-MT]",
              "isOriginalCosponsor": "True",
              "lastName": "Daines",
              "party": "R",
              "sponsorshipDate": "2025-12-18",
              "state": "MT"
            }
          },
          "latestAction": {
            "actionDate": "2025-12-18",
            "links": {
              "link": {
                "name": "SA 4140",
                "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/4140"
              }
            },
            "text": "Amendment SA 4140 agreed to in Senate by Unanimous Consent."
          },
          "number": "4140",
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
          "proposedDate": "2025-12-18T05:00:00Z",
          "purpose": "In the nature of a substitute.",
          "sponsors": {
            "item": {
              "bioguideId": "M001176",
              "firstName": "Jeff",
              "fullName": "Sen. Merkley, Jeff [D-OR]",
              "lastName": "Merkley",
              "party": "D",
              "state": "OR"
            }
          },
          "submittedDate": "2025-12-18T05:00:00Z",
          "textVersions": {
            "count": "1"
          },
          "type": "SAMDT",
          "updateDate": "2025-12-19T00:57:20Z"
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
        "item": [
          {
            "date": "2025-12-19T00:48:00Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-07-15T20:47:29Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres321is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 321\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Mr. Merkley (for himself and Mr. Daines ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCommemorating 30 years of diplomatic relations between the United States and Vietnam on July 11, 2025.\nThat the Senate\u2014\n**(1)**\nrecognizes\u2014\n**(A)**\nthe significance of the 30th anniversary of normalization of the bilateral relationship between the United States and Vietnam; and\n**(B)**\nthe strong and enduring relationship built by United States and Vietnam based on mutual respect, trust, and a shared commitment to peace and prosperity;\n**(2)**\nhonors the contributions of Vietnamese Americans to the United States during the past 50 years, including\u2014\n**(A)**\ntheir tireless commitment to strengthening ties among different communities, sectors, businesses, youths, and people\u2019s organizations between the United States and Vietnam; and\n**(B)**\nfacilitating reconciliation and economic prosperity between the 2 countries;\n**(3)**\nhonors\u2014\n**(A)**\nthe service of members of the United States Armed Forces who fought in Vietnam, including those who gave their lives in the conflict; and\n**(B)**\nUnited States veteran-led initiatives established and dedicated to engaging in reconciliation efforts with the Vietnamese people;\n**(4)**\nexpresses the commitment of the United States to the sustained continuation of funding and operational support to war legacy programs in Vietnam foundational to the bilateral relationship, including\u2014\n**(A)**\ndioxin remediation at Bien Hoa Airport;\n**(B)**\nunexploded ordnance removal;\n**(C)**\nsupport for persons with disabilities;\n**(D)**\ncapacity building in provincial and national efforts on mine action; and\n**(E)**\naccounting for Vietnamese missing and fallen soldiers from the war;\n**(5)**\nacknowledges the significant progress in various areas of cooperation, including political and diplomatic relations, trade and economic ties, defense and security, and people-to-people exchanges;\n**(6)**\nreaffirms the commitment of the United States to sustaining and building on the partnership officially established in the U.S.-Vietnam Comprehensive Strategic Partnership in September 2023, underscored by the fundamental principles guiding the bilateral relationship, including respect for the United Nations Charter, international law, and respect for each other\u2019s independence, sovereignty, and territorial integrity; and\n**(7)**\nexpresses\u2014\n**(A)**\nthe determination of the United States to continue strengthening cooperation across sectors; and\n**(B)**\nthe vital importance of the bilateral relationship between the United States and Vietnam to addressing shared challenges and promoting continued regional peace and stability in the Indo-Pacific region.",
      "versionDate": "2025-07-15",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres321ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 321\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Mr. Merkley (for himself and Mr. Daines ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nDecember 18, 2025 Committee discharged; considered, amended, and agreed to with an amended preamble\nRESOLUTION\nCommemorating 30 years of diplomatic relations between the United States and Vietnam on July 11, 2025.\nThat the Senate\u2014\n**(1)**\nrecognizes\u2014\n**(A)**\nthe significance of the 30th anniversary of normalization of the bilateral relationship between the United States and Vietnam; and\n**(B)**\nthe strong and enduring relationship built by the United States and Vietnam based on mutual respect, trust, and a shared commitment to peace and prosperity;\n**(2)**\nhonors the contributions of Vietnamese Americans to the United States during the past 50 years, including\u2014\n**(A)**\ntheir tireless commitment to strengthening ties between the United States and Vietnam; and\n**(B)**\nfacilitating reconciliation and economic prosperity between the 2 countries;\n**(3)**\nhonors\u2014\n**(A)**\nthe service of members of the United States Armed Forces who fought in Vietnam, including those who gave their lives in the conflict; and\n**(B)**\nUnited States veteran-led initiatives established and dedicated to engaging in reconciliation efforts with the Vietnamese people;\n**(4)**\nexpresses the commitment of the United States to the sustained continuation of funding and operational support to war legacy programs in Vietnam foundational to the bilateral relationship, including\u2014\n**(A)**\ndioxin remediation at Bien Hoa Airport;\n**(B)**\nunexploded ordnance removal;\n**(C)**\nsupport for persons with disabilities;\n**(D)**\ncapacity building in provincial and national efforts on mine action; and\n**(E)**\naccounting for Vietnamese missing and fallen soldiers from the war;\n**(5)**\nacknowledges the significant progress in various areas of bilateral cooperation, including political and diplomatic relations, trade and economic ties, defense and security, and people-to-people exchanges, including the United States-supported Fulbright University, Vietnam\u2019s first independent nonprofit higher education institution;\n**(6)**\nreaffirms the commitment of the United States to sustaining and building on the partnership officially established in the U.S.-Vietnam Comprehensive Strategic Partnership in September 2023, underscored by the fundamental principles guiding the bilateral relationship, including respect for the United Nations Charter, international law, and respect for each other\u2019s independence, sovereignty, and territorial integrity; and\n**(7)**\nexpresses\u2014\n**(A)**\nthe determination of the United States to continue strengthening cooperation with Vietnam across sectors; and\n**(B)**\nthe vital importance of the bilateral relationship between the United States and Vietnam to addressing shared challenges and promoting continued peace and stability in the Indo-Pacific region.",
      "versionDate": "2025-12-18",
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
            "name": "Asia",
            "updateDate": "2026-01-06T12:51:37Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2026-01-05T16:49:15Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-01-05T16:48:50Z"
          },
          {
            "name": "Vietnam",
            "updateDate": "2026-01-05T16:47:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-07-17T21:44:44Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres321is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres321ats.xml"
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
      "title": "A resolution commemorating 30 years of diplomatic relations between the United States and Vietnam on July 11, 2025.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T02:33:23Z"
    },
    {
      "title": "A resolution commemorating 30 years of diplomatic relations between the United States and Vietnam on July 11, 2025.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T10:56:19Z"
    }
  ]
}
```
