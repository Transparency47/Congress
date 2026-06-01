# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7087?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7087
- Title: Grave Injustice Parity Act
- Congress: 119
- Bill type: HR
- Bill number: 7087
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-03-26T08:06:47Z
- Update date including text: 2026-03-26T08:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7087",
    "number": "7087",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001224",
        "district": "1",
        "firstName": "Nathaniel",
        "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
        "lastName": "Moran",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Grave Injustice Parity Act",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:47Z",
    "updateDateIncludingText": "2026-03-26T08:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:00:20Z",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "AL"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7087ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7087\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Moran (for himself and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow for deductions for transfers from estates or gifts to certain cemeteries.\n#### 1. Short title\nThis Act may be cited as the Grave Injustice Parity Act .\n#### 2. Deductions for transfers from estates or gifts to certain cemeteries\n##### (a) Estates\nSection 2055(a) of the Internal Revenue Code of 1986 is amended by striking or at the end of paragraph (4), by striking the period at the end of paragraph (5) and inserting ; or , and by inserting after paragraph (5) the following new paragraph:\n(6) to a cemetery company owned and operated exclusively for the benefit of its members, or any corporation chartered solely for burial purposes as a cemetery corporation and not permitted by its charter to engage in any business not necessarily incident to that purpose, if such company or corporation is not operated for profit and no part of the net earnings of such company or corporation inures to the benefit of any private shareholder or individual. .\n##### (b) Gifts\n**(1) Residents**\nSection 2522(a) of the Internal Revenue Code of 1986 is amended by striking the period at the end of paragraph (4) and inserting ; or , and by inserting after paragraph (4) the following new paragraph:\n(5) a cemetery company owned and operated exclusively for the benefit of its members, or any corporation chartered solely for burial purposes as a cemetery corporation and not permitted by its charter to engage in any business not necessarily incident to that purpose, if such company or corporation is not operated for profit and no part of the net earnings of such company or corporation inures to the benefit of any private shareholder or individual. .\n**(2) Nonresidents**\nSection 2522(b) of the Internal Revenue Code of 1986 is amended by striking the period at the end of paragraph (5) and inserting ; or , and by inserting after paragraph (5) the following new paragraph:\n(6) a cemetery company owned and operated exclusively for the benefit of its members, or any corporation chartered solely for burial purposes as a cemetery corporation and not permitted by its charter to engage in any business not necessarily incident to that purpose, if such company or corporation is not operated for profit and no part of the net earnings of such company or corporation inures to the benefit of any private shareholder or individual. .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to taxable years beginning after the date of enactment of this Act.\n#### 3. Distributions of private foundations to cemeteries\n##### (a) Taxes on failure To distribute income\nSection 4942(g)(1)(A) of the Internal Revenue Code of 1986 is amended by inserting to a cemetery company described in section 170(c)(5) or after paid .\n##### (b) Taxes on taxable expenditures\nSection 4945(d)(4)(A) is amended by striking or at the end of clause (ii) and by adding at the end the following new clause:\n(iv) is a cemetery company described in section 170(c)(5), or .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to distributions made after the date of the enactment of this Act.",
      "versionDate": "2026-01-15",
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
        "updateDate": "2026-02-03T17:09:00Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7087ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow for deductions for transfers from estates or gifts to certain cemeteries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-28T06:32:23Z"
    },
    {
      "title": "Grave Injustice Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Grave Injustice Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-28T04:53:18Z"
    }
  ]
}
```
