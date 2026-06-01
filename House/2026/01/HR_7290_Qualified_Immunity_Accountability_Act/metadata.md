# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7290?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7290
- Title: Qualified Immunity Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 7290
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-04-21T15:52:52Z
- Update date including text: 2026-04-21T15:52:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H1989)
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H1989)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7290",
    "number": "7290",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "J000310",
        "district": "32",
        "firstName": "Julie",
        "fullName": "Rep. Johnson, Julie [D-TX-32]",
        "lastName": "Johnson",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Qualified Immunity Accountability Act",
    "type": "HR",
    "updateDate": "2026-04-21T15:52:52Z",
    "updateDateIncludingText": "2026-04-21T15:52:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1989)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-01-30T15:32:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7290ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7290\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Ms. Johnson of Texas introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to revise the applicable standards regarding death resulting from a deprivation of rights under color of law.\n#### 1. Short title\nThis Act may be cited as the Qualified Immunity Accountability Act .\n#### 2. Deprivation of rights under color of law\nSection 242 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking willfully and inserting knowingly or recklessly ;\n**(2)**\nby striking , or may be sentenced to death ; and\n**(3)**\nby adding at the end the following: For purposes of this section, an act shall be considered to have resulted in death if the act was a substantial factor contributing to the death of the person. .\n#### 3. Qualified immunity reform\nSection 1979 of the Revised Statutes of the United States ( 42 U.S.C. 1983 ) is amended by adding at the end the following:\nIt shall not be a defense or immunity in any action brought under this section against a local law enforcement officer (as such term is defined in section 2 of the George Floyd Justice in Policing Act of 2025), or in any action under any source of law against a Federal investigative or law enforcement officer (as such term is defined in section 2680(h) of title 28, United States Code), that\u2014 (1) the defendant was acting in good faith, or that the defendant believed, reasonably or otherwise, that his or her conduct was lawful at the time when the conduct was committed; or (2) the rights, privileges, or immunities secured by the Constitution and laws were not clearly established at the time of their deprivation by the defendant, or that at such time, the state of the law was otherwise such that the defendant could not reasonably have been expected to know whether his or her conduct was lawful. .",
      "versionDate": "2026-01-30",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-09-15",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Armed Services, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5361",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "George Floyd Justice in Policing Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-21T15:52:52Z"
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
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7290ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Qualified Immunity Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T05:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Qualified Immunity Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T05:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to revise the applicable standards regarding death resulting from a deprivation of rights under color of law.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T05:48:38Z"
    }
  ]
}
```
