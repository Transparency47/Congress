# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/250?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/250
- Title: Protecting Life in Foreign Assistance Act
- Congress: 119
- Bill type: S
- Bill number: 250
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2026-02-25T13:41:39Z
- Update date including text: 2026-02-25T13:41:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/250",
    "number": "250",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Protecting Life in Foreign Assistance Act",
    "type": "S",
    "updateDate": "2026-02-25T13:41:39Z",
    "updateDateIncludingText": "2026-02-25T13:41:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-24",
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
      "actionDate": "2025-01-24",
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
        "item": {
          "date": "2025-01-24T20:14:17Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TN"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "LA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ND"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NE"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IN"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "SC"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TX"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NE"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "AL"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IN"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "WI"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s250is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 250\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mr. Lee (for himself, Mr. Budd , Mrs. Blackburn , Mr. Kennedy , Mr. Cramer , Mr. Ricketts , Mr. Banks , Mr. Scott of South Carolina , Mr. Cornyn , Mrs. Fischer , Mr. Tuberville , Mr. Young , and Mr. Johnson ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo restrict the availability of Federal funds to organizations associated with the abortion industry.\n#### 1. Short title\nThis Act may be cited as the Protecting Life in Foreign Assistance Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nIn 1984, President Ronald Reagan issued the Mexico City Policy, which prohibits foreign nongovernmental associations from performing or promoting abortions as a condition of receiving United States family planning assistance.\n**(2)**\nIn 1993, President Bill Clinton rescinded the Mexico City Policy.\n**(3)**\nIn 2001, President George W. Bush reinstated the Mexico City Policy.\n**(4)**\nIn 2009, President Barack Obama rescinded the Mexico City Policy.\n**(5)**\nIn 2017, President Donald Trump reinstated the Mexico City Policy upon taking office, renamed it Protecting Life in Global Health Assistance, and expanded it to cover all United States global health assistance funds granted to foreign nongovernmental organizations.\n**(6)**\nIn 2021, President Joe Biden rescinded the Protecting Life in Global Health Assistance Policy.\n##### (b) Sense of Congress\nIt is the sense of Congress that:\u2014\n**(1)**\nthe Protecting Life in Global Health Assistance Policy should be expanded to cover funding to foreign and domestic nongovernmental organizations, multilateral organizations, and subcontractors; and\n**(2)**\nCongress should codify this policy to prevent further inconsistency between presidential administrations.\n#### 3. Restriction on availability of Federal funds\n##### (a) In general\nNotwithstanding any other provision of law, Federal funds may not be made available for purposes outside of the United States (including its territories and possessions) to\u2014\n**(1)**\nany foreign nonprofit organization, foreign nongovernmental organization, foreign multilateral organization, or foreign quasi-autonomous nongovernmental organization that\u2014\n**(A)**\nperforms or promotes abortions, including providing referrals, counseling, lobbying, and training relating to abortions;\n**(B)**\nfurnishes or develops any item intended to procure abortions; or\n**(C)**\nprovides financial support to\u2014\n**(i)**\nany entity that conducts any of the activities described in subparagraph (A) or (B); or\n**(ii)**\nany entity described in paragraph (2); or\n**(2)**\nany domestic nonprofit organization or domestic nongovernmental organization that\u2014\n**(A)**\nperforms abortions;\n**(B)**\nfurnishes or develops any item intended to procure abortions;\n**(C)**\nwithin the scope of any program or activity that receives Federal funds\u2014\n**(i)**\nperforms or promotes abortions, including providing referrals, counseling, lobbying, and training relating to abortions; or\n**(ii)**\nfails to maintain a complete physical and financial separation from activities described in clause (i) and such failure includes co-locating such a program or activity at any site where activities described in clause (i) are conducted; or\n**(D)**\nprovides financial support to\u2014\n**(i)**\nany entity that conducts activities described in subparagraph (A), (B), or (C); or\n**(ii)**\nany entity described in paragraph (1).\n##### (b) Inclusions\nThe prohibitions described in subsection (a) include the transfer of Federal funds and goods financed with such funds.",
      "versionDate": "2025-01-24",
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
        "actionDate": "2025-02-21",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "1465",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Life in Foreign Assistance Act",
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
        "updateDate": "2025-04-17T17:54:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119s250",
          "measure-number": "250",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s250v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Life in Foreign Assistance Act</strong></p><p>This bill prohibits the provision of funding for purposes outside the United States to certain foreign or domestic organizations that\u00a0perform or promote abortions, furnish or develop items intended to procure abortions, or provide financial support for an entity that conducts such activities.</p>"
        },
        "title": "Protecting Life in Foreign Assistance Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s250.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Life in Foreign Assistance Act</strong></p><p>This bill prohibits the provision of funding for purposes outside the United States to certain foreign or domestic organizations that\u00a0perform or promote abortions, furnish or develop items intended to procure abortions, or provide financial support for an entity that conducts such activities.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s250"
    },
    "title": "Protecting Life in Foreign Assistance Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Life in Foreign Assistance Act</strong></p><p>This bill prohibits the provision of funding for purposes outside the United States to certain foreign or domestic organizations that\u00a0perform or promote abortions, furnish or develop items intended to procure abortions, or provide financial support for an entity that conducts such activities.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s250"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s250is.xml"
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
      "title": "Protecting Life in Foreign Assistance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Life in Foreign Assistance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to restrict the availability of Federal funds to organizations associated with the abortion industry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:20Z"
    }
  ]
}
```
