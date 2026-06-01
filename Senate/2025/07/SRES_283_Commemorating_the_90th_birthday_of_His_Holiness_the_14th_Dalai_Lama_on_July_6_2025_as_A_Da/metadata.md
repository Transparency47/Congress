# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/283?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/283
- Title: A resolution commemorating the 90th birthday of His Holiness the 14th Dalai Lama on July 6, 2025, as "A Day of Compassion" and expressing support for the human rights and distinct religious, cultural, linguistic, and historical identity of the Tibetan people.
- Congress: 119
- Bill type: SRES
- Bill number: 283
- Origin chamber: Senate
- Introduced date: 2025-06-17
- Update date: 2026-03-12T15:06:59Z
- Update date including text: 2026-03-12T15:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in Senate
- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3439-3440)
- 2025-07-14 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S4342)
- 2025-07-14 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate with an amendment and with a preamble by Unanimous Consent.
- 2025-07-14 - Floor: Resolution agreed to in Senate with an amendment and with a preamble by Unanimous Consent. (text: CR S4342-4343)
- 2025-07-14 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-07-14 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-06-17: Introduced in Senate

## Actions

- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3439-3440)
- 2025-07-14 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S4342)
- 2025-07-14 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate with an amendment and with a preamble by Unanimous Consent.
- 2025-07-14 - Floor: Resolution agreed to in Senate with an amendment and with a preamble by Unanimous Consent. (text: CR S4342-4343)
- 2025-07-14 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-07-14 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/283",
    "number": "283",
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
    "title": "A resolution commemorating the 90th birthday of His Holiness the 14th Dalai Lama on July 6, 2025, as \"A Day of Compassion\" and expressing support for the human rights and distinct religious, cultural, linguistic, and historical identity of the Tibetan people.",
    "type": "SRES",
    "updateDate": "2026-03-12T15:06:59Z",
    "updateDateIncludingText": "2026-03-12T15:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate with an amendment and with a preamble by Unanimous Consent. (text: CR S4342-4343)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate with an amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Measure laid before Senate by unanimous consent. (consideration: CR S4342)",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-14",
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
      "actionDate": "2025-07-14",
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
      "actionDate": "2025-06-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S3439-3440)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-17",
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
                "actionDate": "2025-07-14",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 2852 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2025-07-14",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 2852 proposed by Senator Thune for Senator Merkley. (consideration: CR S4342) To improve the resolution.",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-07-14",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2025-07-14",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 2852 proposed by Senator Thune for Senator Merkley.",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2025-07-14",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 2852 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-07-14",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "283",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "A resolution commemorating the 90th birthday of His Holiness the 14th Dalai Lama on July 6, 2025, as \"A Day of Compassion\" and expressing support for the human rights and distinct religious, cultural, linguistic, and historical identity of the Tibetan people.",
          "type": "SRES",
          "updateDateIncludingText": "2026-03-12"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2025-07-14",
          "links": {
            "link": {
              "name": "SA 2852",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/2852"
            }
          },
          "text": "Amendment SA 2852 agreed to in Senate by Unanimous Consent."
        },
        "number": "2852",
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
        "proposedDate": "2025-07-14T04:00:00Z",
        "purpose": "To improve the resolution.",
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
        "submittedDate": "2025-07-14T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-03-12T15:06:59Z"
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
            "date": "2025-07-14T22:55:25Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-06-17T21:06:46Z",
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "IN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "NH"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "UT"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "NV"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "NE"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "ID"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "AK"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "VT"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MA"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "WA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres283is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 283\nIN THE SENATE OF THE UNITED STATES\nJune 17, 2025 Mr. Merkley (for himself, Mr. Young , Mrs. Shaheen , Mr. Curtis , Ms. Rosen , Mr. Ricketts , Mr. Crapo , and Mr. Sullivan ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCommemorating the 90th birthday of His Holiness the 14th Dalai Lama on July 6, 2025, as A Day of Compassion and expressing support for the human rights and distinct religious, cultural, linguistic, and historical identity of the Tibetan people.\nThat the Senate\u2014\n**(1)**\nrecognizes July 6, 2025, as a Day of Compassion ;\n**(2)**\ncongratulates His Holiness the 14th Dalai Lama on his 90th birthday and affirms its recognition of his outstanding contributions to peace, nonviolence, human rights, and mutual respect within and across faiths;\n**(3)**\naffirms the Tibetan people\u2019s human rights and fundamental freedoms, including their right to exercise regional autonomy and to protect the distinct religious, cultural, linguistic, and historical identity of the Tibetan people;\n**(4)**\nreiterates, as outlined in the Tibetan Policy and Support Act of 2020 (subtitle E of title III of division K of Public Law 116\u2013260 ), that the identification and installation of Tibetan Buddhist religious leaders, including a future 15th Dalai Lama, is a matter that should be determined by the present 14th Dalai Lama and within the Tibetan Buddhist faith community, in accordance with the inalienable right to religious freedom;\n**(5)**\nreiterates that any attempt by the Government of the People\u2019s Republic of China or any other government to recognize a successor or reincarnation of the 14th Dalai Lama and any future Dalai Lamas not selected by the Tibetan people would represent a clear abuse of the right to religious freedom of Tibetan Buddhists and the Tibetan people; and\n**(6)**\nrequests that a copy of this resolution be presented to His Holiness the Dalai Lama as an expression of its esteem and respect.",
      "versionDate": "2025-06-17",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres283ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 283\nIN THE SENATE OF THE UNITED STATES\nJune 17, 2025 Mr. Merkley (for himself, Mr. Young , Mrs. Shaheen , Mr. Curtis , Ms. Rosen , Mr. Ricketts , Mr. Crapo , Mr. Sullivan , Mr. Welch , Mr. Schumer , Mr. Markey , Ms. Cantwell , and Mr. Wyden ) submitted the following resolution; which was referred to the Committee on the Judiciary\nJuly 14, 2025 Committee discharged; considered, amended, and agreed to\nRESOLUTION\nCommemorating the 90th birthday of His Holiness the 14th Dalai Lama on July 6, 2025, as A Day of Compassion and expressing support for the human rights and distinct religious, cultural, linguistic, and historical identity of the Tibetan people.\nThat the Senate\u2014\n**(1)**\nrecognizes July 6, 2025, as a Day of Compassion ;\n**(2)**\ncongratulates His Holiness the 14th Dalai Lama on his 90th birthday and affirms its recognition of his outstanding contributions to peace, nonviolence, human rights, and mutual respect within and across faiths;\n**(3)**\naffirms the Tibetan people's internationally recognized human rights and fundamental freedoms, including their right to exercise regional autonomy and to protect the distinct religious, cultural, linguistic, and historical identity of the Tibetan people;\n**(4)**\nreiterates, as outlined in the Tibetan Policy and Support Act of 2020 (subtitle E of title III of division K of Public Law 116\u2013260 ), that the identification and installation of Tibetan Buddhist religious leaders, including a future 15th Dalai Lama, is a matter that should be determined by the present 14th Dalai Lama and within the Tibetan Buddhist faith community, in accordance with the inalienable right to religious freedom;\n**(5)**\nreiterates that any attempt by the Government of the People\u2019s Republic of China or any other government to recognize a successor or reincarnation of the 14th Dalai Lama and any future Dalai Lamas not selected by the Tibetan people would represent a clear abuse of the right to religious freedom of Tibetan Buddhists and the Tibetan people; and\n**(6)**\nrequests that a copy of this resolution be presented to His Holiness the Dalai Lama as an expression of its esteem and respect.",
      "versionDate": "2025-07-14",
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
            "updateDate": "2025-07-24T13:13:15Z"
          },
          {
            "name": "China",
            "updateDate": "2025-07-24T13:13:21Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-07-24T13:12:51Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-07-24T13:13:35Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-07-24T13:13:04Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-07-24T13:12:57Z"
          },
          {
            "name": "Tibet",
            "updateDate": "2025-07-24T13:13:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-07-22T12:39:05Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres283is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres283ats.xml"
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
      "title": "A resolution commemorating the 90th birthday of His Holiness the 14th Dalai Lama on July 6, 2025, as \"A Day of Compassion\" and expressing support for the human rights and distinct religious, cultural, linguistic, and historical identity of the Tibetan people.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:36Z"
    },
    {
      "title": "A resolution commemorating the 90th birthday of His Holiness the 14th Dalai Lama on July 6, 2025, as \"A Day of Compassion\" and expressing support for the human rights and distinct religious, cultural, linguistic, and historical identity of the Tibetan people.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T10:56:16Z"
    }
  ]
}
```
