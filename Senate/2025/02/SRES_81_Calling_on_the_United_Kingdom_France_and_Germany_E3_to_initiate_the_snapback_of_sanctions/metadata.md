# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/81?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/81
- Title: A resolution calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).
- Congress: 119
- Bill type: SRES
- Bill number: 81
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-03-12T15:07:20Z
- Update date including text: 2026-03-12T15:07:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S982)
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S982)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/81",
    "number": "81",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "A resolution calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).",
    "type": "SRES",
    "updateDate": "2026-03-12T15:07:20Z",
    "updateDateIncludingText": "2026-03-12T15:07:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S982)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
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
                  "actionDate": "2025-07-23",
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
                  "actionDate": "2025-07-23",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2025-07-23",
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
            "number": "81",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "A resolution calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).",
            "type": "SRES",
            "updateDateIncludingText": "2026-03-12"
          },
          "chamber": "Senate",
          "congress": "119",
          "latestAction": {
            "actionDate": "2025-07-23",
            "text": "Referred to the Committee on Foreign Relations."
          },
          "number": "3006",
          "purpose": "In the nature of a substitute.",
          "sponsors": {
            "item": {
              "bioguideId": "P000603",
              "firstName": "Rand",
              "fullName": "Sen. Paul, Rand [R-KY]",
              "lastName": "Paul",
              "party": "R",
              "state": "KY"
            }
          },
          "submittedDate": "2025-07-23T04:00:00Z",
          "textVersions": {
            "count": "1"
          },
          "type": "SAMDT",
          "updateDate": "2025-07-23T21:25:28Z"
        },
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionDate": "2025-07-23",
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
                  "actionDate": "2025-07-23",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2025-07-23",
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
            "number": "81",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "A resolution calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).",
            "type": "SRES",
            "updateDateIncludingText": "2026-03-12"
          },
          "chamber": "Senate",
          "congress": "119",
          "latestAction": {
            "actionDate": "2025-07-23",
            "text": "Referred to the Committee on Foreign Relations."
          },
          "number": "3005",
          "purpose": "To amend the preamble.",
          "sponsors": {
            "item": {
              "bioguideId": "P000603",
              "firstName": "Rand",
              "fullName": "Sen. Paul, Rand [R-KY]",
              "lastName": "Paul",
              "party": "R",
              "state": "KY"
            }
          },
          "submittedDate": "2025-07-23T04:00:00Z",
          "textVersions": {
            "count": "1"
          },
          "type": "SAMDT",
          "updateDate": "2025-07-23T21:25:11Z"
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
          "date": "2025-02-13T20:14:21Z",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WY"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WV"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TN"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WV"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "MT"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AK"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WY"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "ID"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NE"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "OK"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "ME"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NC"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "ID"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres81is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 81\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Ricketts (for himself, Mr. Cornyn , Mr. Barrasso , Mrs. Capito , Mrs. Blackburn , Mr. Justice , Mr. Hagerty , Mr. Sheehy , Mr. Sullivan , Ms. Lummis , Mr. Crapo , Mrs. Fischer , Mr. Cruz , and Mr. Young ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCalling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).\nThat the Senate\u2014\n**(1)**\nrecognizes that Iran\u2019s possession of a nuclear weapon would threaten not only the security of the United States, but global security at large, including United States allies and partners in Europe and the Middle East;\n**(2)**\ncondemns the Government of Iran\u2019s flagrant and repeated violations of commitments it made under the JCPOA and its international obligations under UNSCR 2231;\n**(3)**\ncondemns the Russian Federation and the People\u2019s Republic of China, who remain participants in the JCPOA, for their role in supporting Iran\u2019s malign activities;\n**(4)**\nreaffirms that the United States Government maintains the right to take any necessary measures to prevent the Government of Iran from acquiring nuclear weapons;\n**(5)**\nsupports the imposition and enforcement of robust sanctions on Iran for its nuclear and missile programs and on entities and individuals involved in these programs to deter further proliferation efforts; and\n**(6)**\nurges the E3 to invoke the snapback of United Nations sanctions against Iran under UNSCR 2231 as soon as possible before the option expires on October 18, 2025.",
      "versionDate": "2025-02-13",
      "versionType": "IS"
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
        "actionDate": "2025-02-14",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "139",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-02-20T14:54:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119sres81",
          "measure-number": "81",
          "measure-type": "sres",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres81v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>The resolution urges the E3 (the United Kingdom, France, and Germany) to invoke the snapback of United Nations (UN) sanctions against Iran under UN Security Council Resolution 2231 before the option expires on October 18, 2025.\u00a0</p><p>This resolution also (1) recognizes that Iran's possession of a nuclear weapon would threaten U.S. and global security, (2) condemns Iran's repeated violations of certain international commitments related to nuclear weapons, and (3) reaffirms that the United States maintains the right to prevent Iran from acquiring nuclear weapons.</p>"
        },
        "title": "A resolution calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015)."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres81.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>The resolution urges the E3 (the United Kingdom, France, and Germany) to invoke the snapback of United Nations (UN) sanctions against Iran under UN Security Council Resolution 2231 before the option expires on October 18, 2025.\u00a0</p><p>This resolution also (1) recognizes that Iran's possession of a nuclear weapon would threaten U.S. and global security, (2) condemns Iran's repeated violations of certain international commitments related to nuclear weapons, and (3) reaffirms that the United States maintains the right to prevent Iran from acquiring nuclear weapons.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119sres81"
    },
    "title": "A resolution calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015)."
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>The resolution urges the E3 (the United Kingdom, France, and Germany) to invoke the snapback of United Nations (UN) sanctions against Iran under UN Security Council Resolution 2231 before the option expires on October 18, 2025.\u00a0</p><p>This resolution also (1) recognizes that Iran's possession of a nuclear weapon would threaten U.S. and global security, (2) condemns Iran's repeated violations of certain international commitments related to nuclear weapons, and (3) reaffirms that the United States maintains the right to prevent Iran from acquiring nuclear weapons.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119sres81"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres81is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-15T05:18:37Z"
    },
    {
      "title": "A resolution calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:56:17Z"
    }
  ]
}
```
