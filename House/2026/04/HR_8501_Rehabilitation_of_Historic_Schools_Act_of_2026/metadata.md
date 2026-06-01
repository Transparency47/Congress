# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8501?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8501
- Title: Rehabilitation of Historic Schools Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8501
- Origin chamber: House
- Introduced date: 2026-04-27
- Update date: 2026-05-07T02:44:31Z
- Update date including text: 2026-05-07T02:44:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-27: Introduced in House

## Actions

- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8501",
    "number": "8501",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "E000296",
        "district": "3",
        "firstName": "Dwight",
        "fullName": "Rep. Evans, Dwight [D-PA-3]",
        "lastName": "Evans",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Rehabilitation of Historic Schools Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-07T02:44:31Z",
    "updateDateIncludingText": "2026-05-07T02:44:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T16:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "WI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "DC"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "PA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8501ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8501\nIN THE HOUSE OF REPRESENTATIVES\nApril 27, 2026 Mr. Evans of Pennsylvania (for himself, Mr. Davis of Illinois , Ms. Moore of Wisconsin , Ms. Norton , Ms. Scanlon , and Ms. Schakowsky ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow rehabilitation expenditures for public school buildings to qualify for rehabilitation credit.\n#### 1. Short title\nThis Act may be cited as the Rehabilitation of Historic Schools Act of 2026 .\n#### 2. Qualification of rehabilitation expenditures for public school buildings for rehabilitation credit\n##### (a) In general\nSection 47(c)(2)(B)(v) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subclause:\n(III) Clause not to apply to public schools This clause shall not apply in the case of the rehabilitation of any building which was used as a qualified public educational facility (as defined in section 142(k)(1), determined without regard to subparagraph (B) thereof) at any time during the 5-year period ending on the date that such rehabilitation begins and which is used as such a facility immediately after such rehabilitation. .\n##### (b) Report\nNot later than the date which is 5 years after the date of the enactment of this Act, the Secretary of the Treasury, after consultation with the heads of appropriate Federal agencies, shall report to Congress on the effects resulting from the amendment made by subsection (a), including\u2014\n**(1)**\nthe number of qualified public education facilities rehabilitated (stated separately with respect to each State) and the number of students using such facilities (stated separately with respect to each such State),\n**(2)**\nthe number of qualified public education facilities rehabilitated in low income communities (as section 45D(e)(1) of the Internal Revenue Code of 1986) and the number of students using such facilities,\n**(3)**\nthe amount of qualified rehabilitation expenditures for each qualified public education facility rehabilitated, and\n**(4)**\nand any other data determined by the Secretary to be useful in evaluating the impact of such amendment.\n##### (c) Effective date\nThe amendment made by this section shall apply to property placed in service after the date of the enactment of this Act.",
      "versionDate": "2026-04-27",
      "versionType": "Introduced in House"
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
        "name": "Taxation",
        "updateDate": "2026-05-07T02:44:31Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8501ih.xml"
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
      "title": "Rehabilitation of Historic Schools Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T13:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rehabilitation of Historic Schools Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T13:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow rehabilitation expenditures for public school buildings to qualify for rehabilitation credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T13:03:31Z"
    }
  ]
}
```
