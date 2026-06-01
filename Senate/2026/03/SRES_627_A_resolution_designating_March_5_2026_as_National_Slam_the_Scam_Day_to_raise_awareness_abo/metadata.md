# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/627?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/627
- Title: A resolution designating March 5, 2026, as "National Slam the Scam Day" to raise awareness about pervasive scams and to prevent government imposter scams and other types of scams by promoting education about such scams.
- Congress: 119
- Bill type: SRES
- Bill number: 627
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-04-20T22:19:21Z
- Update date including text: 2026-04-21T05:48:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S887-888)
- 2026-03-05 - IntroReferral: Submitted in Senate
- 2026-04-15 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-04-15 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1789)
- 2026-04-15 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-04-15 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2026-03-05: Submitted in Senate

## Actions

- 2026-03-05 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S887-888)
- 2026-03-05 - IntroReferral: Submitted in Senate
- 2026-04-15 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-04-15 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1789)
- 2026-04-15 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-04-15 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/627",
    "number": "627",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A resolution designating March 5, 2026, as \"National Slam the Scam Day\" to raise awareness about pervasive scams and to prevent government imposter scams and other types of scams by promoting education about such scams.",
    "type": "SRES",
    "updateDate": "2026-04-20T22:19:21Z",
    "updateDateIncludingText": "2026-04-21T05:48:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1789)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S887-888)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-05",
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
      "text": "Submitted in Senate",
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
            "date": "2026-04-16T01:59:22Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-03-05T17:24:37Z",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "GA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "ME"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "TN"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "SD"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres627is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 627\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Scott of Florida (for himself, Mr. Kelly , Mrs. Gillibrand , Mr. Warnock , Mr. Blumenthal , Ms. Collins , Mrs. Blackburn , Mr. Rounds , and Mrs. Moody ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating March 5, 2026, as National Slam the Scam Day to raise awareness about pervasive scams and to prevent government imposter scams and other types of scams by promoting education about such scams.\nThat the Senate\u2014\n**(1)**\ndesignates March 5, 2026, as National Slam the Scam Day ;\n**(2)**\nrecognizes National Slam the Scam Day as an opportunity to raise awareness and amplify the messaging about scams that involve individuals impersonating government employees by any means, including by mail, telephone, text message, email, social media, or internet websites (referred to in this resolution as government imposter scams );\n**(3)**\nrecognizes that law enforcement agencies, consumer protection groups, telephone companies, area agencies on aging, and financial institutions all play vital roles in\u2014\n**(A)**\npreventing government imposter scams from targeting the people of the United States; and\n**(B)**\neducating the people of the United States about government imposter scams;\n**(4)**\nencourages\u2014\n**(A)**\nthe implementation of policies and programs to prevent government imposter scams; and\n**(B)**\nthe improvement of measures to protect the people of the United States from government imposter scams;\n**(5)**\nencourages members of the public to\u2014\n**(A)**\nignore solicitations from individuals falsely claiming to represent government agencies;\n**(B)**\nshare information about government imposter scams with family and friends; and\n**(C)**\nreport government imposter scams to the corresponding agency, such as\u2014\n**(i)**\nthe Office of the Inspector General of the Social Security Administration;\n**(ii)**\nthe Treasury Inspector General for Tax Administration; or\n**(iii)**\nthe Federal Trade Commission; and\n**(6)**\nhonors the commitment and dedication of the individuals and organizations that work tirelessly to fight against government imposter scams.",
      "versionDate": "2026-03-05",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres627ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 627\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Scott of Florida (for himself, Mr. Kelly , Mrs. Gillibrand , Mr. Warnock , Mr. Blumenthal , Ms. Collins , Mrs. Blackburn , Mr. Rounds , Mrs. Moody , and Ms. Alsobrooks ) submitted the following resolution; which was referred to the Committee on the Judiciary\nApril 15 (legislative day, April 14), 2026 Committee discharged; considered and agreed to\nRESOLUTION\nDesignating March 5, 2026, as National Slam the Scam Day to raise awareness about pervasive scams and to prevent government imposter scams and other types of scams by promoting education about such scams.\nThat the Senate\u2014\n**(1)**\ndesignates March 5, 2026, as National Slam the Scam Day ;\n**(2)**\nrecognizes National Slam the Scam Day as an opportunity to raise awareness and amplify the messaging about scams that involve individuals impersonating government employees by any means, including by mail, telephone, text message, email, social media, or internet websites (referred to in this resolution as government imposter scams );\n**(3)**\nrecognizes that law enforcement agencies, consumer protection groups, telephone companies, area agencies on aging, and financial institutions all play vital roles in\u2014\n**(A)**\npreventing government imposter scams from targeting the people of the United States; and\n**(B)**\neducating the people of the United States about government imposter scams;\n**(4)**\nencourages\u2014\n**(A)**\nthe implementation of policies and programs to prevent government imposter scams; and\n**(B)**\nthe improvement of measures to protect the people of the United States from government imposter scams;\n**(5)**\nencourages members of the public to\u2014\n**(A)**\nignore solicitations from individuals falsely claiming to represent government agencies;\n**(B)**\nshare information about government imposter scams with family and friends; and\n**(C)**\nreport government imposter scams to the corresponding agency, such as\u2014\n**(i)**\nthe Office of the Inspector General of the Social Security Administration;\n**(ii)**\nthe Treasury Inspector General for Tax Administration; or\n**(iii)**\nthe Federal Trade Commission; and\n**(6)**\nhonors the commitment and dedication of the individuals and organizations that work tirelessly to fight against government imposter scams.",
      "versionDate": "2026-04-15",
      "versionType": "ATS"
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
        "actionDate": "2025-03-06",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1616-1617; text: CR S1609-1610)"
      },
      "number": "118",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution designating March 6, 2025, as \"National Slam the Scam Day\" to raise awareness about pervasive scams and to promote education to prevent government imposter scams and other types of scams.",
      "type": "SRES"
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
        "name": "Commerce",
        "updateDate": "2026-04-20T22:19:21Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres627is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres627ats.xml"
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
      "title": "A resolution designating March 5, 2026, as \"National Slam the Scam Day\" to raise awareness about pervasive scams and to prevent government imposter scams and other types of scams by promoting education about such scams.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-07T04:18:28Z"
    },
    {
      "title": "A resolution designating March 5, 2026, as \"National Slam the Scam Day\" to raise awareness about pervasive scams and to prevent government imposter scams and other types of scams by promoting education about such scams.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T11:56:28Z"
    }
  ]
}
```
