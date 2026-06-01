# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/708?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/708
- Title: A resolution amending rule XXXVII of the Standing Rules of the Senate to prohibit Senators from trading on prediction markets.
- Congress: 119
- Bill type: SRES
- Bill number: 708
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-18T19:24:55Z
- Update date including text: 2026-05-18T19:24:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate with amendments by Unanimous Consent.
- 2026-04-30 - Floor: Resolution agreed to in Senate with amendments by Unanimous Consent.
- 2026-04-30 - IntroReferral: Submitted in Senate
- 2026-04-30 - IntroReferral: Submitted in the Senate.
- Latest action: 2026-04-30: Submitted in Senate

## Actions

- 2026-04-30 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate with amendments by Unanimous Consent.
- 2026-04-30 - Floor: Resolution agreed to in Senate with amendments by Unanimous Consent.
- 2026-04-30 - IntroReferral: Submitted in Senate
- 2026-04-30 - IntroReferral: Submitted in the Senate.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/708",
    "number": "708",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "A resolution amending rule XXXVII of the Standing Rules of the Senate to prohibit Senators from trading on prediction markets.",
    "type": "SRES",
    "updateDate": "2026-05-18T19:24:55Z",
    "updateDateIncludingText": "2026-05-18T19:24:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate with amendments by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate with amendments by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-30",
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
                "actionDate": "2026-04-30",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 5442 as modified agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2026-04-30",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 5442 proposed by Senator Moreno for Senator Padilla. (consideration: CR S2161)",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2026-04-30",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2026-04-30",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 5442 proposed by Senator Moreno for Senator Padilla.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2026-04-30",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2026-04-30",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 5442 as modified agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "708",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "A resolution amending rule XXXVII of the Standing Rules of the Senate to prohibit Senators from trading on prediction markets.",
          "type": "SRES",
          "updateDateIncludingText": "2026-05-18"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2026-04-30",
          "links": {
            "link": {
              "name": "SA 5442",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/5442"
            }
          },
          "text": "Amendment SA 5442 as modified agreed to in Senate by Unanimous Consent."
        },
        "number": "5442",
        "onBehalfOfSponsor": {
          "item": [
            {
              "bioguideId": "M001242",
              "firstName": "Bernie",
              "fullName": "Sen. Moreno, Bernie [R-OH]",
              "lastName": "Moreno",
              "party": "R",
              "state": "OH",
              "type": "Submitted on behalf of"
            },
            {
              "bioguideId": "M001242",
              "firstName": "Bernie",
              "fullName": "Sen. Moreno, Bernie [R-OH]",
              "lastName": "Moreno",
              "party": "R",
              "state": "OH",
              "type": "Proposed on behalf of"
            }
          ]
        },
        "proposedDate": "2026-04-30T04:00:00Z",
        "purpose": "To improve the bill.",
        "sponsors": {
          "item": {
            "bioguideId": "P000145",
            "firstName": "Alex",
            "fullName": "Sen. Padilla, Alex [D-CA]",
            "lastName": "Padilla",
            "party": "D",
            "state": "CA"
          }
        },
        "submittedDate": "2026-04-30T04:00:00Z",
        "textVersions": {
          "count": "2"
        },
        "type": "SAMDT",
        "updateDate": "2026-05-02T11:08:27Z"
      }
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres708ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 708\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Moreno submitted the following resolution; which was considered amended and agreed to\nRESOLUTION\nAmending rule XXXVII of the Standing Rules of the Senate to prohibit Senators from trading on prediction markets.\n#### 1. Prohibition on prediction market trading by Senators\nRule XXXVII of the Standing Rules of the Senate is amended\u2014\n**(1)**\nby redesignating paragraph 15 as paragraph 16; and\n**(2)**\nby inserting after paragraph 14 the following:\n15. No Member, officer, or employee of the Senate may enter into, or offer to enter into, an agreement, contract, swap, or transaction that provides for any purchase, sale, payment, or delivery of an excluded commodity, as defined in section 1a of the Commodity Exchange Act ( 7 U.S.C. 1a ), that is dependent on the occurrence, nonoccurrence, or the extent of the occurrence of a specific event or contingency. Nothing in this paragraph shall be construed to apply to insurance for which the insured holds a lawful insurable interest. .\n#### 2. Sense of the Senate\nIt is the sense of the Senate that the House of Representatives, executive branch, and judicial branch should establish restrictions similar to those under section 1 relating to participation in prediction markets.",
      "versionDate": "2026-04-30",
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
        "name": "Congress",
        "updateDate": "2026-05-18T19:24:54Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres708ats.xml"
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
      "title": "A resolution amending rule XXXVII of the Standing Rules of the Senate to prohibit Senators from trading on prediction markets.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T10:56:34Z"
    },
    {
      "title": "A resolution amending rule XXXVII of the Standing Rules of the Senate to prohibit Senators from trading on prediction markets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T10:56:34Z"
    }
  ]
}
```
