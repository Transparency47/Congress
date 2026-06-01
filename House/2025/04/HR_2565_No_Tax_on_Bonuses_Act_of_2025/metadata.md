# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2565?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2565
- Title: No Tax on Bonuses Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2565
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-03-19T08:07:18Z
- Update date including text: 2026-03-19T08:07:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2565",
    "number": "2565",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "No Tax on Bonuses Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:18Z",
    "updateDateIncludingText": "2026-03-19T08:07:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:00:20Z",
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
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "AZ"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "FL"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "MP"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2565ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2565\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Mast introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude enlistment and reenlistment bonuses for members of the armed forces from gross income.\n#### 1. Short title\nThis Act may be cited as the No Tax on Bonuses Act of 2025 .\n#### 2. Exclusion from gross income of enlistment and reenlistment bonuses for members of the armed forces\n##### (a) In general\nSection 112 of the Internal Revenue Code of 1986 is amended by redesignating subsections (c) and (d) as subsections (d) and (e), respectively, and by inserting after subsection (b) the following new subsection:\n(c) Qualified bonus Gross income does not include a qualified bonus. .\n##### (b) Qualified bonus defined\nSection 112(d) of such Code, as redesignated by subsection (a), is amended by adding at the end the following new paragraph:\n(6) Qualified bonus (A) In general The term qualified bonus means an enlistment, accession, reenlistment, retention, incentive, or other bonus paid by the Secretary concerned to a member of the Armed Forces of the United States in exchange for the agreement of the member to accept a commission as an officer, extend an active service commitment as an officer, enlist, reenlist, or extend an enlistment as an enlisted member in an active or reserve component, or enter into a reserve affiliation agreement. (B) Other definitions For purposes of subparagraph (A), the terms active service , enlisted member , officer , and Secretary concerned have the meanings given to such terms in section 101 of title 10, United States Code. .\n##### (c) Conforming amendments\n**(1)**\nSection 2201 of such Code is amended by striking section 112(c) both places it appears and inserting section 112(d) .\n**(2)**\nThe heading for section 112 of such Code is amended by inserting and other before compensation .\n**(3)**\nSection 3401(a)(1) of such Code is amended by inserting and other before compensation .\n**(4)**\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by striking the item relating to section 112 and inserting the following new item:\nSec. 112. Certain combat zone and other compensation of members of the Armed Forces. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-04-01",
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
        "updateDate": "2025-05-09T16:19:29Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2565ih.xml"
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
      "title": "No Tax on Bonuses Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Tax on Bonuses Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude enlistment and reenlistment bonuses for members of the armed forces from gross income.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:26Z"
    }
  ]
}
```
