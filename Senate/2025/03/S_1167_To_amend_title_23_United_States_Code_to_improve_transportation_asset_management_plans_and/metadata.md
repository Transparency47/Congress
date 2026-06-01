# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1167?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1167
- Title: Transportation Asset Management Simplification Act
- Congress: 119
- Bill type: S
- Bill number: 1167
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2025-08-05T17:07:04Z
- Update date including text: 2025-08-05T17:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-07-23 - Committee: Committee on Environment and Public Works Senate Subcommittee on Transportation and Infrastructure. Hearings held.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-07-23 - Committee: Committee on Environment and Public Works Senate Subcommittee on Transportation and Infrastructure. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1167",
    "number": "1167",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Transportation Asset Management Simplification Act",
    "type": "S",
    "updateDate": "2025-08-05T17:07:04Z",
    "updateDateIncludingText": "2025-08-05T17:07:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Subcommittee",
          "systemCode": "ssev08"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works Senate Subcommittee on Transportation and Infrastructure. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T15:15:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-23T19:08:03Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Transportation and Infrastructure Subcommittee",
          "systemCode": "ssev08"
        }
      },
      "systemCode": "ssev00",
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
      "sponsorshipDate": "2025-03-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1167is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1167\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Cramer (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend title 23, United States Code, to improve transportation asset management plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transportation Asset Management Simplification Act .\n#### 2. Transportation asset management plans\nSection 119(e) of title 23, United States Code, is amended\u2014\n**(1)**\nin paragraph (5)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking each fiscal year and inserting once every 4 years, in conjunction with the recertification under paragraph (6)(B) ; and\n**(ii)**\nby striking in that fiscal year ; and\n**(B)**\nby striking subparagraph (B) and inserting the following:\n(B) Application (i) Compliant States A determination of compliance under subparagraph (A) shall apply until the next recertification date under subparagraph (A) and paragraph (6)(B). (ii) Noncompliant States A determination of noncompliance under subparagraph (A) shall apply during the period beginning on the date of the determination and ending on the date on which the Secretary determines that the State is in compliance. (C) Submission (i) In general A State shall submit to the Secretary information to support a determination under subparagraph (A) in conjunction with a submission with respect to recertification under paragraph (6)(B). (ii) Requirements For purposes of subparagraph (A) and paragraph (6)(B), a submission of a State shall\u2014 (I) be considered sufficient with respect to time period if the submission is for the most recent year; and (II) for applicable years other than the most recent year, include a certification by the State that asset management undertaken in those years by the State meets the requirements of this subsection. (D) Opportunity to cure (i) In general If the Secretary determines that a State is not in compliance under subparagraph (A), the Secretary shall provide to the State\u2014 (I) a written statement of the specific actions the Secretary determines to be necessary for the State to comply under that subparagraph; and (II) a period of not less than 90 days to cure the deficiencies, during which time period all penalties and other legal impacts of a determination of noncompliance shall be stayed. (ii) Extension The Secretary, on request of the State, may extend the time period provided to cure deficiencies under clause (i)(II), including the stay of all penalties and other legal impacts of a determination of noncompliance. ; and\n**(2)**\nin paragraph (6)(C)\u2014\n**(A)**\nby redesignating clauses (i) and (ii) as subclauses (I) and (II), respectively, and indenting appropriately;\n**(B)**\nin the matter preceding subclause (I) (as so redesignated), by striking If the and inserting the following:\n(i) In general If the ; and\n**(C)**\nby adding at the end the following:\n(ii) Extension The Secretary, on request of the State, may extend the time period provided to cure deficiencies under clause (i)(I), including the stay of all penalties and other legal impacts of a denial of certification. .",
      "versionDate": "2025-03-27",
      "versionType": "Introduced in Senate"
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
            "name": "Performance measurement",
            "updateDate": "2025-08-05T17:06:37Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2025-08-05T17:06:45Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-08-05T17:07:04Z"
          },
          {
            "name": "Transportation programs funding",
            "updateDate": "2025-08-05T17:06:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-04-11T12:31:03Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1167is.xml"
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
      "title": "Transportation Asset Management Simplification Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Transportation Asset Management Simplification Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 23, United States Code, to improve transportation asset management plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:18:21Z"
    }
  ]
}
```
